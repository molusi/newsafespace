import re
from django.contrib.auth import authenticate
from django.contrib.auth import login, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import redirect, get_object_or_404
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.core.exceptions import ObjectDoesNotExist
from accounts.forms import UserForm, CreateuserForm
from blog.forms import *
from .models import Article,Vote
from .tokens import account_activation_token

user = get_user_model()


@login_required
def bloghome(request, *args, **kwargs):
    try:
        articles = Article.objects.all().order_by('-created')
        p = Paginator(articles, 3)
        page_number = request.GET.get('page')
        try:
            page_obj = p.get_page(page_number)
        except PageNotAnInteger:
            page_obj = p.page(1)
        except EmptyPage:
            page_obj = p.page(p.num_pages)
        context = {"articles": articles, "page_obj": page_obj}
        return render(request, "blog/index.html", context)
    except ObjectDoesNotExist:
        messages.info(request, "No articles to show..")

        return redirect('blog:myposts')



class MyPostsView(ListView):
    def get(self, *args, **kwargs):
        try:
            articles = Article.objects.filter(author__user=self.request.user)
            context = {"articles": articles}
            return render(self.request, "blog/myposts.html", context)
        except ObjectDoesNotExist:
            messages.info(self.request, "No articles to show..Add your first article")
            return redirect('blog:article-create')


def person_login(request):
    if request.user.is_authenticated:
        return redirect('blog:home')
    else:
        form = UserForm()
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None and user.is_email_verified:
                login(request, user)
                return redirect('blog:home')
            elif user is not None and not user.is_email_verified:
                messages.add_message(request, messages.ERROR, 'Email is not verified, please check your email inbox')
            else:
                messages.error(request, 'Invalid credentials')
        return render(request, 'accounts/person_login.html', {"form": form})


def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        if user.is_email_verified:
            messages.info(request, "Your account has already been activated.")
        else:
            user.active = True
            user.is_email_verified = True
            user.save()
            messages.success(request, "Thank you for your email confirmation. Now you can login to your account.")
        return redirect(reverse_lazy("accounts:person_login"))

    else:
        messages.error(request, "Activation link is invalid or has already been used.")
        return redirect(reverse_lazy("accounts:person_login"))


def activateEmail(request, user, to_email):
    mail_subject = "Activate your user account."

    name = re.split('[.@,]', user.email)[0]

    message = render_to_string("blog/template_activate_account.html", {
        'user': user,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http',
        'name': name
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    email.content_subtype = 'html'

    if email.send():
        messages.success(request, f'Dear {name}, please go to your email inbox and click on \
        received activation link to confirm and complete the registration. Note: Check your spam folder.')
        return redirect(reverse_lazy("accounts:person_login"))
    else:
        messages.error(request, f'Problem sending email to {to_email},check if you typed it correctly.')


def createaccount(request):
    form = CreateuserForm()
    user = request.user
    if request.user.is_authenticated:
        return redirect('blog:home')
    elif user.is_superuser and not user.is_email_verified:
        activateEmail(request, user.email)
        return redirect(reverse_lazy("accounts:person_login"))
    else:
        if request.method == 'POST':
            form = CreateuserForm(request.POST)
            if form.is_valid():
                realuser = form.save(commit=False)
                realuser.save()
                activateEmail(request, realuser, form.cleaned_data.get("email"))
                return redirect(reverse_lazy("accounts:person_login"))
    context = {"form": form}
    return render(request, 'accounts/register.html', context)




def comment_createview(request, pk):
    try:
        userprofile = Userprofile.objects.get(user__email=request.user)
    except ObjectDoesNotExist:
        messages.info(request, 'Please complete your profile first...')
        return redirect('blog:userprofile_create')
    article = get_object_or_404(Article, id=pk)
    comments = article.comments_all.all()
    if request.method == 'POST':
        form = CommentUpdateForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = Userprofile.objects.get(user__id=request.user.id)
            comment.article = article
            comment.save()
            return HttpResponseRedirect(reverse("blog:detail", kwargs={"pk": pk}))
    else:
        form = CommentUpdateForm()

    return render(request, 'blog/articledetail.html', {'article': article, 'comments': comments, 'form': form})




def articlecreateview(request, *args, **kwargs):
    try:
        userprofile = Userprofile.objects.get(user__email=request.user)
    except ObjectDoesNotExist:
        messages.info(request, 'Please complete your profile first...')
        return redirect('blog:userprofile_create')
    initial_data = {'author': userprofile.preferred_name}
    form = ArticleForm(request.POST or None, initial=initial_data)
    context = {'form': form}
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            if 'image' in request.FILES:
                picture = request.FILES.get('image')
                article = Article()
                article.title = title
                article.content = content
                article.image = picture
                article.author = get_object_or_404(Userprofile, user__email=request.user)
                article.save()
                context["article"] = article
                return redirect('blog:home')
            else:
                article = Article()
                article.title = title
                article.content = content
                article.author = get_object_or_404(Userprofile, user__email=request.user)
                article.save()
                context["article"] = article
                return redirect('blog:home')
    return render(request, "blog/article_create.html", context)





def commentdelete(request, pk):
    comment_ = get_object_or_404(Comment, id=pk)
    article_ = comment_.article
    comment_.delete()
    return HttpResponseRedirect(reverse("blog:detail", kwargs={"pk": article_.pk}))


voters = []
def upvote(request, article_id):
    article = Article.objects.get(id=article_id)
    vote, created = Vote.objects.get_or_create(user=request.user, article=article)

    if request.user not in voters:
        if created:
            vote.upvote = 1
        else:
            vote.upvote += 1
            vote.save()
        voters.append(request.user)
    return redirect('blog:detail', pk=article_id)



class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ArticleModelForm
    template_name = 'blog/article_update.html'
    queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Article, pk=id_)


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/articledetail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = self.get_object()
        comments = Comment.objects.filter(article=article)
        try:
            votes=Vote.objects.get(article__id=article.id)
            upvotes=votes.upvote
            context['comments'] = comments
            context["upvotes"]=upvotes
        except ObjectDoesNotExist:
            pass
        return context



class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'blog/article_delete.html'

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Article, pk=id_)

    def get_success_url(self):
        return reverse('blog:myposts')


class SearchView(View):
    template_name = 'blog/search.html'

    def get(self, *args, **kwargs):
        query = self.request.GET.get("q", "")
        if query:
            qset = (
                    Q(title__icontains=query) |
                    Q(author__preferred_name__icontains=query) |
                    Q(content__icontains=query)
            )
            results = Article.objects.filter(qset).distinct()
            context = {"results": results, "query": query}
            return render(self.request, self.template_name, context)
        else:
            return redirect('blog:home')



def userprofileview(request, *args, **kwargs):
    form = UserProfileForm()


    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            preferred_name = form.cleaned_data.get('preferred_name')
            about = form.cleaned_data.get('about')
            profilepic = form.cleaned_data.get('profilepic')
            linkedin = form.cleaned_data.get('linkedin')
            twitter = form.cleaned_data.get('twitter')
            userprofile, created = Userprofile.objects.get_or_create(user=request.user)

            userprofile.preferred_name = preferred_name
            userprofile.about = about
            userprofile.linkedin=linkedin
            userprofile.twitter=twitter

            if profilepic:
                userprofile.profilepic = profilepic

            userprofile.save()

            return HttpResponseRedirect(reverse('blog:existingprofile', kwargs={'pk': userprofile.user.id}))
    context = {'form': form}
    return render(request, "blog/profile.html", context)



class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    form_class = UserProfileUpdateForm
    template_name = 'blog/existing_profile_update.html'
    queryset = Userprofile.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Userprofile, pk=id_)



def existinguserprofile(request, pk):
    try:
        userprofile = Userprofile.objects.get(user__id=pk)
        context = {"userprofile": userprofile}
        return render(request, 'blog/existing_profile.html', context)
    except ObjectDoesNotExist:
        if pk == request.user.id:
            return redirect("blog:userprofile_create")
        else:
            messages.info(request, 'Profile no longer exists..')
            return HttpResponseRedirect(reverse('blog:home'))

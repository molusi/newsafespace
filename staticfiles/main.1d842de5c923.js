

const msg= document.querySelector(".alert");
const info = document.querySelector(".info")

window.addEventListener("DOMContentLoaded",()=>{
if(msg.contains(info)){
setTimeout(()=>msg.remove(),5000)}
});







const control = document.querySelectorAll(".input");
const isDanger = document.querySelectorAll(".is-danger");
const subBtn = document.querySelector("#sub-btn");
const huge = document.querySelector(".huge");
const myForm = document.querySelector(".my-form")
const modalo = document.querySelector(".modalo")
const closePop = document.querySelector(".close-btn")




myForm.addEventListener(("submit"),(e)=>{
e.preventDefault();
modalo.classList.add("show-modal");
document.body.style.backgroundColor="rgba(0,0,0,0.7)";
const formData = new FormData(myForm);
fetch("/yvfoundation/contact/",{
method:"post",
body:formData
}).then(function(response){
return response.text();
}).catch(function(error){
console.error(error);
});
const message = myForm.querySelector("#message");
const sender = myForm.querySelector("#sender");
message.value="";
sender.value="";
});


closePop.addEventListener(("click"),()=>{
modalo.classList.remove("show-modal");
document.body.style.backgroundColor="white";
});



control.forEach((inpEl)=>{inpEl.addEventListener(('input'),isDanger.forEach((pr)=>setTimeout(()=>pr.remove(),4000)))})

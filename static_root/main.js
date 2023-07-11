

const msg= document.querySelector(".alert");
const info = document.querySelector(".info")

window.addEventListener("DOMContentLoaded",()=>{
if(msg.contains(info)){
setTimeout(()=>msg.remove(),5000)}
});



const control = document.querySelectorAll(".input");
const isDanger = document.querySelectorAll(".is-danger");



control.forEach((inpEl)=>{inpEl.addEventListener(('input'),isDanger.forEach((pr)=>setTimeout(()=>pr.remove(),4000)))})
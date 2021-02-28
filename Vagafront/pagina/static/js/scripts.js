let form = document.getElementById("register-form")
let submit = document.getElementById("btn-submit")

submit.addEventListener('click',function(e){
    e.preventDefaut();
    console.log("Funcionou")
})
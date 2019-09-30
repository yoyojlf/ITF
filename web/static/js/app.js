$(document).ready(function () {
    $("#formulario").validate({
        errorClass: "is-invalid",
        rules: {
            nombre: {
                required: true,
            },
            apellidos:{
                required: true,
            },
            correo: {
                email: true,
                required: true,
            },
            contrasena:{

                required: true,
                password: true,
            },
        },
        messages: {
            nombre: {
                required: "the name field is required",
            },
            apellidos:{
                required: "the last name field is required",
            },
            correo:{
                required: "the email field is required",
            },
            contrasena:{
                required: "the password field is required",
            },
        }
    })
})

$("#formulario").submit(function(){
    var hoy             = new Date();
var fechaFormulario = new Date('2016-06-07');

// Comparamos solo las fechas => no las horas!!
hoy.setHours(0,0,0,0);  // Lo iniciamos a 00:00 horas
var diferencia = hoy-18;
var diferencia2 =fechaFormulario-0 
if (fechaFormulario >= diferencia) {

  console.log("Mayor de 18");
  console.log(diferencia);
  console.log(diferencia2);
  
}
else {
  console.log("Menor de 18");
  console.log(diferencia);
  console.log(diferencia2);
}
    if($("#formulario").valid()){
        console.log("Valido")
    }
    else{
        Swal.fire({
            type:'error',
            title:'Oops',
            text:'Some fields are not complete or are wrong',
        })
    }
    
})

var UsuarioN = document.getElementById('UsuarioN');
var Cor = document.getElementById('Cor');
var NomC = document.getElementById('NomC');
var UsuarioC = document.getElementById('UsuarioC');
var error = document.getElementById('error');
error.style.color = 'red'; //no me sale la especificacion del error

function enviarFormulario(){
    console.log('Enviando formulario . . . ');

//    return false;
//}

//validar_registro = function(){


var form = document.getElementById('for');
    form.addEventListener('submit', function(evt){
        evt.preventDefault();
        var mensajesError = [];

    if(UsuarioN.value === null || UsuarioN.value === ''){
        mensajesError.push('Ingresar nombre de usuario');
    }

    if(Cor.value === null || Cor.value === ''){
        mensajesError.push('Ingresar tu correo electronico');
    }

    if(NomC.value === null || NomC.value === ''){
        mensajesError.push('Ingresar tu nombre completo');
    }
    
    if(UsuarioC.value === null || UsuarioC.value === ''){
        mensajesError.push('Ingresar tu contraseña');
    }

    error.innerHTML = mensajesError.join(', ');
    });
}

function validarFormulario() {
    var nombre = document.getElementById('nombre').value;
    var email = document.getElementById('email').value;
    var mensaje = document.getElementById('mensaje').value;
    
    if (nombre === '' || email === '' || mensaje === '') {
        alert('Por favor, completa todos los campos');
        return false; // Detener el envío del formulario
      }

      if (nombre.length < 3) {
        alert('Por ingrese un nombre minimo con 3 caracteres.');
        return false;
      }
      

      var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailRegex.test(email)) {
        alert('Por favor, ingresa un correo electrónico válido');
        return false;  }

      // Validar el límite de caracteres en el campo de mensaje
     var limiteCaracteres = 500; // Cambia el número según tus necesidades
     var caracteresRestantes = limiteCaracteres - mensaje.length;
    
     if (caracteresRestantes < 0) {
        alert('Has superado el límite de caracteres permitidos');
        return false; // Detener el envío del formulario
      }

      // Mostrar el número de caracteres restantes
     document.getElementById('caracteres-restantes').innerText = caracteresRestantes;
        return true;
    }
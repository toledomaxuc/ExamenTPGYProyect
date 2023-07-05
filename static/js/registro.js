

function validarRegistro() {


    // Obtenemos los valores de los campos nomnre, email y password.

    var rut = document.getElementById('rut').value;
    var nombre = document.getElementById('nombre').value;
    var apellidos = document.getElementById('apellidos').value;
    var email = document.getElementById('email').value;
    var telefono = document.getElementById('telefono').value;
    var password = document.getElementById('password').value;

    
    if (nombre === '' || email === '' || password === '') {
        alert('Ingresar todos los campos');
        return false; // Se detiene el envío del formulario.
    }
    if(rut.length != 9){
        alert('Por favor ingrese un rut valido');
        return false;
    }

    if (nombre.length < 3) {
        alert('Por favor ingrese un nombre minimo con 3 caracteres.');
        return false;
    }
    if(apellidos.length < 3){
        alert('Por favor ingrese ambos apellidos.')
        return false;

    }

    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        alert('Ingresa un correo electrónico válido');
        return false;
    }
    
    var telefonoRegex = /^\d{9}$/;
    if(!telefonoRegex.test(telefono)){
        alert('Por favor ingrese un telefono valido.')
        return false;
    }

    if(validarPassword(password)){
        alert('Registro realizado correctamente');
        return true;
        
    }else{
        alert('Contraseña invalida, utilice al menos una mayuscula y un caracter especial');
        return false;       
    }

    

    function validarPassword(password) {
        // La constraseña debe tener al menos una mayuscula
        if (!/[A-Z]/.test(password)) {
            return false;
        }
        // La constraseña debe tener al menos un caracter especial
        if (!/[!@#$%^&*()_++\-=[\]{};':"\\|,.<>/?]+/.test(password)) {
            return false;
        }
        // Si lo anterior se cumple, la contraseña es valida
        return true;
    }
}
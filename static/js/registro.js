function validarRegistro() {
    // Obtenemos los valores de los campos
    var nombre = document.getElementById('nombre').value;
    var apellidos = document.getElementById('apellidos').value;
    var email = document.getElementById('email').value;
    var telefono = document.getElementById('telefono').value;
    var password1 = document.getElementById('password1').value;
    var password2 = document.getElementById('password2').value;

    // Realizamos las validaciones
    if (nombre === '' || email === '' || password1 === '') {
        alert('Ingresar todos los campos');
        return false;
    }

    if (nombre.length < 3) {
        alert('Por favor ingrese un nombre mínimo con 3 caracteres.');
        return false;
    }
    if (apellidos.length < 3) {
        alert('Por favor ingrese ambos apellidos.');
        return false;
    }
    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        alert('Ingrese un correo electrónico válido');
        return false;
    }
    var telefonoRegex = /^\d{9}$/;
    if (!telefonoRegex.test(telefono)) {
        alert('Por favor ingrese un teléfono válido.');
        return false;
    }
    if (!validarPassword(password1)) {
        alert('Contraseña inválida. Utilice al menos una mayúscula y un carácter especial.');
        return false;
    }

    if (password1 !== password2) {
        alert('Las contraseñas no coinciden');
        return false;
    }
    return true; // Si todas las validaciones pasan, el formulario se puede enviar
}

function validarPassword(password) {
    // La contraseña debe tener al menos una mayúscula
    if (!/[A-Z]/.test(password)) {
        return false;
    }
    // La contraseña debe tener al menos un carácter especial
    if (!/[!@#$%^&*()_++\-=[\]{};':"\\|,.<>/?]+/.test(password)) {
        return false;
    }
    return true; // La contraseña cumple con todas las validaciones
}

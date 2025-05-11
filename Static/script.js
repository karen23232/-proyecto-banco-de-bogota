// script.js
document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector('form');
    form.addEventListener('submit', function(event) {
        // Validar los campos antes de enviar el formulario
        const nombre = document.getElementById('nombre').value;
        if (!nombre) {
            alert("El nombre es obligatorio.");
            event.preventDefault();
        }
    });
});

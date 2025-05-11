from flask import Flask, request, render_template, redirect, url_for, flash
from flask import session
from db import init_db, guardar_practicante, obtener_practicantes, actualizar_estado,eliminar_practicante
import os

USUARIO_ANALISTA = 'analista'
CONTRASENA_ANALISTA = '1234'


app = Flask(__name__)
app.secret_key = 'clave_secreta_segura'  # Necesaria para flash

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']
        if usuario == USUARIO_ANALISTA and contrasena == CONTRASENA_ANALISTA:
            session['analista'] = True
            flash("Inicio de sesión exitoso.")
            return redirect(url_for('panel'))
        else:
            flash("Credenciales incorrectas.")
            return redirect(url_for('login'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('analista', None)
    flash("Sesión cerrada.")
    return redirect(url_for('login'))



@app.route('/init_db')
def init():
    init_db()
    return "Base de datos inicializada."

# Ruta para el formulario de registro
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para el panel del analista
@app.route('/panel')
def panel():
    if not session.get('analista'):
        flash("Debes iniciar sesión como analista.")
        return redirect(url_for('login'))

    practicantes = obtener_practicantes()
    return render_template('panel_analista.html', practicantes=practicantes)


# Ruta para guardar los datos del practicante
@app.route('/guardar', methods=['POST'])
def guardar():
    nombre = request.form['nombre']
    correo = request.form['correo']
    carrera = request.form['carrera']
    semestre = request.form['semestre']
    hoja_vida = request.files['hoja_vida']

    if hoja_vida and hoja_vida.filename != '':
        upload_folder = 'static/uploads'
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)

        nombre_archivo = hoja_vida.filename
        ruta_completa = os.path.join(upload_folder, nombre_archivo)
        hoja_vida.save(ruta_completa)

        guardar_practicante(nombre, correo, carrera, semestre, nombre_archivo)

        flash("✅ Registro exitoso del practicante.")
        return redirect(url_for('index'))
    else:
        flash("❌ Error: debes subir una hoja de vida en PDF.")
        return redirect(url_for('index'))

# Ruta para actualizar el estado del practicante
@app.route('/actualizar_estado/<int:id>', methods=['POST'])
def actualizar(id):
    estado = request.form.get('estado')
    if estado:
        actualizar_estado(id, estado)
        flash(f'Estado actualizado a "{estado}" correctamente.')
    else:
        flash("Error: No se recibió el estado.")
    return redirect(url_for('panel'))


@app.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    eliminar_practicante(id)
    flash("Practicante eliminado correctamente.")
    return redirect(url_for('panel'))


if __name__ == '__main__':
    app.run(debug=False)


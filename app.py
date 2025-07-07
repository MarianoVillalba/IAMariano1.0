from flask import Flask, render_template, request, send_file
import pyttsx3
import os
import uuid

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'audios'

# Crear carpeta si no existe
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/', methods=['GET', 'POST'])
def index():
    respuesta = None
    audio_filename = None

    if request.method == 'POST':
        texto = request.form.get('texto')

        if texto and texto.strip():
            respuesta = texto.strip()

            # Inicializar pyttsx3 y configurar voz
            engine = pyttsx3.init()
            engine.setProperty('rate', 150)

            # Generar archivo de audio
            audio_filename = f"{uuid.uuid4()}.wav"
            audio_path = os.path.join(app.config['UPLOAD_FOLDER'], audio_filename)

            engine.save_to_file(respuesta, audio_path)
            engine.runAndWait()
        else:
            return render_template('index.html', error="Por favor escribí algo.")

    return render_template('index.html', respuesta=respuesta, audio_file=audio_filename)

@app.route('/audio/<filename>')
def audio(filename):
    path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(path):
        return send_file(path, mimetype='audio/wav')
    return "Archivo no encontrado", 404

if __name__ == '__main__':
    app.run(debug=True)

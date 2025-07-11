# IAMariano1.0
Inteligencia Artificial de voz
Sí, esto que es una Inteligencia Artificial — aunque es una forma simple y controlada de IA.

¿Por qué es una IA?
En este caso:

Se usa pyttsx3, que convierte texto en voz.
👉 Esto es una forma de IA llamada "síntesis de voz", o TTS (Text to Speech).

🔹 Tecnologías utilizadas
Python 3

Flask (para la web)

pyttsx3 (para convertir texto en voz con IA local)

HTML/CSS (interfaz web)

UUID & OS (para generar archivos de audio temporales)

Visual Studio Code o cualquier editor

🔹 Paso a paso de implementación
1. Instalación del entorno

pip install flask pyttsx3

Esto instala Flask para crear la app web, y pyttsx3 para generar voz localmente (funciona en CPU).


2. Estructura del proyecto
/IAMariano1.0
│
├── app.py                  # Lógica del servidor
├── /templates/
│   └── index.html          # Interfaz web
├── /static/
│   └── estilos.css         # Estilos visuales
└── /audios/                # Carpeta para guardar archivos de audio generados


3. Desarrollo del archivo app.py
Se configura un formulario que recibe el texto ingresado.

Se utiliza pyttsx3 para convertir el texto a voz.

Se guarda el audio como .wav en una carpeta local.

Se muestra el texto ingresado y un botón para reproducir el audio.


4. Pruebas del sistema
Se probó ingresando distintos textos (frases, preguntas, textos largos).

El sistema generó correctamente la voz, con fluidez y sin errores.

Se verificó compatibilidad con navegadores y funcionamiento offline.

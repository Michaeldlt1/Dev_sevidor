from flask import Flask

app = Flask(__name__)

# Definimos el HTML directamente en una variable de Python
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Aplicación en Un Solo Archivo</title>
</head>
<body>
    <h1>¡Hola mundo desde app.py!</h1>
    <p>Este HTML está integrado dentro de Python, sin usar carpetas externas.</p>
</body>
</html>
"""

@app.route('/')
def home():
    # Retornamos el texto HTML directamente
    return HTML_TEMPLATE

if __name__ == '__main__':
    app.run(debug=True)

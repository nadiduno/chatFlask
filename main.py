from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

#Funcionalidade de enviar mensagem
@socketio.on('message')
def send_mensagem(message):
    send(message, broadcast=True)

#decorator
@app.route('/')
def homepage():
    return render_template("index.html")

# app.run(debug=True) para desenvol
#Intranet com ipconfig
#socketio.run(app, host='192.168.100.3')
socketio.run(app, host='localhost')
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<h1>Gayret bizden Salim, takdir Allah'tan... Yazılım öğrenmek lazım :P</h1> "
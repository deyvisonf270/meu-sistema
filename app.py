from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
  return "Olá! Meu sistema está rodando no Docker"

if__name__ == "__main__":
  app.run(host="0.0.0.0",port=5000)

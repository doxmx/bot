from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def info():
    return "Welcome"


@app.route("/tg-bot", methods=["POST"])
def tg_bot():
    if request.method == "POST" and request.is_json:
        # telegram_bot.msg(request.get_json())
        return "ok"


app.run(
    host="localhost",
    port="8080",
)

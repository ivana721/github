from flask import render_template, Flask # type: ignore

app = Flask(__name__)

@app.route("/")
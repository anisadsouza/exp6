from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1> anisa dsouza appid:2407188 </h1>"

@app.route("/resume")
def resume():
    return render_template("resume.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)

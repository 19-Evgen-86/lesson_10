from flask import Flask, render_template, request
import functions

app = Flask(__name__)


@app.route("/")
def page_home():
    data = functions.data_request()
    return render_template("candidates.html", data=data)


@app.route("/candidate/<int:id>")
def candidate(id):
    data = functions.data_request(id)
    return render_template("candidat.html", data=data)


@app.route("/skill/<string:skill>")
def skill(skill):
    data = functions.data_request(skill)
    return render_template("candidates.html", data=data)


if __name__ == '__main__':
    app.run()

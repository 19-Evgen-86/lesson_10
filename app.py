from flask import Flask, render_template, request
import functions

app = Flask(__name__)


@app.route("/")
def page_home():
    return render_template("index.html")


@app.route("/candidates/", methods=["GET", "POST"])
def candidate():
    if request.method == "GET":
        data = functions.data_request()
        return render_template("candidates.html", data=data)
    else:
        request_data = request.form.get("Search")

        if request_data.isdigit():
            data = functions.data_request(int(request_data))
            return render_template("candidat.html", data=data)

        else:
            data = functions.data_request(request_data)



# @app.route("/skill/<string:skill>")
# def skill(skill):
#     data = functions.data_request(skill)
#     return render_template("candidates.html", data=data)


if __name__ == '__main__':
    app.run()

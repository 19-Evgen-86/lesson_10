from flask import Flask, render_template, request
import functions

app = Flask(__name__)


@app.route("/")
def page_home():
    return render_template("index.html")


@app.route("/candidates/", methods=["GET", "POST"])
def candidate():
    # Проверяем метод запроса
    # если данные из формы не переданы выводим всех кандитатов
    if request.method == "GET":
        data = functions.data_request()
        # передаем в шаблон данные из json
        return render_template("candidates.html", data=data)
    else:
        # если данные из формы переданны, то проверяем ID(число) это или Навыки(строка)
        search_data = request.form.get("Search")
        # если в форме число, то вызываем функцию data_request с параметром int
        if search_data.isdigit():
            data = functions.data_request(int(search_data))
            return render_template("candidat.html", data=data)
        else:
        # если переданна строка
            data = functions.data_request(search_data)
            return render_template("candidates.html", data=data)


# @app.route("/skill/<string:skill>")
# def skill(skill):
#     data = functions.data_request(skill)
#     return render_template("candidates.html", data=data)


if __name__ == '__main__':
    app.run()

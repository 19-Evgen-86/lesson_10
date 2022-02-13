from flask import Flask, render_template, request

import functions
from classes import MyErrors

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['port'] = 80

@app.route("/")
def page_home():
    return render_template("index.html")


@app.route("/candidates/")
def page_candidate():
    # выводим всех кандидатов
    data: list = functions.data_request()
    # передаем в шаблон данные из json
    return render_template("candidates.html", data=data)


@app.route("/search_data/", methods=["GET", "POST"])
def candidate_search():
    if request.args.get('Search'):
        # если данные из формы переданны, то проверяем ID(число) это или Навыки(строка)
        search_data: str = request.args.get("Search")
        # если в форме число, то вызываем функцию data_request с параметром int
        if search_data.isdigit():
            try:
                data: dict = functions.data_request(int(search_data))
                return render_template("candidat.html", data=data)
            except MyErrors as error:
                return render_template('error.html', error=MyErrors)
        else:
            # если переданна строка
            try:
                data: list = functions.data_request(search_data)
                return render_template("candidates.html", data=data)
            except MyErrors as error:
                return render_template('error.html', error=repr(error))
    else:
        return render_template('error.html', error="введите критерии поиска")


if __name__ == '__main__':
    app.run()


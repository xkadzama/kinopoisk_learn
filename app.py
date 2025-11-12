from flask import Flask, request, jsonify


app = Flask(__name__)


posts = [
    {'id': 1, 'title': 'Статья про Python', 'content': 'У Python вышла версия 3.15!'},
    {'id': 2, 'title': 'Финансовая реформа', 'content': 'В государстве Буркина-Фасо...'},
    {'id': 3, 'title': 'Новый iPhone 17', 'content': 'В последней презентации...'},
]


@app.route('/') # route -> путь/ручка
def start(): # view function -> вьюха
    return '<h1> Hello </h1>'


# @app.route('/hello/<name>')
# def greet(name):
#     return f'Привет, {name}'


@app.route('/post/<int:id>') # url.com/post/3
def one_post(id):
    # Запрос в БД -> найти пост с айди 3 -> показать на этой странице
    for post in posts:
        if post.get('id') == id:
            title = post.get('title')
            content = post.get('content')

    return f'<h1> {title} </h1><br><p>{content}</p>'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login = request.form.get("login")
        print(login)
        # Перенаправить на другую страницу

    return '''
    <form method="POST"> 
        <input type="text" name="login">
        <button type="submit>Войти</button>
    </form>
    '''


@app.route('/api/v2.2/all_films')
def get_movie():
    films = [
        {'id': 1, 'name': 'Мстители'},
        {'id': 2, 'name': 'Интерстеллар'},
        {'id': 3, 'name': 'Бэтмен'}
    ]
    return jsonify(films)




if __name__ == '__main__':
    app.run(debug=True)

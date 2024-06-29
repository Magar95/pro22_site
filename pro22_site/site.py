from flask import Flask, render_template, request, redirect

import myDB

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/create_article', methods=['POST', 'GET'])
def create_article():
    if request.method == 'POST':
        title = request.form.get('title')
        intro = request.form.get('intro')
        text = request.form.get('text')

        myDB.insert_article(title, intro, text)
        return redirect('/posts')

    return render_template('create_article.html')


@app.route('/posts')
def posts():
    lst_articles = myDB.show_articles()
    return render_template('posts.html', articles=lst_articles)


@app.route('/posts/<int:id>')
def post_detail(id):
    article = myDB.show_one_article(id)
    return render_template('post_detail.html', article=article)


if __name__ == '__main__':
    app.run(debug=True)


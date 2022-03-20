import random

from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from logic.person import Person
from logic.document import Document

app = Flask(__name__)
bootstrap = Bootstrap(app)
model = []
model_d = []
sp: str = " "


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/person', methods=['GET'])
def person():
    return render_template('person.html')


"""""
@app.route('/person_detail', methods=['POST'])
def person_detail():
    id_person = request.form['id_person']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    p = Person(id_person=id_person, name=first_name, last_name=last_name)
    model.append(p)
    return render_template('person_detail.html', value=p)
"""


@app.route('/people')
def people():
    data = [(i.id_person, i.name, i.last_name) for i in model]
    print(data)
    return render_template('people.html', value=data)


@app.route('/document', methods=['GET'])
def document():
    return render_template('document.html')


@app.route('/document_detail', methods=['POST'])
def document_detail():
    title = request.form['title']
    author = request.form['author']
    last_author = request.form['last_author']
    theme = request.form['theme']
    leaves = request.form['leaves']
    d = Document(title=title, author=author+sp+last_author, theme=theme, leaves=leaves, last_author="")
    p1 = Person(id_person=random.randint(10000000, 20000000), name=author, last_name=last_author)
    model.append(p1)
    model_d.append(d)
    return render_template('document_detail.html', value=d)


@app.route('/book')
def book():

    data_d = [(i.title, i.author, i.theme, i.leaves, i.last_author) for i in model_d]
    print(data_d)
    return render_template('book.html', value=data_d)


if __name__ == '__main__':
    app.run(debug=True)
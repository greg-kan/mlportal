from flask import Flask, render_template, request

app = Flask(__name__)


class Item:
    def __init__(self, context, question, answer):
        self.context = context
        self.question = question
        self.answer = answer


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/question_answering_extractive', methods=['POST', 'GET'])
def question_answering_extractive():
    item = Item('', '', '')
    if request.method == 'POST':
        context = request.form['context']
        question = request.form['question']

        answer = context + question

        item = Item(context, question, answer)

    return render_template('question_answering_extractive.html', data=item)


if __name__ == '__main__':
    app.run(debug=True)

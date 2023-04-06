from flask import Flask, request
from train_data import fetch_result

app = Flask(__name__)


@app.route('/chat')
def chat():
    question = request.args.get('question', None)
    answer = fetch_result(question)
    return f'🕵🏻‍♂️ My research said so:\n {answer}'


if __name__ == '__main__':
    app.run()

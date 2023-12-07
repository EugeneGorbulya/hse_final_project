from flask import Flask, request, render_template
import pandas as pd

from utils.utils import check_hypothesis, make_series

app = Flask(__name__)

@app.route('/check')
def check():
    return render_template('check.html')

@app.route('/collab')
def home():
    return render_template('collab.html')

@app.route('/res_check', methods=['POST'])
def res_check():
    our_params = [str(x) for x in request.form.values()][0].split(',')  # если в форме больше одного поля для ввода юзером, будет больше чем 1 элемент ([0] возьмёт только первый)
    columns = [s.strip() for s in our_params]
    df = pd.read_csv('data/salaries.csv')
    action = make_series(df, "company_location", columns[0])  # можно доработать, с чётом ввода того же "Genre" в поле юзером
    sports = make_series(df, "company_location", columns[1])

    result = check_hypothesis(action, sports)

    return render_template('check.html', result=result)

@app.route('/')
def start():
    return render_template('main.html')

@app.route('/graphic')
def graph():
    return render_template('graphics.html')




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8002)

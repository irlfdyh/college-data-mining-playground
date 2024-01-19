# Author: Irshal Firdeansyah
# Github: github.com/irlfdyh

from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model_file = open('../model/mv_bank_full.pkl', 'rb')
model = pickle.load(model_file, encoding='bytes')


@app.route('/')
def index():
    return render_template('index.html', result=0)


@app.route('/predict', methods=['post'])
def predict():
    (
        age,
        job,
        marital,
        education,
        default,
        balance,
        housing,
        loan,
        contact,
        day,
        month,
        duration,
        campaign,
        p_days,
        previous,
        p_outcome
    ) = [x for x in request.form.values()]

    data = [
        int(age),
        int(job),
        int(marital),
        int(education),
        int(default),
        int(balance),
        int(housing),
        int(loan),
        int(contact),
        int(day),
        int(month),
        int(duration),
        int(campaign),
        int(p_days),
        int(previous),
        int(p_outcome)
    ]

    prediction = model.predict([data])
    output = round(prediction[0], 2)

    return render_template(
        'index.html',
        result=output,
        age=age,
        job=job,
        marital=marital,
        education=education,
        default=default,
        balance=balance,
        housing=housing,
        loan=loan,
        contact=contact,
        day=day,
        month=month,
        duration=duration,
        campaign=campaign,
        p_days=p_days,
        previous=previous,
        p_outcome=p_outcome
    )


if __name__ == '__main__':
    app.run(debug=True)

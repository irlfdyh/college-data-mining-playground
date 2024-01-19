from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model_file = open('../model/mv_model.pkl', 'rb')
model = pickle.load(model_file, encoding='bytes')

@app.route('/')
def index():
    return render_template('index.html', result=0)

@app.route('/predict', methods=['post'])
def predict():
    f1, f2, f3, f4, t = [x for x in request.form.values()]

    data = []
    # if f1 == '1':
    #     data.extend([1])
    # else:
    #     data.extend([0])
    # if f2 == '1':
    #     data.extend([1])
    # else:
    #     data.extend([0])
    # if f3 == '1':
    #     data.extend([1])
    # else:
    #     data.extend([0])
    # if f4 == '1':
    #     data.extend([1])
    # else:
    #     data.extend([0])
    # if t == '1':
    #     data.extend([1])
    # else:
    #     data.extend([0])

    data.append(int(f1))
    data.append(int(f2))
    data.append(int(f3))
    data.append(int(f4))
    data.append(int(t))

    prediction = model.predict([data])
    output = round(prediction[0], 2)

    return render_template('index.html', result=output, f1=f1, f2=f2, f3=f3, f4=f4, t=t)

if __name__ == '__main__':
    app.run(debug=True)
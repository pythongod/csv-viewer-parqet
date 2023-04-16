from flask import Flask, render_template, request
import csv
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            data = pd.read_csv(uploaded_file, sep=';', index_col=False)
            data = data.to_dict(orient='records')
            return render_template('display.html', data=data)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

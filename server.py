# Importing Flask and csv

import csv
from flask import Flask, render_template, url_for, request, redirect

# Instantiating a Flask class

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

def storing_database(data):
    with open('database.csv', 'a') as file:
        user_name = data['user_name']
        email = data['email']
        subject = data['subject']
        message = data['text']
        csv_file = csv.writer(file, delimiter = ',', quoting = csv.QUOTE_MINIMAL)
        csv_file.writerow([user_name, email, subject, message])

@app.route("/submited_form", methods = ['POST', 'GET'])
def submited_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        storing_database(data)
        return redirect('/thank_you.html')
    else:
        return redirect('/error404.html')

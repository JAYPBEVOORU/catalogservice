from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

def persist_data_to_csv(data_list):
    with open('database.csv', mode='a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(data_list)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/<pagename>')
def get_page(pagename):
    return render_template(pagename)

@app.route('/submit_contact', methods=['Post'])
def submit_contact():
    print(request.form['email'])
    persist_data_to_csv([request.form['email'],request.form['subject'],request.form['text']])
    return redirect('thanks.html')

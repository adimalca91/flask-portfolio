#from tkinter.messagebox import NO
from lib2to3.pgen2.token import NEWLINE
from flask import Flask, render_template, url_for, request, redirect
# render_template is a flask function that allows us to send the html file
import csv


app = Flask(__name__)
print(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as databse:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = databse.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as databse2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(databse2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])



@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_file(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong. Try again!'

# @app.route('/about.html')
# def about():
#     return render_template('about.html')

# @app.route('/works.html')
# def works():
#     return render_template('works.html')

# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')


# @app.route('/blog')
# def blog():
#     return 'These are my thoughts on blogs!'


# @app.route('/blog/2022/backend')
# def blog2():
#     return 'Trying to learn Backend development'
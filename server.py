from flask import Flask,send_file, render_template, url_for, request,redirect
import csv
app = Flask(__name__)

@app.route('/')
def hello_world():
    return  render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return  render_template(page_name)

'''
@app.route('/about.html')
def hello_about():
    return  render_template('about.html')

@app.route('/works.html')
def hello_works():
    return  render_template('works.html')

@app.route('/contact.html')
def hello_contact():
    return  render_template('contact.html')



@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
'''
def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer =csv.writer(database2, delimiter=',', quotechar='|',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('thankyou.html')
    else:
        return 'something went wrong'
from flask import Flask, render_template, request
from flask_mail import Mail, Message
from datetime import datetime

app = Flask(__name__)
mail = Mail(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['POST'])
def contact():
    msg = Message('Hello', sender = 'yourId@gmail.com', recipients = ['someone@gmail.com'])
    msg.body = 'This is the email body'
    mail.send(msg)
    return 'Sent'

@app.route('/time')
def get_current_time():
    return {'time': datetime.now()}

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, flash, url_for, redirect
import smtplib
from dotenv import load_dotenv
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

load_dotenv()

MY_EMAIL = os.environ["my_email"]
PASSWORD = os.environ["password"]

@app.route('/', methods=['GET', 'POST'])
def send_mail():
    if request.method == 'POST':
        recipient_email = request.form['email']
        message         = request.form['message']
        
        try:
            connection = smtplib.SMTP("smtp.gmail.com", 587)
            connection.starttls()
            
            connection.login(user=MY_EMAIL, password=PASSWORD)

            email_message = f"Subject:Hello\n\n{message}"

            connection.sendmail(
                from_addr = MY_EMAIL,
                to_addrs  = recipient_email,
                msg       = email_message
            )
            
            connection.close()
            
            flash("Email sent successfully!", "success")
            return redirect(url_for('send_mail'))
        except Exception as e:
            flash(f"An error occurred: {e}", "error")
            return redirect(url_for('send_mail'))
    
    return render_template('send_mail.html')


if __name__ == '__main__':
    app.run(
        debug=True
    )
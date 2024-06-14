
from flask import Flask, render_template, redirect, url_for, flash, request
from email_validator import validate_email, EmailNotValidError

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/subscribe', methods=['POST'])
def subscribe():
    email = request.form['email']
    
    try:
        # Validate the email address
        valid = validate_email(email)
        email = valid.email
    except EmailNotValidError:
        flash('Invalid email address. Please try again.')
        return redirect(url_for('home'))
    
    # Add the email to a database or email marketing platform
    # In a real-world application, this would be done here

    flash('You have successfully subscribed to our newsletter!')
    return redirect(url_for('success'))

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('register.html', username="", email="", phone="", message=None, message_type="")


@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    email = request.form['email']
    phone = request.form['phone']
    password = request.form['password']
    confirm_password = request.form['confirm_password']
    message = ""
    message_type = ""

    # Validation
    if username == "":
        message += "Enter username. "
        message_type = "error"
    elif len(username) < 4:
        message += "Username must be at least 4 characters long. "
        message_type = "error"
    
    if email == "":
        message += "Enter email. "
        message_type = "error"
    
    if phone == "":
        message += "Enter phone number. "
        message_type = "error"
    
    if password == "":
        message += "Enter password. "
        message_type = "error"
    elif len(password) < 6:
        message += "Password must be longer than 6 characters. "
        message_type = "error"
    elif password != confirm_password:
        message += "Passwords do not match. "
        message_type = "error"
    else:
        message = "Registration successful!"
        message_type = "success"

    # Re-render the registration page with the current inputs and validation message
    return render_template('register.html', username=username, email=email, phone=phone, message=message, message_type=message_type)

if __name__ == '__main__':
    app.run(debug=True)

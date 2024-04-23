from connect_to_db import *
from flask import Flask, request, jsonify
#to create flask application

app = Flask(__name__)

email_m = None

@app.route('/hey', methods=['GET', 'POST']) 
def receive_data():
    
    if request.method == 'POST':
        email_m = request.form.get('email')
        name_m = request.form.get('name')
        phone_m = request.form.get('phone')
    data = request.form # Getting data from the request
    move_to_db(name_m,email_m,phone_m)
    
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)

while True:
    if email_m is None:
        pass
    else:
        print(email_m)
        break
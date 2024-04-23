from flask import Flask, request, jsonify

#to create flask application
app = Flask(__name__)

#creating a root / 
@app.route('/')
def home():
    return 'This is the Home Page'


#making a get root
@app.route('/get-user/<user_id>/<name_input>')

def get_user(user_id,name_input):
    user_data = {
        'user_id' : user_id,
        'name' : name_input,
        'email' : f'{name_input}{user_id}@gmail.com'
    }
    
    #query paarameter
    extra = request.args.get('extra')
    if extra:
        user_data['extra'] = extra
    return jsonify(user_data), 200

#making a POST root
@app.route('/create-user', methods=['POST'])
def create_user():
    data = request.get_json()
    
    return jsonify(data), 201


#run flask application server
if __name__ == "__main__":
    app.run(debug=True)
    


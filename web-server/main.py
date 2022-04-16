from flask import Flask, jsonify


app = Flask(__name__)



@app.route('/', methods=['GET'])
def index():
    jsonify({'message': 'Welcome to Automating-Home'})

@app.route('/users', methods=['GET'])
def users():
    jsonify({'User': 'These are the users registered in this house'})



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
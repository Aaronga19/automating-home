from flask import Flask, jsonify
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)



@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Welcome to Automating-Home'})

@app.route('/users', methods=['GET'])
def users():
    return jsonify({'User': 'These are the users registered in this house'})



if __name__ == '__main__':
    # app.run(host='0.0.0.0', debug=True)
    app.run()
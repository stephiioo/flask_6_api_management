from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return f'Hello from my Flask API Endpoint Server'

@app.route('/hello', methods=['GET'])
def hello_get():
    name = request.args.get('name', 'World')
    lastname = request.args.get('lastname', 'no last name provided')
    return f'Hello {name} {lastname}!'

@app.route('/hello', methods=['POST'])
def hello_post():
    data = request.get_json()
    if data is None:
        return jsonify({'error': 'Invalid JSON'}), 400
    
    name = data.get('name', 'World')
    return jsonify({'message': f'Hello {name}!'})

if __name__ == '__main__':
    app.run(debug=True)

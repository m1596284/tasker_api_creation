from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/greet')
def greet():
    name = request.args.get('name', 'World')
    message = f"Hello, {name}!"
    return jsonify({'message': message})


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')

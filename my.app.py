from flask import Flask, request

app = Flask(__name__)


@app.route('/callback', methods=['GET'])
def callback():
    authorization_code = request.args.get('code')
    return f'Authorization Code: {authorization_code}'


if __name__ == '__main__':
    app.run(ssl_context='adhoc', host='localhost', port=3000)

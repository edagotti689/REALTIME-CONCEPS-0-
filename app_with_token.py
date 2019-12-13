from flask import Flask, jsonify, request, make_response
import jwt
import datetime
from functools import wraps

app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisisthesecretkey'


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        print(' \n\n\n token :', token, '\n\n\n')
        if not token: return jsonify({'message': 'Token is missing'})

        try:
            data = jwt.decode(token,app.config['SECRET_KEY'])

        except:
            return jsonify({'message': 'Token is invalid'})
        return f(*args,**kwargs)
    return decorated

@app.route('/get_names', methods=['POST'])
@token_required
def get_names():
    names = ['balu','babu','ganesh']
    return jsonify(names)


@app.route('/login', methods=['GET'])
def login():
    auth = request.authorization
    if auth.username == 'admin' and auth.password == 'sriram':
        token = jwt.encode({'user':auth.username, 'exp':datetime.datetime.utcnow()+ datetime.timedelta(seconds=60)},app.config['SECRET_KEY'])
        return jsonify({'token':token.decode('UTF-8')})

    return make_response(' Please enter username and password ')

app.run(debug=True)


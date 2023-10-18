import os
from functools import wraps
from flask import Flask, jsonify, request


app = Flask(__name__)
#app.config['SECRET_KEY'] = os.environ['API_PKEY']

app.config['SECRET_KEY'] = "789"

def token_required(f):
     @wraps(f)
     def validate(*args, **kwargs):
         #export API_PKEY=mytoken  MaC/Linux
         #set API_PKEY=mytoken  Windows
         token = request.headers['token']
         if token == app.config['SECRET_KEY']:
             return f(*args, **kwargs)
         else:
             return jsonify({"message":"token is invalid"}), 403    
     return validate 




@app.route('/')
@token_required
def index():
    return jsonify({"Choo Choo": "Welcome class"})


"""
MAIN ...........................................................................
"""
if __name__ == '__main__':
    #app.run()
    app.run(debug=True, port=os.getenv("PORT", default=5000 )) 
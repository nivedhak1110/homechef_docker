
from flask import Flask, jsonify, send_file, render_template, redirect
from flask import request
from flask_cors import CORS

from core.logic import helper

app = Flask(__name__)
CORS(app)

"""
1. Home page 
"""
@app.route('/login')
def page1():
    return render_template('login.html')

@app.route('/signup')
def page2():
    return render_template('signup.html')

@app.route('/customer')
def page3():
    return render_template('customer-dashboard.html')

@app.route('/homechef')
def page4():
    return render_template('homechef-dashboard.html')


"""
1. method to verify the login credentials
"""
@app.route('/test', methods=['POST'])
def user_input():
    if request.method == 'POST':
       try:
           helper.read_input(request)
           print(" Hello Madammu")
       except Exception as exception:
           return jsonify(status=exception.args[0], code=500)
    else:
        return jsonify(status='Invalid request type', code=500)
    #return redirect("https://34.84.229.189/console/")
    return jsonify(status="Login Success", code=200)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

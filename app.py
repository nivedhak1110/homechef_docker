from flask import Flask, jsonify, render_template
from flask import request
#from core.logic import helper
from flask_cors import CORS
import helper

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

@app.route('/save',methods=['POST'])
def save():
    #status = helper.disp(request)
    status = helper.get_input(request)
    if(status == "success"):
        return render_template('login.html')
    else:
        return jsonify(status='Failed to save the details', code=400)



"""
1. method to verify the login credentials
"""
@app.route('/test', methods=['POST'])
def user_input():
        status = helper.read_input(request)
        return jsonify(result=status)

#login check method
@app.route('/login_verify' , methods=['POST'])
def login_verify():
    status = helper.read_input(request)
    if (status == "success"):
        return render_template('homechef-dashboard.html')
    else:
        return jsonify(status='Failed to login , Please check uname,pwd', code=400)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)


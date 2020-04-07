
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

@app.route('/page4',methods=['POST'])
def page4():
    status = helper.disp_input(request)
    return render_template('homechef-dashboard.html')



"""
1. method to verify the login credentials
"""
@app.route('/test', methods=['POST'])
def user_input():
        status = helper.read_input(request)
        return jsonify(result=status)
#login check method
@app.route('/logincheck' , methods=['POST'])
def check():

    status = helper.read_input(request)
    if(status=="success"):
         return render_template("homechef-dashboard.html")
    else:
        print("invalid entry")
        return render_template('login.html')




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

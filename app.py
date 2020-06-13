from flask import Flask, jsonify, render_template
from flask import request
from flask_cors import CORS
from core.logic import helper_nodb

app = Flask(__name__)
CORS(app)



"""
1. SignUP page
"""

@app.route('/signup')
def signup():
    return render_template('signup.html')

"""
2. Saving signup details
"""

@app.route('/save',methods=['POST'])
def save():
    status = helper_nodb.save_details(request)
    if(status == "success"):
        return render_template('login.html')
    else:
        return jsonify(status='Failed to save the details, try Signup Again', code=400)

"""
3. Login  page
"""

@app.route('/login')
def login():
    return render_template('login.html')

"""
4. Validate the Login credentials 
"""

#login check method
@app.route('/logincheck' , methods=['POST'])
def logincheck():
    status = helper_nodb.check_credentials(request)
    if (status == "success"):
        return render_template('homechef-dashboard.html')
    else:
        return jsonify(status='Invalid credentials, Failed to login , Please try again', code=400)




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)


from flask import Flask, jsonify, render_template
from flask import request
from flask_cors import CORS
from core.logic import helper_nodb
from core.logic import helper

app = Flask(__name__)
CORS(app)



"""
1. SignUP page
"""

@app.route('/signup')
def signup():
    return render_template('signup_design1.html')

"""
2. Saving signup details
"""

@app.route('/save',methods=['POST'])
def save():
    helper.create_database_signup()
    helper.create_table_signup()
    status = helper.get_input(request)
    if(status == "success"):
        return render_template('login_design1.html')
    else:
        return jsonify(status='Failed to save the details, try Signup Again', code=400)
    
"""
3. Login  page
"""

@app.route('/login')
def login():
    return render_template('login_design1.html')

"""
4. Validate the Login credentials 
"""

#login check method
@app.route('/logincheck' , methods=['POST'])
def logincheck():
    status = helper.read_input(request)
    print(status)
    if (status == "homechef"):
        return render_template('homechef-dashboard.html')
    elif(status == "customer"):
        return render_template('customer_dashboard.html')


    else:
        return jsonify(status='Invalid credentials, Failed to login , Please try again', code=400)

"""
5. homechef   page
"""
# return Homechef dashboard to add more dishes

@app.route('/add_dish' , methods=['get'])
def homechef():
    return render_template('homechef-dashboard.html')
"""
6. save homechef entries  page
"""
@app.route('/homechef_save',methods=['post'])
def homechef_save():

    helper.create_database_homechef()
    helper.create_table_homechef()
    status = helper.get_input_homechef(request)


    if (status == "success"):
        return render_template('thankyou.html')
    else:
        return jsonify(status='Failed to save the details, try Signup Again', code=400)


@app.route('/restclient')
def restclient_test():
    return render_template('customer_dashboard.html')

@app.route('/test',methods=['get'])
def test_get():
    list = helper.print_homechef_ID(request)
        
    return jsonify( name = list )


# Method to get the homechef details
@app.route("/get/homechef/<name>")
def get_dish(name):
        try:
           #homechefname = name
           print(name)
           dish_details = helper.dish_details(name)
           dish = dish_details[0][0]
           cost = dish_details[0][1]
           availability = dish_details[0][2]

           # get the dish details from DB and return
           return jsonify(dishname = dish, price = cost , availability = availability, chefname = name)

        except Exception as exception:
            return jsonify(status=exception.args[0], code=500)
# place order
@app.route("/order" , methods = ['GET', 'POST'])
def place_order():
    try:

        name = request.form['name']
        print(name)
        quantity = request.form['quantity']
        print(quantity)
        print("inside place_order")
        current_availability = helper.place_order(name , quantity)
        print(current_availability)
        return jsonify( response = "thank you , your order placed!"  )
    except Exception as exception:
        return jsonify(status=exception.args[0], code=500)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)


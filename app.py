from flask import Flask, jsonify, render_template
from flask import request
from flask_cors import CORS
from core.logic import helper_nodb
from core.logic import helper




app: Flask = Flask(__name__)
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
        return jsonify(status= 'Invalid credentials, Failed to login , Please try again', code=400)

"""
5. homechef   page
"""
# return Homechef dashboard to add more dishes

@app.route('/add_dish' ,methods=['post'] )
def homechef():
    helper.create_database_homechef()
    helper.create_table_homechef()
    status = helper.get_input_homechef(request)
    if (status == "success"):
        return render_template('homechef-dashboard.html')
    else:
        return jsonify(status='Failed to save the details, try Signup Again', code=400)

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

    return jsonify( name = list)

# Method to get the homechef details

@app.route("/get/homechef/<name>")
def get_dish(name ):
        try:
           #homechefname = name
           print(name)

           dish_details = helper.dish_details(name )
           dish = dish_details[0][0]
           cost = dish_details[0][1]
           availability = dish_details[0][2]
           contact =  dish_details[0][3]
           # get the dish details from DB and return
           return jsonify(dishname = dish, price = cost , availability = availability, chefname = name , contact = contact)

        except Exception as exception:
            return jsonify(status=exception.args[0], code=500)
# place order

@app.route("/order" , methods = ['GET', 'POST'])
def place_order():
    try:
        if request.method == 'POST':
            print(request)
            order_details = request.get_json(force=True)
            chef_name = order_details['chef_name']
            print(chef_name)
            dish = order_details['dish']
            print(dish)
            quantity = int(order_details['order_quantity'])
            print(quantity)
            customer_name = order_details['customer_name']
            print(customer_name)
            address = order_details['address']
            print(address)
            customer_contact = int(order_details['customer_contact'])
            print(customer_contact )

            current_availability = helper.place_order(chef_name ,quantity )
            print(current_availability)

            print("create a order_details database and table")
            helper.create_database_order_details()
            status = helper.create_table_order_details()
            print(status)
            if(status == "success"):
                helper.insert_order_details(chef_name,customer_name,customer_contact,address ,dish, quantity)
            else:
                return jsonify(status='Failed to save the order details', code=400)

            return jsonify( response = "thank you , your order placed!"  )

    except Exception as exception:
        return jsonify(status=exception.args[0], code=500)


#homechef check orders
@app.route('/check_orders', methods=['POST'])
def homechef_check_orders():
    return render_template('thankyou.html')
#method to retrive the name,order_details  of the customers who ordered the dish
@app.route('/get/ordercustomer/<name>')
def get_customer_order_details(name):
    try:

        print(name)
        customer_order_details = helper.customer_order_details(name)

        print(customer_order_details)

        return jsonify(customer_order_details = customer_order_details)
    except Exception as exception:
        return jsonify(status=exception.args[0], code=500)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)



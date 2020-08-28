import mysql.connector
from mysql.connector import Error
import hashlib



try:
    mydb = mysql.connector.connect(
        host="mysql",
        user="root",
        passwd="mypassword"
        # database="signup"
    )

except Error as e:
    print("Error while connecting to MySQL", e)


# method to create database if not exist
def create_database_signup():
    try:

        mycursor = mydb.cursor()
        mycursor.execute("SHOW DATABASES")
        databases = mycursor.fetchall()

        db_create = True
        for database in databases:
            signup_db = "{0}".format(database[0])

            print(signup_db, flush=True)

            if (signup_db == "signup"):
                print("Signup Database already created !", flush=True)
                db_create = False
                break
        if (db_create):
            mycursor.execute("CREATE DATABASE signup")
            print("Signup Database created !", flush=True)
    except Error as e:
        print("Error while creating database", e)



#  method to create signup table if not exist
def create_table_signup():
    try:
        mydb = mysql.connector.connect(
            host="mysql",
            user="root",
            passwd="mypassword")

        mycursor = mydb.cursor()
        mycursor.execute("USE signup")
        mycursor.execute("SHOW TABLES")
        tables = mycursor.fetchall()


        table_create = True
        for table in tables:
            signup_table = "{0}".format(table[0])

            print(signup_table, flush=True)

            if (signup_table == "signup"):
                print("Signup table already created !", flush=True)
                table_create = False
                break
        if (table_create):
            mycursor.execute(
                "CREATE TABLE signup (fname VARCHAR(50), lname VARCHAR(50) ,  email VARCHAR(20) NOT NULL PRIMARY KEY, password TINYTEXT,category VARCHAR(50) , address VARCHAR(100))")
            print("Signup table  created !", flush=True)

    except Error as e:
        print("Error while creating table ", e)




# Method to read login details

def read_input(request):
    try:
        mydb = mysql.connector.connect(
            host="mysql",
            user="root",
            passwd="mypassword"
        )


        email_id = request.form.get('ID')
        b = request.form.get('password')
        hash2 = hashlib.md5(b.encode())
        passwd = hash2.hexdigest()

        print(email_id)
        print(passwd)

        # status = "success"
        status = login_verify(email_id, passwd)
        print(status)
        return status
    except Error as e:
        print("Error while reading input ", e)



"""  except Exception as exception:
        print("Error ")
        print(exception.args[0])"""


##verify login details


def login_verify(email_id, passwd ):
    try:
        mydb = mysql.connector.connect(
            host="mysql",
            user="root",
            passwd="mypassword"
            # database="signup"
        )
        mycursor = mydb.cursor()
        mycursor.execute("USE signup")
        sql= "select count(email)   from signup where email= '" + email_id + "'"
        mycursor.execute(sql)
        count = mycursor.fetchone()
        if(count[0] == 1):

            sql = "select password   from signup where email= '" + email_id + "'"
            mycursor.execute(sql)
            myresult1 = mycursor.fetchone()[0]
            print(myresult1)

        else:
            print("the query doesnot return any value ")
            return "failed"

        sql = "select category   from signup where email= '" + email_id + "'"
        mycursor.execute(sql)
        myresult2 = mycursor.fetchone()[0]
        print(myresult2)

        try:
            if (passwd == myresult1  and myresult2.lower() == "customer"):
                print("login success")
                return "customer"
            elif(passwd == myresult1  and myresult2.lower() == "homechef"):
                print("login success")
                return "homechef"
            else:
                print("login failed")
                return "failed"
        except Error as e:
            print("Error while checking credentials ", e)

            mydb.commit()
            print_all()



    except Error as e:
        print("Error while verifying details ", e)


# print all signup database details
def print_all():
    try:
        mydb = mysql.connector.connect(
            host="mysql",
            user="root",
            passwd="mypassword"
        )

        print("Printing all DB data")
        mycursor = mydb.cursor()
        mycursor.execute("USE signup")
        mycursor.execute("SELECT * FROM signup")
        myresult = mycursor.fetchall()

        for x in myresult:
            print(x)
    except Error as e:
        print("Error while printing DB details ", e)


# method to read  user input during signup


def get_input(request):
    try:

        mydb = mysql.connector.connect(
            host="mysql",
            user="root",
            passwd="mypassword"
        )

        fname = request.form.get('fname')
        lname = request.form.get('lname')
        email = request.form.get('email')
        a = request.form.get('password')
        hash1 =  hashlib.md5(a.encode())
        password = hash1.hexdigest()
        print(password)
        category = request.form.get('category')
        address = request.form.get('add')


        signup_insert(fname, lname, email, password, category, address)
        return "success"
    except Error as e:
        print("Error while reading input ", e)


# save user signup  details in database
def signup_insert(fname, lname, email, password,category, address):
    try:
        mydb = mysql.connector.connect(
            host="mysql",
            user="root",
            passwd="mypassword"
        )
        mycursor = mydb.cursor()
        mycursor.execute("USE signup")
        sql = "INSERT INTO signup VALUES(%s,%s,%s,%s,%s,%s)"
        val = (fname, lname, email, password, category , address)
        mycursor.execute(sql, val)
        mydb.commit()
        print_all()

    except Error as e:
        print("Error while inserting into table ", e)

# create   homechef database

def create_database_homechef():
    try:
        mydb = mysql.connector.connect(
            host="mysql",
            user="root",
            passwd="mypassword")

        mycursor = mydb.cursor()
        mycursor.execute("SHOW DATABASES")
        databases = mycursor.fetchall()

        db_create = True
        for database in databases:
            homechef_db = "{0}".format(database[0])

            print(homechef_db, flush=True)

            if (homechef_db == "homechef"):
                print("Homechef Database already created !", flush=True)
                db_create = False
                break
        if (db_create):
            mycursor.execute("CREATE DATABASE homechef")
            print("Homechef Database created !", flush=True)
    except Error as e:
        print("Error while creating database", e)

# create homechef table
def create_table_homechef():
    try:
        mydb = mysql.connector.connect(
            host="mysql",
            user="root",
            passwd="mypassword")

        mycursor = mydb.cursor()
        mycursor.execute("USE homechef")
        mycursor.execute("SHOW TABLES")
        tables = mycursor.fetchall()

        table_create = True
        for table in tables:
            homechef_table = "{0}".format(table[0])

            print(homechef_table, flush=True)

            if (homechef_table == "homechef"):
                print("Homechef table already created !", flush=True)
                table_create = False
                break
        if (table_create):
            mycursor.execute(
                "CREATE TABLE homechef ( ID VARCHAR(50) NOT NULL PRIMARY KEY , chef_name VARCHAR(50), date VARCHAR(20) ,  dish VARCHAR(100), cost int , availability int , location VARCHAR(100), contact bigint)")
            print("homechef table  created !", flush=True)

    except Error as e:
        print("Error while creating table ", e)

# method to read  user input by homechef
def get_input_homechef(request):
    try:

        mydb = mysql.connector.connect(
            host="mysql",
            user="root",
            passwd="mypassword"
        )
        ID=  request.form.get('ID')
        chef = request.form.get('chef')
        date = request.form.get('date')
        dish = request.form.get('dish')
        cost = request.form.get('cost')
        availability = request.form.get('available')
        location = request.form.get('location')
        contact =  request.form.get('contact')

        homechef_insert( ID, chef, date , dish, cost, availability , location , contact)
        return "success"
    except Error as e:
        print("Error while reading input ", e)


# save  chef entries   in homechef database
def homechef_insert(ID, chef, date , dish, cost, availability,location, contact):
    try:
        mydb = mysql.connector.connect(
            host="mysql",
            user="root",
            passwd="mypassword"
        )
        mycursor = mydb.cursor()
        mycursor.execute("USE homechef")
        sql = "INSERT INTO homechef VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (ID,chef, date , dish, cost, availability , location, contact)
        mycursor.execute(sql, val)
        mydb.commit()
        print("insert into homechef database successful")
        print_all_homechef()

    except Error as e:
        print("Error while inserting into table ", e)

# print all homechef table details
def print_all_homechef():
    try:
        mydb = mysql.connector.connect(
            host="mysql",
            user="root",
            passwd="mypassword"
        )

        print("Printing all homechef data")
        mycursor = mydb.cursor()
        mycursor.execute("USE homechef")
        mycursor.execute("SELECT * FROM homechef")
        myresult = mycursor.fetchall()

        for x in myresult:
            print(x)
    except Error as e:
        print("Error while printing homechef table  details ", e)


# retrive homechef ID from database
def print_homechef_ID(request):
    try:

        mydb = mysql.connector.connect(
            host="mysql",
            user="root",
            passwd="mypassword"
        )

        mycursor = mydb.cursor()
        mycursor.execute("USE homechef")
        mycursor.execute("select ID from homechef")
        data = mycursor.fetchall() #data from database
        print(data)
        return data


    except Error as e:
        print("Error while printing homechef id", e)

# retrive dish details from the respective homechef table
def dish_details(name):
    try:

        mydb = mysql.connector.connect(
            host="mysql",
            user="root",
            passwd="mypassword"
        )
        mycursor = mydb.cursor()
        mycursor.execute("USE homechef")
        mycursor.execute("select dish,cost, availability,contact from homechef where ID = '" + name + "' ")
        dish_details = mycursor.fetchall()  # data from database
        print(dish_details)


        return dish_details

    except Error as e:
        print("Error while printing dish details", e)
# place order

def place_order( name ,quantity):
    try:

        mydb = mysql.connector.connect(
            host="mysql",
            user="root",
            passwd="mypassword"
        )

        mycursor = mydb.cursor(buffered=True)
        mycursor.execute("USE homechef")
        mycursor.execute("select  availability from homechef where ID = '" + name + "' ")
        print("inside helper place order")
        availability = mycursor.fetchone()[0]
        print(availability)
        current_availability = availability - quantity
        print(current_availability)
        if(availability > 0):

            sql = "update  homechef set availability = {availability}  where ID = '{name}' ".format (availability = current_availability , name= name)
            #val = current_availability
            mycursor.execute(sql)
            print(current_availability)
            print("database updated successfully")
            mydb.commit()
            return current_availability

        else:
            print("Else:" + current_availability)
            return -1



    except Error as e:
        print("Error while ordering ", e)

# create   order_details database

def create_database_order_details():
    try:
        mydb = mysql.connector.connect(
            host="mysql",
            user="root",
            passwd="mypassword")

        mycursor = mydb.cursor()
        mycursor.execute("SHOW DATABASES")
        databases = mycursor.fetchall()

        db_create = True
        for database in databases:
            order_db = "{0}".format(database[0])

            print(order_db, flush=True)

            if (order_db == "order_details"):
                print("order_details Database already created !", flush=True)
                db_create = False
                break
        if (db_create):
            mycursor.execute("CREATE DATABASE order_details")
            print(" Database order_details created !", flush=True)
    except Error as e:
        print("Error while creating database", e)

# create order_details table
def create_table_order_details():
    try:
        mydb = mysql.connector.connect(
            host="mysql",
            user="root",
            passwd="mypassword")

        mycursor = mydb.cursor()
        mycursor.execute("USE order_details ")
        mycursor.execute("SHOW TABLES")
        tables = mycursor.fetchall()

        table_create = True
        for table in tables:
            order_table = "{0}".format(table[0])

            print(order_table, flush=True)

            if (order_table == "order_details"):
                print("order_details table already created !", flush=True)
                table_create = False
                break
        if (table_create):
            mycursor.execute(
                "CREATE TABLE order_details (  chef_name VARCHAR(50), customer_name VARCHAR(50), customer_contact bigint , customer_address VARCHAR(200), dish VARCHAR(50) , quantity int  )")
            print(" order_details table  created !", flush=True)
        return "success"
    except Error as e:
        print("Error while creating table ", e)



#insert order_details into order_details table

def insert_order_details(chef_name,customer_name,customer_contact,address ,dish, quantity):
    try:
        mydb = mysql.connector.connect(
            host="mysql",
            user="root",
            passwd="mypassword")
        mycursor = mydb.cursor()
        mycursor.execute("USE order_details")
        sql = "insert into order_details values (%s,%s,%s,%s,%s,%s)"
        val =  (chef_name,customer_name,customer_contact,address ,dish, quantity)
        mycursor.execute(sql,val)
        mydb.commit()
        print("insert into order_details table successful")
        print_all_order_details()

    except Error as e:
        print("Error while inserting into order_details table ", e)

#print all order_details
def print_all_order_details():
    try:
        mydb = mysql.connector.connect(
            host="mysql",
            user="root",
            passwd="mypassword"
        )

        print("Printing all order_details ")
        mycursor = mydb.cursor()
        mycursor.execute("USE order_details")
        mycursor.execute("SELECT * FROM order_details")
        myresult = mycursor.fetchall()

        for x in myresult:
            print(x)
    except Error as e:
        print("Error while printing  order_details table  details ", e)






#method to retrive order details for homechef to  check order details from database
def customer_order_details(name):

    try:

        mydb = mysql.connector.connect(
            host="mysql",
            user="root",
            passwd="mypassword"
        )
        mycursor = mydb.cursor()
        mycursor.execute("USE order_details")
        mycursor.execute("select customer_name,customer_contact,customer_address,dish,quantity  from order_details where chef_name = '" + name + "' ")

        order_details = mycursor.fetchall() # data from database

        print(order_details)

        return order_details

    except Error as e:
        print("Error while printing customer order details", e)

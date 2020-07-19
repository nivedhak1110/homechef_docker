import mysql.connector
from mysql.connector import Error

try:
    mydb = mysql.connector.connect(
        host="mysql",
        user="root",
        passwd="mypassword"
        #database="signup"
    )

except Error as e:
    print("Error while connecting to MySQL", e)
            
# method to create database if not exist
def create_database():
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
def create_table():
    try:
        mydb = mysql.connector.connect(
        host="mysql",
        user="root",
        passwd="mypassword" )
            
        
        mycursor = mydb.cursor()
        mycursor.execute("USE signup")
        mycursor.execute("SHOW TABLES")
        tables = mycursor.fetchall()

        table_create = True
        for table in  tables :
            signup_table = "{0}".format(table[0])

            print(signup_table, flush=True)

            if (signup_table == "signup"):
                print("Signup table already created !", flush=True)
                table_create = False
                break
        if ( table_create ):
            mycursor.execute("CREATE TABLE signup (fname VARCHAR(20), lname VARCHAR(20) ,  email VARCHAR(20), password VARCHAR(20), category VARCHAR(20) , address VARCHAR(20))")
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
        
        

        print("Inside readInput")
        email_id = request.form.get('ID')
        passwd = request.form.get('password')
        print(email_id)
        print(passwd)
        #status = "success"
        status =  login_verify(email_id, passwd)
        print(status)
        return status
    except Error as e:
        print("Error while reading input ", e)
    
    



# verify login details


def login_verify(email_id, passwd):
    try:
        mydb = mysql.connector.connect(
        host="mysql",
        user="root",
        passwd="mypassword"
        #database="signup"
    )
        mycursor = mydb.cursor()
        mycursor.execute("USE signup")
        sql= "select count(email)   from signup where email= '" + email_id + "'"
        mycursor.execute(sql)
        count = mycursor.fetchone()
        print(count[0])
        if(count[0] == 1):
            sql = "select password   from signup where email= '" + email_id + "'"
            mycursor.execute(sql)
            myresult1 = str(mycursor.fetchone()[0])
            print(myresult1)

        else:
            print("the query doesnot return any value ")
            return "failed"

        sql = "select category   from signup where email= '" + email_id + "'"
        mycursor.execute(sql)
        myresult2 = str(mycursor.fetchone()[0])
        print(myresult2)

        try:
            if (passwd == myresult1  and myresult2 == "customer"):
                print("login success")
                return "customer"
            elif(passwd == myresult1  and myresult2 == "homechef"):
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


# print all signup details
def print_all():
    try:
        mydb = mysql.connector.connect(
        host="mysql",
        user="root",
        passwd="mypassword"
        #database="signup"
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
        password = request.form.get('password')
        category = request.form.get('category')
        address = request.form.get('add')
        signup_insert(fname, lname, email, password, category , address)
        return "success"
    except Error as e:
        print("Error while reading input ", e) ,
    
    
# save user signup  details in database
def signup_insert(fname, lname, email, password, category, address):
    try:
        mydb = mysql.connector.connect(
        host="mysql",
        user="root",
        passwd="mypassword"
        #database="signup"
    )
        mycursor = mydb.cursor()
        mycursor.execute("USE signup")
        sql = "INSERT INTO signup VALUES(%s,%s,%s,%s,%s,%s)"
        val = (fname, lname, email, password, category, address)
        mycursor.execute(sql, val)
        mydb.commit()
        print_all()

    except Error as e:
         print("Error while inserting into  table ", e)

            
# create   homechef database,create  homechef table

def create_database_homechef():
    try:
        mydb = mysql.connector.connect(
        host="mysql",
        user="root",
        passwd="mypassword"
         )
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
        passwd="mypassword"
         )
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
                "CREATE TABLE homechef ( ID VARCHAR(20) NOT NULL PRIMARY KEY , chef_name VARCHAR(20), date VARCHAR(20) ,  dish VARCHAR(40), cost int , availability int , time varchar(20) , location VARCHAR(20))")
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
        time = request.form.get('availtime')
        location = request.form.get('location')


        homechef_insert( ID, chef, date , dish, cost, availability, time , location)
        return "success"
    except Error as e:
        print("Error while reading input ", e)


# save  chef entries   in homechef database
def homechef_insert(ID, chef, date , dish, cost, availability, time,location):
    try:
        mydb = mysql.connector.connect(
        host="mysql",
        user="root",
        passwd="mypassword"
         )
        mycursor = mydb.cursor()
        mycursor.execute("USE homechef")
        sql = "INSERT INTO homechef VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (ID,chef, date , dish, cost, availability,time, location)
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


# retrive datas from database and print in customer dashboard
def print_data_customerDB(request):
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
        print(type(data))
        for i  in range(len(data)):
            print(data[0])
        return data


    except Error as e:
        print("Error while printing homechef table  details on customer dashboard", e)

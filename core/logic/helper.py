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
    finally:
        if (mydb.is_connected()):
            mycursor.close()
            mydb.close()
            print("MySQL connection is closed")
    
        
#  method to create signup table if not exist
def create_table():
    try:
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
            mycursor.execute("CREATE TABLE signup (fname VARCHAR(20), lname VARCHAR(20) ,  email VARCHAR(20), password VARCHAR(20), address VARCHAR(20))")
            print("Signup table  created !", flush=True)
    except Error as e:
        print("Error while creating table ", e)
    finally:
        if (mydb.is_connected()):
            mycursor.close()
            mydb.close()
            print("MySQL connection is closed")
    
    
    







"""
def check(request):
    print("Inside check")
    #email_id = ''
    email_id = request.form.get('uname')
    passwd = request.form.get('password')
    print(email_id)
    print(passwd)
    return "success" """

# Method to read login details

def read_input(request):
    try:

        print("Inside readInput")
        email_id = request.form.get('ID')
        passwd = request.form.get('password')
        print(email_id)
        print(passwd)
        #status = "success"
        status =  login_verify(email_id, passwd)
        return status
    except Error as e:
        print("Error while reading input ", e)


"""  except Exception as exception:
        print("Error ")
        print(exception.args[0])"""


# verify login details


def login_verify(email_id, passwd):
    try:
        mycursor = mydb.cursor()
        sql = "select password from signup where email= '" + email_id + "'"
        mycursor.execute(sql)
        myresult = str(mycursor.fetchone()[0])
        print(myresult)
        if (passwd == myresult):
            print("login success")
            mycursor.close()
            mydb.commit()
            print_all()
            return "success"
        else:
            print("login failed")
            return "failed"
    except Error as e:
        print("Error while verifying details ", e)


# print all database details
def print_all():
    try:
        print("Printing all DB data")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM signup")
        myresult = mycursor.fetchall()
        mycursor.close()

        for x in myresult:
            print(x)
    except Error as e:
        print("Error while printing DB details ", e)


# method to read  user input during signup


def get_input(request):
    try:
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        email = request.form.get('email')
        password = request.form.get('password')
        address = request.form.get('add')
        signup_insert(fname, lname, email, password, address)
        return "success"
    except Error as e:
        print("Error while reading input ", e)


# save user signup  details in database
def signup_insert(fname, lname, email, password, address):
    try:
        mycursor = mydb.cursor()
        sql = "INSERT INTO signup VALUES(%s,%s,%s,%s,%s)"
        val = (fname, lname, email, password, address)
        mycursor.execute(sql, val)
        mycursor.close()
        mydb.commit()
        print_all()

    except Error as e:
         print("Error while creating table ", e)

"""
def disp(request):

    data={
    "college":
    {
    "name":"ngpit", "depts":
    {

    "cse":[

    {"name":"nive", "rollno":"18cs040"},
    {"name":"priyu","rollno":"18cs046"}
    ],

    "IT":[
    {"name":"mothika","rollno":"18IT036"},
    {"name":"harini","rollno":"18IT053"}
    ],

    "ece":[
    {"name":"miruthu","rollno":"18EC035"},
    {"name":"yamuna","rollno":"18EC060"}
    ]

    }
    }
    }
    with open("sample.json","a") as fp:
        json.dump(data,fp)

return("printed details")"""



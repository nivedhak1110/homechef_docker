import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="mydata"
)


def print_all():
    print("Printing all DB data")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM emp")
    myresult = mycursor.fetchall()
    mycursor.close()

    for x in myresult:
        print(x)



def insert_data():
    print("Inserting data")
    # read input from user and insert into table
    mycursor = mydb.cursor()

    sql = "INSERT INTO emp VALUES(%s,%s,%s,%s,%s)"
    val= (3,"rahul",27,"chennai",4000)
    mycursor.execute(sql,val)
    mycursor.close()
    mydb.commit()
    print_all()


def update_data():
    print("Updating data")
    # update the any data
    mycursor = mydb.cursor()

    sql = "UPDATE emp SET address = 'pune' WHERE id=3"
    mycursor.execute(sql)
    mycursor.close()
    mydb.commit()
    print_all()


def print_only_one():
    print("print single user data")
    mycursor = mydb.cursor()

    sql="select id,name,age from emp where id=1"
    mycursor.execute(sql)
    myresult = mycursor.fetchone()
    print(myresult)
    mycursor.close()
    mydb.commit()
    print_all()

def delete_data():
    print("Delete user Data")
    # delete single row
    mycursor = mydb.cursor()

    sql = "DELETE FROM emp WHERE id =3"

    mycursor.execute(sql)
    mydb.commit()
    print_all()


def main():
    print_all()
    insert_data()
    update_data()
    print_only_one()
    delete_data()



if __name__ == "__main__":
    main()


"""
1 Method to read and verify user input
"""
def read_input(request):
    username = request.form.get('uname')
    password = request.form.get('password')
    print(username)
    print(password)
    # login is success if usernme is master , password is madam
    if username == "master" and password == "madam":
        print ("Login is success")
        return "success"
    else:
        return "failed"
    # method to read and disp user input
def disp_input(request):
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    email = request.form.get('email')
    password = request.form.get('password')
    address = request.form.get('add')
    print(fname)
    print(lname)
    print(email)
    print(password)
    print(address)
    fp=open("signupdetails.txt" ,"a")
    fp.write(fname)
    fp.write(lname)
    fp.write(email)
    fp.write(password)
    fp.write(address)
    fp.close()

    return ("printed details")
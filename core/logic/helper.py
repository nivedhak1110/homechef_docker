
"""
1 Method to read user input
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
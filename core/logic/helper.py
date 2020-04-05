
"""
1 Method to read user input
"""
def read_input(request):
    username = request.form.get('uname')
    password = request.form.get('password')
    print(username)
    print(password)
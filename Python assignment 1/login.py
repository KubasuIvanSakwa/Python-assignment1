cridentials = ['Ivan', 'Private']

userName = str(input("Enter Username: \n"))
password = str(input('Enter password: \n'))

if userName != cridentials[0] or password != cridentials[1]:
    print("invalid credentials")
else:
    print("Login Successful")

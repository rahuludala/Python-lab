username = "admin"
password = "1234"

u = input("Enter username: ")
p = input("Enter password: ")

login_success = (u == username) and (p == password)

print("Login Successful:", login_success)

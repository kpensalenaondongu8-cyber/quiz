from create_acct import create_acct

import time

print("--- 1.Login. ---\n--- 2.SignUp ---")
print()
user_input1 =  input("select mode: ")
print()
if user_input1 ==  "SignUp" or user_input1 == "2":
    print("---- fill the spaces bellow ----")
    print()
    first_name = input("Enter first name: ")
    middle_name = input("Enter middle name: ")
    last_name = input("Enter last name: ")
    number = input("Enter number: ")
    password = input("Enter password: ")
    create_acct(first_name, middle_name, last_name, number, password)
    print()
    time.sleep(2)
    print("----- Account created successfully -----")
    print()


elif user_input1 == "Login" or user_input1 == "1":
    number = input("Enter registered number: ")
    password = input("Enter Password: ")
    print()
    time.sleep(2)
    print("---- Login Successfully ----")
    print()





print("select: \n1.Quiz\n2.Lessons")
print()

user_input = input("select:  ")


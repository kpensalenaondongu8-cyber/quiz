from create_acct import create_acct
from login import login
import time
from pathlib import Path
from quiz_subjects.biology_quiz import biology_quiz
from quiz_subjects.chemistry_quiz import chemistry_quiz
from quiz_subjects.physics_quiz import physics_quiz
from quiz_subjects.python_quiz import python_quiz 
from quiz_subjects.current_aff_quiz import current_affairs_quiz
from quiz_subjects.golang_quiz import golang_quiz
from quiz_subjects.math_quiz import math_quiz
from quiz_subjects.java_script_quiz import java_script_quiz




print("--- 1.Login. ---\n--- 2.SignUp ---")
print()
user_input1 =  input("select mode: ")
print()

project_dir = Path(__file__).resolve().parent
file_path = project_dir /"quiz_subjects"
questions_path = project_dir /"questions"


while True: 
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

            try:
                number = input("Enter registered number: ")

            except ValueError:
                print("Invalid Sytax") 
            password = input("Enter Password: ")
            time.sleep(2)
            login(number, password)
            print()
            time.sleep(2)




        print("select: \n1.Quiz\n2.Lessons\n3.Exit")
        print()

        user_input2 = input("select:  ")

        if user_input2 == "1" or user_input2 == "Quiz":

            available_quizzes = list(questions_path.glob("*.json"))
            print("----- Available Quizzes -----")
            print()
            for index, path in enumerate(available_quizzes, 1):
                 print(f"{index}. {path.stem.capitalize()}")

            print()
            choice = input("Select a number: ")

            if choice == "1":
                  biology_quiz()

            elif choice == "2":
                 chemistry_quiz()

            elif choice == "3": 
                 current_affairs_quiz()

            elif choice == "4":
                 physics_quiz()

            elif choice == "5":
                 golang_quiz()

            elif choice == "6":
                 math_quiz()

            elif choice == "7":
                 python_quiz()

            elif choice == "8":
                 java_script_quiz()

            else:
                 print("subject not available now")                                            
             
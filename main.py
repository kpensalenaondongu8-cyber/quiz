from create_acct import create_acct
from login import login
import time
from pathlib import Path
from quiz_subjects.quiz import run_quiz
from lesson_subjects.lessons import lessons
from read_history import show_history 



project_dir = Path(__file__).resolve().parent
file_path = project_dir /"quiz_subjects"
questions_path = project_dir /"questions"
lessons_path = project_dir /"lesson_subjects"
lessons_file = project_dir/"lessons"


while True: 
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
            time.sleep(1)
            logged_in = login(number, password)
            if logged_in:
                 login(number, password)
                 print("Loggin Succesful!")
                 print()
                 time.sleep(1)
            else:
                 print('You cant access the dashboard')
                 print()
                 continue     
        else:
            print("Enter the above values")
            print() 
            continue
              



        while True:
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

                if choice == "1": run_quiz('biology')

                elif choice == "2":run_quiz('chemistry')

                elif choice == "3": run_quiz('current_affairs')

                elif choice == "4":run_quiz('physics')

                elif choice == "5":run_quiz('golang')

                elif choice == "6":run_quiz('math')

                elif choice == "7":run_quiz('python')

                elif choice == "8": run_quiz('java_script')

                elif choice == "9": show_history()

                else:
                    print("subject not available now")
                    print()

            elif user_input2 == "2":
                available_lessons = list(lessons_file.glob("*.txt"))
                print("-------- AVAILABLE-LESSONS --------")
                print()
                for index, path in enumerate(available_lessons, 1):
                        print(f"{index}. {path.stem.capitalize()}")
                        print()

                choice2 = input("Select choice: ")
                print()

                if choice2 == "1":lessons('physics')

                elif choice2 == "2":
                    lessons('biology')

                elif choice2 == "3":    
                    lessons('math')

                elif choice2 == "4":
                    lessons('golang')

                elif choice2 == "5":
                    lessons('current_affairs')

                elif choice2 == "6":
                    lessons('python')

                elif choice2 == "7":
                    lessons('java_script') 

                elif choice2 == "8":
                    lessons('chemistry')
                else:
                        print("Subject unavailable")
                        print()                          

            elif user_input2 == "3":
                print()
                print()
                break           
            
            else:
                print("Enter the above digits")
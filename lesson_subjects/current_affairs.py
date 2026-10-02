from pathlib import Path

def current_affairs_lesson():
    print("====================================")
    print("      WELCOME TO THE LESSONS BOT    ")
    print("           CURRENT_AFFAIRS               ")
    print("    take your lessons. Good luck!")
    print("====================================\n")
    
    dir_path = Path(__file__).resolve().parent
    file_path = dir_path.parent /"lessons"/"current_Affairs.txt"


    try:   
        with open(file_path, "r") as file:
            data = file.read()
            print(data)

    except FileNotFoundError:
        print(f"file not found at {file_path}")        
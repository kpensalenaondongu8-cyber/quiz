from pathlib import Path

def lessons(lessons_subject):
    print("====================================")
    print("      WELCOME TO THE LESSONS BOT    ")
    print(f"         {lessons_subject}                  ")
    print("    take your lessons. Good luck!")
    print("====================================\n")

    dir_path = Path(__file__).resolve().parent
    file_path = dir_path.parent/"lessons"/f"{lessons_subject}.txt"

    try:
        with open(file_path, "r") as file:
            data = file.read()
            print(data)

    except FileNotFoundError:
        print(f"file nor found at {file_path}")        

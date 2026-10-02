from pathlib import Path

def math_lesson():
    print("====================================")
    print("      WELCOME TO THE LESSONS BOT    ")
    print("            MATHEMATICS               ")
    print("    take your lessons. Good luck!")
    print("====================================\n")

    dir_path = Path(__file__).resolve().parent
    file_path = dir_path.parent/"lessons"/"maths.txt"
    
    try:
        with open(file_path, "r") as file:
            data = file.read()
            print(data)

    except FileNotFoundError:
        print(f"didnt find file at {file_path}")        
    
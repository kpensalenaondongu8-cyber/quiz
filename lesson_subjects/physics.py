from pathlib import Path

def physics_lessons():
    print("====================================")
    print("      WELCOME TO THE LESSONS BOT    ")
    print("              PHYSICS               ")
    print("    take your lessons. Good luck!")
    print("====================================\n")

    dir_path = Path(__file__).resolve().parent
    file_path = dir_path.parent/"lessons"/"physics.txt"

    try:
        with open(file_path, "r") as file:
            data = file.read()
            print(data)

    except FileNotFoundError:
        print(f"Didnt find file at {file_path}")        
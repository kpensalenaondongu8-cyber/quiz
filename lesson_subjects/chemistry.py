from pathlib import Path



def chemistry_lesson():
    print("====================================")
    print("      WELCOME TO THE LESSONS BOT    ")
    print("            CHEMISTRY             ")
    print("    take your lessons. Good luck!")
    print("====================================\n")

    dir_path = Path(__file__).resolve().parent
    file_path = dir_path.parent /"lessons"/"chemistry.txt"

    try:
        with open(file_path, "r") as file:
                data = file.read() 
                print(data)

    except FileNotFoundError: 
        print(f"file not found at {file_path}")
            
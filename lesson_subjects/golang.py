from pathlib import Path

def golang_lesson():
    print("====================================")
    print("      WELCOME TO THE LESSONS BOT    ")
    print("            GOLANG             ")
    print("    take your lessons. Good luck!")
    print("====================================\n")

    dir_path = Path(__file__).resolve().parent
    file_path = dir_path.parent /"lessons"/"golang.txt"
    
    try:
        with open(file_path, "r") as file:
            data = file.read()
            print(data)

    except FileNotFoundError:
        print(f"File not found at {file_path}")
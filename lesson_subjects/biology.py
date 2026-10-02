from pathlib import Path

def biology_lesson():
    print("====================================")
    print("      WELCOME TO THE LESSONS BOT    ")
    print("           BIOLOGY               ")
    print("    take your lessons. Good luck!")
    print("====================================\n")

    current_dir = Path(__file__).resolve().parent

    file_path = current_dir.parent /"lessons"/"biology.txt"

    try:
        with open(file_path, "r") as file:
            file_content = file.read()
            print(file_content)             


    except FileNotFoundError:
            print(f"couldnt find the file at {file_path}")
            print("make sure lessons and biology exist in your director")
            return None


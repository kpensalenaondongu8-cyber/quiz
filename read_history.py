from pathlib import Path

def show_history():
    history_file = Path(__file__).resolve().parent/ "quiz_history.json"


    print("\n========================= QUIZ HISTORY =========================")
    if not history_file.exists():
        print("No quiz history found yet. Take yout first quiz to log your first ")
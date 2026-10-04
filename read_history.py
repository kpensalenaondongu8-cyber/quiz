from pathlib import Path
import json

def show_history():
    history_file = Path(__file__).resolve().parent/ "quiz_history.json"


    print("\n========================= QUIZ HISTORY =========================")
    if not history_file.exists():
        print("No quiz history found yet. Take yout first quiz to log your first score ")
        print("================================================================")
        return
    
    with open(history_file, "r") as file:
        try:
            history_data = json.load(file)
        except json.JSONDecodeError:
            print("History file is empty or corrupted")
            return

    print(f"{'Date & Time':<20} | {'Subject':<12} | {'Score':<8} | {'Percentage':<10}")
    print("-"*64)


    for entry in reversed(history_data):  
        print(f"{entry['timestamp']:<20} | {entry['subject']:<12} | {entry['score']:<8} | {entry['percentage']:<10}")
    print("================================================================\n")

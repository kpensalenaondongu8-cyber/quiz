from datetime import datetime
from pathlib import Path
import json

def save_quiz_result(subject_name, score, total_questions):

    history_file = Path(__file__).resolve().parent/ "quiz_history.json"

    percentage = (score/total_questions) * 100

    result_entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "subject": subject_name,
        "score": f"{score}/{total_questions}",
        "percentage": f"{percentage:.1f}%"
    }

    if history_file.exists():
        with open(history_file, "r") as file:
            try:
                history_data = json.load(file)
            except json.JSONDecodeError: 
                history_data = []   

    else:
        history_data = []
        
    history_data.append(result_entry)
    with open(history_file, "w") as file:
        json.dump(history_data, file, indent=4)     

        
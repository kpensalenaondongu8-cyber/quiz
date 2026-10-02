from pathlib import Path
import time
import json

def chemistry_quiz():
    print("====================================")
    print("      WELCOME TO THE QUIZ BOT    ")
    print("            CHEMISTRY            ")
    print("Prepare for your exams. Good luck!")
    print("====================================\n")
    
    current_dir = Path(__file__).resolve().parent
    file_path = current_dir.parent /"quiz" /"questions" /"python.json"
    try:
      with open(file_path, "r") as file:
        all_data = json.load(file)  
    except FileNotFoundError:
        print(f"\n❌ Error: Could not find your JSON file at: {file_path}")
        print("Please check that the 'questions' folder and 'python.json' exist inside your project.")
        return
     
    quiz_questions = all_data['python']

    score = 0
    total_questions = len(quiz_questions)
    
    for index, item in enumerate(quiz_questions, 1):
        print(f"Question {index}: {item['question']}")
        
        for option in item['options']:
            print(option)
            
        user_guess = input("\nYour answer (A, B, C, or D): ").strip().upper()
        
        if user_guess == item['correct_answer']:
            print("✅ Correct! Brilliant.\n")
            score += 1
        else:
            print(f"❌ Incorrect. The correct answer was {item['correct_answer']}.\n")
            print("getting explanation....... ")
            time.sleep(1)
            print()
            print(item['explanation'])
            time.sleep(1)
  
        time.sleep(1) 
        print("-" * 40)

    print("\n========================= RESULTS =========================")
    print(f"You scored {score} out of {total_questions}!")
    
    percentage = (score / total_questions) * 100
    print(f"Percentage: {percentage:.1f}%")
    
    if percentage >= 70:
        print("Status: Excellent! You are fully ready for JAMB/WAEC. 🎉")
    elif percentage >= 50:
        print("Status: Pass. Put in a bit more study time! 👍")
    else:
        print("Status: Keep practicing! Failure is just an opportunity to learn. 💪")
    print("===========================================================")
from pathlib import Path
import time
import json

def python_quiz():
    print("====================================")
    print("      WELCOME TO THE QUIZ BOT    ")
    print("Prepare for your exams. Good luck!")
    print("====================================\n")
    
    current_dir = Path(__file__).resolve().parent
    file_path = current_dir.parent /"quiz" /"questions" /"python.json"
    try:
      with open(file_path, "r") as file:
        all_data = json.load(file)  
    except FileNotFoundError:
        print(f"\n❌ Error: Could not find your JSON file at: {file_path}")
        print("Please check that the 'questions' folder and 'python.json' exist inside your project.")
        return
     
    quiz_questions = all_data['chemistry']

    score = 0
    total_questions = len(quiz_questions)
    
    for index, item in enumerate(quiz_questions, 1):
        print(f"Question {index}: {item['question']}")
        
        for option in item['options']:
            print(option)
            
        user_guess = input("\nYour answer (A, B, C, or D): ").strip().upper()
        
        if user_guess == item['correct_answer']:
            print("✅ Correct! Brilliant.\n")
            score += 1
        else:
            print(f"❌ Incorrect. The correct answer was {item['correct_answer']}.\n")
            print("getting explanation....... ")
            time.sleep(1)
            print()
            print(item['explanation'])
            time.sleep(1)
  
        time.sleep(1) 
        print("-" * 40)

if __name__ == "__main__":
    chemistry_quiz()

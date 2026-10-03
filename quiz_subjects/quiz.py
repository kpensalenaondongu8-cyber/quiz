from pathlib import Path
import time
import json
import random

def run_quiz(subject_name):
    print("====================================")
    print("      WELCOME TO THE QUIZ BOT    ")
    print(f"        {subject_name.upper()}      ")
    print("Prepare for your exams. Good luck!")
    print("====================================\n")
    
    current_dir = Path(__file__).resolve().parent
    file_path = current_dir.parent /"questions" /f"subject_name.lower()"

    try:
      with open(file_path, "r") as file:
        all_data = json.load(file)  
    except FileNotFoundError:
        print(f"\n❌ Error: Could not find your JSON file at: {file_path}")
        print(f"Please check that the 'questions {subject_name.lower()}' exist inside your project.")
        return
     
    quiz_questions = (all_data[subject_name.lower()])

    random.shuffle(quiz_questions)

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
        elif user_guess not in ['A', 'B', 'C', "'D"]:
            print("invalid option moving to next question")    
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
        print("Status: Excellent!. 🎉")
    elif percentage >= 50:
        print("Status: Pass. Put in a bit more study time! 👍")
    else:
        print("Status: Keep practicing! Failure is just an opportunity to learn. 💪")
    print("===========================================================")

if __name__ == "__main__":
    run_quiz()

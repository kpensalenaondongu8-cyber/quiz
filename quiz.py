import time

quiz_questions = [
    {
        "question": "Which of the following is a physical change?",
        "options": ["A. Burning of wood", "B. Melting of ice", "C. Rusting of iron", "D. Souring of milk"],
        "correct_answer": "B"
    },
    {
        "question": "In Nigeria, the National Youth Service Corps (NYSC) was established in what year?",
        "options": ["A. 1960", "B. 1973", "C. 1999", "D. 2011"],
        "correct_answer": "B"
    },
    {
        "question": "If 2x + 5 = 15, what is the value of x?",
        "options": ["A. 5", "B. 10", "C. 7", "D. 3"],
        "correct_answer": "A"
    }
]

def run_quiz():
    print("====================================")
    print("🇳🇬 WELCOME TO THE NAIJA QUIZ BOT 🇳🇬")
    print("Prepare for your exams. Good luck!")
    print("====================================\n")
    
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

if __name__ == "__main__":
    run_quiz()

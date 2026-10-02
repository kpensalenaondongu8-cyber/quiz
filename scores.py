def scores(score, total_questions):
     

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

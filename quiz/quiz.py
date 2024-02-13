import random

questions = [
    {"question_text": "1. Which gas do plants absorb during photosynthesis?",
     "options": ["A. Oxygen", "B. Carbon dioxide", "C. Nitrogen", "D. Hydrogen"],
     "correct_answer": "B"},
    {"question_text": "2. What is the SI unit of force?",
     "options": ["A. Newton", "B. Watt", "C. Joule", "D. Pascal"],
     "correct_answer": "A"},
    {"question_text": "3. What is the chemical symbol for water?",
     "options": ["A. Wo", "B. H2O", "C. Co2", "D. H2SO4"],
     "correct_answer": "B"},
    {"question_text": "4. What is the process of conversion of water vapor into liquid water called?",
     "options": ["A. Condensation", "B. Evaporation", "C. Sublimation", "D. Precipitation"],
     "correct_answer": "A"},
    {"question_text": "5. What is the largest organ in the human body?",
     "options": ["A. Liver", "B. Skin", "C. Heart", "D. Lungs"],
     "correct_answer": "B"},
    {"question_text": "6. Which planet is known as the Red Planet?",
     "options": ["A. Jupiter", "B. Mars", "C. Venus", "D. Saturn"],
     "correct_answer": "B"},
    {"question_text": "7. What is the pH of pure water?",
     "options": ["A. 0", "B. 7", "C. 14", "D. 10"],
     "correct_answer": "B"},
    {"question_text": "8. Which metal is the best conductor of electricity?",
     "options": ["A. Aluminum", "B. Copper", "C. Iron", "D. Silver"],
     "correct_answer": "D"},
]

random.shuffle(questions)

score = 0

for question in questions:
    print("-----------------------")
    print(f"{question['question_text']}\n")

    for option in question["options"]:
        print(f"{option}\n")

    user_input = input("Enter your answer: ").strip().upper()
    question["user_input"] = user_input

    print()

for index, question in enumerate(questions):
    if question["user_input"] == question["correct_answer"]:
        score += 1
        print(f"{index + 1}. Correct answer!\n")
    else:
        print(f"{index + 1}. Wrong answer, the correct answer is {question['correct_answer']}\n")

result = score / len(questions)
print(f"You scored {score}/{len(questions)} ({result * 100:.2f}%).")
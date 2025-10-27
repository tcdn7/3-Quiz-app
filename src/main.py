from question import Question
from storage import load_questions_from_json

def get_user_name():
    while True:
        name = input("Enter your name: ").strip()
        if name:
            return name
        else:
            print("Name cannot be empty. Please try again.")

def ask_ready():
    attempts = 0
    while attempts < 3:
        ready= input("Are you ready? (yes/no): ").strip().lower()
        if ready in ["yes", "y"]:
            print("Great, let's start!")
            return True
        elif ready in ["no", "n"]:
            print("No worries, see you next time!")
            return False
        else:
            attempts += 1
            print("Please enter \"yes\" or \"no\". Try again.")
            if attempts == 3:
               print("Too many invalid attempts.")
               return False 
            
def ask_question(q: Question) -> bool:
    """Show the question, get an answer, and return True if correct"""
    print("\n" + q.text)
    for opt in q.options:
        print(opt)

    user_answer = input("Your answer (A/B/C/D): ").strip().upper()

    if user_answer not in {"A", "B", "C", "D"}:
        print("Invalid choice. Please answer with A, B, C, or D.")
        return False

    if q.check_answer(user_answer):
        print("Correct!")
        return True
    else:
        print(f"Wrong! The correct answer was {q.answer}.")
        return False

def run_quiz(questions):
    correct = 0
    for q in questions:
        result = ask_question(q)
        if result:
            correct += 1

    print(f"\nYou answered {correct} out of {len(questions)} correctly.")
    percentage = round(100 * correct / len(questions), 2)
    print(f"Your score: {percentage}%")
                        

if __name__ == "__main__":
    name = get_user_name()
    print(f"Hello, {name}! Let's start the quiz.")
    ready = ask_ready()
    
    if not ready:
        exit()
    else:
        print("Starting the quiz...")

        try:
            questions = load_questions_from_json("data/questions.json")
        except (FileNotFoundError, ValueError) as e:
            print(f"Error while loading questions: {e}")
            exit()


        run_quiz(questions)
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

if __name__ == "__main__":
    name = get_user_name()
    print(f"Hello, {name}! Let's start the quiz.")
    ready = ask_ready()
    
    if not ready:
        exit()
    else:
        print("Starting the quiz...")    
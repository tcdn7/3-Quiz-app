# 🎯 Quiz App

A simple yet functional **Quiz Application** built with **Python**.  
Users can enter their name, confirm readiness, and answer multiple-choice questions loaded dynamically from a JSON file.  
At the end, the app displays the total score and percentage of correct answers.  

---

## 🧩 Features

- 🧠 **Dynamic Questions:** Questions are loaded from `data/questions.json`.
- 📝 **Input Validation:** Ensures valid user inputs for name and answers.
- 💬 **Interactive Flow:** Step-by-step quiz experience via the terminal.
- 🧾 **Score Summary:** Shows total correct answers and percentage.
- 💾 **Modular Code Structure:** Divided into separate Python files:
  - `main.py` – main quiz logic  
  - `question.py` – question model class  
  - `storage.py` – JSON loader and schema validation  

---

## 🗂️ Project Structure

\`\`\`
quiz-app/
  ├─ data/
  │  └─ questions.json
  ├─ src/
  │  ├─ main.py
  │  ├─ question.py
  │  └─ storage.py
  ├─ .gitignore
  └─ README.md
\`\`\`



---


---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/tcdn7/3-quiz-app.git
   cd 3-quiz-app

2. (Optional) Create and activate a virtual environment:
    python -m venv .venv
    .venv\Scripts\activate      # on Windows
    source .venv/bin/activate   # on macOS/Linux

3. Run the app:
    python src/main.py

4. Enjoy your quiz! 🎉

---

🧠 Example Output
    Welcome to the Quiz App!
    Enter your name: Mehmet
    Hello, Mehmet! Let's start the quiz.
    Are you ready? (yes/no): y
    Starting the quiz...

    What is the capital of France?
    A) Paris
    B) Rome
    C) Madrid
    D) Berlin
    Your answer (A/B/C/D): A
    Correct!

    You answered 3 out of 3 correctly.
    Your score: 100.0%

---

🛠️ Technologies Used

    Python 3.10+

    JSON for data storage

    VS Code for development

---

👨‍💻 Author

    Tacdin Özmen
    📍 Python Developer | Data Science Learner
    🔗 GitHub: tcdn7

---

🏁 License

    This project is licensed under the MIT License — feel free to use and modify.

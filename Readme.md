# 🧠 Python Quiz & Learning App

A command-line learning application built with Python that allows users to create accounts, log in, take quizzes across different subjects, study educational lessons, and track their quiz performance.

The project combines interactive quizzes with learning materials to help users test their knowledge, understand their mistakes, and improve their understanding of different subjects.

## 📌 Table of Contents

- [About the Project](#-about-the-project)
- [Features](#-features)
- [Available Subjects](#-available-subjects)
- [Technologies Used](#-technologies-used)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [How to Use](#-how-to-use)
- [How the Application Works](#-how-the-application-works)
- [What I Learned](#-what-i-learned)
- [Future Improvements](#-future-improvements)
- [Author](#-author)

## 📖 About the Project

The Python Quiz & Learning App is a terminal-based educational application designed to make learning and self-assessment more interactive.

Users can create accounts, log in, choose a subject, answer multiple-choice questions, receive feedback, and view their quiz results. The application also provides educational lessons that users can read before testing their knowledge.

Questions are stored in JSON files, while lessons are maintained in text files. This approach separates educational content from the main application logic, making the project easier to organize and extend.

This project was built as a practical way to strengthen my Python programming skills while learning how to structure a multi-file application.

## ✨ Features

### 👤 User Accounts
- Create an account with personal details and a password.
- Log in using registered credentials.
- Validate user input during account creation.
- Store user information in a JSON file.

### 📝 Interactive Quizzes
- Choose from multiple quiz subjects.
- Answer multiple-choice questions.
- Receive immediate feedback on answers.
- View the correct answer and its explanation when an answer is incorrect.
- Questions are shuffled before each quiz.
- Receive a final score and percentage after completing a quiz.

### 📊 Performance Evaluation
The application evaluates quiz performance based on the percentage scored.

- **70% and above:** Excellent!
- **50%–69.9%:** Pass.
- **Below 50%:** Keep practicing!

### 📚 Educational Lessons
- Access lessons for supported subjects.
- Read educational materials directly in the terminal.
- Study lesson content before attempting a quiz.

### 📅 Quiz History
- Save quiz results to a JSON file.
- Record the date and time of each result.
- Store the subject, score, and percentage.
- View previous quiz attempts.

### 🗂️ Organized Learning Content
- Store quiz questions in separate JSON files.
- Store lesson materials in separate text files.
- Keep application functionality organized across multiple Python modules.

## 📚 Available Subjects

The project contains quiz question files for the following subjects:

| Subject | Quiz Questions | Lesson Materials |
|---|---|---|
| Biology | Available | Available |
| Chemistry | Available | Available |
| Current Affairs | Available | Available |
| Mathematics | Available | Available |
| Physics | Available | Available |
| Python | Available | Available |
| JavaScript | Available | Available |
| Go (Golang) | Available | Available |

## 🛠️ Technologies Used

- **Python 3** — Main programming language.
- **JSON** — Stores user information, quiz questions, and quiz history.
- **Text files** — Store educational lesson materials.
- **Pathlib** — Helps locate project files and directories.
- **Random** — Shuffles quiz questions.
- **Datetime** — Records the date and time of quiz attempts.
- **Git & GitHub** — Version control and project hosting.

The project currently uses Python's standard library and does not require third-party packages.

## 📁 Project Structure

```text
quiz/
│
├── main.py
│
├── create_acct.py
├── login.py
├── history.py
├── read_history.py
│
├── users.json
├── quiz_history.json
│
├── questions/
│   ├── biology.json
│   ├── chemistry.json
│   ├── current_affairs.json
│   ├── geography.json
│   ├── golang.json
│   ├── java_script.json
│   ├── math.json
│   ├── physics.json
│   └── python.json
│
├── lessons/
│   ├── biology.txt
│   ├── chemistry.txt
│   ├── current_afairs.txt
│   ├── golang.txt
│   ├── java_Script.txt
│   ├── maths.txt
│   ├── physics.txt
│   └── python.txt
│
├── quiz_subjects/
│   └── quiz.py
│
└── lesson_subjects/
    └── lessons.py
```

### Main Files Explained

| File | Responsibility |
|---|---|
| `main.py` | Entry point of the application. Handles the main menus, account flow, and subject selection. |
| `create_acct.py` | Creates user accounts and saves user information. |
| `login.py` | Checks login credentials against stored user information. |
| `quiz_subjects/quiz.py` | Loads questions, runs quizzes, checks answers, calculates scores, and saves results. |
| `lesson_subjects/lessons.py` | Loads and displays educational lesson materials. |
| `history.py` | Saves quiz results and timestamps. |
| `read_history.py` | Displays previously recorded quiz results. |
| `questions/` | Contains the quiz questions in JSON format. |
| `lessons/` | Contains educational materials in text format. |
| `users.json` | Stores registered user information. |
| `quiz_history.json` | Stores recorded quiz results. |

## 🚀 Getting Started

Follow these steps to run the project on your computer.

### Prerequisites

You need:

- Python 3 installed on your computer.
- A terminal or command-line application.
- Git (optional, if you want to clone the repository).

Check whether Python is installed:

```bash
python3 --version
```

### 1. Clone the Repository

Replace `YOUR_USERNAME` with your GitHub username.

```bash
git clone https://github.com/kpensalenaondongu8-cyber/quiz.git
```

### 2. Navigate to the Project Directory

```bash
cd quiz
```

If you downloaded the project as a ZIP file, extract it and navigate into the extracted `quiz` directory instead.

### 3. Run the Application

```bash
python3 main.py
```

On Windows, you can also use:

```bash
python main.py
```

No additional package installation is currently required.

## 🎮 How to Use

### Step 1: Create an Account or Log In

When the application starts, you will see the account menu:

```text
--- 1.Login. ---
--- 2.SignUp ---
```

Choose `1` to log in or `2` to create an account.

Follow the prompts to enter your details.

### Step 2: Choose an Activity

After the account flow, the application presents the main menu:

```text
1. Quiz
2. Lessons
3. Exit
```

Choose an activity by entering its corresponding number.

### Step 3: Take a Quiz

Select the quiz option and choose an available subject.

Read each question and enter your answer using the available options:

```text
Your answer (A, B, C, or D):
```

The application checks your answer and provides feedback.

When you finish, your score and percentage are displayed.

### Step 4: Study a Lesson

Choose the lessons option and select an available subject.

The application reads the corresponding text file and displays the lesson in the terminal.

### Step 5: Review Quiz History

Use the quiz history functionality to review recorded attempts, including their timestamps, subjects, scores, and percentages.

## ⚙️ How the Application Works

The application is divided into smaller modules, each responsible for a particular task.

1. **User interaction:** `main.py` displays menus and collects input.
2. **Account management:** `create_acct.py` handles account creation, while `login.py` checks credentials.
3. **Quiz execution:** `quiz.py` loads questions from JSON files, shuffles them, accepts answers, and calculates results.
4. **Lesson delivery:** `lessons.py` reads educational content from text files.
5. **Result tracking:** `history.py` records quiz results, while `read_history.py` displays saved history.

Separating these responsibilities makes the code easier to understand, maintain, and improve.

## 🎓 What I Learned

Building this project helped me practice several important programming concepts:

- **Functions and modular programming:** Dividing an application into reusable functions and separate Python modules.
- **File handling:** Reading from and writing to JSON and text files.
- **Data structures:** Working with dictionaries, lists, and nested data.
- **Control flow:** Using loops, conditionals, and menu-driven interactions.
- **Input validation:** Checking user input before processing it.
- **Exception handling:** Handling situations such as missing files and invalid JSON data.
- **Path management:** Using `pathlib` to locate project files.
- **Randomization:** Shuffling questions to vary the quiz experience.
- **Date and time handling:** Recording when quiz attempts occur.
- **Application design:** Organizing a multi-file Python project with separate responsibilities.
- **Version control:** Using Git to manage changes and GitHub to host the project.

## 🔮 Future Improvements

The project provides a foundation that can be extended with additional features.

Potential improvements include:

- [ ] Improve password security by hashing passwords instead of storing them as plain text.
- [ ] Add stronger account validation and prevent duplicate registrations.
- [ ] Associate quiz history with the currently logged-in user.
- [ ] Improve error handling for missing, empty, or invalid question files.
- [ ] Add more questions and explanations across all subjects.
- [ ] Allow users to select quiz difficulty levels.
- [ ] Add a timer for each quiz.
- [ ] Track progress across multiple attempts.
- [ ] Add leaderboards and user rankings.
- [ ] Introduce a graphical user interface or web interface.
- [ ] Move from JSON files to a database such as SQLite as the application grows.
- [ ] Add automated tests for account creation, login, quizzes, and result tracking.

## 🔐 Security Note

This project is an educational application and is still a work in progress.

The current implementation stores passwords as plain text in `users.json`. This is not appropriate for a production application. Password hashing, safer authentication practices, and better user-data protection should be implemented before the application is used to store real user credentials.

The application also currently stores quiz history in a shared JSON file rather than associating every result with an authenticated user.

## 🤝 Contributions

Suggestions, bug reports, and improvements are welcome.

If you would like to contribute:

1. Fork the repository.
2. Create a new branch for your changes.
3. Make and test your changes.
4. Commit your changes.
5. Open a pull request.

## 👨‍💻 Author

**KPENSALEN THOMAS AONDONGU**

Python Developer in Progress

This project represents part of my journey toward becoming a better software developer through practical programming, problem-solving, and continuous learning.

---

⭐ If you find this project useful, consider giving the repository a star!
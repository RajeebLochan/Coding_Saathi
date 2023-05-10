import time

# Database or data storage for user credentials, profiles, questions, answers, etc.
users = {
    "admin": {
        "password": "password123",
        "profile": {
            "name": "Your Name",
            "email": "Your@mail.com"
        }
    }
}

questions = {
    1: {
        "question": "What is the capital of France?",
        "options": ["A. London", "B. Paris", "C. Rome", "D. Madrid"],
        "correct_answer": "B"
    },
    2: {
        "question": "Who painted the Mona Lisa?",
        "options": ["A. Michelangelo", "B. Leonardo da Vinci", "C. Vincent van Gogh", "D. Pablo Picasso"],
        "correct_answer": "B"
    },
    3: {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Mars", "B. Venus", "C. Jupiter", "D. Saturn"],
        "correct_answer": "A"
    },
    4: {
        "question": "What is the chemical symbol for gold?",
        "options": ["A. Go", "B. Au", "C. Ag", "D. Fe"],
        "correct_answer": "B"
    }
    # Add more questions here
}

# Global variables
current_user = None
selected_answers = {}

# Login Functionality
def login():
    global current_user
    print("=== Login ===")
    username = input("Username: ")
    password = input("Password: ")
    if username in users and users[username]["password"] == password:
        current_user = username
        print("Login successful!")
        dashboard()
    else:
        print("Invalid username or password. Please try again.")
        login()

# Update Profile and Password
def update_profile_and_password():
    print("=== Update Profile and Password ===")
    print("Current Profile:")
    print(users[current_user]["profile"])
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Enter your new password: ")
    users[current_user]["profile"]["name"] = name
    users[current_user]["profile"]["email"] = email
    users[current_user]["password"] = password
    print("Profile and password updated successfully!")
    dashboard()

# Selecting answers for MCQs
def select_answers():
    print("=== Select Answers for MCQs ===")
    for qid, question in questions.items():
        print("\nQuestion {}: {}".format(qid, question["question"]))
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer (A, B, C, D): ")
        selected_answers[qid] = answer
    print("Answers submitted successfully!")
    dashboard()

# Timer function
def start_timer(duration):
    print("Starting timer...")
    time.sleep(duration)

# Timer and Auto-submit
def timer_and_auto_submit():
    print("=== Timer and Auto-submit ===")
    print("Preparing for the exam...")
    start_timer(60)  
    print("The exam has started. You have 30 minutes to complete the exam.")
    start_time = time.time()
    end_time = start_time + 300 
    while time.time() < end_time:
        pass
    print("Time's up! Your exam has been submitted.")
    display_result()
    dashboard()

def logout():
    global current_user
    print("Closing session and logging out...")
    current_user = None
    print("Logged out successfully!")
    login()

# Dashboard
def dashboard():
    print("\n=== Dashboard ===")
    print("Welcome, {}".format(users[current_user]["profile"]["name"]))
    print("1. Update Profile and Password")
    print("2. Select Answers for MCQs")
    print("3. Start Exam")
    print("4. Logout")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        update_profile_and_password()
    elif choice == "2":
        select_answers()
    elif choice == "3":
        timer_and_auto_submit()
    elif choice == "4":
        logout()
    else:
        print("Invalid choice. Please try again.")
        dashboard()

# Start Exam
def timer_and_auto_submit():
    print("=== Exam ===")
    print("The exam has started. You have 30 minutes to complete the exam.")
    start_time = time.time()
    end_time = start_time + 1800  # 30 minutes

    for qid, question in questions.items():
        print("\nQuestion {}: {}".format(qid, question["question"]))
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer (A, B, C, D): ")
        selected_answers[qid] = answer
        print("Answer submitted for Question {}".format(qid))

    print("All questions answered. Your exam has been submitted.")
    display_result()
    time.sleep(5)
    dashboard()

# Display Exam Result
def display_result():
    print("\n=== Exam Result ===")
    correct_answers = 0
    total_questions = len(questions)
    for qid, question in questions.items():
        if selected_answers.get(qid) == question["correct_answer"]:
            correct_answers += 1

    percentage = (correct_answers / total_questions) * 100
    print("Total Questions: {}".format(total_questions))
    print("Correct Answers: {}".format(correct_answers))
    print("Percentage: {:.2f}%".format(percentage))

# Main Program Flow
def main():
    print("=== Online Examination System ===")
    login()

# Run the main program
main()


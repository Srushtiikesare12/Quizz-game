import random
import os

# File to store high scores
SCORE_FILE = "high_scores.txt"

class Question:
    """Class to represent a single quiz question"""
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

    def check_answer(self, user_answer):
        """Check if the user's answer is correct"""
        return user_answer.upper() == self.answer

class Quiz:
    """Class to manage the quiz"""
    def __init__(self):
        self.questions = []
        self.score = 0

    def load_questions(self):
        """Load questions into the quiz"""
        self.questions = [
            Question("What is the capital of France?", ["A) London", "B) Berlin", "C) Paris", "D) Rome"], "C"),
            Question("Which programming language is known for data science?", ["A) Java", "B) Python", "C) C++", "D) JavaScript"], "B"),
            Question("What is 5 + 7?", ["A) 10", "B) 11", "C) 12", "D) 13"], "C"),
            Question("Which planet is known as the Red Planet?", ["A) Earth", "B) Mars", "C) Venus", "D) Jupiter"], "B"),
            Question("Who wrote 'To Kill a Mockingbird'?", ["A) J.K. Rowling", "B) William Shakespeare", "C) Harper Lee", "D) Charles Dickens"], "C")
        ]
        random.shuffle(self.questions)  # Shuffle questions for randomness

    def play(self):
        """Run the quiz game"""
        print("\nWelcome to the Quiz Game!\n")

        for q in self.questions:
            print("\n" + q.question)
            for option in q.options:
                print(option)
            user_answer = input("Enter your answer (A, B, C, or D): ").strip().upper()

            if q.check_answer(user_answer):
                print("✅ Correct!")
                self.score += 1
            else:
                print(f"❌ Wrong! The correct answer was {q.answer}.")

        print(f"\n🎉 Your final score: {self.score}/{len(self.questions)}\n")
        self.save_score()

    def save_score(self):
        """Save the score to a file"""
        name = input("Enter your name to save the score: ").strip()
        with open(SCORE_FILE, "a") as file:
            file.write(f"{name}: {self.score}/{len(self.questions)}\n")
        print("✅ Score saved successfully!")

    def show_high_scores(self):
        """Display high scores"""
        if not os.path.exists(SCORE_FILE):
            print("No high scores available yet.")
            return
        print("\n📜 High Scores:")
        with open(SCORE_FILE, "r") as file:
            print(file.read())

# Main function to run the quiz
def main():
    quiz = Quiz()
    quiz.load_questions()

    while True:
        print("\n📌 Menu:\n1. Play Quiz\n2. View High Scores\n3. Exit")
        choice = input("Choose an option (1/2/3): ").strip()

        if choice == "1":
            quiz.play()
        elif choice == "2":
            quiz.show_high_scores()
        elif choice == "3":
            print("👋 Thanks for playing! Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please enter 1, 2, or 3.")

# Run the game
if __name__ == "__main__":
    main()
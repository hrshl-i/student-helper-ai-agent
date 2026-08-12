"""Simple Student Helper AI Agent.
This script accepts user input, performs simple math, shares study tips,
and answers basic questions in a beginner-friendly way.
"""

def greet_user():
    """Print a greeting message to the student."""
    print("Welcome to the Student Helper AI Agent!")
    print("I can help with simple calculations, study tips, and basic questions.")
    print("Type 'exit' anytime to leave.")


def calculate_expression():
    """Ask the user for a basic math expression and print the result."""
    expression = input("Enter a simple math expression (for example 5 + 3): ")
    try:
        # Evaluate the expression safely for beginner use
        result = eval(expression, {"__builtins__": None}, {})
        print(f"Result: {result}")
    except Exception:
        print("Sorry, I couldn't calculate that. Please use a valid expression like 2 + 2.")


def give_study_tips():
    """Show a short list of helpful study tips."""
    tips = [
        "1. Break study time into smaller chunks and take short breaks.",
        "2. Practice active recall by testing yourself on the material.",
        "3. Keep a consistent study schedule each day.",
        "4. Use simple notes, diagrams, or flashcards to remember key ideas.",
        "5. Stay hydrated and sleep well before a study session."
    ]
    print("Here are some study tips:")
    for tip in tips:
        print(tip)


def answer_basic_question():
    """Respond to a few simple questions from the user."""
    question = input("Ask a basic question (for example 'What is a study tip?'): ").strip().lower()

    if "study" in question and "tip" in question:
        print("A good study tip is to review your notes regularly and practice with examples.")
    elif "calculate" in question or "how much" in question or "what is" in question:
        print("I can help with calculations if you choose the math option.")
    elif "hello" in question or "hi" in question:
        print("Hello! I'm here to help you study and solve simple problems.")
    else:
        print("That's a great question! I am still learning and can help best with study tips or simple math.")


def show_menu():
    """Display the menu options for the user to choose from."""
    print("\nPlease choose one of the following options:")
    print("1 - Perform a calculation")
    print("2 - Get study tips")
    print("3 - Ask a basic question")
    print("exit - Quit the agent")


def main():
    """Main function that runs the student helper agent loop."""
    greet_user()

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip().lower()

        if choice == "1":
            calculate_expression()
        elif choice == "2":
            give_study_tips()
        elif choice == "3":
            answer_basic_question()
        elif choice == "exit":
            print("Good luck with your studies! Goodbye.")
            break
        else:
            print("Please choose 1, 2, 3, or type 'exit'.")


if __name__ == "__main__":
    main()

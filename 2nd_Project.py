# List of questions; each question contains:
# [question_text, option1, option2, option3, option4, correct_option_number]
questions = [
    ["Which is the world's richest country?", "China", "USA", "Luxembourg", "Canada", 3],
    ["What is the color of the sky?", "Red", "Blue", "Violet", "Green", 2],
    ["How many colors are there in a rainbow?", "3", "2", "7", "4", 3],
    ["Who founded Apple?", "Steve Jobs", "Tim Cook", "Elon Musk", "Bill Gates", 1],
    ["Which of the following is a programming language?", "MS", "Google", "Meta", "Python", 4],
    ["Which of these is not part of the EU?", "Germany", "Poland", "Switzerland", "France", 3],
    ["Which of these is called 'Sin City'?", "Wuhan", "Delhi", "South Carolina", "Las Vegas", 4],
    ["What is the world's longest river?", "Indus", "Nile", "Amazon", "Madeira", 2],
    ["Which country has the lowest taxes?", "India", "USA", "UAE", "Ireland", 3]
]

# Prize money for each correct answer in increasing order
prizes = [1000, 2000, 10000, 20000, 50000, 100000, 200000, 500000, 1000000]

# Index to track current question
i = 0

# Main game loop
for question in questions:
    # Display the current question number and question text
    print(f"\nQuestion {i + 1}: {question[0]}")
    # Display the multiple-choice options
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}")

    # Ask for user input and validate it
    try:
        a = int(input("Enter your answer (1 for a, 2 for b, 3 for c, 4 for d): "))
        # If input is out of valid range
        if a < 1 or a > 4:
            print("Invalid option! Please enter a number between 1 and 4.")
            break
    except ValueError:
        # If input is not an integer
        print("Invalid input! Please enter a number.")
        break

    # Check if the answer is correct
    if a == question[5]:
        print("✅ Correct Answer!")
        print(f"You won ₹{prizes[i]}")
        i += 1  # Move to the next question
    else:
        print("❌ Wrong Answer. Better luck next time!")
        break  # End game on wrong answer

# If player answered all questions correctly
if i == len(questions):
    print("\n🎉🎉 Congratulations! 🎉🎉")
    print("You have answered all the questions correctly!")
    print("💰 You are now a MILLIONAIRE! 💰")

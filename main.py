#python quiz game

Questions = ("How many elements are in the periodic table?: ",
             "Which animal lays the largest eggs?: ",
             "What is the most abundant gas in the Earth's atmosphere?: ",
             "How many bones are in the human body?: ", 
             "Which is the hottest planet in the solar system?: ")

options = (("A. 116 ", "B. 117 ", "C. 118 ", "D. 119 "),
           ("A. Snake ", "B. Ostrich", "C. Bat", "D. Hen"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-dioxide", "D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Earth", "B. Saturn", "C. Venus", "D. Mercury"))

answers = ("C", "B", "A", "A", "C")
guesses = []
score = 0
question_num = 0

for question in Questions:
    print("----------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter A, B, C, D: ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct")

    else:
        print("Incorrect")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1


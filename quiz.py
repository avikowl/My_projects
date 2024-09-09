data = [
    ("What is the capital of France?", "C", ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"]),
    ("Which planet is known as the Red Planet?", "B", ["A) Earth", "B) Mars", "C) Jupiter", "D) Venus"]),
    ("Who wrote 'To Kill a Mockingbird'?", "A",
     ["A) Harper Lee", "B) Mark Twain", "C) J.K. Rowling", "D) Charles Dickens"]),
    ("What is the largest ocean?", "C", ["A) Atlantic", "B) Indian", "C) Pacific", "D) Arctic"]),
    ("Which element has the chemical symbol O?", "A", ["A) Oxygen", "B) Gold", "C) Iron", "D) Carbon"]),
    ("What is the hardest natural substance?", "D", ["A) Gold", "B) Silver", "C) Iron", "D) Diamond"]),
    ("Which country is famous for pizza?", "B", ["A) Spain", "B) Italy", "C) Japan", "D) China"]),
    ("How many continents are there?", "C", ["A) Five", "B) Six", "C) Seven", "D) Eight"]),
    ("Which is the largest planet in the solar system?", "D", ["A) Earth", "B) Venus", "C) Saturn", "D) Jupiter"]),
    ("Which language is used to write web pages?", "A", ["A) HTML", "B) Python", "C) C++", "D) SQL"]),
    ("What is the chemical formula for water?", "B", ["A) CO2", "B) H2O", "C) O2", "D) N2"]),
    ("Which country is home to the kangaroo?", "A", ["A) Australia", "B) Canada", "C) Brazil", "D) India"]),
    ("What is the tallest mountain in the world?", "B", ["A) K2", "B) Mount Everest", "C) Kilimanjaro", "D) Elbrus"]),
    ("Which planet is closest to the Sun?", "C", ["A) Earth", "B) Venus", "C) Mercury", "D) Mars"]),
    ("Which sport is known as 'the beautiful game'?", "A", ["A) Football", "B) Tennis", "C) Cricket", "D) Basketball"]),
    ("Which famous physicist developed the theory of relativity?", "B",
     ["A) Isaac Newton", "B) Albert Einstein", "C) Galileo", "D) Nikola Tesla"]),
    ("Which fruit is known as the king of fruits?", "C", ["A) Apple", "B) Banana", "C) Mango", "D) Pineapple"]),
    ("What is the fastest land animal?", "A", ["A) Cheetah", "B) Lion", "C) Gazelle", "D) Horse"]),
    ("Which is the smallest country in the world?", "D",
     ["A) Monaco", "B) Singapore", "C) Luxembourg", "D) Vatican City"]),
    ("What is the boiling point of water in Celsius?", "B", ["A) 90°C", "B) 100°C", "C) 110°C", "D) 120°C"])
]
def run_quiz():
    score = 0
    for question, correct_answer, options in data:
        print(f"\n{question}")
        for option in options:
            print(option)
        user_answer = input("(A/B/C/D): ").upper()
        if user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer}.")
    print(f"\nYour final score is: {score}/{len(data)}")
run_quiz()
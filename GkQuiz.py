import random

gk = """⟦G⟧⟦e⟧⟦n⟧⟦e⟧⟦r⟧⟦a⟧⟦l⟧ ⟦K⟧⟦n⟧⟦o⟧⟦w⟧⟦l⟧⟦e⟧⟦d⟧⟦g⟧⟦e⟧ ⟦Q⟧⟦u⟧⟦i⟧⟦z⟧"""

class GeneralKnowledgeQuiz:
    def __init__(self):
        self.questions = [
            "What is the capital of France?", "Which planet is known as the Red Planet?",
            "Who painted the Mona Lisa?", "What is the largest mammal?",
            "What is the currency of Japan?", "What is the chemical symbol for gold?",
            "What is the tallest mountain in the world?", "Which gas do plants use for photosynthesis?",
            "What is the smallest prime number?", "Who wrote the play 'Romeo and Juliet'?",
            "What is the main component of air?", "What is the largest organ in the human body?",
            "In which year did World War II end?", "What is the process by which plants make their food?",
            "Which famous scientist developed the theory of relativity?", "Which country is known as the Land of the Rising Sun?",
            "What is the national flower of Japan?", "What is the chemical symbol for water?",
            "Which animal is known as the 'King of the Jungle'?", "What is the largest ocean on Earth?",
            "Who painted the Sistine Chapel ceiling?", "What is the capital of China?",
            "What is the smallest planet in our solar system?", "What is the world's longest river?",
            "Which gas do humans inhale and then exhale?", "Who is often referred to as the 'Father of India'?",
            "What is the chemical symbol for oxygen?", "Which famous scientist discovered the law of gravity?",
            "What is the primary gas responsible for climate change?", "What is the largest continent?",
            "Which natural satellite orbits the Earth?", "What is the national flower of India?",
            "Which famous playwright wrote 'Hamlet'?", "What is the tallest animal in the world?",
            "What is the largest desert in the world?", "Which gas do plants release during photosynthesis?",
            "Which famous leader gave the 'I Have a Dream' speech?", "What is the capital of Australia?",
            "Which planet is known as the 'Morning Star' or 'Evening Star'?", "What is the largest species of shark?",
            "What is the national animal of China?", "What is the chemical symbol for nitrogen?",
            "Which famous scientist is known for the theory of evolution?", "What is the currency of the United Kingdom?",
            "What is the closest star to Earth?", "What is the largest species of penguin?",
            "Which famous queen ruled England for over 63 years?", "What is the smallest bone in the human body?",
            "In which year did the Titanic sink?"
        ]

        self.answers = [
            "Paris", "Mars", "Leonardo da Vinci", "Blue whale", "Yen", "Au", "Mount Everest", "Carbon dioxide",
            "2", "William Shakespeare", "Nitrogen", "Skin", "1945", "Photosynthesis", "Albert Einstein", "Japan",
            "Cherry blossom", "H2O", "Lion", "Pacific Ocean", "Michelangelo", "Beijing", "Mercury", "Nile",
            "Oxygen", "Mahatma Gandhi", "O", "Isaac Newton", "Carbon dioxide", "Asia", "Moon", "Lotus",
            "William Shakespeare", "Giraffe", "Sahara Desert", "Oxygen", "Martin Luther King Jr.", "Canberra",
            "Venus", "Whale shark", "Giant panda", "N", "Charles Darwin", "Pound sterling", "Sun", "Emperor penguin",
            "Queen Victoria", "Stapes (in the ear)", "1912"
        ]

    def play_quiz(self):
        while self.questions:
            print(f"\n\n ------------------ {gk} -------------------")
            index = random.randint(0, len(self.questions) - 1)
            print(f"\nQUESTION: {self.questions[index]}")
            user_input = input("\nANSWER: ").strip().lower().replace(" ", "")
            correct_answer = self.answers[index].strip().lower().replace(" ", "")

            if user_input == correct_answer:
                print("\n✅ CONGRATULATIONS! Correct answer.")
            else:
                print("\n❌ SORRY! Wrong answer.")
                print("✅ The Correct Answer is:", self.answers[index])

            # Remove the question after it's asked
            self.questions.pop(index)
            self.answers.pop(index)

            if self.questions:
                again = input("\nDo you want to play again? (Y/N): ")
                if again.strip().lower() != 'y':
                    print("\n🎉 THANK YOU for playing!")
                    break
            else:
                print("\n🎉 You've completed all the questions! Well done!")

if __name__ == "__main__":
    quiz = GeneralKnowledgeQuiz()
    quiz.play_quiz()
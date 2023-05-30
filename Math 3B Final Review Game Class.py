import random
import time

question_list = []
question_list.append(("What is the anti-derivative of f(x) = 2^x?", 2))
question_list.append(("What is the anti-derivative of f(x) = -3x^3?", 2))
question_list.append(("What is the anti-derivative of f(x) = ln(x)?", 4))
question_list.append(("What is the anti-derivative of f(x) = 1/x?", 2))
question_list.append(("What is the integral of f(x) = 1/(x-2) from a=1 to b=5?", 6))
question_list.append(("What is the anti-derivative of f(x) = x^2*e^(x^3)?", 6))
question_list.append(("What is the anti-derivative of f(x) = x^5*e^(x^3)", 12))
question_list.append(("What is the anti-derivative of f(x) = x^4*ln(x^3)", 8))
question_list.append(("What is the partial fraction decomposition of f(x) = (x^2 + x + 1)/(x^2 - 5x + 6)?", 12))
question_list.append(("What is the partial fraction decomposition of f(x) = (x^2 + x + 1)/(x^3 - x^2)?", 12))
question_list.append(("Does the series with terms 1/n converge or diverge? Why?", 4))
question_list.append(("Does the series with terms (-1)^n * (1/n) converge or diverge? Why?", 4))
question_list.append(("Does the series with terms 1/n! converge or diverge? Why?", 4))
question_list.append(("Does the series with terms n! converge or diverge? Why?", 4))
question_list.append(("Does the series with terms n^(1.2) converge or diverge? Why?", 4))
question_list.append(("Does the series with terms (1/2)^n converge or diverge? Why?", 4))
question_list.append(("Find the anti-derivative of f(x) = ((x+9)^.5)/x", 18))
question_list.append(("Find the radius of convergence for the power series with terms x^n/n", 6))
question_list.append(("Find the radius of convergence for the power series with terms x^n/n!", 6))
# question_list.append(("", 4))
# question_list.append(("", 4))
# question_list.append(("", 4))
# question_list.append(("", 4))
# question_list.append(("", 4))
# question_list.append(("", 4))
# question_list.append(("", 4))
# question_list.append(("", 4))





class Question_List():
    def __init__(self, question_list):
        self.question_list = question_list.copy()

class Final_Review_Game():
    def __init__(self, question_list = question_list, score = 0, drum_roll_time = 3, speed_up_factor = 1):
        self.score = score
        self.questions_attempted = 0
        self.question_list = question_list
        self.drum_roll_time = drum_roll_time
        self.speed_up_factor = speed_up_factor
        self.number_attempted = 0
        print(f"The game is set up! Use the .play() method to begin playing.")
        
    def play(self):
        input_string = ""
        if self.number_attempted == 0:
            print(f"There are {len(self.question_list)} total questions and a maximum score of {sum([item[1] for item in self.question_list])}.")
            random.shuffle(self.question_list)
        else:
            print(f"Picking up from where we left off, with {self.number_attempted} question(s) answered and a score of {self.score}.")
        print('Type "stop" or "s" to terminate the program early.')
        
        # Gameplay Steps
        while len(self.question_list) > 0:
            question = self.question_list.pop()
            input_string = input(f"{self.number_attempted + 1}) \t{question[0]} (worth {question[1]} points)")
            if not input_string.isnumeric():
                self.question_list.append(question)
                break
            else:
                self.number_attempted += 1
                self.score += int(input_string)
                # print(f"Answer:\t", end = " ")
                if int(input_string) == question[1]:
                    print(f"\t Correct! Your score is {self.score}. \n")
                elif int(input_string) == 0:
                    print(f"\t This is incorrect, so 0 points have been awarded. Better luck next time! \n")
                else:
                    print(f"\t Partially Correct. {input_string} points have been awarded for partial credit. Your score is now {self.score}. \n")
                time.sleep(5/self.speed_up_factor)
                
            
        if self.score == self.number_attempted and len(self.practice_list) == 0:
            print("CONGRATULATIONS!!!! YOU FINISHED EVERY QUESTION WITH 100% ACCURACY!")
        
        if self.number_attempted != 0:
            print(f"Thanks for playing! \n Questions Answered: {self.number_attempted} \t Score: {self.score} \t Accuracy: {int(self.score/self.number_attempted*100+.499)}% (this part is broken at the moment b/c of variable point values)")






copy_list = Question_List(question_list)

our_game = Final_Review_Game(copy_list.question_list)

our_game.play()




import random
import time

question_list = []
question_list.append(("Suppose a list of vectors (v_1, ..., v_n) is linearly dependent. Prove that there must be a first vector v_i that is in the span of the vectors before it. ", 4))
question_list.append(("Prove that any vector space's zero vector is unique to that vector space.", 4))
question_list.append(("Prove that scaling a vector by -1 turns it into its additive inverse.", 4))
question_list.append(("Prove that if two subspaces have just the zero vector in common then their sum is a direct sum.", 10))
question_list.append(("Prove that any linearly independent list of vectors has unique linear combinations in the following sense: For every vector v in their span, there is a unique list of scalers used to obtain v as a linear combination.", 4))
question_list.append(('Explain why a linearly independent spanning set yields a "coordinate system" function for a vector space that outputs unique coordinates for each vector in the space. Is this function a vector space isomorphism?', 4))
question_list.append(('Given a list of vectors (v_1, ..., v_n) in a vector space V, explain the "coordinate map" from F^n into V. When is this map injective, surjective and invertible? What do we call the list of vectors when this map is invertible?', 15))
question_list.append(("Prove that the range of a linear transformation is a subspace.", 5))
question_list.append(("Prove that the kernel of a linear transformation is a subspace", 5))
question_list.append(("Suppose T is a linear transformation from V to W and U_1, U_2 are subspaces of V. Prove that T(U_1)+T(U_2) = T(U_1 + U_2)", 5))
question_list.append(('Prove the Rank-Nullity Theorem, a.k.a. the "Fundamental Theorem of Linear Algebra".', 10))
question_list.append(("Suppose U is an invariant subspace under the operator T. Prove that U is also invariant under any polynomial of the operator T.", 5))
question_list.append(("Write two equivalent definitions of eigenvector.", 5))
question_list.append(("Write the definition of set equality.", 5))
question_list.append(("Write the definition of basis.", 5))
question_list.append(("Prove that every operator on a finite dimensional complex vector space has an eigenvalue.", 10))
question_list.append(("Prove that a list of eigenvectors (v_1, ..., v_n) with distinct eigenvalues (s_1, ..., s_1) (I don't know how to type lambdas in Python) must be linearly independent.", 10))


"""This line was used to print a list of the questions because the output I copy-pasted apparently 
skipped parts of questions 7-8 (according to the randomized ordering of the .play() method)."""
# for i, item in enumerate(question_list):
#     print(f"{i+1} \t {item[0]}")


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
        self.points_attempted = 0
        self.maximum_possible_score = sum([item[1] for item in self.question_list])
        print(f"The game is set up! Use the .play() method to begin playing.")
        
    def play(self):
        input_string = ""
        if self.number_attempted == 0:
            print(f"There are {len(self.question_list)} total questions and a maximum score of {self.maximum_possible_score}.")
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
                self.points_attempted += question[1]
                self.score += int(input_string)
                # print(f"Answer:\t", end = " ")
                if int(input_string) == question[1]:
                    print(f"\t Correct! Your score is {self.score}. \n")
                elif int(input_string) == 0:
                    print(f"\t This is incorrect, so 0 points have been awarded. Better luck next time! \n")
                else:
                    print(f"\t Partially Correct. {input_string} points have been awarded for partial credit. Your score is now {self.score}. \n")
                time.sleep(5/self.speed_up_factor)
                
            
        if self.score == self.maximum_possible_score:
            print("CONGRATULATIONS!!!! YOU FINISHED EVERY QUESTION WITH 100% ACCURACY!")
        
        elif self.number_attempted != 0:
            print(f"Thanks for playing!")
        if self.number_attempted != 0:
            print(f"Questions Answered: {self.number_attempted} \t Score: {self.score} \t Accuracy: {int(self.score/self.points_attempted*100+.499)}%")





if __name__ == "__main__":
    copy_list = Question_List(question_list)

    our_game = Final_Review_Game(copy_list.question_list)
    our_game.speed_up_factor = 20

    our_game.play()




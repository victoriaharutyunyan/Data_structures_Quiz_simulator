from threading import Timer
import json
import Stack_



class QuizQuestion(Stack_.Node):

    def __init__(self, question, choice1, choice2, choice3, choice4, correct):
        self.question = question
        self.choice1 = choice1
        self.choice2 = choice2
        self.choice3 = choice3
        self.choice4 = choice4
        self.correct = correct


    def isCorrect(self):

        answer = input("Your answer...").lower()
        if answer == self.correct:
            print ("True")

        else:
            print ("False")
            print("The correct answer is", self.correct)


class MyQuiz(Stack_.Stack):
    count = -1
    inProgress = True

    def startQuiz(self):
       MyQuiz.count = -1
       MyQuiz.inProgress = True


       def timer():
           if (MyQuiz.inProgress == True):
               MyQuiz.count = MyQuiz.count + 1
               Timer(1.0, timer).start()
           elif (MyQuiz.inProgress == False):
               return MyQuiz.count

       if self.head != None:

               current_node = self.head
               while current_node is not None:
                          print(current_node.value.question)
                          print (current_node.value.choice1,"\n",current_node.value.choice2,"\n",current_node.value.choice3,"\n",current_node.value.choice4)
                          MyQuiz.inProgress = True
                          timer()
                          QuizQuestion.isCorrect(current_node.value)
                          MyQuiz.inProgress = False
                          thisCount = str(MyQuiz.count)
                          print("you have spent " + thisCount + " seconds on this task")
                          MyQuiz.count = -1
                          current_node = current_node.next



       else:
                      print("the list is empty")

def main():
    with open("edited.json") as data_file:
        dict = json.load(data_file)

    quest = MyQuiz()
    quiz_subject = input("Which quiz do you want to take"
                             "\n""1)Geography"
                             "\n""2)History"
                             "\n""3)Cinema"
                             "\n""Your answer...").lower()
    new_dict = dict[quiz_subject]


    for value in new_dict:

        qq1 = QuizQuestion(value["Question"], value["answers"][0],value["answers"][1],value["answers"][2],value["answers"][3], value["correct"])
        quest.push(qq1)


    quest.startQuiz()
main()
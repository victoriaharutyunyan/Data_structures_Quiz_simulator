
from threading import Timer
import json


class Node:

    def __init__(self, value, next_node, previous=None):
        self.value = value
        self.next = next_node
        self.previous = previous


class QuizQuestion(Node):

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
            print("True")
        else:
            print("False")
            print("The correct answer is", self.correct)


class Quiz:
    count = -1
    inProgress = True

    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def insertFirst(self, value):
        node = Node(value, self.first)
        self.first = node
        if self.last is None:
            self.last = node
        self.size += 1

    def removeFirst(self):
        if self.first is None:
            return
        if self.size == 1:
            self.first = None
            self.last = None
            self.size -= 1
            return
        tmp = self.first
        self.first = self.first.next
        tmp.next = None
        self.size -= 1

    def insertLast(self, data):
        node = Node(data, None)
        if self.last is None:
            self.first = node
            self.last = node
            self.size += 1
            return
        self.last.next = node
        self.last = node
        self.size += 1

    def removeLast(self):
        if self.size == 0:
            return
        if self.size == 1:
            self.first = None
            self.last = None
            self.size -= 1
            return
        tmp = self.first
        while tmp.next != self.last:
            tmp = tmp.next
        tmp.next = None
        self.last = tmp
        self.size -= 1

    def get_size(self):
        return self.size

    def get_first(self):
        return self.first

    def get_last(self):
        return self.last

    def insertBefore(self, data, data_to_check):
        if self.first and self.last:
            current_node = self.first
            previous_node = None
            while current_node is not None:
                if current_node.data == data_to_check:
                    new_node = Node(data, current_node)
                    if previous_node is None:
                        self.first = new_node
                    else:
                        previous_node.next = new_node
                    self.size += 1
                    return
                else:
                    previous_node = current_node
                    current_node = current_node.next
        else:
            print("List is empty")

    def insertAfter(self, data, data_to_check):
        if self.first and self.last:
            current_node = self.first
            while current_node is not None:
                if current_node.data == data_to_check:
                    new_node = Node(data, current_node.next)
                    if current_node.next is None:
                        current_node.next = new_node
                        self.last = new_node
                    else:
                        current_node.next = new_node
                    self.size += 1
                    return
                else:
                    current_node = current_node.next
        else:
            print("List is empty")

    def remove(self, data):
        current_node = self.first
        previous_node = None
        while current_node is not None:
            if current_node.data == data:
                if previous_node is not None:
                    previous_node.next = current_node.next
                else:
                    self.first = current_node.next
                self.size -= 1
                return
            else:
                previous_node = current_node
                current_node = current_node.next

    def indexOf(self, data):
        current_node = self.first
        index = 0
        while current_node.next is not None:
            if current_node.data == data:
                return index
            else:
                current_node = current_node.next
                index += 1
        print("No such data")

    def displayItems(self):
        if self.size != 0:
            current_node = self.first
            while current_node is not None:
                print(current_node.value.question, current_node.value.choice1, current_node.value.choice2,
                      current_node.value.choice3, current_node.value.choice4, current_node.value.correct)
                current_node = current_node.next
        else:
            print("the list is empty")


class MyQuiz(Quiz):

    def startQuiz(self):
        Quiz.count = -1
        Quiz.inProgress = True

        def timer():
            if (Quiz.inProgress == True):
                Quiz.count = Quiz.count + 1
                Timer(1.0, timer).start()
            elif (Quiz.inProgress == False):
                return Quiz.count

        if self.size != 0:
            current_node = self.first
            while current_node is not None:
                print(current_node.value.question)
                print(current_node.value.choice1, "\n", current_node.value.choice2, "\n", current_node.value.choice3,
                      "\n", current_node.value.choice4)
                Quiz.inProgress = True
                timer()
                QuizQuestion.isCorrect(current_node.value)
                Quiz.inProgress = False
                thisCount = str(Quiz.count)
                print("you have spent " + thisCount + " seconds on this task")
                Quiz.count = -1
                current_node = current_node.next

        else:
            print("the list is empty")

# Hashmap

class Entry():
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashMap():
    def __init__(self):
        self._capacity = 26
        self._hashtable = [None] * self._capacity * 10
        self._size = 0

    def _hash(self, element):
        # return hash(element) % self._capacity
        return ord(element[0]) % self._capacity

    def put(self, key, value):
        index = self._hash(key)
        # print(index, key)
        for i in range(index, len(self._hashtable)):
         if (self._hashtable[i] != None):
                if key == self._hashtable[i].key:
                    oldValue = self._hashtable[i].value
                    self._hashtable[i].value = value
                    return oldValue
         else:
                self._hashtable[index] = Entry(key, value)
                self._size += 1
                return None


    def get(self, key):
        index = self._hash(key)
        for i in range(index, len(self._hashtable)):
            if (self._hashtable[i] != None):
                if key == self._hashtable[i].key:
                    return self._hashtable[i].value
            else:
                return None

    def hasKey(self, key):
        index = self._hash(key)
        for i in range(index, len(self._hashtable)):
            if (self._hashtable[i] != None):
                if key == self._hashtable[i].key:
                    return True
            else:
                return None

    # This function should remove the entry with specified key and return the value. In case if the key does not exist, None should be returned
    def remove(self, key):
        index = self._hash(key)
        for i in range(index, len(self._hashtable)):
            if (self._hashtable[i] != None):
                if key == self._hashtable[i].key:
                    print(self._hashtable[i].value)
                    self._hashtable[i] = None
                    break
            else:
                return None

    def size(self):
        return self._size

    def print(self):
        print("printing hashset elements")
        for e in self._hashtable:
            while (e != None):
                print(e)
                e = e.next

    def __iter__(self):
        for i in range(len(self._hashtable)):
            if (self._hashtable[i] != None):
                self._index = i;
                break
        return self

    def __next__(self):
        if self._index >= len(self._hashtable):
            raise StopIteration
        tmpInd = self._index
        self._index = len(self._hashtable)
        for i in range(tmpInd + 1, len(self._hashtable)):
            if (self._hashtable[i] != None):
                self._index = i;
                break

        return self._hashtable[tmpInd].value

def main():

    with open("edited.json") as data_file:
            dict = json.load(data_file)

    # Hashmap
    quiz = HashMap()
    for key in dict:
     (quiz.put(key, dict[key]))
     quest = MyQuiz()

    quiz_subject = input("Which quiz do you want to take"
                             "\n""1)Geography"
                             "\n""2)History"
                             "\n""3)Cinema"
                             "\n""Your answer...").lower()

    if quiz.hasKey(quiz_subject) == True:
        question = quiz.get(quiz_subject)
        for value in question:
            # quest.insertFirst(value)
            qq1 = QuizQuestion(value["Question"], value["answers"][0], value["answers"][1], value["answers"][2],
                               value["answers"][3], value["correct"])
            quest.insertLast(qq1)


    print("There are" ,(quest.get_size()),"questions in the quiz")
    quest.startQuiz()

    quiz.print()
main()



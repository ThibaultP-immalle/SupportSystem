from Responder import *
from InputReader import *

class SupportSystem:
    def __init__(self):
        self.reader = InputReader()
        self.responder = Responder()
    
    def start(self):
        finished = False

        self.printWelcome()

        while not finished:
            user_input = self.reader.getInput()

            if 'bye' in user_input:
                finished = True
            else:
                response = self.responder.generateResponse(user_input)
                print(response)

        self.printGoodbye()

    def printWelcome(self):
        print("Welcome to the Tech Support!")
        print()
        print("Explain your problem...")
        print("Type 'bye' to stop.")

    def printGoodbye(self):
        print("Goodbye!")
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

            if user_input.startswith('bye'):
                finished = True
                self.printGoodbye()
            else:
                response = self.responder.generateResponse()
                print(response)

    def printWelcome(self):
        print("Welcome to the Tech Support!")
        print()
        print("Explain your problem...")
        print("Type 'bye' to stop.")

    def printGoodbye(self):
        print("Goodbye!")
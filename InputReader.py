class InputReader:
    def getInput(self):
        user_input = input(" > ")
        wordArray = user_input.split()

        words =  set()
        for word in wordArray:
            words.add(word)

        return words
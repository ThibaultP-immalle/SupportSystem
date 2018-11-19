import random

class Responder:
    def __init__(self):
        self.DefaultResponses = []
        self.responseMap = dict({})
        self.fillDefaultResponses()
        self.fillResponseMap()

    def generateResponse(self, words):
        for word in words:
            if word in self.responseMap:
                response = self.responseMap[word]
            else:
                response = None

            if response != None:
                return response

        return self.pickDefaultResponse()

    def pickDefaultResponse(self):
        index = random.randint(0, len(self.DefaultResponses)-1)
        return self.DefaultResponses[index]

    def fillDefaultResponses(self):
        self.DefaultResponses.append("That sounds odd. Could you describe this in more detail?")
        self.DefaultResponses.append("No other customer has ever complained about this before. What is your system configuration?")
        self.DefaultResponses.append("I need a bit more information on that.")
        self.DefaultResponses.append("Have you checked that you do not have a dll conflict?")
        self.DefaultResponses.append("That is covered in the manual. Have you read the manual?")
        self.DefaultResponses.append("Your description is a bit wishy-washy. Have you got an expert there with you who could describe this better?")
        self.DefaultResponses.append("That's not a bug, it's a feature!")
        self.DefaultResponses.append("Could you elaborate on that?")
        self.DefaultResponses.append("Have you tried running the app on your phone?")
        self.DefaultResponses.append("I just checked StackOverflow - they don't know either.")

    def fillResponseMap(self):
        self.responseMap["crash"] = "Well, it never crashes on our system. It must have something to do with your system. Tell me more about your configuration."
        self.responseMap["crashes"] ="Well, it never crashes on our system. It must have something to do with your system. Tell me more about your configuration."
        self.responseMap["slow"] =  "I think this has to do with your hardware. Upgrading your processor should solve all performance problems. Have you got a problem with our software?"
        self.responseMap["performance"] =  "Performance was quite adequate in all our tests. Are you running any other processes in the background?"
        self.responseMap["bug"] =  "Well, you know, all software has some bugs. But our software engineers are working very hard to fix them. Can you describe the problem a bit further?"
        self.responseMap["buggy"] =  "Well, you know, all software has some bugs. But our software engineers are working very hard to fix them. Can you describe the problem a bit further?"
        self.responseMap["windows"] = "This is a known bug to do with the Windows operating system. Please report it to Microsoft. There is nothing we can do about this."
        self.responseMap["mac"] =  "This is a known bug to do with the Mac operating system. Please report it to Apple. There is nothing we can do about this."
        self.responseMap["expensive"] = "The cost of our product is quite competitive. Have you looked around and really compared our features?"
        self.responseMap["installation"] =  "The installation is really quite straight forward. We have tons of wizards that do all the work for you. Have you read the installation instructions?"
        self.responseMap["memory"] =  "If you read the system requirements carefully, you will see that the specified memory requirements are 1.5 giga byte. You really should upgrade your memory. Anything else you want to know?"
        self.responseMap["linux"] =  "We take Linux support very seriously. But there are some problems. Most have to do with incompatible glibc versions. Can you be a bit more precise?"
        self.responseMap["bluej"] =  "Ahhh, BlueJ, yes. We tried to buy out those guys long ago, but they simply won't sell... Stubborn people they are. Nothing we can do about it, I'm afraid."
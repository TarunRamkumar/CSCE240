import FileParser as Parser
class CLI:
    def __init__(self):
        self.google = Parser.FileParser("..\\data\\Google10k-4Q-2024.txt")
        self.generalMotors = Parser.FileParser("..\\data\\GeneralMotors10k-4Q-2024.txt")

    def processResponse(response):

        
    def userInteraction():
        response = input("What would you like to ask about?")
        processResponse(response)
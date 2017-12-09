class Parser:
    def __init__(self, directory):
        self.directory = directory

    def str_to_array(self):
        file = open(self.directory, "r")
        number = [num.replace("\n", "") for num in file]
        number = [num.split(" ") for num in number]

        return number

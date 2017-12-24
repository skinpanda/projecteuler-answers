class Parser:
    def __init__(self, directory):
        self.directory = directory

    def str_to_array(self):
        file = open(self.directory, "r")
        number = [num.replace("\n", "") for num in file]
        number = [num.split(" ") for num in number]
        return number
    
    def str_to_int(self):
        file = open(self.directory, "r")
        number = [num.replace("\n", "") for num in file]
        number = [int(num) for num in number]
        return number


class Collatz:
    def __init__(self, start):
        self.start = start
        self.sequence = [self.start]

    def get_sequence(self):
        self.sequence = [self.start]

        while self.start != 1:
            if self.start % 2 == 0:
                self.start //= 2
                self.sequence.append(self.start)
            else:
                self.start = (3 * self.start) + 1
                self.sequence.append(self.start)

        return self.sequence

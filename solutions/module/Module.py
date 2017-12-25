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


class Pascal:
    def __init__(self, size=1):
        self.size = size
        self.row = size
        self.line = [1]

    def get_line(self, row):
        self.line = [1]

        for i in range(row):
            self.line.append(self.line[i] * (row - i) // (i + 1))

        return self.line

    def get_table(self):
        for k in range(self.size + 1):
            print(self.get_line(k))

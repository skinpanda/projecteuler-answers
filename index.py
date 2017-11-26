# projecteuler-answers Index
import os

# Greetings!
print("Welcome to projecteuler-answers!")
print("Type \"help\" to get started.")
print("Press q to quit")


# How to use


def indexhelp():
    message = "To view code, use view <space> [problem number]." \
              "\nTo run code, use run <space> [problem number]."
    print(message)


def viewcode(n):
    problem = "solutions/problem_" + n + ".py"
    file = open(problem, "r")
    print(file.read())


def runcode(n):
    problem = "solutions/problem_" + n + ".py"
    os.system("python3 " + problem)


# prompt
while True:
    s = input('-->')

    if s == "help":
        indexhelp()

    if "view" in s:
        pnum = s.replace("view ", '')
        viewcode(pnum)

    if "run" in s:
        pnum = s.replace("run ", '')
        runcode(pnum)

    if s == "q" or s == "Q":
        break

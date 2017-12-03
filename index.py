# projecteuler-answers Index
import os

# Greetings!
print("Welcome to projecteuler-answers!")
print("Type \"help\" to get started.")
print("Press q to quit")


# How to use


def index_help():
    message = "To view code, use view <space> [problem number]." \
              "\nTo run code, use run <space> [problem number]."
    print(message)


def view_code(n):
    problem = "solutions/problem_" + n + ".py"
    file = open(problem, "r")
    print(file.read())


def run_code(n):
    problem = "solutions/problem_" + n + ".py"
    os.system("python3 " + problem)


# prompt
while True:
    s = input('-->')

    if s == "help":
        index_help()

    if "view " in s:
        ProblemNum = s.replace("view ", '')
        view_code(ProblemNum)

    if "run " in s:
        ProblemNum = s.replace("run ", '')
        run_code(ProblemNum)

    if s == "q" or s == "Q":
        break

from stackless import tasklets

def print_nums(num):
    for i in range(num):
        print("tasklets:{i}")

def print_letters(letters):
    for j in letters:
        print("Tasklets :{j}")

tasklets(print_nums)(5)
tasklets(print_letters)("abc")

stackless.run()
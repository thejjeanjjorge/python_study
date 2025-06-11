
def question(answer):
    if answer == '42':
        print("yes")
    elif answer == "forty two":
        print("yes")
    elif answer == "forty-two":
        print("yes")
    else:
        print("No")

answer = input("Great Question of Life, the Universe and Everything? ")

question(answer)
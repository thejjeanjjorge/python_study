def convert(text):
    if ":)" in text:
        text = text.replace(":)","🙂")
    if ":(" in text:
        text = text.replace(":(","🙁")
    return text
    

def main():
    user_input = input()
    converted_input = convert(user_input)
    print(converted_input)

main()


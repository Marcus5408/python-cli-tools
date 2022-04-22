def askUserString(prompt, error):
    while True:
        try:
            response = str(input(prompt))
            break
        except ValueError:
            print(error)
    return response

def askUserInt(prompt, error):
    while True:
        try:
            response = int(input(prompt))
            break
        except ValueError:
            print(error)
    return response
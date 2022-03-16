import time

def askUser(prompt, error):
    while True:
        try:
            response = input(prompt)
            break
        except ValueError:
            print(error)
    return response

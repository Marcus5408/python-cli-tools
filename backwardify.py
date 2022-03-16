import time

def bootup():
    print("Backwardify v1.0")
    time.sleep(1)

def askUser(prompt, error):
    while True:
        try:
            response = input(prompt)
            break
        except ValueError:
            print(error)
    return response

bootup()

i = askUser("Enter a string: ", "How did you even manage to not type a string?")
start_time = time.time()
print("Ouput: " + i[::-1])
print("Finished in " + str(time.time() - start_time) + " seconds")
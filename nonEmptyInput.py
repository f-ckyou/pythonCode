def nonEmpty_input(inp):
    while True:
        usrInput = input(inp)
        if usrInput.strip():
            return usrInput


prompt = nonEmpty_input("Enter your name: ")
print(f"Hi, {prompt}")

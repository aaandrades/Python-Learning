import basics.one as one

print("Top level in two.py")

one.firstExecution()

if __name__ == "main":
    print("TWO.py is being run directly")
else:
    print("ONE.py has been called")

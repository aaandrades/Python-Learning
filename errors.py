def throwError():
    try:
        c = 123/0
        return c
    except:
        print("Sorry, you can't divide by ZERO")


if __name__ == "__main__":
    throwError()

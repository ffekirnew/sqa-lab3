def check_number(num):
    if num > 0 and num % 2 == 0:
        print("Positive even number")
    elif num > 0 and num % 2 != 0:
        print("Positive odd number")
    elif num < 0:
        print("Negative number")
    else:
        print("Zero")

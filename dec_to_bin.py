def decimal_to_binary(number):
    result = ""
    number = int(number)
    while number > 0:               #keep dividing until at 0
        remainder = number % 2
        number = number // 2
        result = remainder + result #place string in reverse order
    return result


def main():
    num = input("Enter Binary Number:")
    print("Decimal {} to binary: {}".format(num, decimal_to_binary(num)))

if __name__== "__main__":
    main()

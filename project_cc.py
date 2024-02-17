
def decimal_to_binary(decimal):
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    return binary


def binary_to_decimal(binary):
    decimal = 0
    power = 0
    while binary > 0:
        decimal += (binary % 10) * (2 ** power)
        binary = binary // 10
        power += 1
    return decimal


def main():
    print("Greetings!!, ")
    print("let us begin the Decimal to Binary and Binary to decimal converter!")
    print("Alright let's go try it ouy")
    while True:
        print("\nPlease select an option!")
        print("A. Convert decimal to binary")
        print("B. Convert binary to decimal")
        print("C. Quit")
        choice = input("Enter your choice (A, B, or C)")

        if choice == 'A':
            try:
                decimal = int(input("Enter a decimal number"))
                binary = decimal_to_binary(decimal)
                print("Decimal {} to Binary: {}".format(decimal, binary))
            except ValueError:
                print("Invalid input! Pleae enter a valid decimal number.")
        elif choice == 'B':
            try:
                binsty = input("Enter a binary number: ")
                decimal = binary_to_decimal(int(binary))
                print("Binary {} to Decimal: {}".format(binary, decimal))
            except ValueError:
                print("Invalid input! Please enter a valid binart number.")
        elif choice == 'C':
            print("Thank you for using the Decimal to Binary and Binary to Decimal Converter. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option (A, B, or C). ")

if __name__ == "__main__":
    main()

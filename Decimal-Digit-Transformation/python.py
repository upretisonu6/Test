class DigitSum:
    def __init__(self, digit):
        if not isinstance(digit, int):
            raise ValueError("The input must be an integer.")
        if digit < 0 or digit > 9:
            raise ValueError("Please enter a single digit between 0 and 9.")
        self.digit = digit

    def calculate(self):
        # Create numbers X, XX, XXX, XXXX by repeating the digit
        num1 = self.digit
        num2 = self.digit * 10 + self.digit
        num3 = self.digit * 100 + self.digit * 10 + self.digit
        num4 = self.digit * 1000 + self.digit * 100 + self.digit * 10 + self.digit
        
        # Calculate and return the sum
        return num1 + num2 + num3 + num4


def main():
    try:
        digit = int(input("Enter a digit (0-9): "))
        sum_calculator = DigitSum(digit)
        result = sum_calculator.calculate()
        print(f"The result of {digit} + {digit*11} + {digit*111} + {digit*1111} is: {result}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()

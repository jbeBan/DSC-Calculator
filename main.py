"""
Uses the calculator module to implement a very basic, interactive calculator.
"""
import calculator


CALCULATOR_OPS = {
    "+": calculator.add,
    "-": calculator.subtract,
    "*": calculator.multiply,
    "/": calculator.divide,
    "^": calculator.power
}


def main():
    print("Welcome to the Basic Calculator!\n")

    user_input = "~"
    while user_input not in {"quit", "q", "Quit", "Q", "exit", ""}:
        print("Please enter an operation in the following form: num_one operator num_two")
        print("(Basic Calculator supports the following operators: + - * / ^)")
        print("Example: 2 ^ 10\n")

        user_input = input("> ")
        try:
            first_num, operator, second_num = user_input.split()

            first_num = float(first_num)
            second_num = float(second_num)

            result = CALCULATOR_OPS[operator](first_num, second_num)
        except:
            print(f"Invalid input ({user_input}).\n")

            continue

        print(f"The result of {user_input} is {result}\n")

    print("Thank you for using the Basic Calculator!")


if __name__ == "__main__":
    main()

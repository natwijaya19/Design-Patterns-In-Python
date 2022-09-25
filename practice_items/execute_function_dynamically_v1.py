def add_one(x):
    return x + 1


def divide_by_two(x):
    return x / 2


def square(x):
    return x ** 2


def invalid_op(x):
    raise Exception("Invalid operation")


# The better way:
def perform_operation(x, chosen_operation="add_one"):
    ops = {
        "add_one": add_one,
        "divide_by_two": divide_by_two,
        "square": square
    }

    chosen_operation_function = ops.get(chosen_operation, invalid_op)

    return chosen_operation_function(x)


def main():
    print(perform_operation(5))
    print(perform_operation(5, chosen_operation="divide_by_two"))
    print(perform_operation(5, chosen_operation="square"))
    # print(perform_operation(5, chosen_operation="invalid_op"))


if __name__ == "__main__":
    main()

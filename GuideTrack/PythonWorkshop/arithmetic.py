def arithmetic(a, b):
    try:
        print(f"Addition: {a} + {b} = " + str(a + b))
        print(f"Subtraction: {a} - {b} = " + str(a - b))
        print(f"Multiplication: {a} * {b} = " + str(a * b))
        print(f"Division: {a} / {b} = " + str(a / b))
        print(f"Modulus: {a} % {b} = " + str(a % b))
        print(f"Exponent: {a} ** {b} = " + str(a ** b))
        print(f"Floor Division: {a} // {b} = " + str(a // b))

        print(f"{a} == {b} = " + str(a == b))
        print(f"{a} != {b} = " + str(a != b))
        print(f"{a} > {b} = " + str(a > b))
        print(f"{a} < {b} = " + str(a < b))
        print(f"{a} >= {b} = " + str(a >= b))
        print(f"{a} <= {b} = " + str(a <= b))
    except TypeError:
        print("TypeError: unsupported operand type(s) for arithmetic operation", a, b)
    except ZeroDivisionError:
        print("ZeroDivisionError: division by zero", a, b)



def main():
    for a in [1, 1.0, "1", True, [1, 2, 3], (1, 2, 3), {"a": 1, "b": 2, "c": 3}, {1, 2, 3, 4, 5}]:
        for b in [2, 2.0, "2", False, [4, 5, 6], (4, 5, 6), {"d": 4, "e": 5, "f": 6}, {4, 5, 6, 7, 8}]:
            print(f"Type of a: {type(a)}")
            print(f"Type of b: {type(b)}")
            arithmetic(a, b)
            print("")


if __name__ == "__main__":
    main()
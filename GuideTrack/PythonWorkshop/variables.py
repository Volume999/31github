def main():
    # Integer type
    a = 1
    print("Integer type: " + str(a)) # str() converts a to a string

    # Float type
    b = 1.0
    print("Float type: " + str(b))

    # String type
    c = "Hello World!"
    print("String type: " + c)

    # Boolean type
    d = True
    print("Boolean type: " + str(d))

    # List type
    e = [1, 2, 3, 4, 5]
    print("List type: " + str(e))

    # Tuple type
    f = (1, 2, 3, 4, 5)
    print("Tuple type: " + str(f))

    # Dictionary type
    g = {"a": 1, "b": 2, "c": 3}
    print("Dictionary type: " + str(g))

    # Set type
    h = {1, 2, 3, 4, 5}
    print("Set type: " + str(h))

    # Print types
    print("Type of a: " + str(type(a)))

    # Implicit conversion
    print(f"Implicit conversion: {a} + {b} = " + str(a + b))

    # Explicit conversion
    print(f"Explicit conversion: int({a} + {b}) = " + str(int(a + b)))

if __name__ == "__main__":
    main()
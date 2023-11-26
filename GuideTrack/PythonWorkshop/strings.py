def main():
    example_string = "This is GrowthHungry challenge"

    print("Example string: " + example_string)

    print("Get first letter:" + example_string[0])

    # Negative index notation - starts from the end
    print("Get last letter:" + example_string[-1])

    # Slicing - get a substring
    print("Get first word:" + example_string[0:4])

    # Split string into words
    print("Split string into words:" + str(example_string.split()))

    # Count number of letters
    print("Count number of letters:" + str(len(example_string)))

    # Count number of words
    print("Count number of words:" + str(len(example_string.split())))

    # Find first occurrence of a letter
    print("Find first occurrence of a letter:" + str(example_string.find("G")))

    # Find first occurrence of a word
    print("Find first occurrence of a word:" + str(example_string.find("challenge")))

    # Replace a word
    print("Replace a word:" + example_string.replace("GrowthHungry", "Growth Hungry"))

    

if __name__ == "__main__":
    main()
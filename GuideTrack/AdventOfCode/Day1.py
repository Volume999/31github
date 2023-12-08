import sys 
import string
sys.stdout = open('output.txt','wt')

numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def solve_part_two():
    data = open("input.txt", "r").readlines()
    res = 0
    for line in data:
        f, l = len(line), -1
        fval, lval = -1, -1
        for i, number in enumerate(numbers):
            fi, li = line.find(number), line.rfind(number)
            if fi != -1 and fi < f:
                f = fi
                fval = i + 1
            if li != -1 and li > l:
                l = li
                lval = i + 1
        for dig in range(10):
            fi, li = line.find(str(dig)), line.rfind(str(dig))
            if fi != -1 and fi < f:
                f = fi
                fval = dig
            if li != -1 and li > l:
                l = li
                lval = dig
        res += fval * 10 + lval
    return res

def solve():
    data = open("input.txt", "r").readlines()
    res = 0
    for line in data:
        f, l = -1, -1
        for c in line:
            if c.isdigit():
                f = int(c)
                break
        for c in line[::-1]:
            if c.isdigit():
                l = int(c)
                break
        res += f * 10 + l
    return res
    

def main():
    print(solve_part_two())

if __name__ == "__main__":
    main()
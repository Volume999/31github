import sys
from icecream import ic
import string
from itertools import product
sys.stdout = open('output.txt','wt')
sys.stdin = open('input.txt','rt')

def solve2():
    games = sys.stdin.readlines()
    lims = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    res = 0
    for game in games:
        s1 = game.split(":")
        # print(s1)
        gameId = int(s1[0].split()[1].strip())
        # print(gameId)
        sets = s1[1].split(";")
        # print(sets)
        good = True
        maxs = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        for set in sets:
            s2 = set.split(",")
            # print(s2)
            for balls in s2:
                balls = balls.strip().split()
                num = int(balls[0])
                color = balls[1]
                # print(balls, color)
                maxs[color] = max(maxs[color], num)
        res += maxs["red"] * maxs["green"] * maxs["blue"]
    print(res)

def solve():
    print(list(product([-1, 0, 1], repeat=2)))
    lines = sys.stdin.readlines()
    lines = [line.strip() for line in lines]
    n = ic(len(lines))
    s = set()
    symbols = string.punctuation.replace(".", "")
    for i, line in enumerate(lines):
        m = len(line)
        # print(line)
        for ci, c in enumerate(line):
            if not c.isdigit() and c != ".":
                for dx, dy in product([-1, 0, 1], repeat=2):
                    s.add((i + dx, ci + dy))
    res = 0
    # print(s)
    for i, line in enumerate(lines):
        add = False
        cur = 0
        for ci, c in enumerate(line):
            if (i, ci) in s:
                add = True
            if not c.isdigit():
                if add:
                    res += cur
                    add = False
                cur = 0
            else:
                cur = cur * 10 + int(c)
        if add:
            res += cur
    print(res)

def main():
    solve()

if __name__ == "__main__":
    main()
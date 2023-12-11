import sys
from icecream import ic
import string
from itertools import product
from regex import regex
sys.stdout = open('output.txt','wt')
sys.stdin = open('input.txt','rt')

def parse_input():
    regex_pattern = r"Card\s+(?P<card_num>\d+):\s+(?P<winning>[0-9, ]+)\s+\|\s+(?P<owned>[0-9, ]+)"
    lines = sys.stdin.readlines()
    lines = [line.strip() for line in lines]
    games = []
    for line in lines:
        winning, owned = [], []
        match = regex.match(regex_pattern, line)
        # ic(match)
        if match:
            winning = list(map(int, match.group("winning").split()))
            # ic(winning)
            owned = list(map(int, match.group("owned").split()))
            # ic(owned)
            games.append((winning, owned))
        else:
            raise ValueError("Invalid input")
    return games

def solve():
    games = parse_input()
    res = 0
    for winning, owned in games:
        cur = 0
        s = set(winning)
        for num in owned:
            if num in s:
                cur = 1 if cur == 0 else cur * 2
        res += cur
    print(res)


def main():
    solve()

if __name__ == "__main__":
    main()
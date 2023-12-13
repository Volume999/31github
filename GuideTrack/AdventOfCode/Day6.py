import sys
from icecream import ic
from regex import regex
sys.stdout = open('output.txt','wt')
sys.stdin = open('input.txt','rt')

def parse_input():
    data = sys.stdin.readlines()
    times = list(filter(lambda k: k != "", map(lambda k: k.strip(), data[0].split(":")[1].strip().split(" "))))
    distances = list(filter(lambda k: k != "", map(lambda k: k.strip(), data[1].split(":")[1].strip().split(" "))))
    ic(times)
    ic(distances)
    return times, distances

def left_bs(time, distance, l, r):
    ans = -1
    while l < r:
        m = l + (r - l) // 2
        d = m * (time - m)
        if d > distance:
            ans = m
            r = m
        else:
            l = m + 1
    return ans

def right_bs(time, distance, l, r):
    ans = -1
    while l < r:
        m = l + (r - l) // 2
        d = m * (time - m)
        if d > distance:
            ans = m
            l = m + 1
        else:
            r = m
    return ans

def solve_task(time, distance):
    l = 0
    r = time
    s1 = ic(left_bs(time, distance, l, r))
    s2 = ic(right_bs(time, distance, l, r))
    return s2 - s1 + 1

def solve():
    times, distances = parse_input()
    tasks = list(zip(times, distances))
    res = 0
    for time, distance in tasks:
        val = solve_task(int(time), int(distance))
        ic(val)
        res = val if not res else res * val
    print(res)

    

def main():
    solve()

if __name__ == "__main__":
    main()
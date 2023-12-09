import sys
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
        for set in sets:
            s2 = set.split(",")
            # print(s2)
            for balls in s2:
                balls = balls.strip().split()
                num = int(balls[0])
                color = balls[1]
                # print(balls, color)
                if num > lims[color]:
                    good = False
                    break
            if not good:
                break
        if good:
            res += gameId
    print(res)
def main():
    solve()

if __name__ == "__main__":
    main()
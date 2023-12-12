import sys
from icecream import ic
import string
from itertools import product
from regex import regex
from collections import defaultdict
sys.stdout = open('output.txt','wt')
sys.stdin = open('input.txt','rt')

class Graph:
    def __init__(self):
        self.g = [[] for _ in range(7)]
    
    def get_path(self, n):
        soil = n if n not in self.g[0].keys() else self.g[0][n]
        fert = soil if soil not in self.g[1] else self.g[1][soil]
        water = fert if fert not in self.g[2] else self.g[2][fert]
        light = water if water not in self.g[3] else self.g[3][water]
        temp = light if light not in self.g[4] else self.g[4][light]
        hum = temp if temp not in self.g[5] else self.g[5][temp]
        loc = hum if hum not in self.g[6] else self.g[6][hum]
        ic(n, soil, fert, water, light, temp, hum, loc)
        return int(loc)

    def sort(self):
        for i in range(7):
            self.g[i].sort(key=lambda x: x[0])

# def parse_input():
#     g = Graph()
#     idx = 0
#     seeds = map(int, input().split(":")[1].strip().split())
#     ic(seeds)
#     input()
#     for idx in range(7):
#         l = input()
#         l = input()
#         while l != "":
#             s, d, l = map(int, l.split())
#             ic(s, d, l, idx)
#             for i in range(l):
#                 g.g[idx].append(())
#             ic(g.g[idx])
#             l = input()
#     ic(seeds)
#     return seeds, g

def solve():
    data = sys.stdin.read().split("\n\n")
    seeds = regex.findall(r'\d+', data[0])

    min_loc = float('inf')
    for x in map(int, seeds):
        for seg in data[1:]:
            for conversion in regex.findall(r"(\d+) (\d+) (\d+)", seg):
                destination, start, delta = map(int, conversion)
                if x in range(start, start + delta):
                    x += destination - start
                    break
        min_loc = min(min_loc, x)
    print(min_loc)

def solve2():
    segments = sys.stdin.read().split("\n\n")
    intervals = []

    for seed in regex.findall(r'(\d+) (\d+)', segments[0]):
        x1, dx = map(int, seed)
        x2 = x1 + dx
        intervals.append((x1, x2, 1))

    min_location = float('inf')
    while intervals:
        x1, x2, level = intervals.pop()
        if level == 8:
            min_location = min(x1, min_location)
            continue

        for conversion in regex.findall(r'(\d+) (\d+) (\d+)', segments[level]):
            z, y1, dy = map(int, conversion)
            y2 = y1 + dy
            diff = z - y1
            if x2 <= y1 or y2 <= x1:    # no overlap
                continue
            if x1 < y1:                 # split original interval at y1
                intervals.append((x1, y1, level))
                x1 = y1
            if y2 < x2:                 # split original interval at y2
                intervals.append((y2, x2, level))
                x2 = y2
            intervals.append((x1 + diff, x2 + diff, level + 1)) # perfect overlap -> make conversion and let pass to next nevel 
            break

        else:
            intervals.append((x1, x2, level + 1))
  
    print(min_location)
    



def main():
    solve2()

if __name__ == "__main__":
    main()

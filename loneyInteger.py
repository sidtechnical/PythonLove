#!/usr/bin/py
def lonelyinteger(a):
    from collections import Counter
    answer = Counter(a).most_common()[:-2:-1][0][0]
    return answer
if __name__ == '__main__':
    a = input()
    b = map(int, raw_input().strip().split(" "))
    print lonelyinteger(b)

from pprint import pprint

LIMIT = 3  # 0,1,2,3


def f(lists):
    for start in range(len(lists)):
        space = [i for i in range(len(lists)) if i != start]
        for i in space:
            state, fl = sip(lists, start, i)
            if fl:
                if win(state):
                    return [[start, i]]
                else:
                    res = f(state)
                    if res is not None:
                        res.append([start, i])
                        return res

    return None

    # return space


def first(l):
    for i in range(len(l)):
        if l[i] != 0:
            return l[i], i
    return 0, LIMIT


def sip(lists, fr, to):
    q = [x[:] for x in lists]
    changed = False
    fr_l = q[fr]
    to_l = q[to]
    w, ai = first(fr_l)
    while True:
        a, ai = first(fr_l)
        b, bi = first(to_l)
        if a == 0 and b == 0:
            break
        if b == 0:
            fr_l[ai] = 0
            to_l[bi] = a
            changed = True
            continue
        if bi <= 0:
            break
        if a == b:
            fr_l[ai] = 0
            to_l[bi - 1] = a
            changed = True
        if a != b:
            break
    if first(fr_l)[0] == w or fr_l == lists[to]:
        changed = False
    return (q, changed) if changed else (lists, changed)


def win(lists):
    for i in lists:
        for j in i:
            if i[-1] != j:
                return False
    return True


def main():
    # 1  2  3  4
    start = [[1, 2, 3, 4],  # 1
             [2, 5, 3, 6],  # 2
             [7, 6, 8, 4],  # 3
             [8, 8, 7, 9],  # 4
             [10, 4, 10, 5],  # 5
             [4, 6, 5, 11],  # 6
             [3, 7, 11, 7],  # 7
             [1, 11, 9, 12],  # 8
             [11, 1, 8, 6],  # 9
             [10, 1, 9, 10],  # 10
             [12, 12, 2, 9],  # 11
             [2, 12, 5, 3],  # 12
             [0, 0, 0, 0],  # 14
             [0, 0, 0, 0]]  # 14
    # pprint(start)
    test1 = [[0, 1, 1, 1],
             [0, 2, 1, 1]]
    test2 = [[1, 1, 1, 1],
             [0, 0, 0, 1]]
    test3 = [[0, 1, 1, 1],
             [0, 0, 0, 0]]
    test4 = [[0, 1, 1, 1],
             [0, 0, 0, 1]]
    test5 = [[0, 1, 1, 1],
             [0, 0, 1, 2],
             [0, 2, 2, 2]]
    test6 = [[2, 1, 1, 1],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [1, 2, 2, 2]]

    x = f(start)
    x.reverse()
    # Menu - what actions are supposed to be done
    for fr, to in x:
        print("Put from {} to {}".format(fr + 1, to + 1))
    # print(x)


if __name__ == '__main__':
    main()

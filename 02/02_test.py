f = 'input'
# f = '2_test.in'
D = open(f).read().strip()


def is_safe(lvl):
    x1 = lvl[0]
    x2 = lvl[1]
    if abs(x1 - x2) > 3:
        return False
    if x1 < x2:
        # inc
        for i in range(2, len(lvl)):
            if lvl[i - 1] >= lvl[i]:
                return False
            if lvl[i] - lvl[i - 1] > 3:
                return False
    elif x1 > x2:
        # dec
        for i in range(2, len(lvl)):
            if lvl[i - 1] <= lvl[i]:
                return False
            if lvl[i - 1] - lvl[i] > 3:
                return False
    else:
        return False
    return True


def is_safe2(lvl):
    for idx_rem in range(len(lvl)):
        lvl_cp = lvl[:idx_rem] + lvl[idx_rem + 1:]
        if is_safe(lvl_cp):
            return True
    return False


safe = 0
safe2 = 0
for line in D.split('\n'):
    lvl = [int(x) for x in line.split()]
    safe += is_safe(lvl)
    safe2 += is_safe2(lvl)
    pass


print(safe)
print(safe2)

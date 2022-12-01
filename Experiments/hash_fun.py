def deliting(mi, group):
    if isinstance(group, set):
        group.discard(mi)
    elif isinstance(group, list):
        del group[group.index(mi)]
    elif isinstance(group, tuple):
        group = list(group)
        del group[group.index(mi)]
    return group


def sort_priority(values, group):
    def h():
        ans = []
        nonlocal values, group
        while True:
            if len(group) == 0:
                break
            else:
                mi = min(group)
                if mi in values:
                    id = values.index(mi)
                    ans.append(values[id])
                    del values[id]
                    group = deliting(mi, group)
                else:
                    group = deliting(mi, group)
        
        ans.extend(sorted(values))
        values[:] = ans
    h()
            
numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {5, 7, 2, 3}
sort_priority(numbers, group)

print(numbers)



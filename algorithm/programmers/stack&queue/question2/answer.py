def solution(priorities, location):
    p_list = [p for p in range(len(priorities))]
    a_list = []

    while priorities:
        if priorities[0] == max(priorities):
            a_list.append(p_list.pop(0))
            priorities.pop(0)
        else:
            p_list.append(p_list.pop(0))
            priorities.append(priorities.pop(0))
    return a_list.index(location)+1

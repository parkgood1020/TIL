def solution(bridge_length, weight, truck_weights):
    time = 0
    b_list = [0] * bridge_length
    sum_weight = 0
    while b_list:
        time += 1
        sum_weight -= b_list.pop(0)
        if truck_weights:
            if truck_weights[0] + sum_weight <= weight:
                sum_weight += truck_weights[0]
                b_list.append(truck_weights.pop(0))
            else:
                b_list.append(0)
    return time

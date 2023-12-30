def fractional_knapsack(knapsack, values):
    values.sort(key=lambda x: x[0]/x[1], reverse=True)
    w = knapsack[1]
    total = 0
    for item in values:
        total += item[0]/item[1] * min(w, item[1])
        w -= min(w, item[1])
        if w == 0:
            break

    return round(total, 4)

knapsack = list(map(int, input().split()))
values = []
for i in range(knapsack[0]):
    values.append(list(map(int, input().split())))

print(fractional_knapsack(knapsack, values))
    

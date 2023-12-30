def car_fueling(total_dist, max_tank, stops):
    tank = max_tank
    stops = [0] + stops + [total_dist]
    num_fuel = 0
    for i in range(len(stops[:-1])):
        d = stops[i + 1] - stops[i]
        if d <= tank:
            tank -= d
        elif tank < d <= max_tank:
            tank = max_tank - d
            num_fuel += 1
        else:
            return -1
    return num_fuel

total_dist = int(input())
max_tank = int(input())
n = int(input())
stops = list(map(int, input().split()))
print(car_fueling(total_dist, max_tank, stops))
        
            

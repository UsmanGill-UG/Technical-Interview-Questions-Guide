import sys


def sum_of_above_floors(floors, current_floor, building):
    upper_floor_sum = 0
    floor_number = 0
    while floor_number < current_floor:
        upper_floor_sum += floors[floor_number][building]
        floor_number += 1
    return upper_floor_sum


def fill_zeros_in_above_floors(floors, floor_number, building):
    while floor_number >= 0:
        floors[floor_number][building] = 0
        floor_number -= 1
    return floors


def merge_floors(merges_remaining, floors, floor_number, buildings):
    for building in range(buildings):
        merges_left_loop = merges_remaining
        floor_number_loop = floor_number
        while merges_left_loop > 0:
            merge = False
            upper_floors_sum = sum_of_above_floors(floors, floor_number_loop, building)
            if floors[floor_number_loop][building] < upper_floors_sum:
                merge = True
                floors = fill_zeros_in_above_floors(floors, floor_number_loop - 1, building)
                floors[floor_number_loop][building] += upper_floors_sum
            if not merge:
                break
            merges_left_loop -= 1
            floor_number_loop += 1
    return floors


def simulate(simulations, merges, floors, buildings):
    for floor_number, _ in enumerate(range(simulations), start=1):
        if floor_number > len(floors) - 1:
            return floors
        floors = merge_floors(merges, floors, floor_number, buildings)
    return floors


def calculate_standing_floors(floors, buildings):
    floors_remaining = []
    for building in range(buildings):
        count = 0
        for floor_number in range(len(floors)):
            if floors[floor_number][building] != 0:
                count = len(floors) - count
                break
            else:
                count += 1
        floors_remaining.append(count)
    return floors_remaining


input_file = sys.argv[1]
f = open(input_file, "r")
simulations = int(f.readline())
merges = int(f.readline())
number_of_buildings = 0
number_of_floors = int(f.readline())

floors = []

for _ in range(number_of_floors):
    input = f.readline()
    input = input.split(',')
    input = [eval(i) for i in input]  # converting string to int
    number_of_buildings = len(input)
    floors.append(input)

floors = simulate(simulations, merges, floors, number_of_buildings)
standing_floors = calculate_standing_floors(floors, number_of_buildings)

result = ','.join(str(item) for item in standing_floors)
print(result)

import sys

def accommodate_tourists(tourists, seats):
    seats_index = 0
    lp = 0
    rp = len(tourists) - 1
    while lp <= rp:
        if tourists[lp] <= seats[seats_index]:
            seats[seats_index] -= tourists[lp]
            lp += 1
        elif tourists[rp] <= seats[seats_index]:
            seats[seats_index] -= tourists[rp]
            rp -= 1
        else:
            tourists[rp] -= seats[seats_index]
            seats[seats_index] -= seats[seats_index]
        if seats[seats_index] == 0:
            seats_index += 1
    return seats_index + 1


input_file = sys.argv[1]
f = open(input_file, "r")
tourists = f.readline()
seats = f.readline()
tourists = tourists.split(',')
seats = seats.split(',')
# Converting elements type to int
tourists = [eval(i) for i in tourists]
seats = [eval(i) for i in seats]
tourists.sort(reverse=True)
seats.sort(reverse=True)
print(accommodate_tourists(tourists, seats))

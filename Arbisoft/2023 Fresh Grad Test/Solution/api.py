import requests
import sys


# get all rides of the driver_id
def get_driver_rides(rides, driver_id):
    return [ride for ride in rides if ride['driver_id'] == int(driver_id)]


# get all driver payments of the driver_id
def get_driver_payments_sum(driver_id):
    payments_data = [
        int(payment['amount'])
        for payment in payments
        if payment['driver_id'] == int(driver_id)
    ]
    return sum(payments_data)


def calculate_commission(ride, joining_date):
    ride_date = ride['trip_date']
    ride_date = ride_date.split('/')
    month = int(ride_date[0])
    if month == int(joining_date[0]) + 1:  # 10%
        return 0.10 * ride['trip_details']['fare']
    elif month > int(joining_date[0]) + 1:  # 20%
        return 0.20 * ride['trip_details']['fare']
    return 0


def get_commission(total_rides, joining_date):
    return sum(calculate_commission(ride, joining_date) for ride in total_rides)


def calculate_payback(total_rides, number_of_testcases, joining_date):
    for test_case in range(number_of_testcases):
        rides = get_driver_rides(total_rides, driver_ids[test_case])
        commission = get_commission(rides, joining_date[test_case])
        driver_payment = get_driver_payments_sum(driver_ids[test_case])
        payback = driver_payment - commission
        print(round(payback, 1))


rides = requests.get("https://www.jsonkeeper.com/b/DM5F")
payments = requests.get("https://www.jsonkeeper.com/b/9QRZ")
rides = rides.json()
payments = payments.json()
input_file = sys.argv[1]
f = open(input_file, "r")
numberOfTestCases = int(f.readline())
driver_ids = []
joining_date = []  # [month, day , year]

for _ in range(numberOfTestCases):
    input = f.readline()
    input = input.split(',')
    driver_ids.append(input[0])
    joining_date.append(input[1].split('/'))

calculate_payback(rides, numberOfTestCases, joining_date)

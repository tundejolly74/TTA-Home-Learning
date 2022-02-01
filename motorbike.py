# Motorbike Depreciation
bike_cost= 2000.00
cost= bike_cost
year = 0

print("yearly depreciation of motorbike value:")

while cost >= 1000.00:
    print("Year", year, ":", cost)
    year = year + 1
    cost = cost - (cost/10)


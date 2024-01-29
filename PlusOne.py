# Number 66

# Finished

# Runtime: 18 ms (Beats 46.72% of Python Users)

# Memory 11.41 mb (Beats 99.46% of Python Users)

digits = [1, 2, 3]

length = len(digits)

firstTotal = ""

finalTotal = 0

finalArray = []

for nums in digits:
    strings = str(nums)
    firstTotal += strings

firstTotal = int(firstTotal)

finalTotal = firstTotal + 1

finalTotal = str(finalTotal)

for i in finalTotal:
    finalArray.append(int(i))

print(finalArray)
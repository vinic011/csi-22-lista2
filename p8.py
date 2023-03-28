def filter_even(numbers):
    return list(filter(lambda x: x%2 == 0,numbers))

print(filter_even([1,2,4,5,6]))
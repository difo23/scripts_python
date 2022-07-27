# Create function return the number of even in a list
# numberPairs - camelCase - Javascript
# number_pairs - snake_case - python


def is_prime(n):
    for div in range(2, n // 2 + 1):
        if n % div == 0:
            return False
    return True


 # not and or
def number_prime(nums):
    count_prime = 0
    
    for num in nums:
        if not is_prime(num):
            count_prime += 1
            
    return count_prime

# Example:
nums_list = [3, 5, 3, 6, 2, 7, 8, 6, 9]

# Result: 4

result = number_prime(nums_list)

if result ==  5:
    print("Correct:", result)
else:
    print("Incorrect: ", result)

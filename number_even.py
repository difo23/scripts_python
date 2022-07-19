# Create function return the number of even in a list
# numberPairs - camelCase - Javascript
# number_pairs - snake_case - python

def number_pairs(nums):
    count_pairs = 0
    
    for num in nums:
        if num % 2 == 0:
            count_pairs += 1
            
    return count_pairs

# Example:
nums_list = [3, 5, 3, 6, 2, 7, 8, 6, 9]

# Result: 4

result = number_pairs(nums_list)

if result ==  4:
    print("Correct:", result)
else:
    print("Incorrect: ", result)

def even_numbers(numbers):
    return (n for n in numbers if n % 2 == 0)

# Sample usage
nums = [1, 2, 3, 4, 5, 6]
result = even_numbers(nums)
print(list(result))
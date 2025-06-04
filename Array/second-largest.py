def second_largest(arr):
    if len(arr) < 2:
        return "Array should have at least two numbers"
    first = float('-inf')
    second = float('-inf')
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second if second != float('-inf') else "No second largest found"

print(second_largest([0,20,20,10,9,10]))  # 7
    
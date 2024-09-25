def ContainDuplicate_fun(num_array):
    seen = set()
    for num in num_array:
        if num in seen:
            return True
        seen.add(num)

    return False

inputArr =list(map(int, input("Input an integer array (Separate with commas): ").split(",")))
print(f"Input array {inputArr} got duplicates. ") if ContainDuplicate_fun(inputArr) else print(f"The input array {inputArr} dont include a duplicate integer.")
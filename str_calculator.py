import sys

def add(nums: str) -> int:
    try:
        # empty string
        if not nums:
            return 0

        delimiter = ','

        # Check for custom delimiter in format "//[delimiter]\n[numbers…]"
        if nums.startswith("//"):
            delimiter_part, nums = nums.split('\n', 1)
            delimiter = delimiter_part[2:]

        # Normalize delimiters
        nums = nums.replace('\n', ',').replace(delimiter, ',')

        numbers_list = [int(num.strip()) for num in nums.split(',')]
        negative_numbers_list = [num for num in numbers_list if num < 0]

        if negative_numbers_list:
            negatives_str = ', '.join(str(num) for num in negative_numbers_list)
            raise ValueError(f"negative numbers not allowed {negatives_str}")

        return sum(numbers_list)
    
    except Exception as e:
        print("Issue in calculating the string resultant.", e)
        raise


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("python str_calculator.py '<numbers_string>'")
        sys.exit(1)

    input_string = sys.argv[1]
    try:
        result = add(input_string)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e}")
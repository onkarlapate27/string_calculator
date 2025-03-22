def add(nums: str) -> int:
    try:
        # empty string
        if not nums:
            return 0
        
        delimiter = ','

        # Check for custom delimiter in format "//[delimiter]\n[numbers…]"
        if nums.startswith("//"):
            split_str = nums.split('\n', 1)
            delimiter = split_str[0][2:]
            nums = split_str[1]

        # Normalize delimiters
        nums = nums.replace('\n', ',')
        nums = nums.replace(delimiter, ',')
        int_numbers_list = [int(num.strip()) for num in nums.split(',')]

        return sum(int_numbers_list)
    
    except Exception as e:
        print("Issue in calculating the string resultant.", e)
        return 0
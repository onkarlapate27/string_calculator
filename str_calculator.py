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
        negative_numbers_list = [num for num in int_numbers_list if num < 0]

        if len(negative_numbers_list) > 0:
            negative_nums_str = str(negative_numbers_list[0])
            if len(negative_numbers_list) > 1:
                for num in range(1, len(negative_numbers_list)):
                    negative_nums_str += f', {str(negative_numbers_list[num])}'

            raise ValueError(f"negative numbers not allowed {negative_nums_str}")

        return sum(int_numbers_list)
    
    except Exception as e:
        print("Issue in calculating the string resultant.", e)
        raise
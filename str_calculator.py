def add(nums: str) -> int:
    # empty string
    if not nums:
        return 0
    # n numbers
    else:
        nums = nums.replace('\n', ',')
        int_numbers_list = [int(num.strip()) for num in nums.split(',')]
        return sum(int_numbers_list)
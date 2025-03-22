def add(nums: str) -> int:
    # empty string
    if not nums:
        return 0
    # n comma separated numbers
    else:
        int_numbers_list = [int(num) for num in nums.split(',')]
        return sum(int_numbers_list)
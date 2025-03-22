def add(nums: str) -> int:
    # empty string
    if nums == "":
        return 0
    
    # n numbers with comma separated values
    if ',' in nums:
        numbers_list = nums.split(',')
        addition = 0

        for item in numbers_list:
            addition += int(item)
        
        return addition
    
    return int(nums)
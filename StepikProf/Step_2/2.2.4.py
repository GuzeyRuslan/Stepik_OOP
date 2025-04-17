def counter_nums(data, num):
    total = 0
    for i in data:
        if num == i:
            total += 1
    return total



nums = list(map(lambda x: int(x), input().split()))

nums_dict = {num: counter_nums(nums, num) for num in set(nums)}
for key in nums_dict.keys():
    if nums_dict[key] > 1:
        print(key, end=" ")
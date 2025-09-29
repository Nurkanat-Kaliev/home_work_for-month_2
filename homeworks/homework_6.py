nums = [2, 7, 11, 15]
target = 9
target_index = []

for i in range(len(nums)):
    for j in range(1,len(nums)):
        if nums[i] + nums[j] == target:
            target_index = [i,j]
            break

    if target_index:
        break

print(target_index)




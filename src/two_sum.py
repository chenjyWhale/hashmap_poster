def two_sum_bruteforce(nums, target):
    # 暴力解法：O(n²)
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def two_sum_hashmap(nums, target):
    # 哈希表优化：O(n)
    hash_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hash_map:
            return [hash_map[complement], i]
        hash_map[num] = i
    return []


# 测试
if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9
    print("暴力解法结果:", two_sum_bruteforce(nums, target))
    print("哈希表解法结果:", two_sum_hashmap(nums, target))
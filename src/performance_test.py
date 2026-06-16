import timeit
import numpy as np
#from memory_profiler import profile
from hash_table import HashTable
from two_sum import two_sum_bruteforce, two_sum_hashmap


# @profile
def test_hashmap_ops():
    """测试哈希表插入、查询性能"""
    np.random.seed(42)
    nums = np.random.randint(0, 100000, 10000)  # 数据量先设小一点，避免跑太久

    ht = HashTable(size=1000)

    insert_time = timeit.timeit(
        lambda: [ht.insert(num) for num in nums],
        number=1
    )
    print(f"哈希表插入10000条数据耗时: {insert_time:.6f}s")

    query_time = timeit.timeit(
        lambda: ht.search(np.random.choice(nums)),
        number=1000
    )
    print(f"哈希表查询1000次平均耗时: {query_time/1000:.8f}s")


def test_two_sum_perf():
    """对比暴力vs哈希表解法耗时"""
    np.random.seed(42)
    nums = np.random.randint(0, 100000, 1000)  # 数据量设小一点，避免暴力解法跑太久
    target = np.random.randint(0, 200000)

    brute_time = timeit.timeit(
        lambda: two_sum_bruteforce(nums, target),
        number=1
    )
    print(f"暴力解法耗时: {brute_time:.6f}s")

    hash_time = timeit.timeit(
        lambda: two_sum_hashmap(nums, target),
        number=10
    ) / 10
    print(f"哈希表解法平均耗时: {hash_time:.6f}s")


if __name__ == "__main__":
    print("===== 哈希表基础操作测试 =====")
    test_hashmap_ops()
    print("\n===== 两数之和解法对比测试 =====")
    test_two_sum_perf()
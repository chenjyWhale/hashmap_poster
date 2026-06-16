import os
import matplotlib.pyplot as plt
import numpy as np
import timeit
from hash_table import HashTable
from two_sum import two_sum_bruteforce, two_sum_hashmap

# ========== 修复1：Windows中文显示，只用系统自带黑体 ==========
plt.rcParams["font.family"] = "SimHei"
plt.rcParams["axes.unicode_minus"] = False

# ========== 修复2：自动创建result文件夹，不存在就新建 ==========
save_dir = "./result"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# 1. 哈希查询耗时折线图
def draw_hash_search_curve():
    data_sizes = [1000, 5000, 10000, 20000, 50000]
    search_cost = []
    for size in data_sizes:
        np.random.seed(42)
        nums = np.random.randint(0, 1000000, size)
        ht = HashTable(size=size//10)
        for num in nums:
            ht.insert(num)
        t = timeit.timeit(lambda: ht.search(np.random.choice(nums)), number=2000)
        avg_t = t / 2000
        search_cost.append(avg_t)
    plt.figure(figsize=(8,4))
    plt.plot(data_sizes, search_cost, marker="o", c="#2E86AB", label="哈希表单次查询耗时")
    plt.xlabel("数据总量")
    plt.ylabel("单次查询耗时(s)")
    plt.title("哈希表查询耗时随数据规模变化曲线")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.savefig(f"{save_dir}/hash_search_curve.png", dpi=300)
    plt.show()

# 2. 两数之和暴力/哈希对比柱状图
def draw_twosum_bar():
    data_sizes = [500, 1000, 2000, 3000]
    brute_time = []
    hash_time = []
    for size in data_sizes:
        np.random.seed(42)
        nums = np.random.randint(0, 200000, size)
        target = np.random.randint(0, 400000)
        t1 = timeit.timeit(lambda: two_sum_bruteforce(nums, target), number=1)
        brute_time.append(t1)
        t2 = timeit.timeit(lambda: two_sum_hashmap(nums, target), number=10)/10
        hash_time.append(t2)
    x = np.arange(len(data_sizes))
    width = 0.35
    plt.figure(figsize=(8,4))
    plt.bar(x-width/2, brute_time, width, label="暴力解法 O(n^2)", color="#A23B72")
    plt.bar(x+width/2, hash_time, width, label="哈希表解法 O(n)", color="#F18F01")
    plt.xticks(x, data_sizes)
    plt.xlabel("数组数据量")
    plt.ylabel("运行耗时(s)")
    plt.title("两数之和：暴力解法 vs 哈希表性能对比")
    plt.legend()
    plt.savefig(f"{save_dir}/twosum_compare.png", dpi=300)
    plt.show()

if __name__ == "__main__":
    draw_hash_search_curve()
    draw_twosum_bar()
from performance_test import test_hashmap_ops, test_two_sum_perf

if __name__ == "__main__":
    print("===== 运行所有性能测试 =====")
    test_hashmap_ops()
    print("\n" + "="*50 + "\n")
    test_two_sum_perf()
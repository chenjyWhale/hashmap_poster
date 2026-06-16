class HashTable:
    def __init__(self, size=100, load_factor_limit=0.75):
        self.table_size = size
        self.load_factor_limit = 0.75
        self.table = [[] for _ in range(self.table_size)]
        self.total_elements = 0
    def hash_func(self, val):
        return val  % self.table_size  # 取模哈希函数
    def get_load_factor(self):
        return self.total_elements / self.table_size  # 计算当前负载因子，衡量哈希冲突程度
    def resize_expand(self):
        old_table = self.table
        self.table_size *= 2
        self.table = [[] for _ in range(self.table_size)]
        self.total_elements = 0
        for bucket in old_table:
            for num in bucket:
                self.insert(num)  # 负载因子超过0.75自动扩容，容量翻倍并重哈希全部数据
    def insert(self, val):
        if self.get_load_factor() >= self.load_factor_limit:  # 达到阈值自动扩容
            self.resize_expand()
        idx = self.hash_func(val)
        if val not in self.table[idx]:
            self.table[idx].append(val)
            self.total_elements += 1
    def search(self, val):
        idx = self.hash_func(val)
        for item in self.table[idx]:
            if item == val:
                return True
        return False
    def delete(self, val):
        idx = self.hash_func(val)
        if val in self.table[idx]:
            self.table[idx].remove(val)
            self.total_elements -= 1
            return True
        return False

# 本地自测
if __name__ == "__main__":
    ht = HashTable(size=10)
    for i in range(20):
        ht.insert(i)
    print("当前负载因子：", ht.get_load_factor())
    print("查询10：", ht.search(10))
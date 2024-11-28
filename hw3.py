def josephus(n, k):
    # 使用遞迴解決約瑟夫問題
    if n == 1:
        return 1
    else:
        return (josephus(n - 1, k) + k - 1) % n + 1

# 輸入
n = int(input("請輸入朋友數量 n: "))
k = int(input("請輸入報數間隔 k: "))

# 輸出
result = josephus(n, k)
print("最後留下來的人的編號是:", result)

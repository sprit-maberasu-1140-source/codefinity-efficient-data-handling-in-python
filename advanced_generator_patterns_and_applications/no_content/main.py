def number_pipeline(numbers):
    # 1. 偶数だけを取り出すフィルター
    def filter_even(nums):
        for n in nums:
            if n % 2 == 0:
                yield n

    # 2. 数を二乗する変換
    def square(nums):
        for n in nums:
            yield n * n

    # 3. 20より大きい値だけを取り出すフィルター
    def filter_greater_than_20(nums):
        for n in nums:
            if n > 20:
                yield n

    # フィルターと変換をつなげて順番に実行する
    return filter_greater_than_20(
        square(
            filter_even(numbers)
        )
    )

# 動かしてみる例
result = number_pipeline([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
for value in result:
    print(value)
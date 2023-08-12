# dict = 連想配列
itemById = {"1": 9, "2": 9}

# list
items = ["1", "2"]

# for
for i in items:
    print(i)

# リスト内包表記
items2 = [i for i in items]

# リスト内包表記
itemById2 = {key: key for key in items}
print(itemById2.get('1'))

import json

item = (
    ('deviceId', 2737),
    ('version', 250),
)

item2 = (
    ('deviceId', 2738),
    ('version', 250),
)

items = [dict(item), dict(item2)]

# ここが内包表記
itemByKey = {items[i]['deviceId']: items[i] for i in range(len(items))}
root = {"deviceInfo": itemByKey}

a = json.dumps(root, indent=2)

print(a)

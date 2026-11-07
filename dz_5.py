result = []

def divider(a, b):
    if a < b:
        raise ValueError("ValueError: a менше за b")
    if b > 100:
        raise IndexError("IndexError: b більше за 100")
    return a / b


data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}

for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except Exception as e:
        print(type(e).__name__, "-", e)

print(result)
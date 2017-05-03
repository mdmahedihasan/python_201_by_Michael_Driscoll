from collections import namedtuple


parts = {"id_num": "1234", "desc": "Ford engine", "cost": 1200, "amount": 10}
pts = namedtuple("parts", parts.keys())(**parts)

print(pts)

pts = namedtuple("parts", parts.keys())
print(pts)
auto_parts = pts(**parts)
print(auto_parts)
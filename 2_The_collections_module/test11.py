from collections import namedtuple


parts = namedtuple('parts', "id_num desc cost amount")
auto_parts = parts(id_num="1234", desc="Ford Engine", cost=1200, amount=10)

print(auto_parts.id_num)
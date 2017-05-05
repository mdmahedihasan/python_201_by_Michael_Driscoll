from itertools import count
from itertools import islice


for i in islice(count(10), 5):
    print(i)
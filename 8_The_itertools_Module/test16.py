from itertools import islice
from itertools import count


for i in islice(count(), 3, 11):
    print(i)
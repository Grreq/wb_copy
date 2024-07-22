import random
from collections import defaultdict
d = defaultdict(list)


list = ['Шорты', 'Футболка', 'Кроссовки','Джинсы','Майка','Носки']



for i in range(10):
    rr = random.randint(1, 10)
    rc = random.choice(list)
    try:
        d[rr].append(rc)
    except KeyError:
        d[rr] = random.choice(list)

print(d)

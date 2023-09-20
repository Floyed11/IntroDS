import random
import math

times = 10000000
cnt = 0
for i in range(times):
    x = random.random() + 2.0
    y = random.random() * 21.0
    if (y <= (x * x + 4 * x * math.sin(x))):
        cnt +=1
    
ans = cnt / times * 21
print(ans)
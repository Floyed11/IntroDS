import time

start_time = time.time()

# 具体程序
for i in range(100000000):
    pass

end_time = time.time()

run_time = end_time - start_time
print("程序运行时间为：", run_time, "秒")
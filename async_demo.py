import asyncio
import time


async def task(name, seconds):
    print(f"{name} 开始")
    await asyncio.sleep(seconds)
    print(f"{name} 结束")



async def serial():
    start = time.time()
    await task("A", 2)
    await task("B", 2)
    return time.time() - start



async def paralell():
    start = time.time()
    await asyncio.gather(task("A", 2), task("B", 2))
    return time.time() - start



print(f"串行耗时： {asyncio.run(serial()):.2f} 秒")
print(f"并行耗时： {asyncio.run(paralell()):.2f} 秒")
import asyncio
from typing import Callable, Awaitable
class CronLike:
    def __init__(self): self.jobs = []
    def every(self, seconds: int, job: Callable[[], Awaitable[None]]): self.jobs.append((seconds, job))
    async def run_forever(self): 
        tasks = [self._runner(i,j) for i,j in self.jobs]
        await asyncio.gather(*tasks)
    async def _runner(self, interval, job):
        await asyncio.sleep(2)
        while True:
            try:
                await job()
            except Exception as e:
                print("[SCHED ERROR]", e)
            await asyncio.sleep(interval)
SCHED = CronLike()

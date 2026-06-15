import asyncio

async def task1(name):
    print(f"Start : {name}")
    await asyncio.sleep(1)
    print(f"End : {name}")
    return f"{name} : Completed"


async def main():
    # Create and schedule the tasks for execution.
    t2 = asyncio.create_task(task1("B"))
    t1 = asyncio.create_task(task1("A"))

    # Query the current task status.
    # At this point the tasks are scheduled but may not have run yet.
    print(f"  t1 status : {t1.done()}")
    print(f"  t2 status : {t2.done()}")

    # Wait for both tasks to complete.
    # While waiting, the event loop runs the scheduled tasks.
    results = await asyncio.gather(t1, t2)

    # Query the task status again.
    # Both tasks have completed, so done() should be True.
    print(f"  t1 status : {t1.done()}")
    print(f"  t2 status : {t2.done()}")

    # Print the return values from all tasks.
    # Results are returned in the same order passed to gather().
    print(f"All tasks results : {results}")

    print("END")

asyncio.run(main())

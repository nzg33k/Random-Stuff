"""Demonstrate a silly way of sorting numbers."""

import asyncio

async def sort_item(item, sleep_modifier):
    """Wait for the item time. 
    Higher sleep modifiers make it faster but could make it less accurate."""
    await asyncio.sleep(item/sleep_modifier)
    return item

async def sort_items(list_to_sort, sleep_modifier=1):
    """Sort the list of items. See 'sort_item' for details on sleep_modifier"""
    results=[]
    tasks=[]
    for item in list_to_sort:
        tasks.append(asyncio.create_task(sort_item(item, sleep_modifier)))
    for result in asyncio.as_completed(tasks):
        results.append(await result)
    return results

def boring_sort(list_to_sort):
    """Cleaner, more efficient, basically better in every way but one,
    it isn't as much fun!"""
    list_to_sort.sort()
    return list_to_sort

data=[5,1,2,1.9,7,3]
print(asyncio.run(sort_items(data)))
#print(boring_sort(data))

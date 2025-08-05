"""Demonstrate a silly way of sorting numbers.

The best way I can describe this really, is imagine you have a list of numbers
You give a number out to each person, 
and tell them to count to that number (divided by the modifier).

Then as they come back you collect their number as it arrives.

Those that have a smaller number will come back sooner, 
those with a bigger number will take longer.

The flaw with sleep_modifier
----------------------------
It takes x time for you to give each person their number. So the first person has a
head start of x. These are cumulative. So the fifth item takes item/modifier + 5x to come back.
If the gap is smaller than 5x then they will arrive out of order!
"""

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
    # Create a task for each list item
    for item in list_to_sort:
        tasks.append(asyncio.create_task(sort_item(item, sleep_modifier)))
    # Collect the sort_item return values as they arrive
    for result in asyncio.as_completed(tasks):
        results.append(await result)
    return results

def boring_sort(list_to_sort):
    """Cleaner, more efficient, basically better in every way but one,
    it isn't as much fun!"""
    list_to_sort.sort()
    return list_to_sort

data=[5,1,2,1.9,7,3]
print(asyncio.run(sort_items(data,10000)))
#print(boring_sort(data))

"""
I was talking to a colleague about why we needed a try-except rather than an if-else. 
This seems to explain it fairly well. 
You can highlight it further by removing each block in turn.
I am purposefully using a broad except to demonstrate better, hence disabling the lint prompt.
Of course, I do not expect the diretory to ever be made successfully.

Don't run this as an administrator/root, otherwise it will work and that is not good.
"""
import os

if os.name == "nt":
    PATH_TO_CREATE = "c:\\Windows\\System32\\testthisout"
else:
    PATH_TO_CREATE = "/bin/testthisout"

print("Try a try-except approach")
try:
    os.makedirs(PATH_TO_CREATE)
except Exception as e: # pylint: disable=broad-except
    print(f"It did not work {e}")
else:
    print("it worked!")
finally:
    print("Finished executing the try-except approach, execution continues.\n\n")

print("Now try using if-else:")
# This won't get past the first line before dying as the osError is unhandled.
# Execution will not continue.
if os.makedirs(PATH_TO_CREATE):
    print("it worked!")
else:
    print("it did not work")
print("Finished executing the if-else approach, execution continues.")

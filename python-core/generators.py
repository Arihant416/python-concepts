"""
Basic Generator
"""


def countTill(rangeEnd):
    count = 0
    while count <= rangeEnd:
        yield count
        count += 1


mygenerator = countTill(10)
print(next(mygenerator))
print(next(mygenerator))
print(next(mygenerator))
print(next(mygenerator))
print(next(mygenerator))
print(next(mygenerator))
print(next(mygenerator))
print(next(mygenerator))
print(next(mygenerator))
print(next(mygenerator))
print(next(mygenerator))
print(
    next(mygenerator)
)  # Since generator stops yielding values Exception : StopIteration is raised
# yield pauses function execution and returns a value
# when resumed execution starts right after the yield


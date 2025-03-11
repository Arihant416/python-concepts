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
# print(next(mygenerator))
print(
    next(mygenerator)
)  # Since generator stops yielding values Exception : StopIteration is raised
# yield pauses function execution and returns a value
# when resumed execution starts right after the yield


# Slightly on the advanced note:
# Generators are memory-efficient
# For example this is also similar to list-comprehension except it's ultra-memory efficient
squares = (x*x for x in range(10))

def fibo(n):
    a , b = 0, 1
    for _ in range(n):
        yield a
        a, b = b , a + b

d = fibo(10)
print(next(d))
print(next(d))
print(next(d))
print(next(d))
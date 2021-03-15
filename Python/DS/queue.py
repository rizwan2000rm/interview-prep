from collections import deque

print("============ deque ============")
print()

print("====== append() & appendleft ======")
print()
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.appendleft("Graham")
print(queue)
print()

print("====== pop() & popleft ======")
print()
queue.pop()
queue.popleft()
print(queue)
print()

print("====== extend() & extendleft ======")
print()
queue.extend([4,5,6])
queue.extendleft([4,5,6])
print(queue)
print()

# rotate()
print("====== rotate() ======")
print()

# Right Rotate
queue.rotate(5)
print(queue)
print()

# Left Rotate
queue.rotate(-3)
print(queue)
print()

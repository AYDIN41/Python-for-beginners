def fibonacci():
    a = 0
    b = 1
    yield a
    yield b
    for i in range(0,125):
        a, b = b, a + b
        yield b
generate = fibonacci()
inerate = iter(generate)
for i in inerate:
    print(i)




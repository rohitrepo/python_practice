def next_fibonacci(threshold):
    i = 0
    a = 0
    b = 1
    next_fibonacci = 0

    if threshold < 0:
        return 1

    while i <= threshold:
        next_fibonacci = a + b
        if next_fibonacci > threshold:
            return next_fibonacci
        else:
            a = b
            b = next_fibonacci
            i += 1

print(next_fibonacci(-10))
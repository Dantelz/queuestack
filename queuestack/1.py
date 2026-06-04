stack = []
operaciones = [
    ("push", 5), ("push", 3), ("pop", None),
    ("push", 2), ("push", 8), ("pop", None), ("pop", None),
    ("push", 9), ("push", 1), ("pop", None),
    ("push", 7), ("push", 6), ("pop", None), ("pop", None),
    ("push", 4), ("pop", None), ("pop", None)
]

for op, val in operaciones:
    if op == "push":
        stack.append(val)
        print(f"push({val}) stack: {stack}")
    else:
        resultado = stack.pop()
        print(f"pop() {resultado} stack: {stack}")
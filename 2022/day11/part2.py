from collections import deque

# input = open("2022/day11/test_input.txt").read()
input = open("2022/day11/data.txt").read()

monkey_inputs = input.split("\n\n")
monkeys = {}
modulo = 1
for monkey_input in monkey_inputs:

    for line in monkey_input.splitlines():
        if line.startswith("Monkey "):
            monkey = int(line.removeprefix("Monkey ").strip(":"))
        elif line.startswith("  Starting items: "):
            items_str = line.removeprefix("  Starting items: ").split(",")
            items = deque(map(int, items_str))
        elif line.startswith("  Operation: "):
            operation = line.removeprefix("  Operation: new = old ")
            operation = operation.replace("old", "item")
        elif line.startswith("  Test: "):
            test = int(line.removeprefix("  Test: divisible by "))
            modulo *= test
        elif line.startswith("    If true: "):
            if_true = int(line.removeprefix("    If true: throw to monkey "))
        elif line.startswith("    If false: "):
            if_false = int(line.removeprefix("    If false: throw to monkey "))

    monkeys[monkey] = {
        "items": items,
        "operation": operation,
        "test": test,
        "true": if_true,
        "false": if_false,
        "inspects": 0,
    }

for round in range(10000):
    for monkey in monkeys.values():

        items = monkey["items"].copy()

        for item in items:
            # inspect
            item = eval(f"item {monkey['operation']}")

            item %= modulo

            # test
            if item % monkey["test"] == 0:
                throw_to = monkey["true"]
            else:
                throw_to = monkey["false"]

            monkeys[throw_to]["items"].append(item)
            monkey["items"].popleft()

            monkey["inspects"] += 1

inspects = sorted([monkey["inspects"] for monkey in monkeys.values()])

print(inspects)

print(inspects[-1] * inspects[-2])

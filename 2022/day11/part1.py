# input = open("2022/day11/test_input.txt").read()
input = open("2022/day11/data.txt").read()

monkey_inputs = input.split("\n\n")
monkeys = {}
for monkey_input in monkey_inputs:

    for line in monkey_input.splitlines():
        if line.startswith("Monkey "):
            monkey = int(line.removeprefix("Monkey ").strip(":"))
        elif line.startswith("  Starting items: "):
            items_str = line.removeprefix("  Starting items: ").split(",")
            items = list(map(int, items_str))
        elif line.startswith("  Operation: "):
            operation = line.removeprefix("  Operation: new = old ")
            operation = operation.replace("old", "item")
        elif line.startswith("  Test: "):
            test = int(line.removeprefix("  Test: divisible by "))
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

for round in range(20):
    for monkey in monkeys.values():

        items = monkey["items"].copy()

        for item in items:
            # inspect
            item = eval(f"item {monkey['operation']}")

            # worry level goes down by dividing by 3 after inspect and round down
            item //= 3

            # test
            if item % monkey["test"] == 0:
                throw_to = monkey["true"]
            else:
                throw_to = monkey["false"]

            monkeys[throw_to]["items"].append(item)
            monkey["items"].pop(0)

            monkey["inspects"] += 1

inspects = sorted([monkey["inspects"] for monkey in monkeys.values()])

print(inspects[-1] * inspects[-2])

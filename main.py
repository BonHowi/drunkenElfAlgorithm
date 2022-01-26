x = 0
y = 0
houses = {f"{x}:{y}": 1}
with open('navigation.txt') as f:
    directions = f.read()
    for v in directions:
        if v == '<':
            x -= 1
        elif v == '>':
            x += 1

        elif v == '^':
            y += 1
        elif v == 'v':
            y -= 1
        movement_key = f"{x}:{y}"

        if movement_key in houses:
            houses[movement_key] += 1
        else:
            houses[movement_key] = 1

    print(f"Santa visited {len(houses)} houses")

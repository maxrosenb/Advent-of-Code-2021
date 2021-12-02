def determine_position(directions):
    x_pos = 0
    depth = 0
    aim = 0

    for l in directions:
        line = l.split(" ")
        x = int(line[1])
        direction = line[0]

        if direction == "up":
            aim -= x
        if direction == "down":
            aim += x
        if direction == "forward":
            x_pos += x
            depth += x * aim

    return x_pos * depth


with open("input.txt") as fp:
    lines = []
    line = fp.readline()
    while line:
        lines.append(line.strip())
        line = fp.readline()
    print(determine_position(lines))

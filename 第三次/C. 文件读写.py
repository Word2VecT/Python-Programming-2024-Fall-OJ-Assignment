import sys

file_name = "output.txt"

inputs = [sys.stdin.readline().rstrip("\n") for _ in range(3)]
while len(inputs) < 3:
    inputs.append("")

initial_content, mode, additional_content = inputs

with open(file_name, "w") as file:
    file.write(initial_content)

write_modes = {"w", "a", "x"}
can_write = any(m in mode for m in write_modes) or "+" in mode

if can_write:
    try:
        with open(file_name, mode) as file:
            file.write(additional_content)
    except FileExistsError:
        pass
    except IOError:
        pass

try:
    with open(file_name, "r") as file:
        content = file.read()
except IOError:
    content = ""

print(content)

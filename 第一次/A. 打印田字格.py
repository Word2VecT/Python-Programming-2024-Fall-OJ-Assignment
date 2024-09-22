t = int(input())

for _ in range(t):
    l, c = map(int, input().split())  # noqa: E741

    top_row = "+" + "--+--+" * c
    middle_row = "|" + "  |  |" * c
    bottom_row = "|" + "--+--|" * c
    sub_grid = f"{top_row}\n{middle_row}\n{bottom_row}\n{middle_row}\n" * l

    print(f"{sub_grid}{top_row}")

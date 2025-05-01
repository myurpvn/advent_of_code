order_list = []
page_order_list = []
with open("q5/input.txt", "r") as f:
    for line in f.readlines():
        if "|" in line:
            order_list.append(line.strip())
        elif "," in line:
            page_order_list.append([int(n) for n in line.strip().split(",")])


def check_page_order(order):
    if len(order) == 2:
        return f"{order[0]}|{order[1]}" in order_list
    elif f"{order[0]}|{order[1]}" in order_list:
        return check_page_order(order[1:])
    return False


def correct_order(order):
    i = 0
    while i < len(order) - 1:
        if f"{order[i]}|{order[i+1]}" not in order_list:
            order[i], order[i + 1] = order[i + 1], order[i]
            i = 0
        else:
            i += 1

    return order


mid_page = []
incorrect_order_list = []
for page_order in page_order_list:
    if check_page_order(page_order):
        mid_page.append(page_order[(len(page_order) - 1) // 2])
    else:
        incorrect_order_list.append(page_order)

print("ordered_sum: ", sum(mid_page))

# print(incorrect_order_list)

mid_page_corrected = []
for page_order in incorrect_order_list:
    corrected_order = correct_order(page_order)
    # print(corrected_page_order)
    mid_page_corrected.append(corrected_order[(len(page_order) - 1) // 2])

# print(mid_page_changed)
print("ordered_corrected_sum: ", sum(mid_page_corrected))

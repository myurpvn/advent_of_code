def validate_levels(levels: list[int]) -> bool:
    is_valid = False
    increasing = False

    level_diffs: list[int] = []

    for id in range(len(levels) - 1):
        level = levels[id]
        next_level = levels[id + 1]
        level_diffs.insert(id, next_level - level)

    diff_size = len(level_diffs)

    if level_diffs[0] >= 0:
        increasing = True

    for id in range(diff_size):
        diff = level_diffs[id]
        if (diff == 0) or (abs(diff) > 3) or (increasing != (diff > 0)):
            break
        if id == diff_size - 1:
            is_valid = True

    return is_valid


reports = []

with open("input.txt", "r") as f:
    reports = f.readlines()


safe_report_count = 0
for report in reports:
    levels = [int(_) for _ in report.strip().split()]

    if validate_levels(levels):  # check for whole levels
        safe_report_count += 1
    else:  # check for 1-level-less levels
        for id in range(len(levels)):
            sub_list = levels[0:id] + levels[id + 1 :]
            if validate_levels(sub_list):
                safe_report_count += 1
                break


print(safe_report_count)

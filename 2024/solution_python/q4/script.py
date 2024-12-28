def convert_string_to_array(string: str) -> dict[int, dict[int, str]]:
    array_dict: dict[int, dict[int, str]] = {}

    rows = string.splitlines()

    length = max(len(rows), len(rows[0]))

    for i in range(length):
        if i < len(rows):
            row = rows[i]
        else:
            row = "" * length

        row_dict = {}
        for j in range(length):
            if j < len(row):
                letter = row[j]
            else:
                letter = ""

            row_dict[j] = letter

        array_dict[i] = row_dict

    return array_dict


def find_and_get_pattern_ids(
    search_string: str, pattern_list: list[str] = ["XMAS", "SAMX"]
) -> list[int]:
    id_list: list[int] = []

    for pattern in pattern_list:
        s = search_string
        absolute_id = 0
        while len(s) > 0:
            relative_id = s.find(pattern)

            if relative_id < 0:
                break
            else:
                absolute_id += relative_id
                id_list.append(absolute_id)
                s = s[relative_id + len(pattern) :]
                absolute_id += 1

    return id_list


def count_xmas(raw_string: str) -> int:
    count = 0

    lines = raw_string.splitlines()

    for line in lines:
        count += len(find_and_get_pattern_ids(line))

    return count


def transpose_array(array: dict[int, dict[int, str]]) -> dict[int, dict[int, str]]:
    array_t: dict[int, dict[int, str]] = {}

    rows = len(array.keys())
    cols = len(array[0].keys())

    for i in range(rows):
        row_dict = {}
        for j in range(cols):
            row_dict[j] = array[j][i]
        array_t[i] = row_dict

    return array_t


def primary_diagonal_string(array: dict[int, dict[int, str]]) -> str:
    dg_string: str = ""
    dg_string_list = []

    length = len(array.keys())

    for i in range(length):
        row_string = ""
        row_string_mirr = ""

        for j in range(length):
            if i + j < length:
                row_string += array[j][i + j]
                row_string_mirr += array[i + j][j]

        dg_string_list.append(row_string)

        if i != 0:
            dg_string_list.append(row_string_mirr)

    dg_string = "\n".join(dg_string_list)

    return dg_string


def secondary_diagonal_string(array: dict[int, dict[int, str]]) -> str:

    dg_string = ""

    array_string_list = convert_array_to_string(array).splitlines()

    reversed_string_list = []
    for line in array_string_list:
        reversed_string_list.append("".join(reversed(line)))

    reversed_string = "\n".join(reversed_string_list)
    dg_string = primary_diagonal_string(convert_string_to_array(reversed_string))

    return dg_string


def find_x_mas_pattern(array: dict[int, dict[int, str]]) -> list[int]:

    pattern_list = ["MAS", "SAM"]
    return_id_list: list[int] = []
    string_list = convert_array_to_string(array).splitlines()

    for line_number, line in enumerate(string_list):
        id_list = find_and_get_pattern_ids(line, ["A"])

        # 1 -- 2
        # - A -
        # 3 -- 4
        for id in id_list:
            if (
                id > 0
                and id < len(line) - 1
                and line_number > 0
                and line_number < len(string_list) - 1
            ):

                letter_1 = array[line_number - 1][id - 1]
                letter_2 = array[line_number - 1][id + 1]
                letter_3 = array[line_number + 1][id - 1]
                letter_4 = array[line_number + 1][id + 1]

                dg_1 = letter_1 + array[line_number][id] + letter_4
                dg_2 = letter_2 + array[line_number][id] + letter_3

                if dg_1 in pattern_list and dg_2 in pattern_list:
                    return_id_list.append(id)

    return return_id_list


def convert_array_to_string(array: dict[int, dict[int, str]]) -> str:
    string = ""
    lines = []

    length = len(array.keys())
    for i in range(length):
        lines.append("".join(array[i].values()))

    string = "\n".join(lines)

    return string


raw_word_search = ""
with open("q4/input.txt", "r") as f:
    raw_word_search = f.read()

raw_array = convert_string_to_array(raw_word_search)
trp_array = transpose_array(raw_array)
dg_array_p = convert_string_to_array(primary_diagonal_string(raw_array))
dg_array_s = convert_string_to_array(secondary_diagonal_string(raw_array))


count_normal = count_xmas(convert_array_to_string(raw_array))
count_transposed = count_xmas(convert_array_to_string(trp_array))
count_primary_dg = count_xmas(convert_array_to_string(dg_array_p))
count_secondary_dg = count_xmas(convert_array_to_string(dg_array_s))
total_count = count_normal + count_transposed + count_primary_dg + count_secondary_dg

count_x_mas_pattern = len(find_x_mas_pattern(raw_array))

print(f"count: normal --> {count_normal}")
print(f"count: transposed --> {count_transposed}")
print(f"count: primary diagonal --> {count_primary_dg}")
print(f"count: secondary diagonal --> {count_secondary_dg}")

print(f"\ncount: 'XMAS' string: {total_count}")
print(f"\ncount: 'X-MAS' pattern {count_x_mas_pattern}")

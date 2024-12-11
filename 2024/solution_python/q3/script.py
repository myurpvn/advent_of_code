def check_enabled_memory(corrupted_raw_memory: str) -> str:

    scanned_s: list[str] = []

    do_pattern = "do()"
    dont_pattern = "don't()"

    sliced_s = "do()" + corrupted_raw_memory

    while len(sliced_s) > 0:

        do_id_start = sliced_s.find(do_pattern)
        do_id_end = do_id_start + len(do_pattern)
        dont_id_start = sliced_s.find(dont_pattern)

        if do_id_start >= 0 and dont_id_start >= 0:
            if do_id_start > dont_id_start:
                scanned_s.append("")
                sliced_s = sliced_s[do_id_start - 1 :]
            else:
                scanned_s.append(sliced_s[do_id_end:dont_id_start])
                sliced_s = sliced_s[dont_id_start - 1 :]

        elif do_id_start >= 0 and dont_id_start < 0:
            scanned_s.append(sliced_s[do_id_end:])
            break
        elif do_id_start < 0 and dont_id_start >= 0:
            scanned_s.append("")
            break
        else:
            scanned_s.append(sliced_s)
            break

    return "".join(scanned_s)


def get_matches(s: str) -> list[str]:

    s_pattern = "mul("
    e_pattern = ")"

    extracted_list: list[str] = []
    sliced_s = s

    while len(sliced_s) > 0:
        s_id = sliced_s.find(s_pattern)
        e_id = sliced_s.find(e_pattern)

        if s_id >= 0:
            if e_id > s_id:
                extracted = sliced_s[s_id : e_id + 1]
                extracted_list.append(extracted)

            sliced_s = sliced_s[e_id + 1 :]
        else:
            break

    return extracted_list


def regex_find(s: str) -> list[tuple[str, str]]:
    import re

    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, s)
    print(matches)
    return matches


raw_corrupt_memory = ""
with open("q3/input.txt", "r") as f:
    raw_corrupt_memory = f.read()

print(f"raw corrupted memory size: {len(raw_corrupt_memory)}")
match_products_list: list[int] = []

corrupt_memory = check_enabled_memory(raw_corrupt_memory)
print(f"corrupted memory size: {len(corrupt_memory)}")

matches: list[str] = get_matches(corrupt_memory)
print(f"cleaned matches: {len(matches)}")

for m in matches:
    m_cleaned = m.split("mul(")

    for i in m_cleaned:
        if len(i) > 0:
            splitted = i.replace(")", "").split(",")
            if (
                len(splitted) == 2
                and splitted[0].isnumeric()
                and splitted[1].isnumeric()
            ):
                product = int(splitted[0]) * int(splitted[1])
                match_products_list.append(product)

print(f"Sum of products: {sum(match_products_list)}")

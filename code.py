def longest_common_prefix(strs):
    str_len = len(strs)
    first_str = strs[0]
    second_str = strs[1]
    third_str = strs[-1]
    common_prefix = []
    min_length = len(min(first_str,second_str, third_str))
    for i in range(min_length):
        if first_str[i] == second_str[i] == third_str[i]:
            common_prefix.append(first_str[i])
        else:
            break

    if common_prefix is None:
        prefix = "\"\" "
    else:
        result = f'{"".join(common_prefix)}'
        prefix=(f"\""+result+"\"")

    print(prefix)

longest_common_prefix(strs)

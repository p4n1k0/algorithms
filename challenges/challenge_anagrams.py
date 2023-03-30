def merge_string(first_str, second_str, index_str=0, index_str2=0,
                 merged_str=''):
    while index_str < len(first_str) and index_str2 < len(second_str):
        if first_str[index_str] < second_str[index_str2]:
            merged_str += first_str[index_str]
            index_str += 1
        else:
            merged_str += second_str[index_str2]
            index_str2 += 1
    return merged_str + first_str[index_str:] + second_str[index_str2:]


def sort_string(str):
    if len(str) <= 1:
        return str
    return merge_string(sort_string(str[:len(str) // 2]),
                        sort_string(str[len(str) // 2:]))


def is_anagram(first_str, second_str):
    first_str = sort_string(first_str.lower())
    second_str = sort_string(second_str.lower())
    is_anagram = first_str, second_str,
    first_str != '' and first_str == second_str
    return is_anagram

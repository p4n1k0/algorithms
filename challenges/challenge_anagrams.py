def merge_string(str, str2, i_str=0, i_str2=0, merge_str=''):
    while i_str < len(str) and i_str2 < len(str2):
        if str[i_str] < str2[i_str2]:
            merge_str += str[i_str]
            i_str += 1
        else:
            merge_str += str2[i_str2]
            i_str2 += 1
    return merge_str + str[i_str:] + str2[i_str2:]


def sort_string(str):
    if len(str) <= 1:
        return str
    return merge_string(sort_string(str[:len(str) // 2]),
                        sort_string(str[len(str) // 2:]))


def is_anagram(str, str2):
    str = sort_string(str.lower())
    str2 = sort_string(str2.lower())
    return str, str2, str != '' and str == str2

def is_palindrome_iterative(word):
    if len(word) < 1:
        return False
    count = 0
    while count <= len(word) // 2:
        if (word[count] != word[len(word) - 1 - count]):
            return False
        count += 1
    return True

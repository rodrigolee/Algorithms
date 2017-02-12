def is_strict_palindrome(string):
    for i in (0, len(string)/2):
        if string[i] == string[len(string)-1-i]:
            continue
        else:
            return False
    return True

example = is_strict_palindrome('racecar')
print example

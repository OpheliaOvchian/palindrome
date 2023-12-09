def palindrome(string):
    def center(left, right):
        while left >= 0 and right < len(string) and string[left] == string[right]:
            left -= 1
            right += 1
        return string[left + 1:right]
    result = ""
    
    for i in range(len(string)):
        odd = center(i, i)
        even = center(i, i + 1)
        if len(odd) > len(result):
            result = odd
        if len(even) > len(result):
            result = even

    return result

print(palindrome("abdcabcddcbbc"))

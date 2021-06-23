def is_palindrome(word):
    # reword = word[::-1]
    reword = ""
    # for i in range(1, len(word)+1):
    #    reword += word[-1]
    # 마지막 인덱스부터 인덱스 0까지 1씩 감소
    for i in range(len(word)-1, -1, -1):
        reword += word[i]
    return reword == word

print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))
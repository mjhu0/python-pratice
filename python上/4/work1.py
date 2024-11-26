def is_match(s: str, pattern: str) -> bool:
    # 如果pattern为空，则返回s是否为空（即s和pattern均为空时为True）
    if not pattern:
        return not s

    # 检查s的第一个字符是否与pattern的第一个字符匹配（考虑pattern[0]为'.'的情况）
    first_match = bool(s) and (pattern[0] == s[0] or pattern[0] == '.')

    # 如果pattern的长度大于1并且第二个字符是'*'
    if len(pattern) >= 2 and pattern[1] == '*':
        # 匹配0次或多次
        return (is_match(s, pattern[2:]) or
                (first_match and is_match(s[1:], pattern)))
    else:
        # 如果第二个字符不是'*'，直接匹配当前字符
        return first_match and is_match(s[1:], pattern[1:])
        
# 测试用例
print(is_match("aaa", "a.a"))  # True
print(is_match("aaa", "ab*ac*a"))  # True
print(is_match("aaa", "aa.a"))  # False
print(is_match("aaa", "ab*a"))  # False


######  542313460109 胡华吉 ###########
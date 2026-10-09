# class Solution:
def isValid(s):
    a = 0
    b = 0
    c = 0
    i = 0
    if len(s) % 2 != 0:
        return False
    for k in "." + s:
        if s[i] == " ":
            break
        if s[i] == ".":
            pass
        if s[i] == "(" and s[i + 1] != "}" and s[i + 1] != "]":
            a += 1
        elif s[i] == ")" and s[i - 1] == "(":
            a -= 1
            s = s[:i - 1] + s[i+1:]
            i -= 1
            continue
        elif s[i] == "[" and s[i + 1] != "}" and s[i + 1] != ")":
            b += 1
        elif s[i] == "]" and s[i - 1] == "[":
            b -= 1
            s = s[:i - 1] + s[i+1:]
            i -= 1
            continue
        elif s[i] == "{" and s[i + 1] != ")" and s[i + 1] != "]":
            c += 1
        elif s[i] == "}" and s[i - 1] == "{":
            c -= 1
            s = s[:i - 1] + s[i+1:]
            i -= 1
            continue
        else:
            return False
        i += 1
    if a == 0 and b == 0 and c == 0:
        return True
    else:
        return False


print(isValid(input("Введите последовательность скобок: ") + "  "))

# s = "()"
# print(!r'Solution.isValid')

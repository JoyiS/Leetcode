def prefix_cal(s):
    s = s[::-1]
    stack = []
    if not s:
        return 0
    while s:
        while s and s[0] == ' ' or s[0] in '()':
            s = s[1:]

        if s[0] in '0123456789':
            num = ''
            while s[0] in '0123456789':
                num = s[0] + num
                s = s[1:]
            num = int(num)
            stack.append(num)

        elif s[0] in '+-*/':
            op2 = stack.pop()
            op1 = stack.pop()
            if s[0] == '+':
                stack.append(op1 + op2)
            if s[0] == '-':
                stack.append(op1 - op2)
            if s[0] == '*':
                stack.append(op1 * op2)
            if s[0] == '/':
                stack.append(op1 / op2)
            print(stack)
            s = s[1:]
    return stack[0]


s = '(+ (+ 2 (* 4 1)) 1)'
res = prefix_cal(s)
print(res)
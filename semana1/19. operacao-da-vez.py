a = '(' + input() + ')'
b = '(' + input() + ')'
op = input()

res = a + op + b

if(op == '/'):
    template = '{:.1f}'
    print(template.format(eval(res)))
else:
    print(eval(res))


a = input()
b = input()
c = input()
if len(a)>len(b)>len(c):
    print('\n',c, '\n', a)
elif len(c)>len(b)>len(a):
    print('\n',a, '\n', c)
elif len(c)>len(a)>len(b):
    print('\n',b, '\n', c)
elif len(b)>len(c)>len(a):
    print('\n',a, '\n', b)
elif len(b)>len(a)>len(c):
    print('\n',c, '\n', b)
elif len(a)>len(c)>len(b):
    print('\n',b, '\n', a)
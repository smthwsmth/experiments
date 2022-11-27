num = input('Введи число больше 99, пёс (чтобы было не менее 3х цифр, долбоёб):  ')
while len(num) < 3 or not num.isdigit():
    num = input('Соси, неправильно, пробуй ещё:  ')
if len(num) == 3:
    ans = int(num)%10
elif len(num) > 3:
    ans = (int(num) // 10**(len(num)-3))%10
print(ans)
"Conversor de bases númericas"
n = input("Você deseja converter números S/N: ")
while n=='S'or n =='s':
    num = int(input("Número a ser convertido: "))
    print('''
        1 para Binário 
        2 para Hexadecimal''')
    x = int(input("Sua escolha: "))
    if x ==1:
     print("número digitado foi {} e sua converção para binário é {}".format(num,bin(num)[2:]))
    else:
        print("o número digitado foi {} e sua converção {}".format(num,hex(num)[2:]))
    n = input("Você deseja converter números S/N: ")




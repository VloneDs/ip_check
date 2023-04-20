# В 4-й версии IP-адрес может 
# быть представлен в виде 4 десятичных чисел от 0 до 255, например, 192.168.1.2.
# Напишите программу с использованием встроенной функции all() для
#  проверки корректности IP-адреса: все ли числа в IP-адресе - числа со значением от 0 до 255.

# 10.0.1.1 -> True
# 10.1.1.a -> False 
# 10.1.1.260 -> False

# func all  возвращзает истину если все истина
# func any возвращает ложь если хоть один компанент лож

ip = input('Введите IP: ')
ip_split = ip.split('.') # получваем айпи
if len(ip_split) > 4 or len(ip_split) < 4: # проверяем что айпи состоит из 4 элементов
    print('error')
else:
    num = 0
    range = 0
    for i in ip_split:
        if i.isdigit(): # прикольная функция которая возвращает True если все символы это цифры
            num += 1 
            if num == 4:
                for no_ABC in ip_split:
                    res = all(map(lambda no_ABC: True if int(no_ABC) <= 155 and int(no_ABC) >= 0 
                              else False, ip_split)) # проверяет все цифры на лимит
                if res:
                    pass
                else:
                    range += 1
    if range == 0 and num == 4:
        print(f'{ip} -> True')
    else:
        print(f'{ip} -> False')




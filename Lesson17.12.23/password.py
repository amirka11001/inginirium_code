def ask_password():
    password=input('Введите пароль')
    if password=='password':
        print('Пароли совпадают')
    else:
        print('Пароли не совпадают')

ask_password()
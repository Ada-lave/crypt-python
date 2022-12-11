import pyAesCrypt

path = input('Введите путь до файла с расширением .txt ')
pathF= input('Введите как будет называется конечный файл ')
passw = input('Введите пароль к файлу ')

pyAesCrypt.encryptFile(path,f'{pathF}.aes',passw)


import pyAesCrypt

path = input('Введите путь до файла с расширением .aes ')
pathF= input('Введите как будет называется конечный файл ')
passw = input('Введите пароль к файлу ')

pyAesCrypt.decryptFile(path,pathF,passw)
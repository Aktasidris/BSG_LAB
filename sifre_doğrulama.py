import tkinter as tk
from tkinter import messagebox
import smtplib
import string
import random
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Şifre üretme fonksiyonu
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


# E-posta gönderme fonksiyonu
def send_email(receiver_email, password):
    sender_email = "gonderici@example.com"
    password = "gonderici_sifresi"
    smtp_server = "smtp.example.com"
    smtp_port = 587

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, password)

    subject = "Oluşturulan Şifre"
    message = "İşte oluşturulan şifreniz: " + password

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(message, "plain"))

    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()


# Şifre gönderme işlemini başlatan fonksiyon
def send_password():
    receiver_email = email_entry.get()
    password = generate_password(12)
    send_email(receiver_email, password)
    messagebox.showinfo("Bilgi", "Şifre e-postayla gönderildi.")

    countdown_label = tk.Label(root, text="", font=("Helvetica", 16))
    countdown_label.pack()

    while True:
        start_time = time.time()
        while True:
            user_input = messagebox.askstring("Doğrulama", "Lütfen şifreyi girin:")
            if user_input == password:
                end_time = time.time()
                elapsed_time = end_time - start_time
                if elapsed_time <= 60:  # 1 dakika (60 saniye) süresi kontrolü
                    messagebox.showinfo("Başarılı Giriş", "Şifre doğru, başarılı giriş!")
                else:
                    messagebox.showerror("Süre Doldu", "Şifre süresi doldu, tekrar deneyin.")
                break
            else:
                messagebox.showerror("Hatalı Şifre", "Hatalı şifre, tekrar deneyin.")

        countdown_label.config(text="Kalan Süre: 60 saniye")
        root.update()
        time.sleep(1)
        for i in range(59, 0, -1):
            countdown_label.config(text=f"Kalan Süre: {i} saniye")
            root.update()
            time.sleep(1)

        yeni_sifre_istegi = messagebox.askquestion("Yeni Şifre Oluştur", "Yeni bir şifre oluşturmak ister misiniz?")
        if yeni_sifre_istegi == "no":
            countdown_label.pack_forget()
            break
        password = generate_password(12)
        send_email(receiver_email, password)
        messagebox.showinfo("Bilgi", "Yeni şifre e-postayla gönderildi.")


# Kullanıcı arayüzü
root = tk.Tk()
root.title("Şifre Gönderme Uygulaması")

email_label = tk.Label(root, text="E-posta Adresi:")
email_label.pack()

email_entry = tk.Entry(root)
email_entry.pack()

send_button = tk.Button(root, text="Şifre Gönder ve Doğrula", command=send_password)
send_button.pack()

root.mainloop()

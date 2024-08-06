import subprocess

def get_wifi_profiles():
    meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])
    data = meta_data.decode('utf-8', errors="backslashreplace")
    return [X.split(":")[1][1:-1] for X in data.split('\n') if "All User Profile" in X]

def retrieve_wifi_password(profile):
    try:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear'])
        results = results.decode('utf-8', errors="backslashreplace")
        passwords = [b.split(":")[1][1:-1] for b in results.split('\n') if "Key Content" in b]
        return passwords[0] if passwords else "No password found"
    except subprocess.CalledProcessError:
        return "Error occurred while retrieving password"

def store_wifi_passwords(profiles):
    with open("wifi_passwords.txt", "w") as file:
        for profile in profiles:
            password = retrieve_wifi_password(profile)
            file.write(f"Wi-Fi Name: {profile}\nPassword: {password}\n\n")

def WiFiPasswords():
    profiles = get_wifi_profiles()
    if not profiles:
        print("No Wi-Fi profiles found.")
        return
    
    store_wifi_passwords(profiles)
    print("Wi-Fi names and passwords stored in 'wifi_passwords.txt'")

if __name__ == "__main__":
    confirmation = input("This action will extract Wi-Fi passwords and store them in a text file. Are you sure you want to proceed? (yes/no): ")
    if confirmation.lower() == "yes":
        WiFiPasswords()
    else:
        print("Exiting")

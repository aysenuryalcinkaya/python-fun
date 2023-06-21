import subprocess
import re

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('latin-1').split('\n')

profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

for profile in profiles:
    try:
        # Uygun şekilde çıktıyı almak için profile adını "utf-8" ile yeniden kodlayın
        profile_encoded = profile.encode('utf-8').decode('latin-1')
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles', profile_encoded, 'key=clear']).decode('latin-1').split('\n')
        password_list = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            print(f"Profil: {profile}, Şifre: {password_list[0]}")
        except IndexError:
            print(f"Profil: {profile}, Şifre bulunamadı.")
    except subprocess.CalledProcessError as e:
        print(f"Hata: Profil '{profile}' alınamadı. Hata kodu: {e.returncode}")

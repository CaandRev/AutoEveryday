#Automatisering av utfylling til aktiv til jobben

#Module til at styrer musen
import mouse
# Modul til at lave pause (sleep)
import time
# Modul til at åpne url
import webbrowser
# Modul til at lukke browser
import os
# Modul til at finde opløsning
import ctypes

# Henter bredden fra skærmopløsningen
user32=ctypes.WinDLL('user32')
screensize = user32.GetSystemMetrics(0)

# Åpner Aktivtil jobben siden
webbrowser.open('https://aktivtiljobben.norconsult.com/my-activities', new=1, autoraise=True)
time.sleep(10)
#Maksimere vinduet for og sikre knappen er på rigtig plads
SW_MAXIMISE=3
hwnd=user32.GetForegroundWindow()
user32.ShowWindow(hwnd, SW_MAXIMISE)

time.sleep(12)
def click(x,y):
        #move mouse
        mouse.move(x,y, absolute=True, duration=0.1)

        #left click
        mouse.click('left')

        #buffer
        time.sleep(2)

if screensize == 5120:
        # click(2560, 670)
        # time.sleep(2)
        click(70, 220)
        click(2560,490)
else:
        click(650,580)

os.system('taskkill /im msedge.exe /f')

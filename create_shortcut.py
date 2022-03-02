#  Skrevet av: CaAnd
# Kan brukes fritt som det er uten noe ansvar

import os
# from pathlib import Path
from win32com.client import Dispatch
import runtime
import tkinter as tk

window = tk.Tk()
label = tk.Label(text = 'Velkommen til snarvei skaperen')
label.pack()

oppdragsnr_label = tk.Label(text = 'Skriv inn oppdragsnummer')
oppdragsnr_label.pack()
oppdragsnr_entry = tk.Entry(width = 60)
oppdragsnr_entry.pack()
oppdragsnr_button = tk.Button(text = 'Bekreft')
oppdragsnr_button.pack()

beskrivelse_label = tk.Label(text = 'Beskrivende tekst av oppdraget')
beskrivelse_label.pack()
beskrivelse_entry = tk.Entry(width = 60)
beskrivelse_entry.pack()
beskrivelse_button = tk.Button(text = 'Bekreft')
beskrivelse_button.pack() 

window.mainloop()
# Variable
print(beskrivelse_entry.get())

# Variable
info = 0

while info == 0:
    
    oppdragsnr = input('Inntast oppdragsnr: ')
    beskrivelse = input('Beskrivelse av oppdraget: ')

    start = runtime.starttime()

    path = 'X:\\nor\\oppdrag'
    regioner = os.scandir(path)
        
    user = os.getlogin()
    path ='C:\\Users\\' + user + '\\OneDrive - Norconsult Group\\Documents\\0_Oppdrag\\'+ oppdragsnr + ' - ' + beskrivelse +  '.lnk'

    print('Jobber med saken')
    # Sjekker om destinasjons mappen eksistere
    endposition = path.rfind('\\')
    shortpath = path[:endposition+1]

    if not os.path.exists(shortpath):
        os.mkdir(shortpath)
        finishpath = shortpath + 'Avsluttet oppdrag\\'
        os.mkdir(finishpath)

    # Finn riktig region
    for region in regioner:
        target = 'X:\\nor\\oppdrag\\' + region.name + '\\'+ oppdragsnr[:3] + '\\' + oppdragsnr[3:5] + '\\' + oppdragsnr
        # targetpath = Path(target)

    #Lager snarvei    
        if os.path.exists(target):
            shell = Dispatch('WScript.Shell')
            shortcut =  shell.CreateShortCut(path)
            shortcut.Targetpath = target
            shortcut.save()
            info += 1

    if info == 0:
        print('Oppdragsmappen eksistere ikke')

runtime.stoptime(start)
input('Push ENTER to finish')

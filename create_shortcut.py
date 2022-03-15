# Skrevet av: CaAnd
# Kan brukes fritt som det er uten noe ansvar

import os
from win32com.client import Dispatch
import runtime

# Variable
info = 0

# Definer funksjon
def create_short(target):
    global info
    if os.path.isdir(target):
        shell = Dispatch('WScript.Shell')
        shortcut =  shell.CreateShortCut(path)
        shortcut.Targetpath = target
        shortcut.save()
        info += 1

while info == 0:
    
    oppdragsnr = input('Inntast oppdragsnr: ')
    beskrivelse = input('Beskrivelse av oppdraget: ')
    region_input = input('Er dit oppdrag i Sogndal tast S + ENTER, er dit oppdrag i Førde tast F + ENTER, ellers kun tast ENTER: ')
    start = runtime.starttime()

    path = 'X:\\nor\\oppdrag'
    regioner = os.scandir(path)
        
    user = os.getlogin()
    path ='C:\\Users\\' + user + '\\OneDrive - Norconsult Group\\Documents\\0_Oppdrag\\'+ oppdragsnr + ' - ' + beskrivelse +  '.lnk'

    print('Jobber med saken')
    # Sjekker om destinasjons mappen eksistere
    endposition = path.rfind('\\')
    shortpath = path[:endposition+1]

    if not os.path.isdir(shortpath):
        os.mkdir(shortpath)
        finishpath = shortpath + 'Avsluttet oppdrag\\'
        os.mkdir(finishpath)

    # Hvis Sogndal
    if region_input.lower() == 's':
        target = 'X:\\nor\\oppdrag\\Sogndal\\'+ oppdragsnr[:3] + '\\' + oppdragsnr[3:5] + '\\' + oppdragsnr
        create_short(target)
    # Hvis Førde
    elif region_input.lower() == 'f':
        target = 'X:\\nor\\oppdrag\\Førde\\'+ oppdragsnr[:3] + '\\' + oppdragsnr[3:5] + '\\' + oppdragsnr
        create_short(target)
    # Ellers finn riktig region
    else:
        for region in regioner:
            target = 'X:\\nor\\oppdrag\\' + region.name + '\\'+ oppdragsnr[:3] + '\\' + oppdragsnr[3:5] + '\\' + oppdragsnr
            create_short(target)  
      
    if info == 0:
        print('Oppdragsmappen eksistere ikke')

runtime.stoptime(start)
input('Push ENTER to finish')

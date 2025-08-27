import pyautogui
import time
import random
import string
import pygetwindow as gw
import subprocess

def random_text(length=8):
    """Genera testo casuale"""
    chars = string.ascii_letters
    return ''.join(random.choice(chars) for _ in range(length))

def ensure_notepad():
    """Apre Notepad se non è già aperto e lo porta in primo piano"""
    windows = gw.getWindowsWithTitle("Notepad")
    if not windows:
        subprocess.Popen(["notepad.exe"])
        time.sleep(2)  # attesa apertura
        windows = gw.getWindowsWithTitle("Notepad")
    if windows:
        windows[0].activate()
        time.sleep(1)
        return windows[0]
    return None

# assicura che Notepad sia aperto e attivo
ensure_notepad()

while True:
    # attesa casuale tra 40 e 60 secondi
    delay = random.randint(40, 60)
    time.sleep(delay)

    # controllo finestra attiva
    active_win = gw.getActiveWindow()
    if active_win and "Notepad" in active_win.title:
        # spostamento mouse
        x_offset = random.randint(-50, 50)
        y_offset = random.randint(-50, 50)

        current_x, current_y = pyautogui.position()
        new_x, new_y = current_x + x_offset, current_y + y_offset

        pyautogui.moveTo(new_x, new_y, duration=0.25)
        pyautogui.click()

        # scrittura testo random
        text = random_text(random.randint(5, 12))
        pyautogui.typewrite(text + "\n")

        print(f"[OK] Su Notepad: scritto '{text}' a ({new_x}, {new_y})")
    else:
        print(f"[SKIP] Non è Notepad: {active_win.title if active_win else 'Nessuna finestra attiva'}")

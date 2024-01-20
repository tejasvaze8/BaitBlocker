import time
from pygetwindow import getActiveWindow
import pyautogui

def get_chrome_url():
    try:
        # Find the Chrome window
        chrome_window = [w for w in getActiveWindow() if 'Google Chrome' in w.title()][0]
        chrome_window.activate()

        # Simulate keyboard shortcut to copy the URL (Ctrl + L, Ctrl + C)
        pyautogui.hotkey('ctrl', 'l')
        pyautogui.hotkey('ctrl', 'c')

        # Get the copied URL from the clipboard
        url = pyautogui.paste()
        return url
    except IndexError:
        return "Chrome not found"
    except Exception as e:
        return str(e)

def main():
    r = 0
    print("start")
    while r < 5:
        active_window = getActiveWindow()
        if 'Google Chrome' in active_window.title():
            print("found")
            url = get_chrome_url()
            print(f"Current URL: {url}")
        time.sleep(3)  # Check every 3 seconds
        r += 1

if __name__ == "__main__":
    main()

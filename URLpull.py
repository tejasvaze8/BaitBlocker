import time
from pygetwindow import getActiveWindow
import pywinauto

def get_chrome_url():
    try:
        # Find the Chrome window
        chrome_window = [w for w in pywinauto.Desktop(backend="uia").windows() if 'Google Chrome' in w.window_text()][0]
        chrome_window.set_focus()

        # Navigate to the address bar
        address_bar = chrome_window.child_window(title="Address and search bar", control_type="Edit").wrapper_object()
        return address_bar.get_value()
    except IndexError:
        return "Chrome not found"
    except Exception as e:
        return str(e)

def main():
    while True:
        active_window = getActiveWindow()
        if 'Google Chrome' in active_window.title:
            url = get_chrome_url()
            print(f"Current URL: {url}")
        print("SERACHING")
        time.sleep(5)  # Check every 5 seconds

if __name__ == "__main__":
    main()

#TESTETSTESTETSTSTET
print("test")
import pygetwindow as gw

def get_active_tab_url():
    active_window = gw.getActiveWindow()
    if active_window:
        return active_window.title
    else:
        return None

# Example usage
current_tab_url = get_active_tab_url()
print("hi")
print("Current tab URL:", current_tab_url)

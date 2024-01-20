import subprocess
import time

def get_chrome_url():
    try:
        # Run an AppleScript to get the URL of the active tab in Google Chrome
        script = '''
            tell application "Google Chrome"
                get URL of active tab of front window
            end tell
        '''
        result = subprocess.run(['osascript', '-e', script], capture_output=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        return str(e)

def main():
    r = 0
    print("start")
    while r < 15:
        url = get_chrome_url()
        if url:
            print(f"Current URL: {url}")
        else:
            print("Chrome not found or active tab URL not available")
        time.sleep(.5)  # Check every 3 seconds
        r += 1

if __name__ == "__main__":
    main()

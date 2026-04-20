import pyautogui as pgui
import time

from get_url_from_clipboard import get_url_from_clipboard

pgui.PAUSE = 0.1
pgui.FAILSAFE = False

def delay(duration = 0.3):
    time.sleep(duration)


def show_detailed_instructions():
    print("\nDetailed Instructions")
    print("=" * 22)
    print("1) Before running downloads:")
    print("   - Open Brave browser first")
    print("   - Keep Brave visible and in front")
    print("   - Avoid typing or moving the mouse during automation")
    print("")
    print("2) Option guide:")
    print("   - Option 1: Opens a new tab and downloads one random wallpaper")
    print("   - Option 2: Downloads wallpaper from the currently open New Tab")
    print("   - Option 3: Downloads N random wallpapers based on your input")
    print("   - Option 4: Shows this help screen")
    print("   - Option 5: Exits the program")
    print("")
    print("3) Cautions:")
    print("   - Do not switch windows while automation is running")
    print("   - Do not close Brave until the current action finishes")
    print("   - If automation targets the wrong place, stop and retry slowly")
    print("")
    print("4) Recommended usage:")
    print("   - Test with option 1 first")
    print("   - Use option 3 only after option 1 works on your system")
    print("   - Keep your system display scaling stable for consistent behavior")


def download_wallpaper():
    # Open DevTools and copy the current element text to the clipboard.
    # `get_url_from_clipboard()` turns that copied text into a Brave wallpaper URL.
    pgui.hotkey("ctrl", "shift", "i")
    delay(1)
    pgui.hotkey("ctrl", "c")
    wallpaper_url = get_url_from_clipboard()
    if not wallpaper_url:
        print("Could not extract wallpaper URL from clipboard.")
        return False

    pgui.hotkey("ctrl", "t")
    pgui.write(wallpaper_url)
    pgui.press("enter")
    delay()
    pgui.hotkey("ctrl", "s")
    delay()
    pgui.press("enter")
    return True


def download_random():
    try:
        # Grab any open Brave window (titles usually end with "- Brave").
        brave_windows_list = pgui.getWindowsWithTitle("- Brave")

        brave_window = brave_windows_list[0]
        brave_window.activate()

        pgui.hotkey("ctrl", "t")

        return download_wallpaper()
    except IndexError:
        print("No brave tabs opened")
        return False


def download_open_tab():
    try:
        delay()
        # This targets the tab created by `download_random()` before downloading.
        pgui.getWindowsWithTitle("New Tab - Brave")[0].activate()

        return download_wallpaper()

    except IndexError:
        print("No New Tabs Opened")
        return False


def download_multiple_random(limit = 2):
    if limit < 1:
        print("Please enter a number greater than 0")
        return False

    count = 0
    successful_downloads = 0

    while count < limit:
        if download_random():
            successful_downloads += 1
        count += 1

    if successful_downloads == 0:
        print("No wallpapers were downloaded")
        return False

    delay()
    with pgui.hold("ctrl"):
        # multiplying by 2 because program opens an extra tab for each download
        # in closing the tabs, program performs the close action two more than when opening
        for _ in range(successful_downloads * 2):
            pgui.press("w")

    return True


def print_menu():
    print("\nBrave Background Extractor")
    print("1. Download 1 random wallpaper")
    print("2. Download currently open Brave New Tab wallpaper")
    print("3. Download multiple random wallpapers")
    print("4. View detailed instructions")
    print("5. Exit")


def get_positive_number(prompt):
    while True:
        user_input = input(prompt).strip()
        try:
            value = int(user_input)
            if value < 1:
                print("Enter a number greater than 0")
                continue
            return value
        except ValueError:
            print("Enter a valid whole number")


def run_cli():
    while True:
        print_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            download_random()
        elif choice == "2":
            download_open_tab()
        elif choice == "3":
            limit = get_positive_number("How many wallpapers to download? ")
            download_multiple_random(limit)
        elif choice == "4":
            show_detailed_instructions()
        elif choice == "5":
            print("Exiting...")
            delay(1)
            break
        else:
            print("Invalid option. Choose 1, 2, 3, 4, or 5")


if __name__ == "__main__":
    run_cli()
import pyautogui as pgui
import time

from get_url_from_clipboard import get_url_from_clipboard

def delay(duration = 0.3):
    time.sleep(duration)


def download_wallpaper():
    # Open DevTools and copy the current element text to the clipboard.
    # `get_url_from_clipboard()` turns that copied text into a Brave wallpaper URL.
    pgui.hotkey("ctrl", "shift", "i")
    delay(1)
    pgui.hotkey("ctrl", "c")
    pgui.hotkey("ctrl", "t")
    pgui.write(get_url_from_clipboard())
    pgui.press("enter")
    delay()
    pgui.hotkey("ctrl", "s")
    delay()
    pgui.press("enter")


def download_random():
    try:
        # Grab any open Brave window (titles usually end with "- Brave").
        brave_windows_list = pgui.getWindowsWithTitle("- Brave")

        brave_window = brave_windows_list[0]
        brave_window.activate()

        pgui.hotkey("ctrl", "t")

        download_wallpaper()
    except IndexError:
        print("No brave tabs opened")


def download_open_tab():
    try:
        delay()
        # This targets the tab created by `download_random()` before downloading.
        pgui.getWindowsWithTitle("New Tab - Brave")[0].activate()

        download_wallpaper()

    except IndexError:
        print("No New Tabs Opened")
        return False


def download_multiple_random(limit = 2):
    count = 0

    while count < limit:
        download_random()
        count += 1

    delay()
    with pgui.hold("ctrl"):
        # multiplying by 2 because program opens an extra tab for each download
        # in closing the tabs, program performs the close action two more than when opening
        for _ in range(limit * 2):
            pgui.press("w")
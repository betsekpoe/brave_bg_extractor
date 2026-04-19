import pyperclip

def get_url_from_clipboard():
    first_line = pyperclip.paste().partition("\n")[0]

    to_remove = '<body style="--ntp-background: url(chrome\:\/\/background-wallpaper\/'

    if to_remove in first_line:
        stripped = first_line.removeprefix(to_remove)
        bg_image_name = stripped[: stripped.index('\\')] + ".jpg"

        return f"brave://background-wallpaper/{bg_image_name}"

    return None

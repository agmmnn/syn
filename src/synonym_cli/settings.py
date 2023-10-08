import os
import json


default_settings = {
    "altervista_apikey": "",
    "default_lang": "en",
}

user_folder = os.path.expanduser("~")
# macOS:    /Users/user
# Linux:    /home/user
# Windows:  C:\Users\user
config_folder = os.path.join(user_folder, ".config", "synonym-cli")
# ~/.config/synonym-cli
config_file = os.path.join(config_folder, "settings.json")
# ~/.config/synonym-cli/settings.json


def settings_get(key: str = None):
    if not settings_file_exist():
        settings_file_create()
    try:
        with open(config_file, "r") as f:
            settings = json.load(f)
    except Exception as e:
        print(e)
    if key:
        return settings[key]
    return settings


def settings_set(key, value) -> None:
    settings = settings_get()
    settings[key] = value
    with open(config_file, "w") as f:
        json.dump(settings, f)
        f.close()


def settings_file_create() -> None:
    if not settings_file_exist():
        if not os.path.exists(config_folder):
            os.makedirs(config_folder)

        with open(config_file, "w") as f:
            json.dump(default_settings, f)


def settings_file_exist() -> bool:
    if not os.path.isfile(config_file):
        return False
    return True


def settings_file_remove() -> None:
    os.remove(config_file)


def settings_show() -> None:
    from rich import print

    print(settings_get())

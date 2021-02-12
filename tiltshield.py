from winreg import ConnectRegistry, HKEY_CURRENT_USER, OpenKey, EnumValue
from shutil import copyfile


# adapted from https://www.reddit.com/r/learnpython/comments/2uwrne/python_and_reading_registry_keys/codc3k5/
def get_steam_path():
    registry = ConnectRegistry(None, HKEY_CURRENT_USER)
    raw_key = OpenKey(registry, "Software\Valve\Steam")

    path = None
    try:
        i = 0
        while 1:
            name, value, type_ = EnumValue(raw_key, i)  # don't use type_, but it's necessary to unpack vars
            if name == "SteamPath":
                path = value
            # print(name, value, i, type_)
            i += 1
    except WindowsError:
        # loop just goes until WindowsError is thrown at the end of the key
        # probably not a great way to do it, but it's in the example
        pass

    if path is None:
        print("Couldn't find Steam install path - is it installed on this user's account?")

    print(path)
    return path


def get_csgo_path(steam_path):
    """In the event that user has multiple Steam libraries installed, CSGO might
    not be installed in the same place that Steam itself is. This function is supposed
    to guarantee we know where it is."""
    # TODO: automate checking of CSGO location using Steam/steamapps/libraryfolders.vdf
    return f'{steam_path}/steamapps/common/Counter-Strike Global Offensive'


def place_cfg(csgo_path):
    copyfile('conf.cfg', f"{csgo_path}/csgo/cfg/gamestate_integration_tiltshield.cfg")



if __name__ == '__main__':
    steam_path = get_steam_path()
    csgo_path = get_csgo_path(steam_path)
    place_cfg(csgo_path)

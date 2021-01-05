# Settings file
settings = "settings.txt"


def get_settings(name=settings):
    file = open(name, "r")
    dest = file.read()
    if dest == '':
        return 'Need path'
    else:
        return dest


def set_settings(src, sets=settings):
    file = open(sets, "w+")
    file.seek(0)
    file.truncate()
    file.write(src)
import os
from pathlib import Path

LIB_NAME = "yonader_lib"

STR_TO_COPY = """
# >.. NUKE YANDRE MENU :
import nuke
nuke.pluginAddPath(r"{PLUGIN_PATH}")
# ..<
"""


def plugin_path():
    parent_module_path = Path(__file__).parent.parent
    module_path = parent_module_path / LIB_NAME

    return module_path.as_posix().replace('\\', '/')


def copy_init():

    print("\n -- COPY INIT REF TO USER INIT -- ")
    user_path = os.path.expanduser('~')
    user_nukeInit_path = os.path.join(user_path, ".nuke", "init.py")

    if not os.path.exists(os.path.dirname(user_nukeInit_path)):
        print("No init .nuke in {}".format(os.path.dirname(os.path.dirname(user_nukeInit_path))))
        return

    if not os.path.exists(user_nukeInit_path):
        param = "w"
        print(f"\t-{user_nukeInit_path} not exist, create this")
    else:
        param = "a"
        print(f"\t-{user_nukeInit_path} exist, append into")

    print(f"\t-Open {user_nukeInit_path} and write content")
    with open(user_nukeInit_path, param) as f:
        f.write("\n\n")
        f.write(STR_TO_COPY.format(PLUGIN_PATH=plugin_path()))
        print(f"\t\t>Content writed")
    print(" -- TASK COMPLETED -- ")
    pass


copy_init()
# plugin_path()

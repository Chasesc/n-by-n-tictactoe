#! python2.7

# Run this file to turn the project into an executable file.

from distutils.core import setup
import py2exe, os


'''
py2exe does not check for the DLL needed for pygame's font library automatically.
The function below overrides py2exe's default isSystemDLL function to include the
check for the required font DLLs.

Thanks to Thadeus Burgess for this fix here: http://thadeusb.com/weblog/2009/4/15/pygame_font_and_py2exe
'''

origIsSystemDLL = py2exe.build_exe.isSystemDLL # save the orginal before we edit it

def isSystemDLL(pathname):
    # checks if the freetype and ogg dll files are being included
    if os.path.basename(pathname).lower() in ("libfreetype-6.dll", "libogg-0.dll", "sdl_ttf.dll"):
            return 0
    return origIsSystemDLL(pathname) # return the orginal function

py2exe.build_exe.isSystemDLL = isSystemDLL # override the default function with this one

setup(console = ['tictactoe.py'])
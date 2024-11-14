import logging
import time
from subprocess import call
import winshell

from Interfece.Core.src.event import Event, EventTypes

logger = logging.getLogger(__name__)


def off_system():
    time.sleep(5)
    call(["shutdown", "/l"])


def off_provodnic():
    call(["taskkill", "/f", "/im", "explorer.exe"])
    print("Проводник закрыт.")


def off_work():
    call('shutdown -s -f -t 5')


def garbage_cleaning():
    winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)


def restart_pk():
    call(["shutdown", "/r"])


def sleep_pk():
    call(["shutdown", "/h"])


def open_provodnic():
    call(["explorer"])

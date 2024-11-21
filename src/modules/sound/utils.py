import logging

from Interfece.Core.src.modules.sound.sound_keyboard import Keyboard
from Interfece.Core.src.event import Event, EventTypes

logger = logging.getLogger(__name__)


class Sound:
    """
    Class Sound
    :author: Paradoxis <luke@paradoxis.nl>
    :description:

    Allows you to control the Windows volume
    The first time a sound method is called, the system volume is fully reset.
    This triggers sound and mute tracking.
    """

    # Current volume, we will set this to 100 once initialized
    __current_volume = None

    @staticmethod
    async def current_volume():
        """
        Current volume getter
        :return: int
        """
        if Sound.__current_volume is None:
            return 0
        else:
            return Sound.__current_volume

    @staticmethod
    async def __set_current_volume(volume):
        """
        Current volumne setter
        prevents numbers higher than 100 and numbers lower than 0
        :return: void
        """
        if volume > 100:
            Sound.__current_volume = 100
        elif volume < 0:
            Sound.__current_volume = 0
        else:
            Sound.__current_volume = volume

    # The sound is not muted by default, better tracking should be made
    __is_muted = False

    @staticmethod
    async def is_muted():
        """
        Is muted getter
        :return: boolean
        """
        return Sound.__is_muted

    @staticmethod
    async def __track():
        """
        Start tracking the sound and mute settings
        :return: void
        """
        if Sound.__current_volume == None:
            Sound.__current_volume = 0
            for i in range(0, 50):
                await Sound.volume_up()

    @staticmethod
    async def mute(*args: tuple):
        """
        Mute or un-mute the system sounds
        Done by triggering a fake VK_VOLUME_MUTE key event
        :return: void
        """
        await Sound.__track()
        Sound.__is_muted = (not Sound.__is_muted)
        Keyboard.key(Keyboard.VK_VOLUME_MUTE)

    @staticmethod
    async def volume_up(*args: tuple):
        """
        Increase system volume
        Done by triggering a fake VK_VOLUME_UP key event
        :return: void
        """
        await Sound.__track()
        await Sound.__set_current_volume(await Sound.current_volume() + 2)
        Keyboard.key(Keyboard.VK_VOLUME_UP)

    @staticmethod
    async def volume_down(*args: tuple):
        """
        Decrease system volume
        Done by triggering a fake VK_VOLUME_DOWN key event
        :return: void
        """
        await Sound.__track()
        await Sound.__set_current_volume(await Sound.current_volume() - 2)
        Keyboard.key(Keyboard.VK_VOLUME_DOWN)

    @staticmethod
    async def volume_set(amount):
        """
        Set the volume to a specific volume, limited to even numbers.
        This is due to the fact that a VK_VOLUME_UP/VK_VOLUME_DOWN event increases
        or decreases the volume by two every single time.
        :return: void
        """
        await Sound.__track()

        if Sound.current_volume() > amount:
            for i in range(0, int((await Sound.current_volume() - amount) / 2)):
                await Sound.volume_down()
        else:
            for i in range(0, int((amount - Sound.current_volume()) / 2)):
                await Sound.volume_up()

    @staticmethod
    async def volume_min(*args: tuple):
        """
        Set the volume to min (0)
        :return: void
        """
        await Sound.volume_set(0)

    @staticmethod
    async def volume_max(*args: tuple):
        """
        Set the volume to max (100)
        :return: void
        """
        await Sound.volume_set(100)

    @staticmethod
    async def volume_pol_zv(*args: tuple):

        await Sound.volume_set(50)
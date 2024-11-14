from .utils import (open_url, keyboard_shortcut,
                    video_on_youtube, search_for_term_on_google,
                    definition_on_wikipedia, person_search, screenshot)


#
intents = [
    {
        "name": "youtube_search",
        "function": video_on_youtube,
    },
    {
        "name": "google_search",
        "function": search_for_term_on_google,
    },
    {
        "name": "wikipedia_search",
        "function": definition_on_wikipedia,
    },
    {
        "name": "person_search",
        "function": person_search,
    },

    {
        "name": "open_youtube",
        "function": open_url("https://www.youtube.com/"),
    },
    {
        "name": "google",
        "function": open_url("https://google.ru/")
    },
    {
        "name": "open_cankuletor",
        "function": open_url("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\Old Calculator.lnk")
    },
    {
        "name": "telegram",
        "function": open_url("https://web.telegram.org/k/")
    },
    {
        "name": "whatsapp",
        "function": open_url("https://web.whatsapp.com/"),
    },
    {
        "name": "yandex",
        "function": open_url("https://yandex.ru/")
    },
    {
        "name": "phonk",
        "function": open_url("https://www.youtube.com/watch?v=ndizAUAR_Cs&t=91s")
    },
    {
        "name": "browser",
        "function": open_url("C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Yandex.lnk")
    },
    {
        "name": "music",
        "function": open_url("https://music.yandex.ru/"),
    },
    {
        "name": "music_stol",
        "function": open_url("https://www.youtube.com/watch?v=kxbGIMVKacg")
    },
    {
        "name": "vk",
        "function": open_url("https://vk.com/feed")
    },
    {
        "name": "open_sittings_windows",
        "function": keyboard_shortcut("win+i"),
    },
    {
        "name": "open_despecher_zadach",
        "function": keyboard_shortcut("ctrl+shift+esc")
    },
    {
        "name": "open_menu_pusk",
        "function": keyboard_shortcut("ctrl+esc")
    },
    {
        "name": "create_papka",
        "function": keyboard_shortcut("ctrl+shift+n")
    },
    {
        "name": "open_vkladca",
        "function": keyboard_shortcut("ctrl+t")
    },
    {
        "name": "create_docx",
        "function": keyboard_shortcut("ctrl+n")
    },
    {
        "name": "cansel_docx",
        "function": keyboard_shortcut("ctrl+w")
    },
    {
        "name": "save_docx",
        "function": keyboard_shortcut("ctrl+s")
    },
    {
        "name": "cop_all_docx",
        "function": keyboard_shortcut("ctrl+a")
    },
    {
        "name": "fat_docx",
        "function": keyboard_shortcut("ctrl+b")
    },
    {
        "name": "italics_docx",
        "function": keyboard_shortcut("ctrl+i")
    },
    {
        "name": "underline_docx",
        "function": keyboard_shortcut("ctrl+u")
    },
    {
        "name": "centered_docx",
        "function": keyboard_shortcut("ctrl+e")
    },
    {
        "name": "left_docx",
        "function": keyboard_shortcut("ctrl+l")
    },
    {
        "name": "right_docx",
        "function": keyboard_shortcut("ctrl+r")
    },
    {
        "name": "zak_okno",
        "function": keyboard_shortcut("alt+f4")
    },
    {
        "name": "change_language",
        "function": keyboard_shortcut("shift+alt")
    },
    {
        "name": "youtube_pause",
        "function": keyboard_shortcut("k")
    },
    {
        "name": "youtube_kon",
        "function": keyboard_shortcut("9")
    },
    {
        "name": "youtube_nach",
        "function": keyboard_shortcut("0")
    },
    {
        "name": "youtube_sled_video",
        "function": keyboard_shortcut("shift+n")
    },
    {
        "name": "youtube_pred_video",
        "function": keyboard_shortcut("shift+p")
    },
    {
        "name": "youtube_sered",
        "function": keyboard_shortcut("5")
    },
    {
        "name": "youtube_poln_okno",
        "function": keyboard_shortcut("F")
    },
    {
        "name": "youtube_min_proig",
        "function": keyboard_shortcut("i")
    },
    {
        "name": "youtube_zak_proig",
        "function": keyboard_shortcut("esc")
    },
    {
        "name": "subtitr",
        "function": keyboard_shortcut("c")
    },
    {
        "name": "screenshot",
        "function": screenshot
    }
]
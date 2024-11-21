from .utils import off_system, off_work, restart_pk, garbage_cleaning, sleep_pk, open_provodnic, off_provodnic

intents = [
    {
        "name": "open_provodnic",
        "function": open_provodnic,
    },
    {
        "name": "off_provodnic",
        "function": off_provodnic,
    },
    {
        "name": "off_system",
        "function": off_system,
    },
    {
        "name": "off_work",
        "function": off_work,
    },
    {
        "name": "restart_pk",
        "function": restart_pk,
    },
    {
        "name": "garbage_cleaning",
        "function": garbage_cleaning,
    },
    {
        "name": "sleep_pk",
        "function": sleep_pk
    },
]
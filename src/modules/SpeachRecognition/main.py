from .recognition import voice_listening, recognize

acceptor = None

sender = voice_listening

intents = []

extensions = [
    {
        "name": "recognize",
        "function": recognize
    }
]

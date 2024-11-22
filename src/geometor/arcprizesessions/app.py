"""
run the main app
"""
from .arcprizesessions import Arcprizesessions


def run() -> None:
    reply = Arcprizesessions().run()
    print(reply)

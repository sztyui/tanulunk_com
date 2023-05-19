"""Tanulunk.com form filler for bonus coupons."""
from pathlib import Path

from config.load import open_config
from tanulunk.base import TanulunkFiller

if __name__ == "__main__":
    conf = open_config(Path("./config.yml"))
    t = TanulunkFiller(conf)
    t.run()

"""Tanulunk.com form filler for bonus coupons."""
from config.load import open_config
from tanulunk.base import TanulunkFiller

if __name__ == "__main__":
    conf = open_config("./config.yml")
    t = TanulunkFiller(conf)
    t.run()

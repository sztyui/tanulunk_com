import logging
from pathlib import Path

import pyautogui

from config.load import open_config


class TanulunkFiller:
    """Helps to full tanulunk.com and runs coupons"""

    def __init__(self, config):
        self.config = config

    def click_coupon(self):
        """Clicking on coupon button"""
        button = pyautogui.locateCenterOnScreen(
            self.config["images"]["coupon"], confidence=0.8
        )
        if not button:
            logging.error("Button not found!")
            return
        pyautogui.click(button)

    def run(self):
        """Main runner, acts like facade."""
        self.click_coupon()


if __name__ == "__main__":
    conf = open_config(Path("./config.yml"))
    t = TanulunkFiller(conf)
    t.run()

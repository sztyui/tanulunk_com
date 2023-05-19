import logging
import time
from pathlib import Path

import pyautogui

from config.load import open_config


class TanulunkFiller:
    """Helps to full tanulunk.com and runs coupons"""

    def __init__(self, config):
        self.config = config

    def _click_button(self, name: str) -> bool:
        if name not in self.config["images"]:
            raise AttributeError(f"no button: {name}")
        button = pyautogui.locateCenterOnScreen(
            self.config["images"][name], confidence=0.8
        )
        if not button:
            logging.error(f"button not found: {name}")
            return False
        pyautogui.click(button)
        return True

    def click_coupon(self) -> bool:
        """Clicking on coupon button"""
        return self._click_button("coupon")

    def watch_advertisment(self):
        return self._click_button("advertisment")

    def run(self):
        """Main runner, acts like facade."""
        self.click_coupon()
        time.sleep(1)
        self.watch_advertisment()


if __name__ == "__main__":
    conf = open_config(Path("./config.yml"))
    t = TanulunkFiller(conf)
    t.run()

import logging
import time
from pathlib import Path

import pyautogui

from config.load import open_config


class TanulunkFiller:
    """Helps to full tanulunk.com and runs coupons"""

    def __init__(self, config, delay: int = 2):
        self.config = config
        self.delay = delay

    def _click_button(self, name: str, confidence: bool = 0.8) -> bool:
        if name not in self.config["images"]:
            raise AttributeError(f"no button: {name}")
        button = pyautogui.locateCenterOnScreen(
            self.config["images"][name], confidence=confidence
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
        """Click on watch advertisment button"""
        return self._click_button("advertisment")

    def play_video(self) -> bool:
        """Click on play video button"""
        return self._click_button(name="play", confidence=0.9)

    def wait_until_vide_ends(self):
        """Search for video end screen"""
        while True:
            ends = pyautogui.locateCenterOnScreen(
                self.config["images"]["video_end"], confidence=0.8
            )
            if ends:
                return
            time.sleep(self.delay)

    def click_on_back_button(self) -> bool:
        """Click on back button upon video finish."""
        return self._click_button("back")

    def run(self):
        """Main runner, acts like facade."""
        while True:
            if not self.click_coupon():
                return
            time.sleep(self.delay)
            if not self.watch_advertisment():
                return
            time.sleep(self.delay)
            if not self.play_video():
                return
            time.sleep(self.delay)
            self.wait_until_vide_ends()
            if not self.click_on_back_button():
                return
            time.sleep(self.delay)


if __name__ == "__main__":
    conf = open_config(Path("./config.yml"))
    t = TanulunkFiller(conf)
    t.run()

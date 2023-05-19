"""Tanulunk.com filler representation class extending pyautogui"""

import logging
import time
from pathlib import Path
from venv import logger

import pyautogui  # pylint: disable=E0401


def wait_delay(timeout):
    """Waits delay after function call"""

    def decorate(function):
        def wrapper(*args, **kwargs):
            output = function(*args, **kwargs)
            time.sleep(timeout)
            return output

        return wrapper

    return decorate


class TanulunkFiller:
    """Helps to full tanulunk.com and runs coupons"""

    def __init__(self, config: Path, delay: int = 2):
        self.config = config
        self.delay = delay

    def _click_button(self, name: str, confidence: bool = 0.8) -> bool:
        if name not in self.config["images"]:
            raise AttributeError(f"no button: {name}")
        button = pyautogui.locateCenterOnScreen(
            self.config["images"][name], confidence=confidence
        )
        if not button:
            logging.error("button not found: %s", name)
            return False
        pyautogui.click(button)
        return True

    @wait_delay(2)
    def click_coupon(self) -> bool:
        """Clicking on coupon button"""
        return self._click_button("coupon")

    @wait_delay(2)
    def watch_advertisment(self):
        """Click on watch advertisment button"""
        return self._click_button("advertisment")

    @wait_delay(2)
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

    @wait_delay(2)
    def click_on_back_button(self) -> bool:
        """Click on back button upon video finish."""
        return self._click_button("back")

    @wait_delay(4)
    def click_on_bouns_tab(self) -> bool:
        """Clicks on bonus tab in menu."""
        return self._click_button("bonus_tab")

    def watch_video(self) -> bool:
        """Watchi video process."""
        if not self.click_coupon():
            return False
        if not self.watch_advertisment():
            return False
        if not self.play_video():
            return False
        self.wait_until_vide_ends()
        if not self.click_on_back_button():
            return False
        return True

    def run(self):
        """Main runner, acts like facade."""
        if not self.click_on_bouns_tab():
            logger.error("bouns card not found!")
        time.sleep(4)
        while True:
            if not self.watch_video():
                break

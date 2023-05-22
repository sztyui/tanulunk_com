"""Tanulunk.com filler representation class extending pyautogui"""

import datetime
import logging
import time
from pathlib import Path

import pyautogui  # pylint: disable=E0401

from tanulunk.wait import wait_delay


class TanulunkFiller:
    """Helps to full tanulunk.com and runs coupons"""

    def __init__(self, config: Path, delay: int = 2) -> None:
        self.config: Path = config
        self.delay: int = delay

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
    def watch_advertisment(self) -> bool:
        """Click on watch advertisment button"""
        return self._click_button("advertisment")

    @wait_delay(2)
    def play_video(self) -> bool:
        """Click on play video button"""
        return self._click_button(name="play", confidence=0.9)

    def wait_until_video_ends(self) -> None:
        """Search for video end screen"""
        start = datetime.datetime.now()
        while True:
            delta = datetime.datetime.now() - start
            if delta.seconds > 600:
                raise ValueError("the video has not finished yet")

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
        return self._click_button("bonus_tab", confidence=0.7)

    def watch_video(self) -> bool:
        """Watchi video process."""
        if not self.click_coupon():
            return False
        if not self.watch_advertisment():
            return False
        if not self.play_video():
            return False
        try:
            self.wait_until_video_ends()
        except ValueError as err:
            logging.error(err)
            return False
        if not self.click_on_back_button():
            return False
        return True

    def run(self) -> None:
        """Main runner, acts like facade."""
        logging.info(
            "Place tanulunk.com at the main screen at full, and minimize this window."
        )
        time.sleep(5)
        self.click_on_bouns_tab()
        while True:
            if not self.watch_video():
                break

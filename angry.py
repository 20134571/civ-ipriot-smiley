# -*- coding: utf-8 -*-
"""
Created on Sun Oct 26 15:09:14 2025

@author: Adam Bradley
Lecturer: Chris Arnold
Student# 20134571
Cert IV (Data Science and AI)
"""
import time
from blinkable import Blinkable
from smiley import Smiley


class Angry(Smiley, Blinkable):
    """
   Provides a Smiley with a happy expression
    """
    DEFAULT_COMPLEXION=Smiley.RED #Overrides at class level
    
    def __init__(self):
        super().__init__(complexion=self.DEFAULT_COMPLEXION)

        self.draw_mouth()
        self.draw_eyes()

    def draw_mouth(self):
        """
       Renders a mouth by blanking the pixels that form that object.
        """
        mouth = [49,50, 51, 52, 53, 54]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self, wide_open=True):
        """
       Draws the eyes (open or closed) on the standard smiley.
        :param wide_open (bool): eyes open or closed.
        """
        eyes = [10, 13, 18, 21]
        for pixel in eyes:
            #self.pixels[pixel] = self.BLANK if wide_open else self.YELLOW
            if wide_open:
               eyes = self.BLANK
            else:               
               eyes = self.DEFAULT_COMPLEXION
            self.pixels[pixel] = eyes
            
    def draw_nostrils(self, wide_open=True):
        """
       Draws the nostrils (open or closed) on the standard smiley.
        :param wide_open (bool): eyes open or closed.
        """
        nostrils = [35, 36]
        for pixel in nostrils:
            #self.pixels[pixel] = self.BLANK if wide_open else self.YELLOW
            if wide_open:
               nostrils = self.BLANK
            else:               
               nostrils = self.DEFAULT_COMPLEXION
            self.pixels[pixel] = nostrils
    def blink(self, delay=2.0):
        """
       Blinks the smiley's eyes twice
        
        :param delay: Delay between blinks (in seconds)
        """
        self.draw_eyes(wide_open=False)
        self.draw_nostrils(wide_open=True)
        self.show()
        time.sleep(delay)
        self.draw_eyes(wide_open=True)
        self.draw_nostrils(wide_open=False)
        self.show()
        self.draw_nostrils(wide_open=True)
        self.show()
        



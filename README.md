# Among-Us-Win-Loss-Tracker

This is a python-based application to track the Wins and Losses automatically in Among Us.

## About

The Wins and Losses are tracked by grabbing the part of the screen where round information is displayed every second. The image is converted to binary Black and White, and given to the opensource Tesseract OCR from Google. The text is then read and acted on accordingly.


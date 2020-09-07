# Among-Us-Win-Loss-Tracker

This is a python-based application to track the Wins and Losses automatically in Among Us.

## About

The Wins and Losses are tracked by grabbing the part of the screen where round information is displayed every second. The image is converted to binary Black and White, and given to the opensource Tesseract OCR from Google. The text is then read and acted on accordingly.

## How it works

My recommended use for this application is to add the winLossStats.txt to OBS.
Each stat is broken down into its own file in case you'd like to make your own overlay and place the information into different locations.

How this application works:

Every .5 seconds, a screenshot is taken of the top middle section of the primary monitor.
This image is sent to the Tesseract OCR application built by google that processes images into text.
The text is then processed to update the status of the UI window.

The flow of information works generally like this:

Open the application before starting your first game.

When the game starts, your role is displayed on screen. This will update the top of the UI to your current role. This will also update the winLossStats.txt file to display your role.

**NOTE: If the role isn't properly grabbed (this can happen if something is obstructing the role on screen) you can press the "Manual Crewmate" or "Manual Impostor" buttons to set your role.

When the game ends, the Victory or Defeat message is displayed on screen. This will update your statistic for the role that you have selected.

**NOTE: If the victory or defeat message isn't properly grabbed (this can happen if something is obstructing the role on screen) you can press the "Manual Win" or "Manual Loss" buttons to set the outcome of the game.

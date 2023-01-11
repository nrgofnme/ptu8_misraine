#!/bin/bash
source venv/bin/activate
pyinstaller --onefile -w --hidden-import='PIL._tkinter_finder' --icon='salad.ico' misraine.py
cp -r images dist/
cp salad.ico dist/

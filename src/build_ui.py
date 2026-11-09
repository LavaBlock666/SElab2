# -*- coding: utf-8 -*-
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ui_screens import SCREENS

out_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "UI"))
os.makedirs(out_dir, exist_ok=True)
for name, fn in SCREENS:
    img = fn()
    path = os.path.join(out_dir, name)
    img.save(path, "PNG")
    print("saved", name, img.size)

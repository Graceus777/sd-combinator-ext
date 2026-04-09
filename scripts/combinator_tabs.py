"""
CombinatorSD - A1111 WebUI Extension entry point.

Registers two standalone tabs:
  1. LoRA Combinator — zone-based LoRA management + generation
  2. Comic Generator — comic/strip generation + assembly
"""
import sys
import os

# Ensure the extension's package is importable
ext_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ext_dir not in sys.path:
    sys.path.insert(0, ext_dir)

from modules import script_callbacks

from combinator.ui_combinator import create_combinator_tab
from combinator.ui_comic import create_comic_tab


def on_ui_tabs():
    combinator_tab = create_combinator_tab()
    comic_tab = create_comic_tab()
    return [combinator_tab, comic_tab]


script_callbacks.on_ui_tabs(on_ui_tabs)

"""
CombinatorSD - A1111 WebUI Extension entry point.

Registers the LoRA Combinator tab — zone-based LoRA management + generation.

The Comic Generator is now a separate extension: sd-comic-ext.
"""
import sys
import os

# Ensure the extension's package is importable
ext_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ext_dir not in sys.path:
    sys.path.insert(0, ext_dir)

from modules import script_callbacks


def on_ui_tabs():
    from combinator.ui_combinator import create_combinator_tab
    return [create_combinator_tab()]


script_callbacks.on_ui_tabs(on_ui_tabs)

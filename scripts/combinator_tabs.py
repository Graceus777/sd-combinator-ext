"""
CombinatorSD - A1111 WebUI Extension entry point.

Registers the LoRA Combinator tab — zone-based LoRA management + generation.

The Comic Generator is now a separate extension: sd-comic-ext.
"""
import sys
import os

# A1111 prepends the extension basedir to sys.path only during script load,
# then restores the original sys.path in a finally block. Import package
# modules now (while basedir is on sys.path) so they're cached in sys.modules
# before the callback fires.
ext_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ext_dir not in sys.path:
    sys.path.insert(0, ext_dir)

from modules import script_callbacks
from combinator.ui_combinator import create_combinator_tab


def on_ui_tabs():
    return [create_combinator_tab()]


script_callbacks.on_ui_tabs(on_ui_tabs)

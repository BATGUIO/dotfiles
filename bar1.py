# DISCLAIMER: bar1.py, colors.py & unicodes.py 
# aren't made by me. The original creator is "tuffgniuz"
# and the repository of the original dotfiles
# is: https://github.com/tuffgniuz/qtile

from libqtile.bar import Bar
from libqtile.widget.battery import Battery
from libqtile.widget.clock import Clock
from libqtile.widget.cpu import CPU
from libqtile.widget.currentlayout import CurrentLayout
from libqtile.widget.groupbox import GroupBox
from libqtile.widget.memory import Memory
from libqtile.widget.net import Net
from libqtile.widget.spacer import Spacer
from libqtile.widget.systray import Systray
from libqtile.widget.window_count import WindowCount
from libqtile.widget.windowname import WindowName
from libqtile.widget.prompt import Prompt  # added by me for my prompt widget

from unicodes import left_half_circle, right_arrow, left_arrow, right_half_circle, lower_left_triangle
from colors import nord_fox

BAR_HEIGHT = 28
# BAR_MARGIN = 5

bar = Bar([
    GroupBox(
        disable_drag=True,
        active=nord_fox['magenta'],
        inactive=nord_fox['black'],
        highlight_method='line',
        block_highlight_text_color=nord_fox['green'],
        borderwidth=0,
        highlight_color=nord_fox['bg'],
        background=nord_fox['bg'],
        # spacing=2
    ),
    lower_left_triangle(nord_fox['bg'], nord_fox['red']),
    CurrentLayout(
        background=nord_fox['red'],
        foreground=nord_fox['white'],
        margin=10,
    ),

    lower_left_triangle(nord_fox['red'], nord_fox['fg_gutter']),
    WindowCount(
        text_format='缾 {num}',
        background=nord_fox['fg_gutter'],
        foreground=nord_fox['white'],
        show_zero=True,
    ),
    lower_left_triangle(nord_fox['fg_gutter'], nord_fox['bg']),

    Prompt(
        fontsize= 11,
        background=nord_fox['bg'],
        foreground=nord_fox['fg']
    ),

    WindowName(
        fontsize= 11,
        background=nord_fox['bg'],
        foreground=nord_fox['fg']
    ),

    left_arrow(nord_fox['bg'], nord_fox['fg_gutter']),
    CPU(
        format=' {freq_current}GHz {load_percent}%',
        background=nord_fox['fg_gutter'],
        foreground=nord_fox['pink']
    ),

    Memory(
        format='󰍛 {MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
        background=nord_fox['fg_gutter'],
        foreground=nord_fox['cyan']
    ),

    Battery(
        background=nord_fox['fg_gutter'],
        foreground=nord_fox['green'],
        format='{char} {percent:2.0%} {hour:d}:{min:02d}'
    ),

    Clock(
        background=nord_fox['fg_gutter'],
        foreground=nord_fox['white'],
        format='  %m | %d  %a  %H %M', locale='en_US.UTF-8'
    ),



],
    # background=nord_fox['bg'],
    size=BAR_HEIGHT,
    margin=8,
)

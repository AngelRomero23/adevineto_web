import reflex as rx
from enum import Enum
from .fonts import Font
from .colors import Color, TextColor


MAX_WIDTH = '1000px'

class Size(Enum):
    ZERO = '0px !important'
    SMALL = '0.5em'
    MEDIUM = '0.8em'
    DEFAULT = '1em'
    BIG = '2em'
    BUTTON = "2.75em"
    VERY_BIG = '4em'

STYLESHEETS = [
    "https://unpkg.com/nes.css@latest/css/nes.min.css",
    "https://fonts.googleapis.com/css?family=Press+Start+2P&display=swap"
]

BASE_STYLE = {
    'font_family': Font.DEFAULT.value,
    'color': TextColor.PRIMARY.value,
    'background': Color.PRIMARY.value,
    '.heading': {
        'color': TextColor.ACCENT.value
    },
    rx.link: {
        'text_decoration':'none',
        'cursor':'url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAzElEQVRYR+2X0Q6AIAhF5f8/2jYXZkwEjNSVvVUjDpcrGgT7FUkI2D9xRfQETwNIiWO85wfINfQUEyxBG2ArsLwC0jioGt5zFcwF4OYDPi/mBYKm4t0U8ATgRm3ThFoAqkhNgWkA0jJLvaOVSs7j3qMnSgXWBMiWPXe94QqMBMBc1VZIvaTu5u5pQewq0EqNZvIEMCmxAawK0DNkay9QmfFNAJUXfgGgUkLaE7j/h8fnASkxHTz0DGIBMCnBeeM7AArpUd3mz2x3C7wADglA8BcWMZhZAAAAAElFTkSuQmCC) 14 0,pointer',
    },
    '.hover-link':{
        ':hover':{
            'color': TextColor.ACCENT.value,
            'text_decoration':'none'
        }
    },
    rx.text.span: {
        'font_size':Size.MEDIUM.value
    },
    '.footer-user-reference':{
        'color':TextColor.ACCENT.value,
        'font_size':Size.MEDIUM.value    
    },
    '.btn-nes-custom':{
        ':after':{
            'position':'relative'
        },
        'margin_bottom':Size.DEFAULT.value,
        'margin_right':Size.DEFAULT.value, 
        'height':'2.75em',
        'color':TextColor.SECONDARY.value,
        ':hover': {
            'color': TextColor.PRIMARY.value,
            'cursor':'url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAzElEQVRYR+2X0Q6AIAhF5f8/2jYXZkwEjNSVvVUjDpcrGgT7FUkI2D9xRfQETwNIiWO85wfINfQUEyxBG2ArsLwC0jioGt5zFcwF4OYDPi/mBYKm4t0U8ATgRm3ThFoAqkhNgWkA0jJLvaOVSs7j3qMnSgXWBMiWPXe94QqMBMBc1VZIvaTu5u5pQewq0EqNZvIEMCmxAawK0DNkay9QmfFNAJUXfgGgUkLaE7j/h8fnASkxHTz0DGIBMCnBeeM7AArpUd3mz2x3C7wADglA8BcWMZhZAAAAAElFTkSuQmCC) 14 0,pointer'
        },
        'box_shadow':'inset -4px -4px #8c2022'
    },
    '.rt-AvatarImage':{
        'width':'100%',
        'height':'100%',
        'border-style':'solid',
        'border-width':'3px',
        'border-color':Color.SECONDARY.value
    },
    '.rt-AvatarRoot':{
        '--avatar-size':'7.5em'
    },
    '.partners-color':{
        'background_color':Color.ACCENT.value,
        'width':'100%',
        'align_items':'center'
    },
    '.container':{
        'display':'flex',
        'align_items':'start',
        'justify-content': 'center',
        #.'--gap':Size.BIG.value,
        'width':'100%',
        'max_width':MAX_WIDTH,
        'padding_y':Size.VERY_BIG.value
    },
    '.heading-container-author':{
        '@media (prefers-color-scheme: light)':{
        'color':TextColor.ACCENT.value ,
        },
        '@media (prefers-color-scheme: dark)':{
        'color':TextColor.SECONDARY.value 
        },
        'padding_bottom':Size.BUTTON.value
    }
    
    
}


max_width_style = dict(
    align_items="start",
    padding_x=Size.BIG.value,
    width="100%",
    max_width=MAX_WIDTH
)
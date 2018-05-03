#!/usr/bin/env python3
# Soubor:  asteroidy.py
# Datum:   26.04.2018 13:26
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL
############################################################################

import pyglet
from pyglet.window.key import A, B, C, MOD_CTRL, MOD_SHIFT
from pyglet.window.mouse import LEFT, RIGHT

window = pyglet.window.Window()

obrazek = pyglet.image.load('obrazek.png')
obrazek.anchor_x = obrazek.width // 2
obrazek.anchor_y = obrazek.height // 2
sprite = pyglet.sprite.Sprite(obrazek)


def tiktak(t):
    sprite.x = sprite.x + 10*t
    sprite.y = sprite.y + 10*t


@window.event
def on_draw():
    window.clear()
    sprite.draw()


@window.event
def on_mouse_press(x, y, button, mod):
    if button == LEFT:
        sprite.x = x
        sprite.y = y
    elif button == RIGHT and (mod & MOD_SHIFT):
        sprite.rotation += 180
    elif button == RIGHT and (mod & MOD_CTRL):
        sprite.rotation += 90
    elif button == RIGHT:
        sprite.rotation += 10


@window.event
def on_key_press(sym, mod):
    if sym != A:
        print(sym, mod)


pyglet.clock.schedule_interval(tiktak, 1/10)

pyglet.app.run()
print('Hotovo!')

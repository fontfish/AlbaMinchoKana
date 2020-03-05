#!/usr/bin/python3
"""
Much of this code inspired by various online examples. Heavily modified.
See the following for help with modification:
https://pycairo.readthedocs.io/en/latest/getting_started.html
https://python-gtk-3-tutorial.readthedocs.io/en/latest/introduction.html
https://lazka.github.io/pgi-docs/
"""

import sys, gi, math
gi.require_version('Gtk', '3.0')
gi.require_version('PangoCairo', '1.0')
from gi.repository import Gtk, Gdk, Pango, cairo, PangoCairo

# All the defs.

def style_gtk():
	css = b"""
* {
	background-color: #ffffff;
}
	"""
	screen = Gdk.Screen.get_default()
	provider = Gtk.CssProvider()
	provider.load_from_data(css)# This can be a load_from_path("/path/to/file.css") to use a separate file.

	Gtk.StyleContext.add_provider_for_screen(screen, provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

def take_text():
	print("Type your input text, followed by a new line and a Ctrl-D.")
	txt = sys.stdin.read()
	if txt == "":
		txt = "You didn't type anything! \n 何も書かなかった！"
	return txt

def set_font():
	print("Choose font. (Default is Alba Mincho Kana for testing.)")
	f = input()
	if f == "":
		f = "Alba Mincho"
	return f
"""
def set_font_style():
	print("Choose font options. (Bold, Italic, etc.) Default is Medium.")
	f = input()
	if f == "":
		f = "Medium"
	return f
"""
def set_font_size():
	print("Choose font size. (Default is 20.)")
	f = input()
	if f == "":
		f = "20"
	return f

def user_rotation():
	print("Rotation of the text: h/v (Default is horizontal.)")
	r = input()
	if r.lower() == "v":
		orientation = 1
	else:
		orientation = 0
	return orientation

def cairo_draws(widget, mything):# mything is the Cairo context.
	width = widget.get_allocated_width()

	mything.set_source_rgba(0, 0, 0, 1)# Sets the text colour.
	if rotation == 1:
		mything.translate(width - 2, 20)
		mything.rotate(math.radians(90))
	else:
		mything.translate(10, 2)

	mypc = PangoCairo.create_context(mything)
	mypc.set_base_gravity(4)# Pango gravity. South = 0, East = 1, North = 2, West = 3, Auto = 4.

	mylayout = Pango.Layout.new(mypc)
	mylayout.set_font_description(Pango.FontDescription("%s %s" %(font, fontsize)))
	mylayout.set_text(usertext, -1)

	PangoCairo.show_layout(mything, mylayout)

# Command line stuff.

usertext = take_text()
font = set_font()
#fontstyle = set_font_style()
fontsize = set_font_size()
rotation = user_rotation()

# All the GTK stuff.

style_gtk()# To add the CSS.
win = Gtk.Window()
win.connect('destroy', Gtk.main_quit)

drawingarea = Gtk.DrawingArea()
box = Gtk.Box.new(1, 1)
box.add(drawingarea)
win.add(box)
drawingarea.connect('draw', cairo_draws)
drawingarea.set_size_request(500, 500)

win.show_all()
Gtk.main()

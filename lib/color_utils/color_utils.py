from colour import Color

def update_color(bg_hex, s, l):
  s = limit_color_hsl(Color(bg_hex).get_saturation() + s)
  l = limit_color_hsl(Color(bg_hex).get_luminance() + l)

  return Color(bg_hex, saturation=s, luminance=l).hex

def limit_color_hsl(value):
  if value > 1: return 1
  elif value < 0: return 0
  else: return value

def gen_bg_bright(bg_hex):
   return update_color(bg_hex, 0, +0.03)

def gen_border(bg_hex):
   return update_color(bg_hex, -0.03, -0.05)

def gen_bg_dark(bg_hex):
   return update_color(bg_hex, -0.01, -0.02)

def gen_subtle(fg_hex):
   return update_color(fg_hex, -0.3, -0.2)
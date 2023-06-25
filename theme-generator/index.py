from colour import Color

def generate_theme(theme_name, colors):
  file_name = theme_name.replace(" ", "_")

  with open('./base-theme.json') as base_theme_file, open(f'./out/{file_name}.json', 'w') as outfile:
    for line in base_theme_file:
      for src, target in colors.items():
        line = line.replace(src, target)
      outfile.write(line)

def generate_themes(themes):
    for theme in themes:
        generate_theme(theme['$THEME_NAME'], theme)

def update_color(bg_hex, s, l):
  s = limit_color_hsl(Color(bg_hex).get_saturation() + s)
  l = limit_color_hsl(Color(bg_hex).get_luminance() + l)

  return Color(bg_hex, saturation=s, luminance=l).hex

def limit_color_hsl(value):
  if value > 1: return 1
  elif value < 0: return 0
  else: return value

def gen_bg3(bg_hex):
   return update_color(bg_hex, 0, +0.03)

def gen_border(bg_hex):
   return update_color(bg_hex, -0.03, -0.05)

def gen_bg0(bg_hex):
   return update_color(bg_hex, -0.01, -0.02)

def gen_subtle(fg_hex):
   return update_color(fg_hex, -0.3, -0.2)

night = {
    '$THEME_NAME':'tomorrow night',

    '$ACCENT':'#C2C77B',

    '$FUNCTION':'#C2C77B',
    '$TYPE':'#9AC9C4',
    '$PARAMETER':'#E6A472',
    '$COMMENT':'#484C50',
    '$KEYWORD':'#C0A7C7',
    '$STRING':'#F4CF86',
    '$PROPERTY':'#D77C79',
    '$FG':'#c5c8c6',
    '$NUMBER':'#92B2CA',

    '$BG2':'#2E3034',
    '$BG1':'#1B1C1D',
    '$BG3': '#282829',
    '$BG0': '#222223',
    '$BORDER': gen_border("#1B1C1D"),
    '$SUBTLE_FG': gen_subtle("#c5c8c6")
}

default = {
    '$THEME_NAME':'default',

    '$ACCENT':'#A8D7F2',

    '$FUNCTION':'#8AD8A9',
    '$TYPE':'#A8D7F2',
    '$PARAMETER':'#DABB98',
    '$COMMENT':'#5D607A',
    '$KEYWORD':'#D77DD3',
    '$STRING':'#D8D5A1',
    '$PROPERTY':'#B1A2ED',
    '$FG':'#C9CBE6',
    '$NUMBER':'#A6B6F0',

    '$BG1':'#151621',
    '$BG3': '#21222E',
    '$BG0': '#191B26',
    '$BORDER': gen_border("#151621"),
    '$SUBTLE_FG': "#5D607A"
}

midnight = {
    '$THEME_NAME':'midnight',

    '$ACCENT':'#B5CC85',

    '$FUNCTION':'#B5CC85',
    '$TYPE':'#99D1CB',
    '$PARAMETER':'#D9B18D',
    '$COMMENT':'#5E6B76',
    '$KEYWORD':'#D1778C',
    '$STRING':'#CFD093',
    '$PROPERTY':'#BEA5CD',
    '$FG':'#CAD4DD',
    '$NUMBER':'#93ACDD',

    '$BG1':'#0A131A',
    '$BG3': '#151F27',
    '$BG0': '#0F181F',
    '$BORDER': gen_border("#0A131A"),
    '$SUBTLE_FG': gen_subtle("#CBCDE2")
}

themes = [default, night, midnight]

generate_themes(themes)
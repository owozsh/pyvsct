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
    '$KEYWORD':'#D77C79',
    '$STRING':'#F4CF86',
    '$PROPERTY':'#C0A7C7',
    '$FG':'#c5c8c6',
    '$NUMBER':'#92B2CA',

    '$BG2':'#2E3034',
    '$BG1':'#1B1C1D',
    '$BG3': gen_bg3("#1B1C1D"),
    '$BG0': gen_bg0("#1B1C1D"),
    '$BORDER': gen_border("#1B1C1D"),
    '$SUBTLE_FG': gen_subtle("#c5c8c6")
}

default = {
    '$THEME_NAME':'default',

    '$ACCENT':'#A2D1EC',

    '$FUNCTION':'#8AD8A9',
    '$TYPE':'#A2D1EC',
    '$PARAMETER':'#DABB98',
    '$COMMENT':'#4C5078',
    '$KEYWORD':'#D77DD3',
    '$STRING':'#D8D5A1',
    '$PROPERTY':'#B1A2ED',
    '$FG':'#C9CBE6',
    '$NUMBER':'#A6B6F0',

    '$BG1':'#12131D',
    '$BG3': '#21222E',
    '$BG0': '#171824',
    '$BORDER': gen_border("#12131D"),
    '$SUBTLE_FG': "#4C5078"
}

gruvbox = {
    '$THEME_NAME':'gruvbox',

    '$ACCENT':'#FABD2F',

    '$FUNCTION':'#B8BB26',
    '$TYPE':'#83A598',
    '$PARAMETER':'#FE8019',
    '$COMMENT':'#665c54',
    '$KEYWORD':'#FB4934',
    '$STRING':'#FABD2F',
    '$PROPERTY':'#8EC07C',
    '$FG':'#D5C4A1',
    '$NUMBER':'#D3869B',

    '$BG2':'#2E3034',
    '$BG1':'#1d2021',
    '$BG3': gen_bg3("#1d2021"),
    '$BG0': gen_bg0("#1d2021"),
    '$BORDER': gen_border("#1d2021"),
    '$SUBTLE_FG': gen_subtle("#D5C4A1")
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
    '$BG0': gen_bg0("#0A131A"),
    '$BORDER': gen_border("#0A131A"),
    '$SUBTLE_FG': gen_subtle("#CBCDE2")
}

dracula = {
    '$THEME_NAME':'dracula',

    '$ACCENT':'#ff79c6',

    '$FUNCTION':'#50fa7b',
    '$TYPE':'#8be9fd',
    '$PARAMETER':'#ffb86c',
    '$COMMENT':'#6272a4',
    '$KEYWORD':'#ff79c6',
    '$STRING':'#f1fa8c',
    '$PROPERTY':'#bd93f9',
    '$FG':'#f8f8f2',
    '$NUMBER':'#bd93f9',

    '$BG2':'#282a36',
    '$BG1':'#282a36',

    '$BG3': gen_bg3("#282a36"),
    '$BG0': gen_bg0("#282a36"),
    '$BORDER': gen_border("#282a36"),
    '$SUBTLE_FG': gen_subtle("#f8f8f2")
}

amora = {
    '$THEME_NAME':'amora',

    '$ACCENT':'#D865A3',

    '$FUNCTION':'#a2baa8',
    '$TYPE':'#aabae7',
    '$PARAMETER':'#D29BDB',
    '$COMMENT':'#594B67',
    '$KEYWORD':'#D865A3',
    '$STRING':'#DACEB1',
    '$PROPERTY':'#D29BDB',
    '$FG':'#D1C5DD',
    '$NUMBER':'#A89DE9',

    '$BG2':'#2F2836',
    '$BG1':'#2a2331',
    '$BG3': gen_bg3("#2a2331"),
    '$BG0': gen_bg0("#2a2331"),
    '$BORDER': gen_border("#2a2331"),
    '$SUBTLE_FG': gen_subtle("#D1C5DD")
}

ayu = {
    '$THEME_NAME':'ayu',

    '$ACCENT':'#E6B450',

    '$FUNCTION':'#AAD94C',
    '$TYPE':'#39BAE6',
    '$PARAMETER':'#FFB454',
    '$KEYWORD':'#FF8F40',
    '$STRING':'#E6B673',
    '$PROPERTY':'#D2A6FF',
    '$FG':'#BFBDB6',
    '$NUMBER':'#A89DE9',

    '$COMMENT':'#364149',

    '$BG2':'#131721',
    '$BG1':'#0D1017',
    '$BG3': gen_bg3("#0D1017"),
    '$BG0': gen_bg0("#0D1017"),
    '$BORDER': gen_border("#0D1017"),
    '$SUBTLE_FG': gen_subtle("#BFBDB6")
}

monokai = {
    '$THEME_NAME':'monokai',

    '$ACCENT':'#E6B450',

    '$FUNCTION':'#a6e12e',
    '$TYPE':'#63d4ea',
    '$PARAMETER':'#fc961f',
    '$KEYWORD':'#f82a71',
    '$STRING':'#e6da73',
    '$PROPERTY':'#d2d3cd',
    '$FG':'#d2d3cd',
    '$NUMBER':'#ae80fe',

    '$COMMENT':'#75705d',

    '$BG2':'#252323',
    '$BG1':'#22231e',
    '$BG3': gen_bg3("#22231e"),
    '$BG0': gen_bg0("#22231e"),
    '$BORDER': gen_border("#22231e"),
    '$SUBTLE_FG': gen_subtle("#d2d3cd")
}

themes = [default, night, gruvbox, dracula, midnight, amora, ayu, monokai]

generate_themes(themes)
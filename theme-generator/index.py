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
   return update_color(bg_hex, -0.05, +0.03)

def gen_border(bg_hex):
   return update_color(bg_hex, -0.03, -0.05)

def gen_bg0(bg_hex):
   return update_color(bg_hex, -0.01, -0.025)

def gen_subtle(fg_hex):
   return update_color(fg_hex, -0.2, -0.2)

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

    '$ACCENT':'#A4DFF9',

    '$FUNCTION':'#8EDCA4',
    '$TYPE':'#A4DFF9',
    '$PARAMETER':'#EAB685',
    '$COMMENT':'#5D6F93',
    '$KEYWORD':'#D970AF',
    '$STRING':'#D7CB8C',
    '$PROPERTY':'#B29AE3',
    '$FG':'#CFCFDF',
    '$NUMBER':'#DDA6F0',

    '$BG2':'#232831',
    '$BG1':'#1C2028',
    '$BG3': gen_bg3("#1C2028"),
    '$BG0': gen_bg0("#1C2028"),
    '$BORDER': gen_border("#1C2028"),
    '$SUBTLE_FG': gen_subtle("#CFCFDF")
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

pro = {
    '$THEME_NAME':'pro',

    '$ACCENT':'#C3C182',

    '$FUNCTION':'#99C07B',
    '$TYPE':'#95C0CD',
    '$PARAMETER':'#CEA77A',
    '$COMMENT':'#545460',
    '$KEYWORD':'#C76DA3',
    '$STRING':'#C3C182',
    '$PROPERTY':'#B090CA',
    '$FG':'#BFC3CA',
    '$NUMBER':'#9B9DD0',

    '$BG1':'#1B1B1F',
    '$BG2':'#212125',
    '$BG3': gen_bg3("#1B1B1F"),
    '$BG0': gen_bg0("#1B1B1F"),
    '$BORDER': gen_border("#1B1B1F"),
    '$SUBTLE_FG': gen_subtle("#BFC3CA")
}

midnight = {
    '$THEME_NAME':'midnight',

    '$ACCENT':'#BBBC81',

    '$FUNCTION':'#88BD91',
    '$TYPE':'#94BAD0',
    '$PARAMETER':'#CEA77A',
    '$COMMENT':'#484E61',
    '$KEYWORD':'#C073AF',
    '$STRING':'#BBBC81',
    '$PROPERTY':'#AC8AD8',
    '$FG':'#B7BDCE',
    '$NUMBER':'#8698CB',

    '$BG1':'#17191F',
    '$BG2':'#212125',
    '$BG3': gen_bg3("#17191F"),
    '$BG0': gen_bg0("#17191F"),
    '$BORDER': gen_border("#17191F"),
    '$SUBTLE_FG': gen_subtle("#B7BDCE")
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

themes = [default, night, gruvbox, pro, dracula, midnight, amora, ayu]

generate_themes(themes)
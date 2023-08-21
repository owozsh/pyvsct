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

def gen_bg_bright(bg_hex):
   return update_color(bg_hex, 0, +0.03)

def gen_border(bg_hex):
   return update_color(bg_hex, -0.03, -0.05)

def gen_bg_dark(bg_hex):
   return update_color(bg_hex, -0.01, -0.02)

def gen_subtle(fg_hex):
   return update_color(fg_hex, -0.3, -0.2)

generate_themes([
   {
    '$THEME_NAME':'yogokai',

    '$ACCENT':'#9AC0D7',

    '$FUNCTION':'#8AC6A2',
    '$TYPE':'#9AC0D7',
    '$PARAMETER':'#D2B38F',
    '$COMMENT':'#534F79',
    '$KEYWORD':'#CD83CA',
    '$STRING':'#D2D08E',
    '$PROPERTY':'#A699CC',
    '$FG':'#BCC0CD',
    '$NUMBER':'#9EAAD5',

    '$ERROR': '#CD83CA',

    '$BLACK': '#534F79',
    '$RED': '#CD83CA',
    '$GREEN': '#8AC6A2',
    '$YELLOW': '#D2D08E',
    '$BLUE': '#9EAAD5',
    '$MAGENTA': '#D2B38F',
    '$CYAN': '#9AC0D7',
    '$WHITE': '#BCC0CD',

    '$SELECTION': '#CFCCC420',

    '$BG_BASE':'#11131D',
    '$BG_BRIGHT': '#1A1C28',
    '$BG_DARK': '#0D0F18',

    '$BORDER': gen_border("#11131D"),
},
{
    '$THEME_NAME':'yogokai midnight',

    '$ACCENT':'#A3B67A',

    '$FUNCTION':'#A3B67A',
    '$TYPE':'#93C5BF',
    '$PARAMETER':'#CBB383',
    '$COMMENT':'#38646D',
    '$KEYWORD':'#C37689',
    '$STRING':'#B7B879',
    '$PROPERTY':'#B09CBC',
    '$FG':'#CFCCC4',
    '$NUMBER':'#869BC2',

    '$BLACK': '#38646D',
    '$RED': '#C37689',
    '$GREEN': '#A3B67A',
    '$YELLOW': '#B7B879',
    '$BLUE': '#869BC2',
    '$MAGENTA': '#CBB383',
    '$CYAN': '#93C5BF',
    '$WHITE': '#CFCCC4',

    '$SELECTION': '#CFCCC420',

    '$BG_BASE':'#0D141A',
    '$BG_BRIGHT': '#131A21',
    '$BG_DARK': '#0B1116',

    '$BORDER': gen_border("#0D141A"),
},
{
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

    '$BLACK': '#594B67',
    '$RED': '#D865A3',
    '$GREEN': '#a2baa8',
    '$YELLOW': '#DACEB1',
    '$BLUE': '#A89DE9',
    '$MAGENTA': '#D29BDB',
    '$CYAN': '#aabae7',
    '$WHITE': '#D1C5DD',

    '$SELECTION': '#D1C5DD20',

    '$BG_BASE':'#2a2331',
    '$BG_BRIGHT': gen_bg_bright("#2a2331"),
    '$BG_DARK': gen_bg_dark("#2a2331"),

    '$BORDER': gen_border("#2a2331"),
},
{
    '$THEME_NAME':'std::river',

    '$ACCENT':'#A8A788',

    '$FUNCTION':'#98AC88',
    '$TYPE':'#81A995',
    '$PARAMETER':'#A6947A',
    '$COMMENT':'#456070',
    '$KEYWORD':'#7B9BA8',
    '$STRING':'#A8A788',
    '$PROPERTY':'#9294AA',
    '$FG':'#B3B4AE',
    '$NUMBER':'#A07D7B',

    '$BLACK': '#456070',
    '$RED': '#A07D7B',
    '$GREEN': '#98AC88',
    '$YELLOW': '#A8A788',
    '$BLUE': '#7B9BA8',
    '$MAGENTA': '#A6947A',
    '$CYAN': '#81A995',
    '$WHITE': '#B3B4AE',

    '$SELECTION': '#B3B4AE20',

    '$BG_BASE':'#1B1D1E',
    '$BG_BRIGHT': '#242525',
    '$BG_DARK': '#18191A',

    '$BORDER': gen_border("#1B1D1E"),
}
])
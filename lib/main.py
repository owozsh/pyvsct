import typer
import json

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

def main(input_dir: str, output_dir: str):
    print(f"{input_dir} {output_dir}")

if __name__ == "__main__":
    typer.run(main)

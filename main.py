import re
import os
import typer
import json

def generate_theme(theme_name, colors, out_dir):
  file_name = theme_name.replace(" ", "_")

  with open('./lib/base-theme.json') as base_theme_file, open(f'{out_dir}/{file_name}.json', 'w') as outfile:
    for line in base_theme_file:
      for src, target in colors.items():
        line = line.replace(src, target)
      outfile.write(line)

def generate_themes(themes, out_dir):
    for theme in themes:
        generate_theme(theme['$THEME_NAME'], theme, out_dir)

def main(in_dir: str, out_dir: str):
    theme_maps = []

    for file_name in os.listdir(in_dir):
        is_filetype_json = re.fullmatch(r"^.*\.json$", file_name)

        if (is_filetype_json):
            json_file = open(os.path.join(in_dir, file_name))
            parsed_json = json.load(json_file)
            theme_maps.append(parsed_json)

    generate_themes(theme_maps, out_dir)

if __name__ == "__main__":
    typer.run(main)

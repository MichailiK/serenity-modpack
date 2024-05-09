#!/usr/bin/env python3

import os
import re

# Extracts the mod name & modrinth ID from a packwiz generated TOML file 
def extract_mod_info(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        mod_name = re.search(r'name = "([^"]+)"', content)
        mod_id = re.search(r'mod-id = "([^"]+)"', content)
        return mod_name.group(1), mod_id.group(1) if mod_id else None

script_directory = os.path.dirname(os.path.realpath(__file__))
mods_directory = os.path.join(script_directory, '../../mods')

mods_info = []

# Go through all the .pw.toml files and extract the mod name & modrinth ID
for filename in os.listdir(mods_directory):
    if filename.endswith(".pw.toml"):
        mod_name, mod_id = extract_mod_info(os.path.join(mods_directory, filename))
        mods_info.append((mod_name, mod_id))

# Generate markdown and write to file
with open(os.path.join(script_directory, "./index.md"), "w", encoding='utf-8') as markdown_file:
    markdown_file.write(
"""
# Mod List

The list of all mods present in the modpack.

For a brief introduction for the mods that matter, please see the
[Mod Introductions](/docs/mod-introductions) page.

"""
    )
    for mod in mods_info:
        if mod[1]:
            markdown_file.write(f"- [{mod[0]}](https://modrinth.com/mod/{mod[1]})\n")
        else:
            markdown_file.write(f"- {mod[0]}\n")

print("Markdown file generated successfully!")

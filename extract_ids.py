import re

with open("achievements_raw.txt", "r", encoding="utf-8") as file:
    text = file.read()

achievement_ids = re.findall(r'\[ACHIEVEMENTS\.(.*?)\]', text)

print(f"Found {len(achievement_ids)} achievements!")
print(achievement_ids)
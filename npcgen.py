import random
import requests

# Tables and dictionaries
genders = ["Male", "Female", "Diverse"]
races = ["Human", "Elf", "Dwarf", "Orc", "Halfling"]
regions = ["Northlands", "Southlands", "Eastlands", "Westlands"]
cities = {
    "Northlands": ["Frosthold", "Icespire"],
    "Southlands": ["Sunshire", "Emberwood"],
    "Eastlands": ["Dawnbreak", "Mistfall"],
    "Westlands": ["Stormhaven", "Duskwood"]
}
descriptions = ["Tall and slender", "Short and stout", "Muscular build", "Lean and agile"]
quirks = ["Fidgets constantly", "Speaks in riddles", "Has a pet companion", "Obsessed with a hobby"]
phrases = ["'By the gods!'", "'I've seen stranger things.'", "'Luck favors the bold.'", "'I have a bad feeling about this.'"]
quests = ["Retrieve a lost artifact", "Escort a VIP", "Investigate a mystery", "Deliver an important message"]
relationships = ["Married", "Engaged", "Widowed", "Single"]
enemies = ["A rival adventurer", "A corrupt official", "A vengeful ex-lover", "A powerful monster"]

# Function to generate an NPC
def generate_npc():
    gender = random.choice(genders)
    race = random.choice(races)
    region = random.choice(regions)
    city = random.choice(cities[region])
    description = random.choice(descriptions)
    quirk = random.choice(quirks)
    phrase = random.choice(phrases)
    quest = random.choice(quests) if random.random() < 0.5 else None
    relationship = random.choice(relationships)
    enemy = random.choice(enemies) if random.random() < 0.3 else None

    # Uncomment the following lines to use the Haiku API for certain fields
    # api_key = "YOUR_API_KEY"
    # api_url = "https://api.anthropic.com/v1/complete"
    # headers = {"X-API-Key": api_key}
    # system_prompt = "Generate a description, quirk, phrase, and quest for an NPC in a TTRPG."
    #
    # description = requests.post(api_url, headers=headers, json={"prompt": system_prompt, "max_tokens_to_sample": 50, "temperature": 0.7}).json()["completion"]
    # quirk = requests.post(api_url, headers=headers, json={"prompt": system_prompt, "max_tokens_to_sample": 20, "temperature": 0.7}).json()["completion"]
    # phrase = requests.post(api_url, headers=headers, json={"prompt": system_prompt, "max_tokens_to_sample": 20, "temperature": 0.7}).json()["completion"]
    # quest = requests.post(api_url, headers=headers, json={"prompt": system_prompt, "max_tokens_to_sample": 50, "temperature": 0.7}).json()["completion"] if random.random() < 0.5 else None

    npc = {
        "Gender": gender,
        "Race": race,
        "Region": region,
        "City": city,
        "Description": description,
        "Quirk": quirk,
        "Phrase": phrase,
        "Quest": quest,
        "Relationship": relationship,
        "Enemy": enemy
    }
    return npc

# Main program
print("Welcome to the NPC Generator!")
gender = input("Select a gender (Male/Female/Diverse): ")
race = input("Select a race (Human/Elf/Dwarf/Orc/Halfling): ")
region = input("Select a region (Northlands/Southlands/Eastlands/Westlands): ")
city = input(f"Select a city ({', '.join(cities[region])}): ")

npc = generate_npc()
npc["Gender"] = gender
npc["Race"] = race
npc["Region"] = region
npc["City"] = city

print("\nGenerated NPC:")
for key, value in npc.items():
    if value:
        print(f"{key}: {value}")
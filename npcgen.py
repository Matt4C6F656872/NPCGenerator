import random
import tkinter as tk
from tkinter import ttk, messagebox

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
    gender = gender_var.get()
    race = race_var.get()
    region = region_var.get()
    city = city_var.get()
    description = random.choice(descriptions)
    quirk = random.choice(quirks)
    phrase = random.choice(phrases)
    quest = random.choice(quests) if random.random() < 0.5 else None
    relationship = random.choice(relationships)
    enemy = random.choice(enemies) if random.random() < 0.3 else None
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

def generate_random_npc():
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

def generate_npc_and_display():
    if not gender_var.get():
        messagebox.showerror("Error", "Please select a gender.")
        return
    if not race_var.get():
        messagebox.showerror("Error", "Please select a race.")
        return
    if not region_var.get():
        messagebox.showerror("Error", "Please select a region.")
        return
    if not city_var.get():
        messagebox.showerror("Error", "Please select a city.")
        return
    npc = generate_npc()
    display_npc(npc)

def generate_random_npc_and_display():
    npc = generate_random_npc()
    display_npc(npc)

def display_npc(npc):
    npc_display.delete("1.0", tk.END)
    for key, value in npc.items():
        if value:
            npc_display.insert(tk.END, f"{key}: {value}\n")

# GUI setup
root = tk.Tk()
root.title("NPC Generator")

# Gender selection
gender_label = ttk.Label(root, text="Select a gender:")
gender_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(root, textvariable=gender_var, values=genders, state="readonly")
gender_combobox.grid(row=0, column=1, padx=5, pady=5)

# Race selection
race_label = ttk.Label(root, text="Select a race:")
race_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
race_var = tk.StringVar()
race_combobox = ttk.Combobox(root, textvariable=race_var, values=races, state="readonly")
race_combobox.grid(row=1, column=1, padx=5, pady=5)

# Region selection
region_label = ttk.Label(root, text="Select a region:")
region_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
region_var = tk.StringVar()
region_combobox = ttk.Combobox(root, textvariable=region_var, values=regions, state="readonly")
region_combobox.grid(row=2, column=1, padx=5, pady=5)

# City selection
city_label = ttk.Label(root, text="Select a city:")
city_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
city_var = tk.StringVar()
city_combobox = ttk.Combobox(root, textvariable=city_var, values=[], state="readonly")
city_combobox.grid(row=3, column=1, padx=5, pady=5)

def update_cities(*args):
    selected_region = region_var.get()
    city_combobox["values"] = cities.get(selected_region, [])

region_var.trace("w", update_cities)

# Generate NPC button
generate_button = ttk.Button(root, text="Generate NPC", command=generate_npc_and_display)
generate_button.grid(row=4, column=0, padx=5, pady=5)

# Generate Random NPC button
random_npc_button = ttk.Button(root, text="Generate Random NPC", command=generate_random_npc_and_display)
random_npc_button.grid(row=4, column=1, padx=5, pady=5)

# NPC display area
npc_display = tk.Text(root, width=50, height=10)
npc_display.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
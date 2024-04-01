import random
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json
from npcdetails import *

# API key (Uncomment the following lines to use the Claude3 API for certain fields)
api_key = "YOUR_API_KEY"
api_url = "https://api.anthropic.com/v1/complete"
headers = {"X-API-Key": api_key}
system_prompt = "Generate a description, quirk, phrase, and quest for an NPC in a TTRPG."

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
    name, surname = random.choice(names_and_surnames[race])
    
    npc = {
        "Name": name,
        "Surname": surname,
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
    name, surname = random.choice(names_and_surnames[race])
    npc = {
        "Name": name,
        "Surname": surname,
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
    display_npc_in_main_tab(npc)  # Display NPC in the main tab

def generate_random_npc_and_display():
    npc = generate_random_npc()
    display_npc(npc)
    display_npc_in_main_tab(npc)  # Display NPC in the main tab

def display_npc_in_main_tab(npc):
    npc_display_main_tab.delete("1.0", tk.END)
    for key, value in npc.items():
        if value:
            npc_display_main_tab.insert(tk.END, f"{key}: {value}\n")

def display_npc(npc):
    npc_display_npc_tab.delete("1.0", "end")
    for key, value in npc.items():
        npc_display_npc_tab.insert("end", f"{key}: {value}\n")

def display_npc_in_npc_tab(npc_data):
    npc_display_npc_tab.delete("1.0", "end")
    for key, value in npc_data.items():
        npc_display_npc_tab.insert("end", f"{key}: {value}\n")

def display_npc(npc_data):
    npc_display_npc_tab.delete("1.0", "end")
    for key, value in npc_data.items():
        npc_display_npc_tab.insert("end", f"{key}: {value}\n")
            
# Create a function to place NPC buttons in rows
def place_npc_buttons():
   npc_buttons = npcs_frame.winfo_children()
   row = 0
   col = 0
   for button in npc_buttons:
       button.grid(row=row, column=col, padx=5, pady=5)
       col += 1
       if col >= 4:
           col = 0
           row += 1

def save_npc():
    npc_text = npc_display_main_tab.get("1.0", "end-1c")
    if npc_text.strip():
        npc_data = {}
        for line in npc_text.split("\n"):
            if ": " in line:
                key, value = line.split(": ", 1)
                npc_data[key] = value
        npc_name = f"{npc_data['Name']} {npc_data['Surname']}"
        npc_button = ttk.Button(npcs_frame, text=npc_name, command=lambda: display_npc(npc_data))
        npc_button.grid(padx=5, pady=5)
        place_npc_buttons()
        display_saved_npc(npc_text)
    else:
        messagebox.showerror("Error", "No NPC to save.")

def display_saved_npc(npc_text):
    npc_display_npc_tab.delete("1.0", tk.END)
    npc_display_npc_tab.insert(tk.END, npc_text)

def save_details():
    details = {
        "genders": genders,
        "races": races,
        "regions": regions,
        "cities": cities,
        "descriptions": descriptions,
        "quirks": quirks,
        "phrases": phrases,
        "quests": quests,
        "relationships": relationships,
        "enemies": enemies,
        "names_and_surnames": names_and_surnames
    }
    file_path = filedialog.asksaveasfilename(defaultextension=".json")
    if file_path:
        with open(file_path, "w") as file:
            json.dump(details, file, indent=4)

def load_details():
    global genders, races, regions, cities, descriptions, quirks, phrases, quests, relationships, enemies, names_and_surnames
    file_path = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
    if file_path:
        with open(file_path, "r") as file:
            details = json.load(file)
            genders = details["genders"]
            races = details["races"]
            regions = details["regions"]
            cities = details["cities"]
            descriptions = details["descriptions"]
            quirks = details["quirks"]
            phrases = details["phrases"]
            quests = details["quests"]
            relationships = details["relationships"]
            enemies = details["enemies"]
            names_and_surnames = details["names_and_surnames"]

def save_api_key():
    global api_key
    api_key =api_key_entry.get()
    messagebox.showinfo("API Key", "API key saved.")

# GUI setup
root = tk.Tk()
root.title("NPC Generator")

# Create a notebook for tabs
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# Create the main tab
main_tab = ttk.Frame(notebook)
notebook.add(main_tab, text="NPC Generator")

# Gender selection
gender_label = ttk.Label(main_tab, text="Select a gender:")
gender_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(main_tab, textvariable=gender_var, values=genders, state="readonly")
gender_combobox.grid(row=0, column=1, padx=5, pady=5)

# Race selection
race_label = ttk.Label(main_tab, text="Select a race:")
race_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
race_var = tk.StringVar()
race_combobox = ttk.Combobox(main_tab, textvariable=race_var, values=races, state="readonly")
race_combobox.grid(row=1, column=1, padx=5, pady=5)

# Region selection
region_label = ttk.Label(main_tab, text="Select a region:")
region_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
region_var = tk.StringVar()
region_combobox = ttk.Combobox(main_tab, textvariable=region_var, values=regions, state="readonly")
region_combobox.grid(row=2, column=1, padx=5, pady=5)

# City selection
city_label = ttk.Label(main_tab, text="Select a city:")
city_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
city_var = tk.StringVar()
city_combobox = ttk.Combobox(main_tab, textvariable=city_var, values=[], state="readonly")
city_combobox.grid(row=3, column=1, padx=5, pady=5)

def update_cities(*args):
   selected_region = region_var.get()
   city_combobox["values"] = cities.get(selected_region, [])

region_var.trace("w", update_cities)

# Generate NPC button
generate_button = ttk.Button(main_tab, text="Generate NPC", command=generate_npc_and_display)
generate_button.grid(row=4, column=0, padx=5, pady=5)

# Generate Random NPC button
random_npc_button = ttk.Button(main_tab, text="Generate Random NPC", command=generate_random_npc_and_display)
random_npc_button.grid(row=4, column=1, padx=5, pady=5)

# NPC display area in the main tab
npc_display_main_tab = tk.Text(main_tab, width=50, height=10)
npc_display_main_tab.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

# Save NPC button
save_button = ttk.Button(main_tab, text="Save NPC", command=save_npc)
save_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

# Create the NPCs tab
npcs_tab = ttk.Frame(notebook)
notebook.add(npcs_tab, text="NPCs")

# Create a frame for saved NPCs
npcs_frame = ttk.Frame(npcs_tab)
npcs_frame.pack(fill="both", expand=True, padx=10, pady=10)

# NPC display area
npc_display_npc_tab = tk.Text(npcs_tab, width=50, height=10)
npc_display_npc_tab.pack(padx=10, pady=10)

# Create the API tab
api_tab = ttk.Frame(notebook)
notebook.add(api_tab, text="API")

# API key entry
api_key_label = ttk.Label(api_tab, text="Enter API Key:")
api_key_label.pack(pady=5)
api_key_entry = ttk.Entry(api_tab)
api_key_entry.pack(pady=5)

# Save API key button
save_api_key_button = ttk.Button(api_tab, text="Save API Key", command=save_api_key)
save_api_key_button.pack(pady=10)

root.mainloop()
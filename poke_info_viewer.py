""" 
Description: 
  Graphical user interface that displays select information about a 
  user-specified Pokemon fetched from the PokeAPI 

Usage:
  python poke_info_viewer.py
"""
from tkinter import Tk, ttk
from poke_api import get_pokemon_info
from tkinter import messagebox


# Create the main window
root = Tk()
root.title("Pokemon Information")

# TODO: 
input = ttk.Frame(root)
input.grid(row= 0, column=0, columnspan=2, pady=(10,5))

info = ttk.LabelFrame(root, text="info")
info.grid(row= 1, column=0,sticky="N", padx=10, pady=(5,10))

stats = ttk.LabelFrame(root, text="stats")
stats.grid(row= 1, column=1, sticky="N", padx=10, pady=(5,10))

# TODO: Populate the user input frame with widgets
input_lbl = ttk.Label(input, text="pokemon Name:")
input_lbl.grid(row=0, column=0)

input_ent =ttk.Entry(input)
input_ent.grid(row=0, column=1)


def get_info():
    poke_name = input_ent.get().strip()
    if not poke_name:
        return
    
    poke_info = get_pokemon_info(poke_name)
    if poke_info:
        height_val["text"] = poke_info["height"]
        Weight_val["text"] = poke_info["weight"]
        #Type_val["text"] = poke_info["types"]

        hp_bar["value"] = poke_info["stats"][0]["base_stat"]
        att_bar["value"] = poke_info["stats"][1]["base_stat"]
        def_bar["value"] = poke_info["stats"][2]["base_stat"]
        Special_attack_bar["value"] = poke_info["stats"][3]["base_stat"]
        Special_defense_bar["value"] = poke_info["stats"][4]["base_stat"]
        speed_bar["value"] = poke_info["stats"][5]["base_stat"]
    else:
        messagebox.showerror("Error", "Invalid Pokemon name entered")
        pass
    return



input_btn = ttk.Button(input, text="Get info", command=get_info)
input_btn.grid(row=0, column=2)

height_lbl =ttk.Label(info, text="Height:")
Weight_lbl =ttk.Label(info, text="Weight:")
Type_lbl =ttk.Label(info, text="Type:")

height_lbl.grid(row=0, column=0, sticky="E", padx=(10,5), pady=(10,5))
Weight_lbl.grid(row=1, column=0, sticky="E", padx=(10,5), pady=(10,5))
Type_lbl.grid(row=2, column=0, sticky="E", padx=(10,5), pady=(10,5))

height_val = ttk.Label(info, width=20)
Weight_val = ttk.Label(info, width=20)
Type_val = ttk.Label(info, width=20)

height_val.grid(row=0, column=1,sticky="W",padx=(5,10), pady=(5,10))
Weight_val.grid(row=1, column=1, sticky="W",padx=(5,10), pady=(5,10))
Type_val.grid(row=2, column=1, sticky="W",padx=(5,10), pady=(5,10))


hp_lbl = ttk.Label(stats, text="Hp:")
attack_lbl = ttk.Label(stats, text="Attack:")
defense_lbl = ttk.Label(stats, text="Defense:")
Special_attack_lbl = ttk.Label(stats, text="Special Attack:")
Special_defense_lbl = ttk.Label(stats, text="Special Defense:")
speed_lbl = ttk.Label(stats, text="Speed:")

hp_lbl.grid(row=0, column=0,sticky="E",padx=(10,10), pady=(5,10))
attack_lbl.grid(row=1, column=0,sticky="E",padx=(10,5), pady=(5,10))
defense_lbl.grid(row=2, column=0,sticky="E",padx=(10,5), pady=(5,10))
Special_attack_lbl.grid(row=3, column=0,sticky="E",padx=(10,5), pady=(5,10)) 
Special_defense_lbl.grid(row=4, column=0,sticky="E",padx=(10,5), pady=(5,10)) 
speed_lbl.grid(row=5, column=0,sticky="E",padx=(10,5), pady=(5,10))


MAX_STAT=255
Bar_LENGTH = 100
hp_bar = ttk.Progressbar(stats, maximum=MAX_STAT, length= Bar_LENGTH)
att_bar = ttk.Progressbar(stats, maximum=MAX_STAT, length= Bar_LENGTH)
def_bar = ttk.Progressbar(stats, maximum=MAX_STAT, length= Bar_LENGTH)
Special_attack_bar = ttk.Progressbar(stats, maximum=MAX_STAT, length= Bar_LENGTH)
Special_defense_bar = ttk.Progressbar(stats, maximum=MAX_STAT, length= Bar_LENGTH)
speed_bar = ttk.Progressbar(stats, maximum=MAX_STAT, length= Bar_LENGTH)

hp_bar.grid(row=0, column=1,padx=(5,10), pady=(10,5))
att_bar.grid(row=1, column=1,padx=(5,10), pady=(5))
def_bar.grid(row=2, column=1,padx=(5,10), pady=(10,5))
Special_attack_bar.grid(row=3, column=1,padx=(5,10), pady=(10,5))
Special_defense_bar.grid(row=4, column=1,padx=(5,10), pady=(10,5))
speed_bar.grid(row=5, column=1,padx=(5,10), pady=(10,5))


root.mainloop()
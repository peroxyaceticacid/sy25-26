import tkinter as tk
import json
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import requests
from io import BytesIO


def safe_int(var):
    try:
        return int(var.get())
    except (ValueError, TypeError):
        return 0

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # load json
        with open("stuff.json", "r") as f:
            self.stuff = json.load(f)
            self.talents_data = self.stuff["talents"][0]
            self.mantras_data = self.stuff["mantras"][0]

        # character data
        self.character = {
            "stats": {
                "strength": 0,
                "fortitude": 0,
                "agility": 0,
                "intelligence": 0,
                "charisma": 0,
                "willpower": 0
            },
            "talents": [],
            "mantras": [],
            "oath": "",
            "attunement": "",
            "armor": ""
        }

        self.MAX_POINTS = 330

        self.title("Deepwoken Builder")
        self.geometry("1100x650")

        # variables for UI
        self.attunement_var = tk.StringVar()
        self.oath_var = tk.StringVar()
        self.armor_var = tk.StringVar()

        self.attunement_var.trace_add("write", self.update_attunement)
        self.oath_var.trace_add("write", self.update_oath)
        self.armor_var.trace_add("write", self.update_armor)

        # top frame
        top_frame = ttk.Frame(self)
        top_frame.grid(row=0, column=0, columnspan=4, pady=10)

        ttk.Label(top_frame, text="Attunement").grid(row=0, column=0, padx=10)
        self.attune_menu = ttk.Combobox(
            top_frame,
            textvariable=self.attunement_var,
            values=self.stuff["attunements"],
            state="readonly"
        )
        self.attune_menu.grid(row=1, column=0)

        ttk.Label(top_frame, text="Oath").grid(row=0, column=1, padx=10)
        self.oath_menu = ttk.Combobox(
            top_frame,
            textvariable=self.oath_var,
            values=self.stuff["oaths"],
            state="readonly"
        )
        self.oath_menu.grid(row=1, column=1)

        ttk.Label(top_frame, text="Armor").grid(row=0, column=2, padx=10)
        self.armor_menu = ttk.Combobox(
            top_frame,
            textvariable=self.armor_var,
            values=self.stuff["armor"],
            state="readonly"
        )
        self.armor_menu.grid(row=1, column=2)

        btn_frame = ttk.Frame(top_frame)
        btn_frame.grid(row=2, column=0, columnspan=4, pady=10)

        save_btn = ttk.Button(btn_frame, text="Save Build", command=self.save_build)
        save_btn.pack(side="left", padx=5)

        load_btn = ttk.Button(btn_frame, text="Load Build", command=self.load_build)
        load_btn.pack(side="left", padx=5)

        # main content frames
        stats_frame = ttk.LabelFrame(self, text="Stats")
        stats_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)

        talent_frame = ttk.LabelFrame(self, text="Talents")
        talent_frame.grid(row=1, column=1, sticky="nsew", padx=10, pady=5)

        mantra_frame = ttk.LabelFrame(self, text="Mantras")
        mantra_frame.grid(row=1, column=2, sticky="nsew", padx=10, pady=5)

        info_frame = ttk.LabelFrame(self, text="Build Data")
        info_frame.grid(row=1, column=3, sticky="nsew", padx=10, pady=5)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_columnconfigure(2, weight=2)
        self.grid_columnconfigure(3, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # stats
        self.stat_vars = {}

        for stat in self.character["stats"]:

            row = ttk.Frame(stats_frame)
            row.pack(fill="x", pady=3)

            ttk.Label(
                row,
                text=stat.capitalize(),
                width=12
            ).pack(side="left")

            var = tk.StringVar(value="0")

            spin = ttk.Spinbox(
                row,
                from_=0,
                to=100,
                textvariable=var,
                width=5
            )
            spin.pack(side="right")

            var.trace_add("write", self.update_stats)

            self.stat_vars[stat] = var

        self.points_label = ttk.Label(stats_frame, text="Total: 0 / 330")
        self.points_label.pack(pady=10)

        # talents
        self.talent_vars = {}

        for talent, desc in self.talents_data.items():

            var = tk.BooleanVar()

            cb = ttk.Checkbutton(
                talent_frame,
                text=talent,
                variable=var,
                command=self.update_talents
            )
            cb.pack(anchor="w")

            ttk.Label(
                talent_frame,
                text=desc,
                wraplength=250,
                foreground="gray"
            ).pack(anchor="w", padx=20, pady=(0, 5))

            self.talent_vars[talent] = var

        # mantras
        self.mantra_vars = {}

        for mantra, gif in self.mantras_data.items():

            row = ttk.Frame(mantra_frame)
            row.pack(anchor="w", pady=5)

            var = tk.BooleanVar()

            cb = ttk.Checkbutton(
                row,
                text=mantra,
                variable=var,
                command=self.update_mantras
            )
            cb.pack(side="left")

            self.load_gif_from_url(gif, row)

            self.mantra_vars[mantra] = var

        # info
        self.info_box = tk.Text(info_frame, wrap="word")
        self.info_box.pack(fill="both", expand=True)

        self.update_info()

    # stat update logic
    def update_stats(self, *args):
        total = sum(safe_int(var) for var in self.stat_vars.values())

        if total > self.MAX_POINTS:
            overflow = total - self.MAX_POINTS
            for stat, var in self.stat_vars.items():
                if safe_int(var) >= overflow:
                    var.set(safe_int(var) - overflow)
                    break

        for stat, var in self.stat_vars.items():
            self.character["stats"][stat] = safe_int(var)

        total = sum(self.character["stats"].values())
        self.points_label.config(text=f"Total: {total} / {self.MAX_POINTS}")

        self.update_info()

    # variable updates
    def update_attunement(self, *args):
        self.character["attunement"] = self.attunement_var.get()
        self.update_info()

    def update_oath(self, *args):
        self.character["oath"] = self.oath_var.get()
        self.update_info()

    def update_armor(self, *args):
        self.character["armor"] = self.armor_var.get()
        self.update_info()

    def update_talents(self):
        self.character["talents"] = [
            name for name, var in self.talent_vars.items() if var.get()
        ]
        self.update_info()

    def update_mantras(self):
        self.character["mantras"] = [
            name for name, var in self.mantra_vars.items() if var.get()
        ]
        self.update_info()

    # display
    def update_info(self):
        self.info_box.delete("1.0", tk.END)
        self.info_box.insert(tk.END, json.dumps(self.character, indent=2))

    def load_gif_from_url(self, url, parent):
        response = requests.get(url)
        gif_data = BytesIO(response.content)

        img = Image.open(gif_data)

        frames = []
        try:
            while True:
                frame = img.copy()
                frame = frame.resize((70, 70))
                frame = ImageTk.PhotoImage(frame)
                frames.append(frame)
                img.seek(len(frames))
        except EOFError:
            pass

        label = ttk.Label(parent)
        label.pack(anchor="w", padx=10)

        def animate(i=0):
            label.configure(image=frames[i])
            self.after(40, animate, (i + 1) % len(frames))

        animate()

        label.frames = frames

    # saving and loading
    def save_build(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON Files", "*.json")],
            title="Save Build As"
        )
        if file_path:
            with open(file_path, "w") as f:
                json.dump(self.character, f, indent=2)

    def load_build(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("JSON Files", "*.json")],
            title="Load Build"
        )
        if file_path:
            with open(file_path, "r") as f:
                data = json.load(f)

            self.character = data
            for stat, var in self.stat_vars.items():
                var.set(data["stats"].get(stat, 0))

            for talent, var in self.talent_vars.items():
                var.set(talent in data.get("talents", []))

            for mantra, var in self.mantra_vars.items():
                var.set(mantra in data.get("mantras", []))

            self.attunement_var.set(data.get("attunement", ""))
            self.oath_var.set(data.get("oath", ""))
            self.armor_var.set(data.get("armor", ""))

            self.update_info()
            self.update_stats()


if __name__ == "__main__":
    app = App()
    app.mainloop()
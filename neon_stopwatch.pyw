import customtkinter as ctk
import tkinter as tk
from tkinter import ttk

running = False
counter = 0  
laps = []

def update_time():
    global counter
    if running:
        counter += 10
        minutes = (counter // 1000) // 60
        seconds = (counter // 1000) % 60
        millis = (counter % 1000) // 10
        time_str = f"{minutes:02}:{seconds:02}:{millis:02}"
        time_label.configure(text=time_str)
        root.after(10, update_time)

def start():
    global running
    if not running:
        running = True
        update_time()

def stop():
    global running
    running = False

def reset():
    global counter, running, laps
    running = False
    counter = 0
    laps.clear()
    time_label.configure(text="00:00:00")
    for i in laps_tree.get_children():
        laps_tree.delete(i)

def lap():
    if running:
        minutes = (counter // 1000) // 60
        seconds = (counter // 1000) % 60
        millis = (counter % 1000) // 10
        lap_time = f"{minutes:02}:{seconds:02}:{millis:02}"
        laps.append(lap_time)
        laps_tree.insert("", "end", values=(len(laps), lap_time))

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.title("⏱️ Neon Stopwatch")
root.geometry("370x520")
root.resizable(False, False)

neon_green = "#00FFC6"
neon_red = "#FF4E4E"
neon_blue = "#7FB3FF"
neon_orange = "#FFC857"
bg_color = "#0D0D1A"

root.configure(fg_color=bg_color)

time_label = ctk.CTkLabel(
    root,
    text="00:00:00",
    font=("Consolas", 50, "bold"),
    text_color=neon_green
)
time_label.pack(pady=30)

def create_glow_button(parent, text, color, hover, border, cmd):
    return ctk.CTkButton(
        parent,
        text=text,
        width=90,
        height=45,
        corner_radius=25,
        fg_color=color,
        hover_color=hover,
        border_width=3,
        border_color=border,
        text_color="black",
        font=("Segoe UI", 12, "bold"),
        command=cmd
    )

button_frame = ctk.CTkFrame(root, fg_color="transparent")
button_frame.pack(pady=15)

start_btn = create_glow_button(button_frame, "START", "#00C896", neon_green, neon_green, start)
start_btn.grid(row=0, column=0, padx=8)

stop_btn = create_glow_button(button_frame, "STOP", "#E63946", neon_red, neon_red, stop)
stop_btn.grid(row=0, column=1, padx=8)

reset_btn = create_glow_button(button_frame, "RESET", "#3B3B98", neon_blue, neon_blue, reset)
reset_btn.grid(row=0, column=2, padx=8)

lap_btn = create_glow_button(root, "LAP", neon_orange, "#FFD166", neon_orange, lap)
lap_btn.configure(width=280)
lap_btn.pack(pady=10)

lap_frame = ctk.CTkFrame(root, fg_color=bg_color)
lap_frame.pack(pady=10, fill="both", expand=True)

columns = ("#1", "#2")
laps_tree = ttk.Treeview(lap_frame, columns=columns, show="headings", height=10)
laps_tree.heading("#1", text="Lap")
laps_tree.heading("#2", text="Time")
laps_tree.column("#1", width=70, anchor="center")
laps_tree.column("#2", width=200, anchor="center")

scrollbar = ttk.Scrollbar(lap_frame, orient="vertical", command=laps_tree.yview)
laps_tree.configure(yscroll=scrollbar.set)
scrollbar.pack(side="right", fill="y")
laps_tree.pack(side="left", fill="both", expand=True)

style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview",
                background="#141429",
                foreground="white",
                rowheight=30,
                fieldbackground="#141429",
                font=("Segoe UI", 10))
style.configure("Treeview.Heading",
                background=neon_green,
                foreground="black",
                font=("Segoe UI", 10, "bold"))
style.map('Treeview', background=[('selected', '#00C896')])

glow_border = ctk.CTkFrame(root, fg_color=neon_green, corner_radius=20)

root.mainloop()

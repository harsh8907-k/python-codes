
import tkinter as tk
import tkinter.font as tkfont
import random
import math

# ------------ SETTINGS ------------
BG = "#050505"
COLORS = ["#ff514f", "#ff625c", "#ff7669"]
FONT_SIZE = 10
WORD_DELAY = 45       # Delay between phrases (ms)
PAUSE_AT_END = 4000

WORDS = [
    "I love you", "maru chu chu", "mari dai dai diki",
    "umma umaaa", "pinuduuu", "happy 6 months",
    "Seni seviyorum", "Aku cinta kamu",
    "Anh yêu em", "Kocham cię", "Ik hou van jou",
    "Jag älskar dig", "Я тебя люблю", "Σ' αγαπώ",
    "愛してる", "사랑해"
]

root = tk.Tk()
root.title("Love Heart")
root.geometry("1000x850")
root.configure(bg=BG)

canvas = tk.Canvas(root, bg=BG, highlightthickness=0)
canvas.pack(fill="both", expand=True)

font = tkfont.Font(
    family="Arial", size=FONT_SIZE, weight="bold"
)

items = []
job = None
restart_job = None


def heart_value(x, y):
    return (x*x + y*y - 1)**3 - x*x*y**3


def build_heart():
    global items, job, restart_job

    if job is not None:
        root.after_cancel(job)
        job = None

    if restart_job is not None:
        root.after_cancel(restart_job)
        restart_job = None

    canvas.delete("all")
    items = []
    root.update_idletasks()

    w = canvas.winfo_width()
    h = canvas.winfo_height()

    cx = w / 2
    cy = h / 2 + 5

    sx = min(w * 0.37, 370)
    sy = min(h * 0.36, 300)

    # Each row is sampled directly from the heart equation.
    y = 1.12
    row_step = 0.065

    while y >= -1.12:
        xs = [
            x / 200
            for x in range(-240, 241)
            if heart_value(x / 200, y) <= 0
        ]

        if xs:
            left = min(xs)
            right = max(xs)
            row_width = (right - left) * sx

            # Leave narrow rows empty rather than distorting the heart.
            if row_width >= font.measure("Te amo") + 8:
                phrases = []
                total_width = 0

                # Fill each row using measured text widths.
                while True:
                    phrase = random.choice(WORDS)
                    phrase_width = font.measure(phrase) + 12

                    if total_width + phrase_width > row_width:
                        break

                    phrases.append((phrase, phrase_width))
                    total_width += phrase_width

                # Center the complete row.
                x_pos = cx - total_width / 2
                py = cy - y * sy

                for phrase, phrase_width in phrases:
                    px = x_pos + phrase_width / 2

                    item = canvas.create_text(
                        px, py,
                        text=phrase,
                        font=font,
                        fill=BG
                    )

                    items.append(
                        (item, random.choice(COLORS))
                    )
                    x_pos += phrase_width

        y -= row_step

    # Animate in row order, from top to bottom.
    reveal(0)


def reveal(i):
    global job, restart_job

    if i >= len(items):
        job = None
        restart_job = root.after(PAUSE_AT_END, build_heart)
        return

    item, color = items[i]
    canvas.itemconfig(item, fill=color)

    job = root.after(WORD_DELAY, reveal, i + 1)


root.after(250, build_heart)
root.mainloop()

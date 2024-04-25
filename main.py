from datetime import datetime as dt
from functools import cache
from PIL import ImageGrab
import tkinter as tk
from tkinter import font
import os
import pyglet


def main() -> None:
  global pos, count
  root = tk.Tk()
  root.title("TTPD TypeWritter")
  root.attributes('-fullscreen', True)

  background_label = tk.Label(
                              root,
                              image=get_image("document_background")
  )
  background_label.pack(expand=True, fill='both')

  pos = (0, 0)
  count = 1

  root.bind_all('<Key>', lambda e: key_pressed(e, background_label))


  root.mainloop()

@cache
def get_image(image_name: str) -> tk.PhotoImage:
  if image_name == "document_background":
    return tk.PhotoImage(file="./Hidden/Images/document_background.png/")
    
  if image_name == "page_background":
    return tk.PhotoImage(file="./Hidden/Images/page_background.png/")

  try:
    return tk.PhotoImage(file=f"./Hidden/Images/Characters/{image_name}.png")
  except fileNotFoundError:
    return None



def take_screenshot(root: tk.Tk) -> int | None:
  global count
  
  x0 = root.winfo_rootx()
  y0 = root.winfo_rooty()
  x1 = x0 + root.winfo_width()
  y1 = y0 + root.winfo_height()

  current_time = dt.now().strftime("%d-%m-%Y %H")
  fp = f"./Files/{current_time}"
  try:
    os.mkdir(fp)
  except: pass
  
  try:
    last = sorted(os.listdir(fp))[-1]
    last_count = int(last.replace('.png', '').strip()[-1])
    if last_count >= count:
      count = last_count + 1
  except:
    pass
  
  ImageGrab.grab().crop((x0, y0, x1, y1)).save(f"{fp}/Page {count}.png")
    
  count + 1

def key_pressed(event, parent):
  global pos
  key = event.keysym
  row, col = pos
  row = 0 if row < 0 else row
  col = 0 if col < 0 else col


  if col > 50:
    return

  if key == 'space':
    img = get_image(f'space')
    label = tk.Label(parent, image=img)
    label.grid(row=row, column=col)
    label.img = img
    pos = (row, col+1)
    return

  if key == 'Return':
    pos = (row+1, 0)
    img = get_image(f'space')
    label = tk.Label(parent, image=img)
    label.grid(row=row+1, column=0)
    label.img = img
    return

  if key == 'BackSpace':
    pos = (row, col-1)
    return

  if key == 'Control_R':
    take_screenshot(parent)

  try:
    img = get_image(f'{key}')
    label = tk.Label(parent, image=img)
    label.grid(row=row, column=col)
    label.img = img
    pos = (row, col+1)
    return

  except Exception as e:
    return


if __name__ == '__main__':
  main()
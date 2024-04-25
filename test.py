from PIL import Image
import os

def compress(image_name: str, width: int, height: int, new_name):
    img = Image.open(image_name)
    
    if width and height:
            # if width and height are set, resize with them instead
            img = img.resize((width, height))
            # split the filename and extension
            filename, ext = os.path.splitext(image_name)
            # make new filename appending _compressed to the original file name
            new_filename = filename + ext
            try:
                # save the image with the corresponding quality and optimize set to True
                img.save(new_name, quality=25, optimize=True)
                print(f"Done {image_name}")
            except Exception as e:
                print(f"Error on {image_name}")
                print(str(e))

fp = './'
for file in sorted(os.listdir(fp)):
    if not file.startswith("A"): continue
    print(file)
    print("edit (y) or skip (n)")
    if input().lower() == 'y':
        new_name = input('New name: ').strip() + '.png'
        compress(fp+file, 20, 40, new_name)
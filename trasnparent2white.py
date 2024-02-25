from PIL import Image
import os

def convert_background_to_white(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".png"):  # or ".tiff", ".bmp" or other file formats that support transparency
            file_path = os.path.join(directory, filename)
            image = Image.open(file_path)
            if image.mode in ('RGBA', 'LA') or (image.mode == 'P' and 'transparency' in image.info):
                # Create a white background
                white_bg = Image.new("RGBA", image.size, "WHITE")
                # Paste the image on the white background
                white_bg.paste(image, (0, 0), image)
                # Save the image
                white_bg.convert('RGB').save(file_path.replace(".png", "_white_bg.png"), "PNG")
                print(f"Processed {filename}")
            else:
                print(f"{filename} does not have a transparent background or is not in a supported format.")

directory = r"your directory"
convert_background_to_white(directory)


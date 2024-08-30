import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageSequence
from moviepy.editor import ImageSequenceClip
import os

class GIFCreatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GIF Creator")

        # Set window size
        self.root.geometry("400x200")

        # Label and Button for selecting folder
        self.label = tk.Label(root, text="Select Folder Containing Images to Create GIF")
        self.label.pack(pady=10)

        self.select_button = tk.Button(root, text="Select Folder", command=self.select_folder)
        self.select_button.pack(pady=5)

        # Button to create GIF
        self.create_button = tk.Button(root, text="Create GIF", command=self.create_gif)
        self.create_button.pack(pady=20)

        # Initialize folder path
        self.folder_path = ""

    def select_folder(self):
        # Open folder dialog to select the folder
        self.folder_path = filedialog.askdirectory(
            title="Select Folder"
        )
        if self.folder_path:
            messagebox.showinfo("Selected Folder", f"Selected folder: {self.folder_path}")

    def create_gif(self):
        if not self.folder_path:
            messagebox.showwarning("No Folder Selected", "Please select a folder first.")
            return

        # Load images from the selected folder
        self.image_files = [os.path.join(self.folder_path, f) for f in os.listdir(self.folder_path) 
                            if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]

        if not self.image_files:
            messagebox.showwarning("No Images Found", "No images found in the selected folder.")
            return

        # Resize images to the same dimensions
        resized_images = []
        for image_file in self.image_files:
            img = Image.open(image_file)
            img = img.resize((500, 500))  # Resize to a fixed size, you can adjust this size
            resized_images.append(img)

        # Save resized images to temporary files
        temp_files = []
        for i, img in enumerate(resized_images):
            temp_file = os.path.join(self.folder_path, f"temp_image_{i}.png")
            img.save(temp_file)
            temp_files.append(temp_file)

        # Ask user where to save the GIF
        save_path = filedialog.asksaveasfilename(
            defaultextension=".gif",
            filetypes=[("GIF files", "*.gif")],
            title="Save GIF As"
        )

        if save_path:
            # Create GIF using MoviePy
            clip = ImageSequenceClip(temp_files, fps=2)  # Change fps to control GIF speed
            clip.write_gif(save_path)
            messagebox.showinfo("Success", f"GIF saved successfully at {save_path}")

            # Cleanup temporary files
            for temp_file in temp_files:
                os.remove(temp_file)

if __name__ == "__main__":
    root = tk.Tk()
    app = GIFCreatorApp(root)
    root.mainloop()

# Image Info Viewer

This application is a simple image information viewer built using Python's Tkinter library and the Pillow library. It allows users to select a folder, scan for images, and display information about each image in a tree view. Users can also view images directly.

## Features

- Select a folder to scan for images.
- Display image information such as name, size, resolution, color depth, and compression type.
- View images in the default image viewer.

## Requirements

- Python 3.x
- Tkinter (usually included with Python installations)
- Pillow library for image handling

You can install Pillow using pip:

```bash
pip install Pillow
```

## How to Use

1. **Choose Folder**: Click the "Choose Folder" button to select a folder containing images.
2. **Scan Images**: The application will automatically scan the selected folder for supported image formats (JPG, GIF, TIF, BMP, PNG, PCX).
3. **View Image Info**: The application will display the image name, size, resolution, color depth, and compression type in a tree view.
4. **Show Image**: Click on any image entry in the tree view to open the image in your default image viewer.

## User Interface

The interface consists of:

- **Folder Selection**: An entry field and button to select the folder.
- **Image Information Table**: A tree view displaying details of the scanned images.
- **Scrollbar**: Allows scrolling through the list of images if it exceeds the window size.

## Example

1. Click "Choose Folder" and select a folder with images.
2. The application will list all images found in the folder along with their details.
3. Click on an image name to open it in your default viewer.

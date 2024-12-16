# Digital Image Processing Application

This is a simple GUI application for digital image processing using Python's Tkinter, OpenCV, and PIL (Pillow). The application provides various image manipulation features such as sharpening and thresholding.

## Features

- **Load Image**: Browse and load an image from your file system.
- **Original Image**: Display the original image.
- **Sharpening Filter**: Apply a sharpening filter to enhance image details.
- **Global Thresholding**: Apply two types of global thresholding:
  - Thresholding with binary conversion.
  - Thresholding with truncation.
- **Adaptive Thresholding**: Apply two types of adaptive thresholding:
  - Adaptive mean thresholding.
  - Adaptive Gaussian thresholding.

## Requirements

Make sure you have the following libraries installed:

- Python 3.x
- OpenCV
- Pillow
- NumPy
- Tkinter (usually comes with Python)

You can install the required libraries using pip:

```bash
pip install opencv-python pillow numpy
```

## Usage

1. **Clone the repository** or download the script.
2. Run the script using Python:

   ```bash
   python image_processing_app.py
   ```

3. Click on the **"Browse"** button to select an image.
4. Use the buttons to apply various image processing techniques.

## Example

1. Load an image using the "Browse" button.
2. Click "Original" to display the image.
3. Apply sharpening by clicking "Sharpening filter".
4. Experiment with global and adaptive thresholding options.

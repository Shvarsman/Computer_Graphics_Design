# 3D Model of the Letter "Ш"

This project is a Python application that visualizes a 3D model of the letter "Ш" using `Tkinter`, `Matplotlib`, and `NumPy`. The application allows users to manipulate the model through scaling and translation, as well as view projections onto different planes.

## Features

- **3D Visualization**: Display a 3D representation of the letter "Ш".
- **Transformations**: Scale and translate the model using sliders.
- **Projections**: View projections of the model onto the Oxy, Oxz, and Oyz planes.

## Requirements

- Python 3.x
- `tkinter`
- `matplotlib`
- `numpy`

You can install the required packages via pip:

```bash
pip install matplotlib numpy
```

## Usage

1. Clone the repository or download the source code.
2. Run the application using:

   ```bash
   python your_script_name.py
   ```

3. The main window will display the 3D model of the letter "Ш".
4. Use the sliders to adjust the scale and translation of the model.
5. Click on the projection buttons to view the 2D projections of the model.

## Code Structure

- **create_letter_sh()**: Generates vertices and faces for the letter "Ш".
- **scale(vertices, sx, sy, sz)**: Scales the given vertices by specified factors.
- **translate(vertices, tx, ty, tz)**: Translates the vertices by specified distances.
- **create_transformation_matrix()**: Creates a transformation matrix for scaling and translation.
- **App**: The main application class that handles the GUI and updates the plot.

## Example

Here's a brief overview of how to scale and translate the model:

- Adjust the **Scale X** slider to change the size of the model.
- Use the **Translate X**, **Translate Y**, and **Translate Z** sliders to move the model in 3D space.
- Click on the projection buttons to view the model from different perspectives.

Raster Graphics Application
This application is a graphical interface for visualizing rasterization algorithms, built using Python's Tkinter library. It allows users to plot points and lines on a grid using various rasterization techniques such as DDA (Digital Differential Analyzer), Bresenham's Line, Bresenham's Circle, and Step-by-Step methods.

Features
Algorithms Supported:

DDA (Digital Differential Analyzer): A simple algorithm for line rasterization.
Bresenham's Line Algorithm: An efficient method for line rasterization.
Bresenham's Circle Algorithm: Used for circle rasterization.
Step-by-Step Algorithm: Calculates line points incrementally based on slope.
Interactive Grid:

A dynamic coordinate grid with customizable scaling.
Displays both positive and negative coordinates.
Real-Time Visualization:

Plots points on the canvas as per the selected algorithm.
Shows execution time for the selected algorithm.
Adjustable Grid Scale:

Change the size of the grid cells interactively.
Installation
Prerequisites:

Python 3.x installed on your system.
The tkinter module (usually included with standard Python installations).
Download or Clone the Repository:

bash
Копировать код
git clone https://github.com/yourusername/raster-graphics-app.git
cd raster-graphics-app
Run the Application:

bash
Копировать код
python raster_graphics.py
Usage
Launch the application.
Use the input fields to define:
Start point (x1, y1).
End point (x2, y2) or radius (for circles).
Select an algorithm from the dropdown menu.
Click "Построить" (Build) to draw.
Adjust the grid scale using the slider at the bottom.
Code Structure
RasterGraphicsApp: Main class for the application.
Grid Functions:
draw_grid(): Renders the coordinate grid.
to_canvas_coordinates(): Converts logical coordinates to canvas coordinates.
draw_pixel(): Draws a pixel on the canvas.
Algorithms:
dda_algorithm(): Implements the DDA line-drawing algorithm.
bresenham_line(): Implements Bresenham's line algorithm.
bresenham_circle(): Implements Bresenham's circle algorithm.
step_by_step(): Implements the step-by-step line-drawing algorithm.
UI Components:
create_interface(): Sets up the user interface.
update_grid_step(): Adjusts the grid scale dynamically.
Performance:
Measures and displays the execution time of each algorithm.
Example
Drawing a Line with Bresenham's Algorithm
Set x1 = 0, y1 = 0 and x2 = 10, y2 = 10.
Select "bresenham_line" from the dropdown.
Click "Построить" to see the line drawn on the grid.
Contribution
Contributions are welcome! Feel free to:

Fork the repository.
Submit pull requests with new features or bug fixes.
Report issues.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements
Tkinter Documentation
Rasterization concepts inspired by computer graphics principles.

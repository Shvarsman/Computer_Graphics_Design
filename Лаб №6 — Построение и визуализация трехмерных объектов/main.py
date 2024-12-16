import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

def create_letter_sh():
    vertices = np.array([
        [0, 0, 0], [0, 0, 5], [0, 1, 5], [0, 1, 0],
        [1, 0, 0], [1, 0, 5], [1, 1, 5], [1, 1, 0],
        [2, 0, 0], [2, 0, 5], [2, 1, 5], [2, 1, 0],
        [3, 0, 0], [3, 0, 5], [3, 1, 5], [3, 1, 0],
        [4, 0, 0], [4, 0, 5], [4, 1, 5], [4, 1, 0],
        [5, 0, 0], [5, 0, 5], [5, 1, 5], [5, 1, 0],
        [0, 1, 0], [5, 1, 0], [0, 1, 1], [5, 1, 1],
        [0, 0, 0], [5, 0, 0], [0, 0, 1], [5, 0, 1],
    ])
    faces = [
        [0, 1, 5, 4], [1, 2, 6, 5], [2, 3, 7, 6], [3, 0, 4, 7],
        [4, 5, 6, 7], [0, 1, 2, 3],
        [8, 9, 13, 12], [9, 10, 14, 13], [10, 11, 15, 14], [11, 8, 12, 15],
        [12, 13, 14, 15], [8, 9, 10, 11],
        [16, 17, 21, 20], [17, 18, 22, 21], [18, 19, 23, 22],
        [19, 16, 20, 23], [20, 21, 22, 23], [16, 17, 18, 19],
        [24, 25, 29, 28], [26, 27, 31, 30], [24, 26, 30, 28],
        [25, 27, 31, 29], [28, 29, 31, 30], [24, 25, 27, 26],
    ]
    return vertices, faces

def scale(vertices, sx, sy, sz):
    scale_matrix = np.diag([sx, sy, sz])
    return np.dot(vertices, scale_matrix)

def translate(vertices, tx, ty, tz):
    return vertices + np.array([tx, ty, tz])

def create_transformation_matrix(sx, sy, sz, tx, ty, tz):
    transformation_matrix = np.array([
        [sx, 0,  0, tx],
        [0, sy,  0, ty],
        [0, 0, sz, tz],
        [0, 0,  0,  1]
    ])
    return transformation_matrix

class App:
    def __init__(self, root):
        self.root = root
        self.root.title('3D Model of the Letter "Ш"')

        self.vertices, self.faces = create_letter_sh()

        self.figure = plt.figure(figsize=(5, 4))
        self.ax = self.figure.add_subplot(111, projection='3d')
        self.canvas_plot = FigureCanvasTkAgg(self.figure, master=root)
        self.canvas_plot_widget = self.canvas_plot.get_tk_widget()
        self.canvas_plot_widget.pack(fill=tk.BOTH, expand=1)

        ttk.Label(root, text="Scale X").pack()
        self.scale_x = ttk.Scale(root, from_=0.5, to=3.0, orient=tk.HORIZONTAL)
        self.scale_x.set(1.0)
        self.scale_x.pack(fill=tk.X)

        ttk.Label(root, text="Translate X").pack()
        self.translate_x = ttk.Scale(root, from_=-10, to=10, orient=tk.HORIZONTAL)
        self.translate_x.set(0)
        self.translate_x.pack(fill=tk.X)

        ttk.Label(root, text="Translate Y").pack()
        self.translate_y = ttk.Scale(root, from_=-10, to=10, orient=tk.HORIZONTAL)
        self.translate_y.set(0)
        self.translate_y.pack(fill=tk.X)

        ttk.Label(root, text="Translate Z").pack()
        self.translate_z = ttk.Scale(root, from_=-10, to=10, orient=tk.HORIZONTAL)
        self.translate_z.set(0)
        self.translate_z.pack(fill=tk.X)

        ttk.Button(root, text="Oxy Projection", command=self.show_oxy_projection).pack(fill=tk.X)
        ttk.Button(root, text="Oxz Projection", command=self.show_oxz_projection).pack(fill=tk.X)
        ttk.Button(root, text="Oyz Projection", command=self.show_oyz_projection).pack(fill=tk.X)

        self.matrix_label = ttk.Label(root, text="Transformation Matrix:\n")
        self.matrix_label.pack()

        self.update_plot()

    def update_plot(self):
        self.ax.clear()

        sx = self.scale_x.get()
        tx = self.translate_x.get()
        ty = self.translate_y.get()
        tz = self.translate_z.get()

        transformed_vertices = scale(self.vertices, sx, sx, sx)
        transformed_vertices = translate(transformed_vertices, tx, ty, tz)

        for face in self.faces:
            face_vertices = [transformed_vertices[idx] for idx in face]
            poly = Poly3DCollection([face_vertices], alpha=0.5, edgecolor='k')
            self.ax.add_collection3d(poly)

        matrix = create_transformation_matrix(sx, sx, sx, tx, ty, tz)
        matrix_text = f"Transformation Matrix:\n{np.array_str(matrix)}"
        self.matrix_label.config(text=matrix_text)

        self.ax.set_xlim([-10, 10])
        self.ax.set_ylim([-10, 10])
        self.ax.set_zlim([-10, 10])

        self.canvas_plot.draw()
        self.root.after(100, self.update_plot)

    def show_oxy_projection(self):
        self.show_projection('Oxy')

    def show_oxz_projection(self):
        self.show_projection('Oxz')

    def show_oyz_projection(self):
        self.show_projection('Oyz')

    def show_projection(self, plane):
        proj_window = tk.Toplevel(self.root)
        proj_window.title(f"{plane} Projection")

        fig = plt.figure(figsize=(5, 4))
        ax_proj = fig.add_subplot(111)

        if plane == 'Oxy':
            proj_vertices = self.vertices[:, :2]
        elif plane == 'Oxz':
            proj_vertices = self.vertices[:, [0, 2]]
        elif plane == 'Oyz':
            proj_vertices = self.vertices[:, 1:]

        ax_proj.scatter(proj_vertices[:, 0], proj_vertices[:, 1], c='b')
        canvas_proj = FigureCanvasTkAgg(fig, master=proj_window)
        canvas_proj_widget = canvas_proj.get_tk_widget()
        canvas_proj_widget.pack(fill=tk.BOTH, expand=1)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

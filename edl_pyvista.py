# PyVista version
import pyvista as pv

mesh = pv.Sphere()

p = pv.Plotter(notebook=False, shape=(1, 2))

p.subplot(0, 0)
p.add_mesh(mesh, color=True)

p.subplot(0, 1)
p.add_mesh(mesh, color=True)

p.enable_eye_dome_lighting()

p.show()

import vtk

# PyVista version
# import pyvista as pv
# sphere = vtk.vtkSphereSource()
# sphere.Update()
# mesh = sphere.GetOutput()
# p = pv.Plotter(shape=(1, 2))
# p.subplot(0, 0)
# p.add_mesh(mesh, color=True)
# p.subplot(0, 1)
# p.add_mesh(mesh, color=True)
# p.enable_eye_dome_lighting((0, 1))
# p.show()

# VTK version
renderer = vtk.vtkRenderer()
renderWindow = vtk.vtkRenderWindow()
renderWindow.AddRenderer(renderer)
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renderWindow)

sphere = vtk.vtkSphereSource()
sphere.Update()
mesh = sphere.GetOutput()

mapper = vtk.vtkPolyDataMapper()
mapper.SetInputData(sphere.GetOutput())

actor = vtk.vtkActor()
actor.SetMapper(mapper)

renderer.AddActor(actor)

basicPasses = vtk.vtkRenderStepsPass()

edl = vtk.vtkEDLShading()
edl.SetDelegatePass(basicPasses)

renderer.SetPass(edl)

renderWindow.Render()
iren.Start()

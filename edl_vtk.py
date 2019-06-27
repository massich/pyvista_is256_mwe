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
renderer1 = vtk.vtkRenderer()
renderer1.SetViewport(0, 0, 200, 200)
renderer2 = vtk.vtkRenderer()
renderer2.SetViewport(200, 0, 400, 400)
renderWindow = vtk.vtkRenderWindow()
renderWindow.SetSize(400, 400)
renderWindow.AddRenderer(renderer1)
renderWindow.AddRenderer(renderer2)
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renderWindow)

sphere = vtk.vtkSphereSource()
sphere.Update()
mesh = sphere.GetOutput()

mapper = vtk.vtkPolyDataMapper()
mapper.SetInputData(sphere.GetOutput())

actor = vtk.vtkActor()
actor.SetMapper(mapper)

renderer1.AddActor(actor)
renderer2.AddActor(actor)

renderer1.ResetCamera()
renderer2.ResetCamera()

basicPasses = vtk.vtkRenderStepsPass()

edl = vtk.vtkEDLShading()
edl.SetDelegatePass(basicPasses)

# renderer1.SetPass(edl)

renderWindow.Render()
iren.Start()

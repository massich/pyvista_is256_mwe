import vtk

# VTK version
renderer1 = vtk.vtkRenderer()
renderer2 = vtk.vtkRenderer()
renderWindow = vtk.vtkRenderWindow()
renderWindow.SetSize(500, 500)
renderWindow.AddRenderer(renderer1)
renderer1.SetViewport(0, 0, 0.5, 1.0)
renderWindow.AddRenderer(renderer2)
renderer2.SetViewport(0.5, 0, 1.0, 1.0)
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
renderer2.SetPass(edl)

renderWindow.Render()
iren.Start()

import vtk

# VTK version
renderWindow = vtk.vtkRenderWindow()
renderWindow.SetSize(500, 500)

iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renderWindow)

sphere = vtk.vtkSphereSource()
sphere.Update()

mapper = vtk.vtkPolyDataMapper()
mapper.SetInputData(sphere.GetOutput())

actor = vtk.vtkActor()
actor.SetMapper(mapper)


def get_cam():
    lights_pass = vtk.vtkLightsPass()
    default_pass = vtk.vtkDefaultPass()

    passes = vtk.vtkRenderPassCollection()
    passes.AddItem(lights_pass)
    passes.AddItem(default_pass)

    seq_pass = vtk.vtkSequencePass()
    seq_pass.SetPasses(passes)

    cameraP = vtk.vtkCameraPass()
    cameraP.SetDelegatePass(seq_pass)
    return cameraP


def get_edl():
    edl = vtk.vtkEDLShading()
    edl.SetDelegatePass(get_cam())
    return edl


renderer1 = vtk.vtkRenderer()
renderer1.SetViewport(0, 0, 0.5, 1.0)
renderer1.SetPass(get_edl())
renderer1.AddActor(actor)
renderer1.ResetCamera()

renderer2 = vtk.vtkRenderer()
renderer2.SetViewport(0.5, 0, 1.0, 1.0)
renderer2.SetPass(get_edl())
renderer2.AddActor(actor)
renderer2.ResetCamera()

renderWindow.AddRenderer(renderer1)
renderWindow.AddRenderer(renderer2)

renderWindow.Render()
iren.Start()

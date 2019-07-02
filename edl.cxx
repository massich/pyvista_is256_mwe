/*=========================================================================

  Program:   Visualization Toolkit

  Copyright (c) Ken Martin, Will Schroeder, Bill Lorensen
  All rights reserved.
  See Copyright.txt or http://www.kitware.com/Copyright.htm for details.

     This software is distributed WITHOUT ANY WARRANTY; without even
     the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
     PURPOSE.  See the above copyright notice for more information.

=========================================================================*/
// test baking shadow maps
//
// The command line arguments are:
// -I        => run in interactive mode; unless this is used, the program will
//              not allow interaction and exit

#include "vtkActor.h"
#include "vtkCamera.h"
#include "vtkCellArray.h"
#include "vtkEDLShading.h"
#include "vtkNew.h"
#include "vtkOpenGLRenderer.h"
#include "vtkSphereSource.h"
#include "vtkPolyDataMapper.h"
#include "vtkProperty.h"
#include "vtkRegressionTestImage.h"
#include "vtkRenderStepsPass.h"
#include "vtkRenderPassCollection.h"
#include "vtkCameraPass.h"
#include "vtkDefaultPass.h"
#include "vtkLightsPass.h"
#include "vtkSequencePass.h"
#include "vtkRenderWindow.h"
#include "vtkRenderWindowInteractor.h"
#include "vtkRenderer.h"
#include "vtkTestUtilities.h"
#include "vtkTimerLog.h"

auto get_cam() -> vtkSmartPointer<vtkCameraPass> {
	auto lights_pass = vtkSmartPointer<vtkLightsPass>::New();
	auto default_pass = vtkSmartPointer<vtkDefaultPass>::New();

	auto passes = vtkSmartPointer<vtkRenderPassCollection>::New();
	passes->AddItem(lights_pass);
	passes->AddItem(default_pass);

	auto seq = vtkSmartPointer<vtkSequencePass>::New();
	seq->SetPasses(passes);

	auto cameraP = vtkSmartPointer<vtkCameraPass>::New();
	cameraP->SetDelegatePass(seq);
	return cameraP;
}

auto get_edl() -> vtkSmartPointer<vtkEDLShading> {
	auto edl = vtkSmartPointer<vtkEDLShading>::New();
	edl->SetDelegatePass(get_cam());
	return edl;
}

int main(int argc, char *argv[])
{
  auto renderWindow = vtkSmartPointer<vtkRenderWindow>::New();
  renderWindow->SetSize(500, 500);

  auto iren = vtkSmartPointer<vtkRenderWindowInteractor>::New();
  iren->SetRenderWindow(renderWindow);

	auto sphere = vtkSmartPointer<vtkSphereSource>::New();
	sphere->Update();

  auto mapper = vtkSmartPointer<vtkPolyDataMapper>::New();
  mapper->SetInputConnection(sphere->GetOutputPort());

  auto actor = vtkSmartPointer<vtkActor>::New();
  actor->SetMapper(mapper);

	auto renderer1 = vtkSmartPointer<vtkRenderer>::New();
	renderer1->SetViewport(0, 0, 0.5, 1.0);
	renderer1->SetPass(get_edl());
	renderer1->AddActor(actor);
	renderer1->ResetCamera();

	auto renderer2 = vtkSmartPointer<vtkRenderer>::New();
	renderer2->SetViewport(0.5, 0, 1.0, 1.0);
	renderer2->SetPass(get_edl());
	renderer2->AddActor(actor);
	renderer2->ResetCamera();

	renderWindow->AddRenderer(renderer1);
	renderWindow->AddRenderer(renderer2);

  renderWindow->Render();
  iren->Start();

  return 0;
}

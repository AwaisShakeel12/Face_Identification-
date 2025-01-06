from django.shortcuts import render
from .forms import DetectionForm
from ultralytics import YOLO
import os
from django.conf import settings

def detect_objects(request):
    if request.method == 'POST':
        form = DetectionForm(request.POST, request.FILES)
        if form.is_valid():
            # Save form data
            detection = form.save(commit=False)
            detection.selected_classes = [int(x) for x in form.cleaned_data['selected_classes']]
            detection.save()

            # Run YOLO detection
            # model = YOLO('yolo11n.pt')
            model = YOLO('personal_yolo.pt')
            model = YOLO('personal_yolo.pt')
            results = model.predict(
                source=detection.image.path,
                # classes=detection.selected_classes,
                conf=0.25,
                save=True  # Make sure saving is enabled
            )

            # Save result image with unique name
            for r in results:
                # Create results directory if it doesn't exist
                results_dir = os.path.join(settings.MEDIA_ROOT, 'results')
                os.makedirs(results_dir, exist_ok=True)
                
                # Save with original filename
                output_filename = f"result_{os.path.basename(detection.image.name)}"
                output_path = os.path.join(results_dir, output_filename)
                
                # Save the results
                r.save(output_path)
                detection.result_image = f'results/{output_filename}'
                detection.save()
                break

            return render(request, 'home2.html', {
                'form': form,
                'detection': detection
            })
    else:
        form = DetectionForm()
    
    return render(request, 'home2.html', {'form': form})

def segmentation_view(request):
    if request.method == 'POST':
        form = DetectionForm(request.POST, request.FILES) 
        if form.is_valid():
            segment = form.save(commit=False)
            segment.selected_classes = [int(x) for x in form.cleaned_data['selected_classes']]
            segment.save()
     
        
            model = YOLO('yolo11n-seg.pt')
            results =model.predict(
                source=segment.image.path,
                classes = segment.selected_classes,
                conf=0.25,
                save=True
            )
        
            for r in results:
                result_dir = os.path.join(settings.MEDIA_ROOT, 'results')
                os.makedirs(result_dir, exist_ok=True)
                
                
                output_filename = f'result_{os.path.basename(segment.image.name)}'
                output_path =os.path.join(result_dir, output_filename)
                
                
                r.save(output_path)
                segment.result_image = f'results/{output_filename}'
                segment.save()
                break
        
            return render(request, 'segments.html', {
                'form': form,
                'segment': segment
            })
    else:
        form = DetectionForm()
             
    return render(request, 'segments.html', {'form':form})




def pose_view(request):
    if request.method == "POST":
        form = DetectionForm(request.POST, request.FILES)
        if form.is_valid():
            
            pose = form.save(commit=False)
            pose.selected_classes = [int(x) for x in form.cleaned_data['selected_classes']]
            pose.save()
            
            model = YOLO('yolo11n-pose.pt')
            
            results = model.predict(
                source=pose.image.path,
                classes = pose.selected_classes,
                conf=0.2,
                save= True
            )
            
            for r in results:
                result_dir = os.path.join(settings.MEDIA_ROOT, 'results')
                os.makedirs(result_dir, exist_ok=True)
                
                
                output_filename = f'result_{os.path.basename(pose.image.name)}'
                output_path = os.path.join(result_dir, output_filename)
                
                
                r.save(output_path)
                pose.result_image = f'results/{output_filename}'
                pose.save()
                break
            return render(request, 'pose.html', {'form':form, 'pose':pose})
    else:
        form = DetectionForm()
        
    
    
    return render(request, 'pose.html',{'form':form})




def class_view(request):
    if request.method == "POST":
        form = DetectionForm(request.POST, request.FILES)
        if form.is_valid():
            
            class_det = form.save(commit=False)
            class_det.selected_classes = [int(x) for x in form.cleaned_data['selected_classes']]
            class_det.save()
            
            model = YOLO('yolo11n-cls.pt')
            
            results = model.predict(
                source=class_det.image.path,
                classes = class_det.selected_classes,
                conf=0.2,
                save= True
            )
            
            for r in results:
                result_dir = os.path.join(settings.MEDIA_ROOT, 'results')
                os.makedirs(result_dir, exist_ok=True)
                
                
                output_filename = f'result_{os.path.basename(class_det.image.name)}'
                output_path = os.path.join(result_dir, output_filename)
                
                
                r.save(output_path)
                class_det.result_image = f'results/{output_filename}'
                class_det.save()
                break
            return render(request, 'class.html', {'form':form, 'class_det':class_det})
    else:
        form = DetectionForm()
        
    
    
    return render(request, 'class.html',{'form':form})
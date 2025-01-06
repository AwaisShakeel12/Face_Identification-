# from django.urls import path
# from . import views

# urlpatterns = [
    
#     path('', views.detect_objects, name='detect_objects'),
# ]


# urls.py
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.detect_objects, name='detect_objects'),
    path('segment', views.segmentation_view, name='segmentation_view'),
    path('pose', views.pose_view, name='pose_view'),
    path('class', views.class_view, name='class_view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
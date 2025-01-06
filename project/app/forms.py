from django import forms
from .models import Detection

class DetectionForm(forms.ModelForm):
    selected_classes = forms.MultipleChoiceField(
        choices=Detection.CLASS_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Select objects to detect'
    )

    class Meta:
        model = Detection
        fields = ['image', 'selected_classes']
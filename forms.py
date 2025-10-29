from django import forms
from django.forms import formset_factory, modelformset_factory
from .models import FacultyUser, Qualification, Experience, Appraisal
from django.contrib.auth.forms import UserCreationForm
from .models import FacultyAppraisal
# Faculty Registration Form
class FacultyRegistrationForm(UserCreationForm):
    class Meta:
        model = FacultyUser
        fields = ['username', 'email', 'password1', 'password2']

# Appraisal Form
class AppraisalForm(forms.ModelForm):
    class Meta:
        model = Appraisal
        fields = ['achievements', 'goals']

# Qualification Formset
QualificationFormset = modelformset_factory(
    Qualification, 
    fields=('institute_name', 'degree', 'year_of_passing'), 
    extra=1, 
    can_delete=True
)

# Experience Formset
ExperienceFormset = modelformset_factory(
    Experience, 
    fields=('institute', 'from_date', 'to_date'), 
    extra=1, 
    can_delete=True
)

class FacultyAppraisalForm(forms.ModelForm):
    class Meta:
        model = FacultyAppraisal
        fields = '__all__'
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'doj': forms.DateInput(attrs={'type': 'date'}),
            'qualification': forms.Textarea(attrs={'rows': 3}),
            'experience': forms.Textarea(attrs={'rows': 3}),
            'additional_qualification': forms.Textarea(attrs={'rows': 3}),
            'patents': forms.Textarea(attrs={'rows': 3}),
            'research_projects': forms.Textarea(attrs={'rows': 3}),
            'fdp_conducted': forms.Textarea(attrs={'rows': 3}),
            'fdp_attended': forms.Textarea(attrs={'rows': 3}),
            'conferences_attended': forms.Textarea(attrs={'rows': 3}),
            'conferences_conducted': forms.Textarea(attrs={'rows': 3}),
            'teaching_methodology': forms.Textarea(attrs={'rows': 3}),
            'teaching_aids_used': forms.Textarea(attrs={'rows': 3}),
            'books_referred': forms.Textarea(attrs={'rows': 3}),
            'course_plan_details': forms.Textarea(attrs={'rows': 3}),
            'ict_used': forms.Textarea(attrs={'rows': 3}),
            'practical_expertise': forms.Textarea(attrs={'rows': 3}),
            'student_activity_coordinator': forms.Textarea(attrs={'rows': 3}),
            'professional_bodies_member': forms.Textarea(attrs={'rows': 3}),
        }
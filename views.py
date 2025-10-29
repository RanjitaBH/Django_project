from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import FacultyAppraisalForm, FacultyRegistrationForm, AppraisalForm, QualificationFormset, ExperienceFormset
from .models import FacultyAppraisal, FacultyUser
from django.contrib.auth.decorators import login_required
from django.contrib import messages



# Faculty Login
def login_faculty(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)  # Use `username` for Django's default `authenticate`
        if user is not None and user.is_faculty:
            login(request, user)
            return redirect('faculty_dashboard')
        else:
            messages.error(request, 'Invalid email or password')
    return render(request, 'appraisal/login.html')

# Faculty Logout
def logout_faculty(request):
    logout(request)
    return redirect('login_faculty')



# Faculty Registration
def register_faculty(request):
    if request.method == 'POST':
        form = FacultyRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('faculty_dashboard')
    else:
        form = FacultyRegistrationForm()
    return render(request, 'appraisal/register.html', {'form': form})
@login_required
# Faculty Dashboard
def faculty_dashboard(request):
    return render(request, 'appraisal/dashboard.html')

# Appraisal Form
def appraisal_form(request):
    if request.method == 'POST':
        appraisal_form = AppraisalForm(request.POST)
        qualification_formset = QualificationFormset(request.POST, queryset=None)
        experience_formset = ExperienceFormset(request.POST, queryset=None)

        if appraisal_form.is_valid() and qualification_formset.is_valid() and experience_formset.is_valid():
            appraisal = appraisal_form.save(commit=False)
            appraisal.faculty = request.user
            appraisal.save()

            for form in qualification_formset:
                if form.cleaned_data.get('institute_name'):
                    qualification = form.save(commit=False)
                    qualification.faculty = request.user
                    qualification.save()

            for form in experience_formset:
                if form.cleaned_data.get('institute'):
                    experience = form.save(commit=False)
                    experience.faculty = request.user
                    experience.save()

            return redirect('faculty_dashboard')
    else:
        appraisal_form = AppraisalForm()
        qualification_formset = QualificationFormset(queryset=None)
        experience_formset = ExperienceFormset(queryset=None)

    return render(request, 'appraisal/appraisal_form.html', {
        'appraisal_form': appraisal_form,
        'qualification_formset': qualification_formset,
        'experience_formset': experience_formset
    })
@login_required
def faculty_appraisal_view(request):
    if request.method == 'POST':
        form = FacultyAppraisalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appraisal_success')  # Redirect to a success page
    else:
        form = FacultyAppraisalForm()
    return render(request, 'appraisal/appraisal_frm.html', {'form': form})

def appraisal_success_view(request):
    return render(request, 'appraisal/appraisal_success.html')

############
def appraisal_list(request):
    appraisals = FacultyAppraisal.objects.all()  # Fetch all appraisals
    return render(request, 'appraisal/appraisal_list.html', {'appraisals': appraisals})
# Display and Edit a single Faculty Appraisal Form
def appraisal_detail(request, pk):
    appraisal = get_object_or_404(FacultyAppraisal, pk=pk)
    
    if request.method == 'POST':
        form = FacultyAppraisalForm(request.POST, instance=appraisal)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/appraisal/')  # Redirect to the list of appraisals
    else:
        form = FacultyAppraisalForm(instance=appraisal)
    
    return render(request, 'appraisal/appraisal_detail.html', {'form': form, 'appraisal': appraisal})
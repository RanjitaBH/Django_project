
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Custom User Manager
class FacultyUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(username, email, password, **extra_fields)

# Custom User Model for Faculty
class FacultyUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_faculty = models.BooleanField(default=True)

    # Avoid clashes with the default `User` model relationships
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='faculty_user_groups',  # Avoid reverse accessor clash
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='faculty_user_permissions',  # Avoid reverse accessor clash
        blank=True
    )

    objects = FacultyUserManager()

    def __str__(self):
        return self.username

# Qualification Model
class Qualification(models.Model):
    faculty = models.ForeignKey(FacultyUser, on_delete=models.CASCADE, related_name="qualifications")
    institute_name = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    year_of_passing = models.IntegerField()

    def __str__(self):
        return f"{self.degree} ({self.year_of_passing}) - {self.institute_name}"

# Experience Model
class Experience(models.Model):
    faculty = models.ForeignKey(FacultyUser, on_delete=models.CASCADE, related_name="experiences")
    institute = models.CharField(max_length=255)
    from_date = models.DateField()
    to_date = models.DateField()

    def __str__(self):
        return f"{self.institute} ({self.from_date} to {self.to_date})"

# Appraisal Model
class Appraisal(models.Model):
    faculty = models.ForeignKey(FacultyUser, on_delete=models.CASCADE, related_name="appraisals")
    achievements = models.TextField()
    goals = models.TextField()

    def __str__(self):
        return f"Appraisal by {self.faculty.username}"
from django.db import models

class FacultyAppraisal(models.Model):
    # Basic Information
    
    faculty_name = models.CharField(max_length=200)
    department = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=50)
    designation = models.CharField(max_length=100)
    dob = models.DateField()
    doj = models.DateField()
    mobile_no = models.CharField(max_length=15)
    pan_no = models.CharField(max_length=20, blank=True, null=True)
    aadhar_no = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField()

    # Qualifications and Experience
    qualification = models.TextField(blank=True, null=True)
    experience = models.TextField(blank=True, null=True)
    certificate = models.BooleanField(default=False)

    # Summary
    teaching_experience = models.CharField(max_length=100, blank=True, null=True)
    industrial_experience = models.CharField(max_length=100, blank=True, null=True)
    research_experience = models.CharField(max_length=100, blank=True, null=True)
    additional_qualification = models.TextField(blank=True, null=True)

    # Research and Publications
    international_journals = models.PositiveIntegerField(default=0)
    national_journals = models.PositiveIntegerField(default=0)
    international_conferences = models.PositiveIntegerField(default=0)
    national_conferences = models.PositiveIntegerField(default=0)
    patents = models.TextField(blank=True, null=True)

    # B.Tech/ME/PhD Projects
    btech_projects = models.PositiveIntegerField(default=0)
    me_projects = models.PositiveIntegerField(default=0)
    phd_dissertations = models.PositiveIntegerField(default=0)

    # Research Projects
    research_projects = models.TextField(blank=True, null=True)

    # Faculty Development Programs
    fdp_conducted = models.TextField(blank=True, null=True)
    fdp_attended = models.TextField(blank=True, null=True)

    # Conferences/Seminars
    conferences_attended = models.TextField(blank=True, null=True)
    conferences_conducted = models.TextField(blank=True, null=True)

    # Teaching Methodology
    teaching_methodology = models.TextField(blank=True, null=True)
    teaching_aids_used = models.TextField(blank=True, null=True)
    books_referred = models.TextField(blank=True, null=True)
    course_plan_details = models.TextField(blank=True, null=True)
    course_material_prepared = models.BooleanField(default=False)
    ict_used = models.TextField(blank=True, null=True)
    practical_expertise = models.TextField(blank=True, null=True)

    # Administrative Responsibility
    faculty_advisor = models.BooleanField(default=False)
    head_of_department = models.BooleanField(default=False)
    chief_warden = models.BooleanField(default=False)
    warden = models.BooleanField(default=False)
    resident_warden = models.BooleanField(default=False)
    student_activity_coordinator = models.TextField(blank=True, null=True)
    professional_bodies_member = models.TextField(blank=True, null=True)

    # Ratings
    seminars_conducted_rating = models.IntegerField(default=0)
    student_activity_rating = models.IntegerField(default=0)
    projects_guided_rating = models.IntegerField(default=0)

    def __str__(self):
        return self.faculty_name

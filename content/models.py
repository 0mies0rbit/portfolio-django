from django.db import models


class SiteSettings(models.Model):
    site_title = models.CharField(max_length=200, default="Omkar Mishra")
    site_description = models.TextField(blank=True)

    hero_eyebrow = models.CharField(
        max_length=255,
        default="Computational Astrophysics / Scientific Computing"
    )
    hero_mini_line = models.CharField(
        max_length=255,
        default="Simulation • Inference • Numerical Methods • Orbital Dynamics"
    )
    hero_title_prefix = models.CharField(max_length=255, default="Building toward")
    hero_title_highlight = models.CharField(max_length=255, default="computational astrophysics")
    hero_title_suffix = models.CharField(
        max_length=255,
        default="with research-driven code and ambitious technical work."
    )

    role = models.CharField(max_length=255, default="B.Tech IT Undergraduate")
    about_text = models.TextField(blank=True)

    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    scholar_url = models.URLField(blank=True)
    researchgate_url = models.URLField(blank=True)
    email = models.EmailField(blank=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Site Settings"


class HeroMetric(models.Model):
    label = models.CharField(max_length=100)
    value = models.CharField(max_length=255)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return f"{self.label}: {self.value}"


class StackItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.name


class NoteCard(models.Model):
    title = models.CharField(max_length=150, default="Notes")
    content = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class SignalStripItem(models.Model):
    text = models.CharField(max_length=120)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.text


class Project(models.Model):
    label = models.CharField(max_length=100, default="Project")
    index = models.CharField(max_length=10, blank=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    summary = models.TextField()
    description = models.TextField(blank=True)
    details = models.TextField(blank=True)

    category = models.CharField(max_length=120, blank=True)
    status = models.CharField(max_length=120, blank=True)
    focus = models.CharField(max_length=200, blank=True)

    github_url = models.URLField(blank=True)
    external_url = models.URLField(blank=True)

    is_featured = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.title


class ProjectTag(models.Model):
    project = models.ForeignKey(Project, related_name="tags", on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return f"{self.project.title} - {self.name}"


class ProjectMedia(models.Model):
    MEDIA_TYPES = [
        ("image", "Image"),
        ("video", "Video"),
        ("placeholder", "Placeholder"),
    ]

    SIZE_TYPES = [
        ("small", "Small"),
        ("large", "Large"),
        ("full", "Full"),
    ]

    project = models.ForeignKey(Project, related_name="media", on_delete=models.CASCADE)
    media_type = models.CharField(max_length=20, choices=MEDIA_TYPES, default="placeholder")
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="project_media/images/", blank=True, null=True)
    video = models.FileField(upload_to="project_media/videos/", blank=True, null=True)
    placeholder_text = models.CharField(max_length=255, blank=True)
    size = models.CharField(max_length=20, choices=SIZE_TYPES, default="small")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return f"{self.project.title} - {self.title}"


class ResearchLog(models.Model):
    meta_one = models.CharField(max_length=100, blank=True)
    meta_two = models.CharField(max_length=100, blank=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class BlogPost(models.Model):
    blog_type = models.CharField(max_length=100, default="Essay")
    title = models.CharField(max_length=220)
    slug = models.SlugField(unique=True)
    summary = models.TextField()
    content = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["order", "-created_at"]

    def __str__(self):
        return self.title
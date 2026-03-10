from django.urls import path
from .views import (
    HomeContentView,
    SiteSettingsView,
    ProjectListView,
    ProjectDetailView,
    ResearchLogListView,
    ResearchLogDetailView,
    BlogListView,
    BlogDetailView,
)

urlpatterns = [
    path("home/", HomeContentView.as_view(), name="home-content"),
    path("site-settings/", SiteSettingsView.as_view(), name="site-settings"),
    path("projects/", ProjectListView.as_view(), name="project-list"),
    path("projects/<slug:slug>/", ProjectDetailView.as_view(), name="project-detail"),
    path("research-logs/", ResearchLogListView.as_view(), name="research-log-list"),
    path("research-logs/<slug:slug>/", ResearchLogDetailView.as_view(), name="research-log-detail"),
    path("blogs/", BlogListView.as_view(), name="blog-list"),
    path("blogs/<slug:slug>/", BlogDetailView.as_view(), name="blog-detail"),
]
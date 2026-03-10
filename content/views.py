from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView



from .models import SiteSettings, Project, ResearchLog, BlogPost
from .serializers import (
    SiteSettingsSerializer,
    ProjectSerializer,
    ResearchLogSerializer,
    BlogPostSerializer,
)


class HomeContentView(APIView):
    def get(self, request):
        settings_obj = SiteSettings.objects.first()
        if not settings_obj:
            settings_obj = SiteSettings.objects.create()

        projects = Project.objects.filter(is_active=True, is_featured=True)
        research_logs = ResearchLog.objects.filter(is_active=True)
        blogs = BlogPost.objects.filter(is_active=True)

        return Response({
            "site": SiteSettingsSerializer(settings_obj, context={"request": request}).data,
            "projects": ProjectSerializer(projects, many=True, context={"request": request}).data,
            "research_logs": ResearchLogSerializer(research_logs, many=True).data,
            "blogs": BlogPostSerializer(blogs, many=True).data,
        })


class SiteSettingsView(APIView):
    def get(self, request):
        settings_obj = SiteSettings.objects.first()
        if not settings_obj:
            settings_obj = SiteSettings.objects.create()
        return Response(SiteSettingsSerializer(settings_obj, context={"request": request}).data)


class ProjectListView(generics.ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.filter(is_active=True)

    def get_serializer_context(self):
        return {"request": self.request}


class ProjectDetailView(generics.RetrieveAPIView):
    serializer_class = ProjectSerializer
    lookup_field = "slug"

    def get_queryset(self):
        return Project.objects.filter(is_active=True)

    def get_serializer_context(self):
        return {"request": self.request}


class ResearchLogListView(generics.ListAPIView):
    serializer_class = ResearchLogSerializer
    queryset = ResearchLog.objects.filter(is_active=True)


class BlogListView(generics.ListAPIView):
    serializer_class = BlogPostSerializer
    queryset = BlogPost.objects.filter(is_active=True)


class BlogDetailView(generics.RetrieveAPIView):
    serializer_class = BlogPostSerializer
    lookup_field = "slug"

    def get_queryset(self):
        return BlogPost.objects.filter(is_active=True)
class ResearchLogDetailView(generics.RetrieveAPIView):
    serializer_class = ResearchLogSerializer
    lookup_field = "slug"

    def get_queryset(self):
        return ResearchLog.objects.filter(is_active=True)
from rest_framework import serializers
from .models import (
    SiteSettings,
    HeroMetric,
    StackItem,
    NoteCard,
    SignalStripItem,
    Project,
    ProjectTag,
    ProjectMedia,
    ResearchLog,
    BlogPost,
)


class HeroMetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroMetric
        fields = ["id", "label", "value", "order", "is_active"]


class StackItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = StackItem
        fields = ["id", "name", "description", "order", "is_active"]


class NoteCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteCard
        fields = ["id", "title", "content", "is_active"]


class SignalStripItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignalStripItem
        fields = ["id", "text", "order", "is_active"]


class ProjectTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectTag
        fields = ["id", "name", "order"]


class ProjectMediaSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    video_url = serializers.SerializerMethodField()

    class Meta:
        model = ProjectMedia
        fields = [
            "id",
            "media_type",
            "title",
            "image_url",
            "video_url",
            "placeholder_text",
            "size",
            "order",
        ]

    def get_image_url(self, obj):
        request = self.context.get("request")
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        if obj.image:
            return obj.image.url
        return ""

    def get_video_url(self, obj):
        request = self.context.get("request")
        if obj.video and request:
            return request.build_absolute_uri(obj.video.url)
        if obj.video:
            return obj.video.url
        return ""


class ProjectSerializer(serializers.ModelSerializer):
    tags = ProjectTagSerializer(many=True, read_only=True)
    media = ProjectMediaSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = [
            "id",
            "label",
            "index",
            "title",
            "slug",
            "summary",
            "description",
            "details",
            "category",
            "status",
            "focus",
            "github_url",
            "external_url",
            "is_featured",
            "is_active",
            "order",
            "tags",
            "media",
        ]


class ResearchLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResearchLog
        fields = ["id", "meta_one", "meta_two", "title", "slug", "content", "is_active"]


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = [
            "id",
            "blog_type",
            "title",
            "slug",
            "summary",
            "content",
            "is_active",
            "order",
            "created_at",
        ]


class SiteSettingsSerializer(serializers.ModelSerializer):
    hero_metrics = serializers.SerializerMethodField()
    stack_items = serializers.SerializerMethodField()
    note_cards = serializers.SerializerMethodField()
    signal_strip = serializers.SerializerMethodField()

    class Meta:
        model = SiteSettings
        fields = [
            "id",
            "site_title",
            "site_description",
            "hero_eyebrow",
            "hero_mini_line",
            "hero_title_prefix",
            "hero_title_highlight",
            "hero_title_suffix",
            "role",
            "about_text",
            "github_url",
            "linkedin_url",
            "scholar_url",
            "researchgate_url",
            "email",
            "hero_metrics",
            "stack_items",
            "note_cards",
            "signal_strip",
        ]

    def get_hero_metrics(self, obj):
        qs = HeroMetric.objects.filter(is_active=True)
        return HeroMetricSerializer(qs, many=True).data

    def get_stack_items(self, obj):
        qs = StackItem.objects.filter(is_active=True)
        return StackItemSerializer(qs, many=True).data

    def get_note_cards(self, obj):
        qs = NoteCard.objects.filter(is_active=True)
        return NoteCardSerializer(qs, many=True).data

    def get_signal_strip(self, obj):
        qs = SignalStripItem.objects.filter(is_active=True)
        return SignalStripItemSerializer(qs, many=True).data
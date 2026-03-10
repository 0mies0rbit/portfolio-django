from django.contrib import admin
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


class HeroMetricAdmin(admin.ModelAdmin):
    list_display = ("label", "value", "order", "is_active")
    list_editable = ("order", "is_active")


class StackItemAdmin(admin.ModelAdmin):
    list_display = ("name", "order", "is_active")
    list_editable = ("order", "is_active")


class NoteCardAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active")
    list_editable = ("is_active",)


class SignalStripItemAdmin(admin.ModelAdmin):
    list_display = ("text", "order", "is_active")
    list_editable = ("order", "is_active")


class ProjectTagInline(admin.TabularInline):
    model = ProjectTag
    extra = 1


class ProjectMediaInline(admin.TabularInline):
    model = ProjectMedia
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "label", "is_featured", "is_active", "order")
    list_editable = ("is_featured", "is_active", "order")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [ProjectTagInline, ProjectMediaInline]


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "blog_type", "slug", "is_active", "order", "created_at")
    list_editable = ("is_active", "order")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(ResearchLog)
class ResearchLogAdmin(admin.ModelAdmin):
    list_display = ("title", "meta_one", "meta_two", "is_active")
    list_editable = ("is_active",)


admin.site.register(SiteSettings)
admin.site.register(HeroMetric, HeroMetricAdmin)
admin.site.register(StackItem, StackItemAdmin)
admin.site.register(NoteCard, NoteCardAdmin)
admin.site.register(SignalStripItem, SignalStripItemAdmin)
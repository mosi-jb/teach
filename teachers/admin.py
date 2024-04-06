from django.contrib import admin

from teachers.models import Category, TeachersVideos, Teachers

# Register your models here.


admin.site.register(Category)


class TeacherInline(admin.StackedInline):
    model = TeachersVideos
    extra = 2


@admin.register(Teachers)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [TeacherInline]

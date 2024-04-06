from django.db import models


# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=48, db_index=True, verbose_name='عنوان')
    image = models.ImageField(upload_to='category/', verbose_name='عکس', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class Teachers(models.Model):
    title = models.CharField(max_length=48, db_index=True, verbose_name='نام دبیر')
    image = models.ImageField(upload_to='teachers/', verbose_name='عکس')
    experience = models.CharField(max_length=48, verbose_name='سابقه')
    price = models.PositiveBigIntegerField(verbose_name='هزینه تدریس')
    description = models.TextField(verbose_name='توضیحات')
    category = models.ManyToManyField(Category, verbose_name='دسته بندی', related_name='teach')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'معلم'
        verbose_name_plural = 'معلم ها'


class TeachersVideos(models.Model):
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE, related_name='videos', verbose_name='معلم')
    video = models.FileField(upload_to='movie/', verbose_name='فیلم')
    display_order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.teacher.title

    class Meta:
        verbose_name = 'فیلم'
        verbose_name_plural = 'فیلم ها'
        ordering = ('display_order',)

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)

        for index, video in enumerate(self.teacher.videos.all()):
            video.display_order = index
            video.save()

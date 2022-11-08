from django.conf import settings
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class BlogImages(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True, related_name="blog_images")
    image = models.ImageField(upload_to='BlogImages/', null=True)
    is_active = models.BooleanField(default=True)

    @property
    def get_image_url(self):
        if settings.DEBUG:
            return f"{settings.LOCAL_BASE_URL}{self.image.url}"
        else:
            return f"{settings.PROD_BASE_URL}{self.image.url}"

    def __str__(self):
        return f'image of {self.blog.id}'

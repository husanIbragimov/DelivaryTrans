from django.db import models


class AboutCompany(models.Model):
    title = models.CharField(max_length=65)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.title


class AboutCompanyImages(models.Model):
    about = models.ForeignKey(AboutCompany, on_delete=models.CASCADE, null=True, related_name="about_images")
    image = models.ImageField(upload_to='about_company_images/', null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'Image of {self.about.id}'

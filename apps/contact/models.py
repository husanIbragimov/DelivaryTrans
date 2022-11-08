from django.db import models
from ckeditor.fields import RichTextField

CONTACT_STATUS = (
    (0, "New"),
    (1, "Process"),
    (2, "Canceled"),
    (3, "Finished")
)


class Contact(models.Model):
    title = models.CharField(max_length=65)
    phone_number = models.CharField(max_length=13)
    status = models.IntegerField(choices=CONTACT_STATUS, default=0)
    from_here = models.CharField(max_length=50)
    to_here = models.CharField(max_length=50)
    description = RichTextField()
    date_created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title

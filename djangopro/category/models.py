from django.db import models

# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=20)
    Category_image=models.ImageField(upload_to="img/categoryimg")
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.category_name

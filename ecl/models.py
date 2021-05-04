from django.db import models


class Tag(models.Model):
    tag = models.CharField(max_length = 20, default='ALL')
    
    def __str__(self):
        return self.tag


# Create your models here.
class Entry(models.Model):
    error_text = models.CharField(max_length = 500)
    correction_text = models.CharField(max_length = 500)
    tag = models.ForeignKey(Tag, on_delete = models.CASCADE, null = True)

    def __str__(self):
        return self.error_text

    def giveCorrection(self):
        return self.correction_text

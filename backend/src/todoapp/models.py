from django.db import models



class Todo(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.title
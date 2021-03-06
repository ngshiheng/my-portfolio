from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    URL = models.URLField()
    image = models.ImageField(default='default_project.png', upload_to='project_pics')

    def __str__(self):
        return self.title       # set how this object defines it self, in this case by the 'title' name


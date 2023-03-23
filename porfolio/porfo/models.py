from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    image = models.ImageField(default="null", upload_to="images")
    tools = models.CharField(max_length=100)
    github = models.URLField(blank=True)

    def __str__(self):
        return f"{self.title}"


class Skill(models.Model):
    title = models.CharField(max_length=40)
    image = models.ImageField(default="null", upload_to="images")

    def __str__(self):
        return f"{self.title}"


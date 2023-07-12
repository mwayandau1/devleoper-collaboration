from django.db import models
import uuid
from users.models import Profile
class Tag(models.Model):
    name = models.CharField(max_length=200)
    created  = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)


    def __str__(self):
        return self.name
    


class Projects(models.Model):
    owner = models.ForeignKey(Profile, blank=True, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    demo_link = models.CharField(max_length=200, blank=True, null=True)
    source_link = models.CharField(max_length=200, blank=True, null=True)
    featured_image = models.ImageField(blank=True, null=True, default='images/logo.svg')
    tags = models.ManyToManyField(Tag, blank=True)
    total_vote = models.IntegerField(default=0, blank=True, null=True)
    vote_ratio = models.IntegerField(default=0, blank=True, null=True)
    created  = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)

    class Meta:
        verbose_name = 'projects'
        verbose_name_plural = 'projects'
        

    def __str__(self) -> str:
        return self.title
    

class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up vote'),
        ('down', 'Down vote')
    )
    #owner =
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    body = models.TextField(max_length=500, null=True, blank=True)
    value = models.CharField(max_length=20, choices=VOTE_TYPE)
    created  = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)


    def __str__(self):
        return self.value
    



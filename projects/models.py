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
    owner = models.ForeignKey(Profile, blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    demo_link = models.URLField(max_length=200, blank=True, null=True)
    source_link = models.URLField(max_length=200, blank=True, null=True)
    featured_image = models.ImageField(blank=True, null=True, default='images/logo.svg')
    tags = models.ManyToManyField(Tag, blank=True)
    total_vote = models.IntegerField(default=0, blank=True, null=True)
    vote_ratio = models.IntegerField(default=0, blank=True, null=True)
    created  = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)

    class Meta:
        verbose_name = 'projects'
        verbose_name_plural = 'projects'
        ordering = ['-vote_ratio', '-total_vote', '-created']
        

    def __str__(self) -> str:
        return self.title
    
    def getImageUrl(self):
        try:
            url = self.featured_image.url
        except:
            url = ''
        return url
    
    

    def reviewers(self):
        query = self.review_set.all().values_list('owner__id', flat=True)
        return query
    
    @property   
    def getVoteCount(self):
        reviews = self.review_set.all()
        upVotes = reviews.filter(value='up').count()
        totalVotes = reviews.count()
        ratio = (upVotes / totalVotes) * 100
        self.total_vote = totalVotes
        self.vote_ratio = ratio
        self.save()
        
    

class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up vote'),
        ('down', 'Down vote')
    )
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    body = models.TextField(max_length=500, null=True, blank=True)
    value = models.CharField(max_length=20, choices=VOTE_TYPE)
    created  = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)

    class Meta:
        unique_together = [['owner', 'project']]

    def __str__(self):
        return self.value
    



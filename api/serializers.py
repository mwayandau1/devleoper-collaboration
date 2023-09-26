from projects.models import Projects, Tag
from rest_framework.serializers import ModelSerializer
from users.models import Profile


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class TagSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class ProjectsSerializer(ModelSerializer):
    owner = ProfileSerializer(many=False)
    # tags = TagSerializer(many=True)
    class Meta:
        model = Projects
        # fields = ['owner', 'title', 'description', 'demo_link', 'source_link', ]
        fields = '__all__'
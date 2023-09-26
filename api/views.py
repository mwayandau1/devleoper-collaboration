from rest_framework.decorators import api_view
from rest_framework.response import Response
from projects.models import Projects, Tag
from .serializers import ProjectsSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'GET':'/api/projects'},
        {'GET':'/api/projects/id'},
        {'POST':'/api/projects/id/vote'},

        {'POST':'/api/users/token'},
        {'POST':'/api/users/token/refresh'},
    ]

    return Response(routes)


@api_view(['GET'])
def getProjects(request):
    projects = Projects.objects.all()
    serializer = ProjectsSerializer(projects, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_single_project(request, pk):
    project = Projects.objects.get(id=pk)
    serializer = ProjectsSerializer(project)
    return Response(serializer.data)


@api_view(['DELETE'])
def removeTag(request):
    tagId = request.data['tag']
    projectId = request.data['project']
    project = Projects.objects.get(id=projectId)
    tag = Tag.objects.get(id=tagId)
    project.tags.remove(tag)
    return Response("A tag has been removed")
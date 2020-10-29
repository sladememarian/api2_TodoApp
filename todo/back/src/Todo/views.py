from django.shortcuts import render
import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import Task
from .serializers import TaskSerializer
# Create your views here.


def taskRemain(request):
    tasks = Task.objects.all()
    serialized = TaskSerializer(tasks, many=True)
    return HttpResponse(json.dumps(serialized.data), status=200)


def taskM_L(request):
    print("REQUEST RECIEVED", request.POST)
    Task.objects.create(
        name=request.POST["name"],
        # is_done=request.POST["is_done"],
    )
    return HttpResponse("tasks was added", status=200)

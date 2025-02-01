from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, RegisterView, LoginView, TaskListCreate, TaskDetail
from rest_framework.response import Response
from rest_framework.views import APIView

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('v1/register/', RegisterView.as_view(), name='register'),
    path('v1/login/', LoginView.as_view(), name='login'),
    path('v1/task-list/', TaskListCreate.as_view(), name='task-list'),
    path('v1/task-detail/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
]

class RegisterView(APIView):
    def post(self, request):
        return Response({'message': 'User registered successfully!'}, status=status.HTTP_201_CREATED)
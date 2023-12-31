from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Task
from projects.models import Project


class TaskListViewTests(APITestCase):
    def setUp(self):
        # Run this before the test
        User.objects.create_user(username='kedi', password='kedi')

    def test_can_list_tasks(self):
        kedi = User.objects.get(username='kedi')
        project = Project.objects.create(owner=kedi, project_name='Test project')
        Task.objects.create(owner=kedi, task_name='Test task', assignees=kedi, project=project)
        response = self.client.get('/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        #print(response.data, len(response.data))

    def test_logged_in_user_can_create_task(self):
        self.client.login(username='kedi', password='kedi')

        kedi = User.objects.get(username='kedi')
        project = Project.objects.create(owner=kedi, project_name='Test project')
        response = self.client.post('/tasks/', {
            'task_name': 'Test task',
            'description': 'dev',
            'assignee': kedi,
            'project': project,
            'status': 0,
            'attachment': 'dfdfdf',
        })
        count = Task.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    

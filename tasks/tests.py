from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Task


class TaskListViewTests(APITestCase):
    def setUp(self):
        # Run this before the test
        User.objects.create_user(username='kedi', password='kedi')

    def test_can_list_tasks(self):
        kedi = User.objects.get(username='kedi')
        Task.objects.create(owner=kedi, task_name='Test task')
        response = self.client.get('/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data, len(response.data))

    def test_logged_in_user_can_create_task(self):
        self.client.login(username='kedi', password='kedi')
        response = self.client.post('/tasks/', {
            'task_name': 'Test task',
            'description': 'dev',
            'assignees': 'daddy',
            'project': 'fo',
            'status': 'complete',
            'attachment': 'dfdfdf'
        })
        count = Task.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print(response.data, len(response.data))

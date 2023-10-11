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
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print(response.data, len(response.data))


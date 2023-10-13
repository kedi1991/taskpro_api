from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Project

class ProjectListViewTests(APITestCase):
    def setUp(self):
        # Run this before the test
        User.objects.create_user(username='kedi', password='kedi')

    def test_can_list_projects(self):
        kedi = User.objects.get(username='kedi')
        Project.objects.create(owner=kedi, project_name='Test project')
        response = self.client.get('/projects/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data, len(response.data))

    def test_logged_in_user_can_create_project(self):
        self.client.login(username='kedi', password='kedi')
        response = self.client.post('/projects/', {
        'project_name': 'Test project', 
        })
        count = Project.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print(response.data, len(response.data))





from django.test import TestCase
from rest_framework.test import APIClient
from .models import TaskList
from .serializer import TaskListSerializer
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

# Create a user with username and password

class TestTask(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='johndoe',
            password='password123',
            first_name='John',
            last_name='Doe',
            email='johndoe@example.com'
        )
        data = {
            'username': 'johndoe',
            'password': 'password123'
        }
        self.my_model = TaskList.objects.create(task="FirstTas", insert_by=self.user)
        self.token = self.client.post('/api-token-auth/', data=data, format='json').json()['token']
        self.header = {"HTTP_AUTHORIZATION": f"Bearer {self.token}"}

    def test_list(self):
        response = self.client.get('/tasks/')
        self.assertEqual(response.status_code, 200)
        serializer_data = TaskListSerializer([self.my_model], many=True).data
        self.assertEqual([response.data['results'][0]], serializer_data)

    def test_retrieve(self):
        response = self.client.get(f'/tasks/{self.my_model.id}/')
        self.assertEqual(response.status_code, 200)
        serializer_data = TaskListSerializer(self.my_model).data
        self.assertEqual(response.data, serializer_data)

    def test_create(self):
        data = {'task': "SecondTask", 'insert_by': 1}
        response = self.client.post(
            '/tasks/',
            data=data,
            **self.header
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(TaskList.objects.count(), 2)
        self.assertEqual(response.json()['task'], 'SecondTask')

    def test_update(self):
        data = {'task': "SecondTask", 'insert_by': 1}
        response = self.client.put(
            f'/tasks/{self.my_model.id}/',
            data=data,
            **self.header
        )
        self.assertEqual(response.status_code, 200)
        self.my_model.refresh_from_db()
        self.assertEqual(self.my_model.task, 'SecondTask')
        self.assertEqual(self.my_model.insert_by, self.user)

    def test_delete(self):
        response = self.client.delete(
            f'/tasks/{self.my_model.id}/',
            **self.header
        )
        self.assertEqual(response.status_code, 204)
        self.assertEqual(TaskList.objects.count(), 0)

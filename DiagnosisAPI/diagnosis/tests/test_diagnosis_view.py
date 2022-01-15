from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from diagnosis.models import Category


class DiagnosisViewTest(APITestCase):

    def setUp(self):
        self.url = reverse('diagnosis-list')
        self.category = Category.objects.create(
            code='CAT1', title='Category 1')

        self.valid_data = {
            'category': self.category.id,
            'code': 'DIA1',
            'description': 'Diagnosis 1',
            'code_type': 'ICD_10'
        }

        self.update_data = {
            'category': self.category.id,
            'code': 'DIA2',
            'description': 'Diagnosis 2',
            'code_type': 'ICD_10'
        }

        self.invalid_data = {
            'category': '',
            'code': '',
            'description': '',
            'code_type': 'ICD_10'
        }

    def test_create_diagnosis(self):
        response = self.client.post(
            self.url, self.valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['code'], 'DIA1')
        self.assertEqual(response.data['description'], 'Diagnosis 1')

    def test_create_diagnosis_with_empty_data(self):
        response = self.client.post(
            self.url, self.invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['category'][0],
                         'This field may not be null.')
        self.assertEqual(response.data['code'][0],
                         'This field may not be blank.')
        self.assertEqual(response.data['description'][0],
                         'This field may not be blank.')

    def test_delete_diagnosis(self):
        response = self.client.post(
            self.url, self.valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['code'], 'DIA1')
        self.assertEqual(response.data['description'], 'Diagnosis 1')
        self.url = reverse('diagnosis-detail', args=[response.data['id']])
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_update_diagnosis(self):
        response = self.client.post(
            self.url, self.valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['code'], 'DIA1')
        self.assertEqual(response.data['description'], 'Diagnosis 1')
        self.url = reverse('diagnosis-detail', args=[response.data['id']])
        response = self.client.put(
            self.url, self.update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['code'], 'DIA2')
        self.assertEqual(response.data['description'], 'Diagnosis 2')

    def test_update_diagnosis_with_empty_data(self):
        response = self.client.post(
            self.url, self.valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['code'], 'DIA1')
        self.assertEqual(response.data['description'], 'Diagnosis 1')
        self.url = reverse('diagnosis-detail', args=[response.data['id']])
        response = self.client.put(
            self.url, self.invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['category'][0],
                         'This field may not be null.')
        self.assertEqual(response.data['code'][0],
                         'This field may not be blank.')
        self.assertEqual(response.data['description'][0],
                         'This field may not be blank.')

    def test_get_diagnosis_list(self):
        response = self.client.post(
            self.url, self.valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['code'], 'DIA1')
        self.assertEqual(response.data['description'], 'Diagnosis 1')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_diagnosis_detail(self):
        response = self.client.post(
            self.url, self.valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['code'], 'DIA1')
        self.assertEqual(response.data['description'], 'Diagnosis 1')
        self.url = reverse('diagnosis-detail', args=[response.data['id']])
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_diagnosis_detail(self):
        response = self.client.post(
            self.url, self.valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['code'], 'DIA1')
        self.assertEqual(response.data['description'], 'Diagnosis 1')
        self.url = reverse('diagnosis-detail', args=[response.data['id']])
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

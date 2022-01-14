from rest_framework.test import APITestCase
from django.urls import reverse
from diagnosis.models import Diagnosis, Category


class DiagnosisViewTest(APITestCase):
    def test_create_diagnosis(self):
        self.url = reverse('diagnosis-list')
        category = Category.objects.create(code='CAT1', title='Category 1')
        data = {
            'category': category.id,
            'code': 'DIA1',
            'description': 'Diagnosis 1',
            'code_type': 'ICD_10'
        }
        response = self.client.post(
            self.url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['code'], 'DIA1')
        self.assertEqual(response.data['description'], 'Diagnosis 1')

    def test_create_diagnosis_with_empty_data(self):
        self.url = reverse('diagnosis-list')
        data = {
            'category': '',
            'code': '',
            'description': '',
            'code_type': 'ICD_10'
        }
        response = self.client.post(
            self.url, data, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['category'][0],
                         'This field may not be null.')
        self.assertEqual(response.data['code'][0],
                         'This field may not be blank.')
        self.assertEqual(response.data['description'][0],
                         'This field may not be blank.')

    def test_delete_diagnosis(self):
        self.url = reverse('diagnosis-list')
        category = Category.objects.create(code='CAT1', title='Category 1')
        data = {
            'category': category.id,
            'code': 'DIA1',
            'description': 'Diagnosis 1',
            'code_type': 'ICD_10'
        }
        response = self.client.post(
            self.url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['code'], 'DIA1')
        self.assertEqual(response.data['description'], 'Diagnosis 1')
        self.url = reverse('diagnosis-detail', args=[response.data['id']])
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, 204)

    def test_update_diagnosis(self):
        self.url = reverse('diagnosis-list')
        category = Category.objects.create(code='CAT1', title='Category 1')
        data = {
            'category': category.id,
            'code': 'DIA1',
            'description': 'Diagnosis 1',
            'code_type': 'ICD_10'
        }
        response = self.client.post(
            self.url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['code'], 'DIA1')
        self.assertEqual(response.data['description'], 'Diagnosis 1')
        self.url = reverse('diagnosis-detail', args=[response.data['id']])
        data = {
            'category': category.id,
            'code': 'DIA2',
            'description': 'Diagnosis 2',
            'code_type': 'ICD_10'
        }
        response = self.client.put(
            self.url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['code'], 'DIA2')
        self.assertEqual(response.data['description'], 'Diagnosis 2')

    def test_update_diagnosis_with_empty_data(self):
        self.url = reverse('diagnosis-list')
        category = Category.objects.create(code='CAT1', title='Category 1')
        data = {
            'category': category.id,
            'code': 'DIA1',
            'description': 'Diagnosis 1',
            'code_type': 'ICD_10'
        }
        response = self.client.post(
            self.url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['code'], 'DIA1')
        self.assertEqual(response.data['description'], 'Diagnosis 1')
        self.url = reverse('diagnosis-detail', args=[response.data['id']])
        data = {
            'category': '',
            'code': '',
            'description': '',
            'code_type': 'ICD_10'
        }
        response = self.client.put(
            self.url, data, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['category'][0],
                         'This field may not be null.')
        self.assertEqual(response.data['code'][0],
                         'This field may not be blank.')
        self.assertEqual(response.data['description'][0],
                         'This field may not be blank.')

    def test_get_diagnosis_list(self):
        self.url = reverse('diagnosis-list')
        category = Category.objects.create(code='CAT1', title='Category 1')
        data = {
            'category': category.id,
            'code': 'DIA1',
            'description': 'Diagnosis 1',
            'code_type': 'ICD_10'
        }
        response = self.client.post(
            self.url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['code'], 'DIA1')
        self.assertEqual(response.data['description'], 'Diagnosis 1')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['code'], 'DIA1')
        self.assertEqual(response.data[0]['description'], 'Diagnosis 1')

    def test_get_diagnosis_detail(self):
        self.url = reverse('diagnosis-list')
        category = Category.objects.create(code='CAT1', title='Category 1')
        data = {
            'category': category.id,
            'code': 'DIA1',
            'description': 'Diagnosis 1',
            'code_type': 'ICD_10'
        }
        response = self.client.post(
            self.url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['code'], 'DIA1')
        self.assertEqual(response.data['description'], 'Diagnosis 1')
        self.url = reverse('diagnosis-detail', args=[response.data['id']])
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_delete_diagnosis_detail(self):
        self.url = reverse('diagnosis-list')
        category = Category.objects.create(code='CAT1', title='Category 1')
        data = {
            'category': category.id,
            'code': 'DIA1',
            'description': 'Diagnosis 1',
            'code_type': 'ICD_10'
        }
        response = self.client.post(
            self.url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['code'], 'DIA1')
        self.assertEqual(response.data['description'], 'Diagnosis 1')
        self.url = reverse('diagnosis-detail', args=[response.data['id']])
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, 204)

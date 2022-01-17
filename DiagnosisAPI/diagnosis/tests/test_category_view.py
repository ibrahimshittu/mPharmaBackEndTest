from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse


class CategoryViewTest(APITestCase):

    def setUp(self):
        self.url = reverse('category-list')
        self.valid_data = {'code': 'CAT1', 'title': 'Category 1'}
        self.update_data = {'code': 'CAT2', 'title': 'Category 2'}
        self.invalid_data = {'code': '', 'title': ''}

    def test_create_category(self):
        self.url = reverse('category-list')
        response = self.client.post(
            self.url, self.valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['code'], 'CAT1')
        self.assertEqual(response.data['title'], 'Category 1')

    def test_create_category_with_empty_data(self):
        self.url = reverse('category-list')
        response = self.client.post(
            self.url, self.invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['code'][0],
                         'This field may not be blank.')

    def test_delete_category(self):
        self.url = reverse('category-list')
        response = self.client.post(
            self.url, self.valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['code'], 'CAT1')
        self.assertEqual(response.data['title'], 'Category 1')
        self.url = reverse('category-detail', args=[response.data['id']])
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_category_with_invalid_id(self):
        self.url = reverse('category-detail', args=[9999])
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_category(self):
        self.url = reverse('category-list')
        response = self.client.post(
            self.url, self.valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['code'], 'CAT1')
        self.assertEqual(response.data['title'], 'Category 1')
        self.url = reverse('category-detail', args=[response.data['id']])
        response = self.client.put(
            self.url, self.update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['code'], 'CAT2')
        self.assertEqual(response.data['title'], 'Category 2')

    def test_update_category_with_empty_data(self):
        self.url = reverse('category-list')
        response = self.client.post(
            self.url, self.valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['code'], 'CAT1')
        self.assertEqual(response.data['title'], 'Category 1')
        self.url = reverse('category-detail', args=[response.data['id']])
        response = self.client.put(
            self.url, self.invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['code'][0],
                         'This field may not be blank.')

    def test_get_category(self):
        self.url = reverse('category-list')
        response = self.client.post(
            self.url, self.valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['code'], 'CAT1')
        self.assertEqual(response.data['title'], 'Category 1')
        self.url = reverse('category-detail', args=[response.data['id']])
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['code'], 'CAT1')
        self.assertEqual(response.data['title'], 'Category 1')

    def test_get_category_list(self):
        self.url = reverse('category-list')
        response = self.client.post(
            self.url, self.valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['code'], 'CAT1')
        self.assertEqual(response.data['title'], 'Category 1')
        self.url = reverse('category-list')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_category_with_invalid_id(self):
        self.url = reverse('category-detail', args=[9999])
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

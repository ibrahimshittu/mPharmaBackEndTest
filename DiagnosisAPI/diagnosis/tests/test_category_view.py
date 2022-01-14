from rest_framework.test import APITestCase
from django.urls import reverse


class CategoryViewTest(APITestCase):
    def test_create_category(self):
        self.url = reverse('category-list')
        response = self.client.post(
            self.url, {'code': 'CAT1', 'title': 'Category 1'}, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['code'], 'CAT1')
        self.assertEqual(response.data['title'], 'Category 1')

    def test_create_category_with_empty_data(self):
        self.url = reverse('category-list')
        response = self.client.post(
            self.url, {'code': '', 'title': ''}, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['code'][0],
                         'This field may not be blank.')

    def test_delete_category(self):
        self.url = reverse('category-list')
        response = self.client.post(
            self.url, {'code': 'CAT1', 'title': 'Category 1'}, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['code'], 'CAT1')
        self.assertEqual(response.data['title'], 'Category 1')
        self.url = reverse('category-detail', args=[response.data['id']])
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, 204)

    def test_delete_category_with_invalid_id(self):
        self.url = reverse('category-detail', args=[9999])
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, 404)

    def test_update_category(self):
        self.url = reverse('category-list')
        response = self.client.post(
            self.url, {'code': 'CAT1', 'title': 'Category 1'}, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['code'], 'CAT1')
        self.assertEqual(response.data['title'], 'Category 1')
        self.url = reverse('category-detail', args=[response.data['id']])
        response = self.client.put(
            self.url, {'code': 'CAT2', 'title': 'Category 2'}, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['code'], 'CAT2')
        self.assertEqual(response.data['title'], 'Category 2')

    def test_update_category_with_empty_data(self):
        self.url = reverse('category-list')
        response = self.client.post(
            self.url, {'code': 'CAT1', 'title': 'Category 1'}, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['code'], 'CAT1')
        self.assertEqual(response.data['title'], 'Category 1')
        self.url = reverse('category-detail', args=[response.data['id']])
        response = self.client.put(
            self.url, {'code': '', 'title': ''}, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['code'][0],
                         'This field may not be blank.')

    def test_get_category(self):
        self.url = reverse('category-list')
        response = self.client.post(
            self.url, {'code': 'CAT1', 'title': 'Category 1'}, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['code'], 'CAT1')
        self.assertEqual(response.data['title'], 'Category 1')
        self.url = reverse('category-detail', args=[response.data['id']])
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['code'], 'CAT1')
        self.assertEqual(response.data['title'], 'Category 1')

    def test_get_category_with_invalid_id(self):
        self.url = reverse('category-detail', args=[9999])
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 404)

    def test_get_category_list(self):
        self.url = reverse('category-list')
        response = self.client.post(
            self.url, {'code': 'CAT1', 'title': 'Category 1'}, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['code'], 'CAT1')
        self.assertEqual(response.data['title'], 'Category 1')
        self.url = reverse('category-list')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['code'], 'CAT1')
        self.assertEqual(response.data[0]['title'], 'Category 1')

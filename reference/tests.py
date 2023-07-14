from django.urls import reverse
from rest_framework import status
from .models import Case
from .serializers import CaseSerializer
import json
from vamt_api.tests import AuthenticatedTestCase


class CaseAPITestCase(AuthenticatedTestCase):
    def setUp(self):
        super().setUp()

    def test_create_case(self):
        # Define the payload
        payload = {
            "name": "Test Case",
            "year": "2022",
            "type": "civil"
        }
        # Send the POST request to create a case
        response = self.client.post(
            "/cases/", data=payload, format="json"
        )

        # Assert the response status code
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Assert the created case in the database
        case = Case.objects.get(pk=response.data["id"])
        self.assertEqual(case.name, "Test Case")
        self.assertEqual(case.year, "2022")
        self.assertEqual(case.type, "civil")

        # Assert the serialized response data
        serializer = CaseSerializer(instance=case)
        self.assertEqual(response.data, serializer.data)


class CaseViewTest(AuthenticatedTestCase):
    def setUp(self):
        super().setUp()
        self.list_url = '/cases/'
        self.case1 = Case.objects.create(
            name='Case 1', year='2022', type='civil')
        self.case2 = Case.objects.create(
            name='Case 2', year='2023', type='criminal')

    def test_list_cases(self):
        response = self.client.get(self.list_url, headers=self.headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Case.objects.count())

    def test_list_cases_data(self):
        response = self.client.get(self.list_url, headers=self.headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['name'], self.case1.name)
        self.assertEqual(response.data[0]['year'], self.case1.year)
        self.assertEqual(response.data[0]['type'], self.case1.type)
        self.assertEqual(response.data[1]['name'], self.case2.name)
        self.assertEqual(response.data[1]['year'], self.case2.year)
        self.assertEqual(response.data[1]['type'], self.case2.type)


class CaseUpdateViewTest(AuthenticatedTestCase):
    def setUp(self):
        super().setUp()
        self.case = Case.objects.create(
            name='Case 1', year='2022', type='civil')
        self.update_url = reverse(
            'case-retrieve-update', kwargs={'id': self.case.id})

    def test_update_case(self):
        updated_data = {
            'name': 'Updated Case',
            'year': '2023',
            'type': 'criminal'
        }
        response = self.client.put(self.update_url, data=json.dumps(
            updated_data), content_type='application/json', headers=self.headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.case.refresh_from_db()
        self.assertEqual(self.case.name, updated_data['name'])
        self.assertEqual(self.case.year, updated_data['year'])
        self.assertEqual(self.case.type, updated_data['type'])

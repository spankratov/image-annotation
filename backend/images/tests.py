import json
from rest_framework.test import APITestCase


class ImageAPITestCase(APITestCase):
    default_annotation = {
        'labels':
            [
                {
                    'meta':
                        {
                             'confirmed': False,
                             'confidence_percent': 0.99
                        },
                    'id': '5b0cd508-587b-493b-98ea-b08a8c31d575',
                    'class_id': 'tooth',
                    'surface': ['B', 'O', 'L'],
                    'shape':
                        {
                            'endX': 983,
                            'endY': 1399,
                            'startY': 605,
                            'startX': 44
                        }
                },
                {
                    'meta':
                        {
                            'confirmed': True,
                            'confidence_percent': 0.99
                        },
                    'id': '13f9d698-8c3c-4948-80c9-50adab2d6e7c',
                    'class_id': 'tooth',
                    'surface': ['B', 'O', 'L'],
                    'shape':
                        {
                            'endX': 983,
                            'endY': 1399,
                            'startY': 605,
                            'startX': 44
                        }
                }
            ],
    }

    default_export_annotation = {
        'labels':
            [
                {
                    'id': '13f9d698-8c3c-4948-80c9-50adab2d6e7c',
                    'class_id': 'tooth',
                    'surface': 'BOL',
                }
            ],
    }

    def setUp(self) -> None:
        with open('tests/test_image.jpg', 'rb') as file:
            response = self.client.post(
                '/images/',
                {'file': file, 'annotation': json.dumps(self.default_annotation)},
            )
            self.image_id = response.data['id']

    def test_create(self):
        with open('tests/test_image.jpg', 'rb') as file:
            response = self.client.post(
                '/images/',
                {'file': file},
            )
            self.assertTrue('id' in response.data)
            self.assertTrue('file' in response.data)
            self.assertTrue('annotation' in response.data)
            self.assertEqual(response.data['annotation'], {'labels': []})

        with open('tests/test_image.jpg', 'rb') as file:
            response = self.client.post(
                '/images/',
                {'file': file, 'annotation': json.dumps(self.default_annotation)},
            )
            self.assertTrue('id' in response.data)
            self.assertTrue('file' in response.data)
            self.assertTrue('annotation' in response.data)
            self.assertEqual(response.data['annotation'], self.default_annotation)

    def test_get_annotation(self):
        response = self.client.get(f'/images/{self.image_id}/')
        self.assertEqual(response.data['annotation'], self.default_annotation)
        response = self.client.get(f'/images/{self.image_id}/?format=export')
        self.assertEqual(response.data['annotation'], self.default_export_annotation)

    def test_update_annotation(self):
        with open('tests/test_image.jpg', 'rb') as file:
            response = self.client.post(
                '/images/',
                {'file': file, 'annotation': json.dumps(self.default_annotation)},
            )
            image_id = response.data['id']

        new_annotation = {'labels': [self.default_annotation['labels'][0]]}

        self.client.put(
            f'/images/{image_id}/',
            {'annotation': new_annotation},
            format='json',
        )
        response = self.client.get(f'/images/{image_id}/')
        self.assertEqual(response.data['annotation'], new_annotation)

        incorrect_annotation = {'labels': {}}
        response = self.client.put(
            f'/images/{image_id}/',
            {'annotation': json.dumps(incorrect_annotation)},
            format='json',
        )
        self.assertEqual(response.status_code, 400)

    def test_get_url(self):
        response = self.client.get(f'/images/{self.image_id}/')
        self.assertTrue(response.data['file'].endswith('.jpg'))

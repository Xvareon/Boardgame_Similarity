from rest_framework.test import APITestCase
from django.urls import reverse
from unittest.mock import patch

class SimilarityAPITest(APITestCase):
    @patch('api.utils.get_user_ratings')
    def test_similarity_endpoint(self, mock_ratings):
        mock_ratings.side_effect = [
            {1:5, 2:4},  # user1
            {1:4, 2:5}   # user2
        ]
        response = self.client.get(reverse('similarity') + '?user1=u1&user2=u2')
        self.assertEqual(response.status_code, 200)
        self.assertIn('similarity_score', response.data)

    @patch('api.utils.get_user_ratings')
    def test_similar_users_endpoint(self, mock_ratings):
        mock_ratings.side_effect = [
            {1:5, 2:4},  # target
            {1:5, 2:5},  # user1
            {1:1, 2:1},  # user2
        ]
        response = self.client.get(reverse('similar_users') + '?username=target')
        self.assertEqual(response.status_code, 200)
        self.assertIn('similar_users', response.data)
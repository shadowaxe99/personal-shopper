```python
import unittest
from unittest.mock import patch
from src import backend_infrastructure as bi

class TestBackendInfrastructure(unittest.TestCase):

    @patch('src.backend_infrastructure.AWS')
    def test_aws_connection(self, mock_aws):
        mock_aws.connect.return_value = True
        result = bi.connect_to_aws()
        self.assertTrue(result)

    @patch('src.backend_infrastructure.GoogleCloud')
    def test_google_cloud_connection(self, mock_gc):
        mock_gc.connect.return_value = True
        result = bi.connect_to_google_cloud()
        self.assertTrue(result)

    @patch('src.backend_infrastructure.AWS')
    def test_aws_data_storage(self, mock_aws):
        mock_aws.store_data.return_value = True
        result = bi.store_data_aws('userProfileData')
        self.assertTrue(result)

    @patch('src.backend_infrastructure.GoogleCloud')
    def test_google_cloud_data_storage(self, mock_gc):
        mock_gc.store_data.return_value = True
        result = bi.store_data_google_cloud('userProfileData')
        self.assertTrue(result)

    @patch('src.backend_infrastructure.AWS')
    def test_aws_data_retrieval(self, mock_aws):
        mock_aws.retrieve_data.return_value = 'userProfileData'
        result = bi.retrieve_data_aws()
        self.assertEqual(result, 'userProfileData')

    @patch('src.backend_infrastructure.GoogleCloud')
    def test_google_cloud_data_retrieval(self, mock_gc):
        mock_gc.retrieve_data.return_value = 'userProfileData'
        result = bi.retrieve_data_google_cloud()
        self.assertEqual(result, 'userProfileData')

if __name__ == '__main__':
    unittest.main()
```
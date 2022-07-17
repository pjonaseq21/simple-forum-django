from django.test import TestCase

# Create your tests here.
class HomePageTest(TestCase):
    def test_status_code(self):
        response = self.client.get("/")
        print(response.content)

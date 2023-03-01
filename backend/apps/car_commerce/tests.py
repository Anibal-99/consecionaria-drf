from django.test import TestCase, SimpleTestCase
from .models import Region

# Create your tests here.

class RegionModelTest(TestCase):

    def test_region_models_exists(self):
        region=Region.objects.count()

        self.assertEqual(region, [])

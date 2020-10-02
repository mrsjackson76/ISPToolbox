from django.test import TestCase
from IspToolboxApp.Models.MarketingConvertModels import MarketingPinConversion
from IspToolboxApp.Tasks.MarketingPinConversionTasks import ConvertPins
from django.contrib.gis.geos import GEOSGeometry

from .static_test_data import exclude_polygon_collection, \
    include_geometry_collection, include_complex_1, exclude_simple_1, \
    include_simple, exclude_simple


class TestMarketingConversionModels(TestCase):
    def test_models_simple(self):
        conversion = MarketingPinConversion(
            include=GEOSGeometry(include_geometry_collection),
            exclude=GEOSGeometry(exclude_polygon_collection),
            num_pins=100
        )
        conversion.save()
        ConvertPins(conversion.uuid)
        conversion.refresh_from_db()
        self.assertEqual(len(conversion.include_output), 8)
        self.assertTrue(conversion.include_output is not None)

    def test_models_complex(self):
        conversion = MarketingPinConversion(
            include=GEOSGeometry(include_complex_1),
            exclude=GEOSGeometry( exclude_simple_1),
            num_pins=100
        )
        conversion.save()
        ConvertPins(conversion.uuid)
        conversion.refresh_from_db()
        print(conversion.error)
        self.assertTrue(len(conversion.include_output) > 0)
        self.assertTrue(conversion.include_output is not None)

    def test_simple_subtraction(self):
        conversion = MarketingPinConversion(
            include=GEOSGeometry(include_simple),
            exclude=GEOSGeometry(exclude_simple),
            num_pins=100
        )
        conversion.save()
        ConvertPins(conversion.uuid)
        conversion.refresh_from_db()
        self.assertTrue(len(conversion.include_output) > 0)
        self.assertTrue(conversion.include_output is not None)
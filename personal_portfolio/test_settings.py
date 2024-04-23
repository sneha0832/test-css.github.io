from django.test import TestCase
from django.db import connections

class DatabaseConnectionTest(TestCase):
    def test_database_connection(self):
        with connections['default'].cursor() as cursor:
            cursor.execute("SELECT 1")
        
        #if the cursor executed without raising an exception, the database connection is successful
        self.assertEqual(cursor.fetchone()[0], 1)

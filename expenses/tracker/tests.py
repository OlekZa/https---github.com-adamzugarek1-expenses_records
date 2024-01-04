from django.test import TestCase
from django.urls import reverse


class ViewTestCase(TestCase):
    def test_display_expense_list(self):
        response = self.client.get(reverse("expense_list"))
        self.assertEqual(response.status_code, 200)

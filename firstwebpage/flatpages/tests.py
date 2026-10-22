from django.test import TestCase
from django.urls import reverse


class Lab2StagesTests(TestCase):
    def test_initial_plain_text_step_is_preserved(self):
        response = self.client.get(reverse("initial_text_stage"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode("utf-8"), "Привет, Мир!")
        self.assertEqual(response["Content-Type"], "text/plain; charset=utf-8")

    def test_hello_returns_same_explicit_plain_text(self):
        response = self.client.get(reverse("hello"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode("utf-8"), "Привет, Мир!")
        self.assertEqual(response["Content-Type"], "text/plain; charset=utf-8")

    def test_hello_plain_uses_django_default_content_type(self):
        response = self.client.get(reverse("hello_plain"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode("utf-8"), "Привет, Мир!")
        self.assertEqual(response["Content-Type"], "text/html; charset=utf-8")

    def test_root_is_green_base_index_with_four_columns_and_five_rows(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        html = response.content.decode("utf-8")
        self.assertIn("background: #1abc9c", html)
        self.assertIn("Столбик 4", html)
        self.assertNotIn("Столбик 5", html)
        self.assertEqual(html.count("<tr>"), 6)  # header + 5 data rows

    def test_table_stage_has_added_rows_columns_borders_and_h4_labels(self):
        response = self.client.get(reverse("table_stage"))
        self.assertEqual(response.status_code, 200)
        html = response.content.decode("utf-8")
        self.assertIn("Столбик 6", html)
        self.assertIn("Строка 7 Столбец 6", html)
        self.assertIn('<table border="1"', html)
        self.assertIn("<h4>Здесь есть маркированный список:</h4>", html)
        self.assertIn("<h4>И нумерованный список:</h4>", html)
        self.assertEqual(html.count("<tr>"), 8)  # header + 7 data rows

    def test_static_handler_is_styled_copy_with_image(self):
        response = self.client.get(reverse("static_handler"))
        self.assertEqual(response.status_code, 200)
        html = response.content.decode("utf-8")
        self.assertIn("Столбик 6", html)
        self.assertIn("Строка 7 Столбец 6", html)
        self.assertIn("/static/index.css", html)
        self.assertIn("/static/finance_chart.svg", html)
        self.assertNotIn("{% static", html)
        self.assertEqual(html.count("<tr>"), 8)  # header + 7 data rows

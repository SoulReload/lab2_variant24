from django.test import TestCase
from django.urls import reverse


class FinancialReportingLab2Tests(TestCase):
    def test_preserved_initial_plain_text_stage(self):
        response = self.client.get(reverse("initial_text_stage"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode("utf-8"), "Привет, Мир!")
        self.assertEqual(response["Content-Type"], "text/plain; charset=utf-8")

    def test_hello_has_explicit_plain_text_type(self):
        response = self.client.get(reverse("hello"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode("utf-8"), "Привет, Мир!")
        self.assertEqual(response["Content-Type"], "text/plain; charset=utf-8")

    def test_hello_plain_uses_default_content_type(self):
        response = self.client.get(reverse("hello_plain"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode("utf-8"), "Привет, Мир!")
        self.assertEqual(response["Content-Type"], "text/html; charset=utf-8")

    def test_financial_index_is_green_and_has_five_data_rows(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        html = response.content.decode("utf-8")
        self.assertIn("background: #1abc9c", html)
        self.assertIn("Анализ финансовой отчётности", html)
        self.assertIn("Предприятие «Север»", html)
        self.assertEqual(html.count("<tr>"), 6)  # header + 5 data rows
        self.assertNotIn("Коэффициент важности", html)

    def test_table_stage_adds_two_columns_and_two_rows_and_borders(self):
        response = self.client.get(reverse("table_stage"))
        self.assertEqual(response.status_code, 200)
        html = response.content.decode("utf-8")
        self.assertIn("Коэффициент важности", html)
        self.assertIn("Предприятие «Импульс»", html)
        self.assertIn('<table border="1"', html)
        self.assertIn("<h4>Показатели для анализа:</h4>", html)
        self.assertIn("<h4>Этапы обработки:</h4>", html)
        self.assertEqual(html.count("<tr>"), 8)  # header + 7 data rows

    def test_static_handler_loads_css_and_financial_image(self):
        response = self.client.get(reverse("static_handler"))
        self.assertEqual(response.status_code, 200)
        html = response.content.decode("utf-8")
        self.assertIn("/static/index.css", html)
        self.assertIn("/static/finance_chart.svg", html)
        self.assertIn("Условные учебные курсы", html)
        self.assertIn("Коэффициент важности", html)
        self.assertEqual(html.count("<tr>"), 12)  # main table 8 rows + rate table 4 rows

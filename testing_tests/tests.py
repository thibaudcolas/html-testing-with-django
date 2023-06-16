from django.test import TestCase
from django.http import HttpResponse


class TestingTestsTestingTests(TestCase):
    def test_assertInHTML(self):
        self.assertInHTML("<b>hey</b>", "<p>Howdy!</p>")

    def test_assertIn(self):
        self.assertIn("<b>hey</b>", "<p>Howdy!</p>")

    def test_assertHTMLEqual(self):
        self.assertHTMLEqual("<b>hey</b>", "<p>Howdy!</p>")

    def test_assertEqual(self):
        self.assertEqual("<b>hey</b>", "<p>Howdy!</p>")

    def test_assertContains(self):
        res = HttpResponse()
        res.content = b"<p>Howdy!</p>"
        res.status_code = 200
        self.assertContains(res, "<b>hey</b>")

    def test_assertRegex(self):
        self.assertRegex("<p>Howdy!</p>", r"<b>hey<\b>")

from django.core.urlresolvers import reverse
from django.test import TestCase


class Test(TestCase):
    def _test_test0(self, count=1):
        for i in xrange(count):
            response = self.client.get(reverse('djmemts:0', args=[]), {'v': i})
            self.assertEqual(response.status_code, 200)

    def test_test0(self):
        self._test_test0()

    def test_test0_multi(self):
        self._test_test0(count=3)

    def test_test0_crazy(self):
        self._test_test0(count=10000)

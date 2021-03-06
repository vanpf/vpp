#!/usr/bin/env python

import unittest

from framework import VppTestCase, VppTestRunner
from vpp_ip_route import VppIpTable, VppIpRoute, VppRoutePath


class TestTCP(VppTestCase):
    """ Bihash Test Cases """

    @classmethod
    def setUpClass(cls):
        super(TestTCP, cls).setUpClass()

    def setUp(self):
        super(TestTCP, self).setUp()

    def tearDown(self):
        super(TestTCP, self).tearDown()

    def test_bihash_unittest(self):
        """ Bihash Add/Del Test """
        error = self.vapi.cli("test bihash ")

        if error:
            self.logger.critical(error)
        self.assertEqual(error.find("failed"), -1)

    def test_bihash_thread(self):
        """ Bihash Thread Test """

        error = self.vapi.cli("test bihash threads 2 nbuckets 64000")

        if error:
            self.logger.critical(error)
            self.assertEqual(error.find("failed"), -1)

if __name__ == '__main__':
    unittest.main(testRunner=VppTestRunner)

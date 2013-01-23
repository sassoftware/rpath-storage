#
# Copyright (c) SAS Institute Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


import tempfile

from testrunner import testhelp

from conary.lib import util

class TestCase(testhelp.TestCase):
    def setUp(self):
        testhelp.TestCase.setUp(self)
        self.workDir = tempfile.mkdtemp(prefix='catalog-service-test-')

    def tearDown(self):
        testhelp.TestCase.tearDown(self)
        util.rmtree(self.workDir, ignore_errors = True)

    @staticmethod
    def normalizeXML(data):
        """lxml will produce the header with single quotes for its attributes,
        while xmllint uses double quotes. This function normalizes the data"""
        return data.replace(
            "<?xml version='1.0' encoding='UTF-8'?>",
            '<?xml version="1.0" encoding="UTF-8"?>').strip()

    def assertXMLEquals(self, first, second):
        self.failUnlessEqual(self.normalizeXML(first),
                             self.normalizeXML(second))

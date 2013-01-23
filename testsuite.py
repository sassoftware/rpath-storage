#!/usr/bin/python
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


import sys

from testrunner import suite

class Suite(suite.TestSuite):
    testsuite_module = sys.modules[__name__]

    def getCoverageDirs(self, *args):
        import rpath_storage
        return [rpath_storage]


_s = Suite()
setup = _s.setup
main = _s.main

if __name__ == '__main__':
    _s.run()

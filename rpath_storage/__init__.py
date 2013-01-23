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


"""
The rPath Common Library Module for XML parsing.

This module provides a stable interface for reading and writing
rPath-generated XML files.  This interface will be
backward-compatible within major versions of this package.
The C{VERSION} data element is a string containing the version.
The portion of the string before the initial C{.} charater is the
major version.

All interfaces in this modules that do not start with a C{_}
character are public interfaces.

If the C{VERSION} starts with C{0.}, none of the included
interfaces is stable and they may change without warning.

To use the latest version of the interface::

    from rpath_common import storage

To use a specific API Version of the interface::

    from rpath_common.storage import api1 as storage
"""

# Default to current API version
#pylint: disable-msg=W0401
from rpath_storage.api1 import *

# Import the automatically-generated VERSION
#pylint: disable-msg=W0212
from rpath_storage.storage_constants import _VERSION as VERSION

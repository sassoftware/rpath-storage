#
# Copyright (c) 2008 rPath, Inc.
#
# This program is distributed under the terms of the Common Public License,
# version 1.0. A copy of this license should have been distributed with this
# source file in a file called LICENSE. If it is not present, the license
# is always available at http://www.rpath.com/permanent/licenses/CPL-1.0.
#
# This program is distributed in the hope that it will be useful, but
# without any warranty; without even the implied warranty of merchantability
# or fitness for a particular purpose. See the Common Public License for
# full details.
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

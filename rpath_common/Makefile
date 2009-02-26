#
# Copyright (c) 2006-2008 rPath, Inc.
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

# Note: do not list __init__.py in python_files -- it is here only
# to support testing out of the tree.  When distributed, this
# file is provided by the rpath-common package instead.

SUBDIRS=storage
SYMLINKS = xmllib

dist_files = Makefile __init__.py

all: default-all default-subdirs symlinks

install: all default-install install-subdirs

dist: default-dist

clean: default-clean clean-symlinks

clean-symlinks:
	@rm -f $(SYMLINKS)

symlinks:
	[ -z "$$XMLLIB_PATH" ] || [ -h xmllib ] || ln -s $$XMLLIB_PATH/rpath_common/xmllib .


include ../Make.rules
include ../Make.defs

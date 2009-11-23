
# Copyright (c) 2008-2009 rPath, Inc.
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

module = storage

python_files =	__init__.py \
		api1.py

dist_files = Makefile $(module)_constants.py.in $(python_files)

all: default-all $(module)_constants.py

$(module)_constants.py: $(module)_constants.py.in ../Makefile ../Make.defs Makefile
	sed -e s,@version@,$(VERSION),g \
	$< > $@

install: all pyfiles-install default-install
	install $(module)_constants.py $(DESTDIR)$(pydir)/$(module)_constants.py
	$(PYTHON) -c "import compileall; compileall.compile_dir('$(DESTDIR)$(pydir)', ddir='$(pydir)', quiet=1)"
	$(PYTHON) -OO -c "import compileall; compileall.compile_dir('$(DESTDIR)$(pydir)', ddir='$(pydir)', quiet=1)"

dist: default-dist

clean: default-clean
	rm -f $(module)_constants.py

include ../Make.rules
include ../Make.defs
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


import os

import testbase
from rpath_storage import api1 as storage


class StorageConfig(object):
    __slots__ = [ 'storagePath' ]

class StorageTest(testbase.TestCase):
    def setUp(self):
        testbase.TestCase.setUp(self)
        self.storageCfg = StorageConfig
        self.storageCfg.storagePath = os.path.join(self.workDir, 'storageTest')
        self.diskStorage = storage.DiskStorage(self.storageCfg)

    def testDiskBasedStorage(self):
        stg = self.diskStorage

        nk = stg.store(42)
        expPath = os.path.join(self.storageCfg.storagePath, nk)
        self.failUnless(os.path.exists(expPath))
        self.failUnlessEqual(file(expPath).read(), "42")
        self.failUnlessEqual(stg.get(nk), "42")
        self.failUnless(stg.exists(nk))
        self.failUnlessEqual(stg.getFileFromKey(nk), expPath)

        nk = stg.store(42, keyPrefix = '11')
        expPath = os.path.join(self.storageCfg.storagePath, nk)
        self.failUnless(nk.startswith('11/'))
        self.failUnless(os.path.exists(expPath))
        self.failUnlessEqual(file(expPath).read(), "42")
        self.failUnlessEqual(stg.get(nk), "42")
        self.failUnlessEqual(stg[nk], "42")
        self.failUnless(stg.exists(nk))

        stg.set(nk, 43)
        self.failUnlessEqual(stg[nk], "43")

        stg[nk] =  44
        self.failUnlessEqual(stg[nk], "44")

        self.failUnlessEqual(stg.get('adfadfadf'), None)
        self.failUnlessEqual(stg.get('adfadfadf', '123'), '123')
        self.failIf(stg.exists('adfadfadf'))

        self.failUnlessRaises(storage.InvalidKeyError,
                              stg.exists, 'a/../b')
        self.failUnlessRaises(storage.InvalidKeyError,
                              stg.exists, '/a/b')
        self.failUnlessRaises(storage.InvalidKeyError,
                              stg.exists, 'a//b')

        self.failUnlessRaises(storage.KeyNotFoundError,
                              stg.__getitem__, 'nosuchkey')

        # Test enumerating the keys
        keys = [ stg.store(str(x), keyPrefix = 'enum') for x in range(3) ]
        keys.sort()
        self.failUnlessEqual(keys, stg.enumerate(keyPrefix = 'enum'))

        self.failUnlessEqual(stg.isCollection('enum'), True)
        self.failUnlessEqual(stg.isCollection('abc'), False)
        self.failUnlessEqual(stg.isCollection(nk), False)

        # Create an empty collection
        stg.newCollection('bleep')
        self.failUnlessEqual(stg.isCollection('bleep'), True)
        self.failUnlessEqual(stg.enumerate(keyPrefix = 'bleep'), [])

        # Create an empty collection, with a random name
        ncoll = stg.newCollection(keyPrefix = "collections")
        self.failUnless(ncoll.startswith("collections/"), ncoll)
        self.failUnlessEqual(stg.isCollection(ncoll), True)
        self.failUnlessEqual(stg.enumerate(keyPrefix = ncoll), [])

        # Delete a collection
        stg.delete('enum')
        self.failUnlessEqual(stg.enumerate(keyPrefix = 'enum'), [])
        self.failUnlessEqual(stg.get('enum'), None)

        # Mock exists to always return true, to test the key failure exception
        self.mock(stg, "exists", lambda x: True)
        self.failUnless(stg.exists('adfadfadf'))

        e = self.failUnlessRaises(storage.StorageError,
                                  stg.store, '123')
        self.failUnlessEqual(str(e), 'Failed to generate a new key')

    def testEnumerateAll(self):
        stg = self.diskStorage
        stg.set("a/a0/a00", "a00")
        stg.set("a/a0/a01", "a01")
        stg.set("a/a1/a10", "a10")
        stg.set("a/a1/a11", "a11")
        stg.set("a/a2", "a2")
        stg.set("b", "b")
        self.failUnlessEqual(
            [ x for x in stg.enumerateAll() ],
            [ 'a/a2', 'a/a1/a11', 'a/a1/a10', 'a/a0/a01', 'a/a0/a00', 'b' ])

    def testSetFields(self):
        stg = self.diskStorage
        stg.setFields(
            [ (("a/a0", "a00"), "a00"), ("a/a0/a01", "a01"),
                ("a/a1/a10", "a10"), ("a/a1/a11", "a11"),
                ("a/a2", "a2"), ("b", "b") ])
        self.failUnlessEqual(
            [ x for x in stg.enumerateAll() ],
            [ 'a/a2', 'a/a1/a11', 'a/a1/a10', 'a/a0/a01', 'a/a0/a00', 'b' ])
        # Remove a01
        stg.setFields(
            [ (("a/a0", "a00"), "b00"), ("a/a0/a01", None) ])
        self.failUnlessEqual(
            [ x for x in stg.enumerateAll() ],
            [ 'a/a2', 'a/a1/a11', 'a/a1/a10', 'a/a0/a00', 'b' ])

    def testDelete(self):
        stg = self.diskStorage
        stg.setFields( [(('a', 'a1'), 'a1'), (('a', 'a2'), 'a2') ] )
        self.failUnlessEqual(
            sorted([ x for x in stg.enumerateAll() ]),
            [ 'a/a1', 'a/a2'])
        stg.delete(('a', 'a2'))
        self.failUnlessEqual(
            [ x for x in stg.enumerateAll() ],
            [ 'a/a1'])

    def testNewKey(self):
        stg = self.diskStorage
        key = stg.newKey(('a0', 'a1'))
        stg.set(key, 'blah')
        self.failUnlessEqual(
            [ x for x in stg.enumerateAll() ],
            [ key ])
        self.failUnlessEqual(stg.get(key), 'blah')
        # Dummy
        stg.commit()

    def testBaseStorage(self):
        stg = storage.BaseStorage()
        self.failUnlessRaises(NotImplementedError, stg._real_exists, 'a')
        self.failUnlessRaises(NotImplementedError, stg._real_get, 'a')
        self.failUnlessRaises(NotImplementedError, stg._real_set, 'a', 'a')
        self.failUnlessRaises(NotImplementedError, stg._real_enumerate, 'a')
        self.failUnlessRaises(NotImplementedError, stg._real_is_collection, 'a')

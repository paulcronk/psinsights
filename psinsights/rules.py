###############################################################################
# Copyright 2012 FastSoft Inc.
# Copyright 2012 Devin Anderson <danderson (at) fastsoft (dot) com>
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License.  You may obtain a copy
# of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  See the
# License for the specific language governing permissions and limitations under
# the License.
###############################################################################

from psinsights.rule import Rule as _Rule

class Rules(object):

    def __contains__(self, name):
        return name in self.__data

    def __del__(self):
        self.__data = None
        self.__rule_map = None

    def __getitem__(self, name):
        rule = self.get(name)
        if rule is None:
            raise KeyError(name)
        return rule

    def __init__(self, data):
        self.__data = data
        self.__rule_map = {}

    def __iter__(self):
        return self.__data.iterkeys()

    def __len__(self):
        return len(self.__data)

    def get(self, name, default=None):
        rule_map = self.__rule_map
        rule = rule_map.get(name)
        if rule is None:
            data = self.__data
            rule_data = data.get(name)
            if rule_data is None:
                return default
            rule = _Rule(rule_data)
            rule_map[name] = rule
        return rule

    def items(self):
        return list(self.iteritems())

    def iteritems(self):
        get = self.get
        return ((k, get(k)) for k in self.__data.iterkeys())

    iterkeys = __iter__

    def itervalues(self):
        get = self.get
        return (get(k) for k in self.__data.iterkeys())

    def keys(self):
        return list(iter(self))

    def values(self):
        return list(self.itervalues())

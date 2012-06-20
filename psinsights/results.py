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

from psinsights.rules import Rules as _Rules

class Results(object):

    __rules = None

    def __del__(self):
        self.__data = None
        self.__rules = None

    def __init__(self, data):
        self.__data = data

    @property
    def locale(self):
        return self.__data["locale"]

    @property
    def rules(self):
        rules = self.__rules
        if rules is None:
            rules = _Rules(self.__data["ruleResults"])
            self.__rules = rules
        return rules

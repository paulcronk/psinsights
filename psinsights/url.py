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

from psinsights.message import Message as _Message

class URL(object):

    __details = None
    __result = None

    def __del__(self):
        self.__data = None
        self.__details = None
        self.__result = None

    def __init__(self, data):
        self.__data = data

    @property
    def details(self):
        details = self.__details
        if details is None:
            details_data = self.__data.get("details")
            if details_data is None:
                details = tuple()
            else:
                details = tuple(_Message(d) for d in details_data)
            self.__details = details
        return details

    @property
    def result(self):
        result = self.__result
        if result is None:
            result = _Message(self.__data["result"])
            self.__result = result
        return result

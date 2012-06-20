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

class Issue(object):

    def __del__(self):
        self.__data = None

    def __init__(self, data):
        self.__data = data

    @property
    def domain(self):
        return self.__data["domain"]

    @property
    def location(self):
        return self.__data["location"]

    @property
    def location_type(self):
        return self.__data["locationType"]

    @property
    def message(self):
        return self.__data["message"]

    @property
    def reason(self):
        return self.__data["reason"]

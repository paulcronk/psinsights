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

from psinsights.issue import Issue as _Issue

class Error(Exception):

    """Exception class for service errors."""

    __issues = None

    def __del__(self):
        self.__data = None
        self.__issues = None

    def __init__(self, data):
        data = data["error"]
        code = data["code"]
        message = data["message"]
        super(Error, self).__init__((message, code))
        self.__code = code
        self.__data = data
        self.__message = message

    @property
    def code(self):
        return self.__code

    @property
    def issues(self):
        issues = self.__issues
        if issues is None:
            issues = tuple((_Issue(d) for d in self.__data["errors"]))
            self.__issues = issues
        return issues

    @property
    def message(self):
        return self.__message

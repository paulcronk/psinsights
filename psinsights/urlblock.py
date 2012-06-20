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
from psinsights.url import URL as _URL

class URLBlock(object):

    __header = None
    __urls = None

    def __del__(self):
        self.__data = None
        self.__header = None
        self.__urls = None

    def __init__(self, data):
        self.__data = data

    @property
    def header(self):
        header = self.__header
        if header is None:
            header = _Message(self.__data["header"])
            self.__header = header
        return header

    @property
    def urls(self):
        urls = self.__urls
        if urls is None:
            url_data = self.__data.get("urls")
            if url_data is None:
                urls = tuple()
            else:
                urls = tuple(_URL(d) for d in url_data)
            self.__urls = urls
        return urls

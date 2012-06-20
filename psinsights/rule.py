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

from psinsights.urlblock import URLBlock as _URLBlock

class Rule(object):

    __url_blocks = None

    def __del__(self):
        self.__data = None
        self.__url_blocks = None

    def __init__(self, data):
        self.__data = data

    @property
    def impact(self):
        return self.__data["ruleImpact"]

    @property
    def localized_name(self):
        return self.__data["localizedRuleName"]

    @property
    def score(self):
        return self.__data["ruleScore"]

    @property
    def url_blocks(self):
        url_blocks = self.__url_blocks
        if url_blocks is None:
            block_data = self.__data.get("urlBlocks")
            if block_data is None:
                url_blocks = tuple()
            else:
                url_blocks = tuple((_URLBlock(d) for d in block_data))
            self.__url_blocks = url_blocks
        return url_blocks

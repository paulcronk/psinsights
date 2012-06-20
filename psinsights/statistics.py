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

class Statistics(object):

    def __del__(self):
        self.__data = None

    def __init__(self, data):
        self.__data = data

    @property
    def css_resource_count(self):
        return self.__data.get("numberCssResources", 0)

    @property
    def css_response_bytes(self):
        return self.__data.get("cssResponseBytes", 0)

    @property
    def flash_response_bytes(self):
        return self.__data.get("flashResponseBytes", 0)

    @property
    def host_count(self):
        return self.__data.get("numberHosts", 0)

    @property
    def html_response_bytes(self):
        return self.__data.get("htmlResponseBytes", 0)

    @property
    def image_response_bytes(self):
        return self.__data.get("imageResponseBytes", 0)

    @property
    def javascript_resource_count(self):
        return self.__data.get("numberJsResources", 0)

    @property
    def javascript_response_bytes(self):
        return self.__data.get("javascriptResponseBytes", 0)

    @property
    def other_response_bytes(self):
        return self.__data.get("otherResponseBytes", 0)

    @property
    def resource_count(self):
        return self.__data.get("numberResources", 0)

    @property
    def static_resource_count(self):
        return self.__data.get("numberStaticResources", 0)

    @property
    def text_response_bytes(self):
        return self.__data.get("textResponseBytes", 0)

    @property
    def total_request_bytes(self):
        return self.__data.get("totalRequestBytes", 0)

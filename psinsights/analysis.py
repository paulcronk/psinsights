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

from json import dumps as _dumps

from psinsights.results import Results as _Results
from psinsights.statistics import Statistics as _Statistics
from psinsights.version import Version as _Version

class Analysis(object):

    __invalid_rules = None
    __results = None
    __statistics = None
    __version = None

    def __del__(self):
        self.__data = None
        self.__invalid_rules = None
        self.__results = None
        self.__statistics = None
        self.__version = None

    def __init__(self, data):
        self.__data = data

    @property
    def id(self):
        return self.__data["id"]

    @property
    def invalid_rules(self):
        invalid_rules = self.__invalid_rules
        if invalid_rules is None:
            invalid_rules_data = self.__data.get("invalidRules")
            if invalid_rules_data is None:
                invalid_rules = tuple()
            else:
                invalid_rules = tuple(invalid_rules_data)
            self.__invalid_rules = invalid_rules
        return invalid_rules

    @property
    def kind(self):
        return self.__data["kind"]

    @property
    def raw_data(self):
        return _dumps(self.__data, indent=4, sort_keys=True)

    @property
    def response_code(self):
        return self.__data["responseCode"]

    @property
    def results(self):
        results = self.__results
        if results is None:
            results = _Results(self.__data["formattedResults"])
            self.__results = results
        return results

    @property
    def score(self):
        return self.__data["score"]

    @property
    def statistics(self):
        statistics = self.__statistics
        if statistics is None:
            statistics = _Statistics(self.__data["pageStats"])
            self.__statistics = statistics
        return statistics

    @property
    def title(self):
        return self.__data["title"]

    @property
    def version(self):
        version = self.__version
        if version is None:
            version = _Version(self.__data["version"])
            self.__version = version
        return version

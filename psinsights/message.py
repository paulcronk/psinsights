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

from psinsights.argument import Argument as _Argument

class Message(object):

    __arguments = None
    __message = None

    def __del__(self):
        self.__arguments = None
        self.__data = None
        self.__message = None

    def __init__(self, data):
        self.__data = data

    def __unicode__(self):
        message = self.__message
        if message is None:
            arguments = self.arguments
            message = self.format
            for i in xrange(len(arguments)):
                argument = arguments[i]
                value = argument.value
                if argument.type == argument.TYPE_VERBATIM_STRING:
                    value = "\n%s" % value
                message = message.replace("$%d" % (i + 1), value)
            self.__message = message
        return message

    @property
    def arguments(self):
        arguments = self.__arguments
        if arguments is None:
            argument_data = self.__data.get("args")
            if argument_data is None:
                arguments = tuple()
            else:
                arguments = tuple((_Argument(d) for d in argument_data))
        return arguments

    @property
    def format(self):
        return self.__data["format"]

# -*- coding: utf-8 -*-

# Copyright 2014 Foxdog Studios
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from .client_message import ClientMessage

__all__ = ['UnsubMessage']


class UnsubMessage(ClientMessage):
    def __init__(self, id):
        super(UnsubMessage, self).__init__()
        self._id = id

    def __eq__(self, other):
        if isinstance(other, UnsubMessage):
            return self._id == other._id
        return super(UnsubMessage, self).__eq__(other)

    def __str__(self):
        return 'UnsubMessage(id={!r})'.format(self._id)

    @property
    def id(self):
        return self._id


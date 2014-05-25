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

from ddp.messages.client_message import ClientMessage

__all__ = ['UnsubMessage']


class UnsubMessage(ClientMessage):
    def __init__(self, id_):
        super(UnsubMessage, self).__init__()
        self._id = id_

    def __eq__(self, other):
        return self._id == other._id

    def __ne__(self, other):
        return not self == other

    def __repr__(self):
        return str(self)

    def __str__(self):
        return 'UnsubMessage(id_={!r})'.format(self._id)

    @property
    def id_(self):
        return self._id


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

import unittest

from ddp.messages.ping_message import PingMessage
from ddp.messages.ping_message_parser import PingMessageParser


class PingMessageParserTestCase(unittest.TestCase):
    def setUp(self):
        self.parser = PingMessageParser()

    def test_parse_with_id(self):
        id = 'test'
        message = self.parser.parse({'msg': 'ping', 'id': id})
        self.assertEqual(message, PingMessage(id=id))

    def test_parse_without_id(self):
        message = self.parser.parse({'msg': 'ping'})
        self.assertEqual(message, PingMessage())


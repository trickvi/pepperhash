# hash_message - submit a message to pepperhash for hash generation
# Copyright (C) 2015 Tryggvi Bjorgvinsson
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import getpass
import urlparse
import urllib

# Grab the stuff we need like host and message we'll be sending
host = raw_input("Cryptkeeper host: ")
msg = getpass.getpass("Message: ")

# Post the message to the service and print the response
response = urllib.urlopen(
    host, urllib.urlencode({'message':msg}))

print response.read()

# submit_keyshard - append a keyshard to pepperhash generator
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

# Grab the stuff we need like host and keyshard we'll be sending
host = raw_input("Cryptkeeper host: ")
keyshard_url = urlparse.urljoin(host, 'keyshard')
keyshard = getpass.getpass("Your keyshard: ")

# Post the keyshard to the service and print the response
response = urllib.urlopen(
    keyshard_url, urllib.urlencode({'keyshard':keyshard}))

print response.read()

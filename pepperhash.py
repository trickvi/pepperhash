# pepperhash - generate a pepper based cryptographic hash for a message
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

import hashlib
import binascii

from flask import Flask, abort, request
app = Flask(__name__)

# Internal key (pepper) used for hashing
app.config['PEPPER'] = ''

@app.route('/', methods=['POST'])
def generate_hash():
    """
    Generate a hash for the message
    """
    
    # We only generate hash if message is a non-empty string
    # and the secret key for the app has been set
    message = request.form.get('message', None, type=str)
    if message is None or message == '':
        abort(403)

    pepper = app.config.get('PEPPER', None)
    if pepper is None or pepper == '':
        abort(500)

    # Hash the message with the pepper (secret key for hashing)
    hashed_value = hashlib.pbkdf2_hmac(
        'sha512', message, pepper, 100000)

    # Return the hex value of the hashed value (128 chars long)
    return binascii.hexlify(hashed_value)


@app.route('/keyshard', methods=['POST'])
def update_secret_key():
    """
    Update the pepper with a keyshard which is appended to the
    existing pepper
    """
    
    # Keyshard cannot be a non-empty string 
    if request.form['keyshard'] == '':
        abort(403)

    # Update the pepper with the keyshard
    app.config.update(
        PEPPER = app.config['PEPPER'] + request.form['keyshard']
    )

    return 'Submitted'

    
if __name__ == "__main__":
    app.run()

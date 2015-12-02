# Pepperhash - a pepper based hash generator

**Proof of concept** code for a small web service that allows building a secret key (a pepper) out of keyshards (e.g. individual persons can input their own keyshards that jointly create the secret key used for salting (peppering because it's secret) the hash.

The cryptographic hashing function is hardcoded to be a sha512 (this is a proof of concept after all). The hash is created with PBKDF2.

## Installing and running

To run the web service install the requirements (it runs of Flask) you can just do:

    pip install -r requirements.txt

Then run the service with:

    python pepperhash.py

This runs the service on localhost:5000 and should of course **not** be run on http. Please do something smarter like binding it to Apache (with mod_wsgi) or something and only allow access via https (the service will actually redirect you if you don't).

## Configuring

Configuration is done with an HTTPS POST call to https://host/keyshard with data *keyshard* where the value is a keyshard. Call this as often as you like and keyshards will be appended (so order of calls is very important and should be coordinated).

    curl -X POST https://pepperhash/keyshard -d "keyshard=donotexposemelikethis"

You could also just use the script included: scripts/submit_keyshard.py

Then you should test this with a known input to output to make sure the key was generated correctly. How you do that is explained in the next session

## Generating a hash

After the key has been set up (however you do that) you can just POST (yeah yeah this should probably be GET if I'm RESTing) to https://host with data *message* to hash the message with sha512 and the pepper created by appending all the keyshards in the right order.

    curl -X POST https://pepperhash -d "message=givemeakeyforthismessage"

You could also just use the script included: scripts/hash_message.py

## Authentication

This is a proof of concept. Don't get pushy too early on.

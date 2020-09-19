# Compact UUID Representation

Using base64 or base32 encoding it is possible to express 16 UUID bytes
as 22 or 26 characters:

* use base64 encoding to pack UUID into 22 chars - digits and CAPS alpha (no U,O)
* use base32 encoding to pack UUID into 26 chars - digits, alpha, _, -

Inspired by:
https://github.com/tonsky/compact-uuids
https://www.crockford.com/base32.html

base32-crockford.py is from
https://github.com/jbittel/base32-crockford/

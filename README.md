# DateCorrection
## MongoDB Database version 4.x: convert timestamp and string formatted date values to ISODate objects.

### What this repository provides

This repository offers source code which examines a MongoDB version 4.x database collection for a key named "published_date". If found, this key is checked to see if the key value is of type Date. If so, no further action is taken on the "published_date" value. 

If the value for this key is of type String, an attempt is made to use a date parsing function to convert the string object to an ISO-8601 date object. if the conversion attempt succeeds, the value of the "published_date" key is updated to a MongoDB ISODate() object.

If the value for this key is a NumberLong value representing the number of milliseconds since the start of the Unix epoch date on January 1, 1970, an attempt is made to convert the NumberLong value to an ISO-8601 date object. If the conversion attempt succeeds, the value of the "published_date" key is updated to a MongoDB ISODate() object. 

### Source Code

Source code is provided as a mix of Node.js v12.13.1 scripts, Python 3 scripts, or Unix (specifically, bash) shell scripts. 

#### Software Prerequisites

Node.js version 12.13.1 or newer.
Python 3 version 3.7.3 or newer.

#### pip3 Modules Required

pymongo          3.9.0        
python-dateutil  2.8.1

Server operating system: Debian 10.1 or later. The provided source code should work under all recent Linux/Unix/Debian operating systems.
MongoDB Database, Community or Enterprise Edition, version 4.x. Version 4.2.1 was used in testing.

#### Database objects

A MongoDB dump directory is provided which contains a problem database and problem collection and a collection containing documents that reflect corrected ISODate() objects in the "published_date" values.

### License
MIT. See LICENSE.txt.


# Clever - the Python library for the Clever API

## API Documentation
View more detailed documentation [here](docs/README.md)

## Requirements.

Python 2.7 and 3.4+

## Installation
From PyPi:

```bash
    $ pip install clever
```

or

```bash
    $ easy_install clever
```

Or from source:

```bash
    $ python setup.py install
```

Then import the package:
```python
import clever
```

## Getting Started

Please follow the [installation procedure](#installation) and then run the following:

```python
from __future__ import print_function
import time
import clever
from clever.rest import ApiException
from pprint import pprint

# Note: This is hard coded for demo purposes only. Keep your access tokens secret!
# https://dev.clever.com/docs/security#section-security-best-practices

# Configure OAuth2 access token for authorization: oauth
configuration = clever.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = clever.DataApi(clever.ApiClient(configuration))

try:
    api_response = api_instance.get_students()
    for student in api_response.data:
        pprint(student.data.id)
except ApiException as e:
    print("Exception when calling DataApi->get_students: %s\n" % e)

```

## Updating the Library

1. Git clone swagger-codegen (https://github.com/swagger-api/swagger-codegen)

2. Git clone Clever's swagger-api repo (https://github.com/Clever/swagger-api)

3. Run this command in the swagger-codegen repo
```
java -jar modules/swagger-codegen-cli/target/swagger-codegen-cli.jar generate -i $PATH_TO_SWAGGER_API_REPO/v1.2-client.yml -c $PATH_TO_THIS_REPO/override/config.json -l python -o $PATH_TO_THIS_REPO --additional-properties packageVersion=$VERSION
```

4. Run `make override` to copy over the override files

5. Update the CHANGELOG.md with the changes!


## Development

### Dependencies

    make deps

### Testing

    make test

## Publishing

Run `make publish` to publish a new version of the library.

In order to publish to PyPI you will need a `.pypirc` file in your `$HOME` directory with the following contents:
```
[distutils]
index-servers =
    pypi

[pypi]
username: ****
password: ****
```

The username and password are in 1Password for Teams under `PyPI`.

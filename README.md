# Clever Python bindings

## Maintenance

Clever is moving to a community supported model with our client libraries. We will still respond to and merge incoming PRs but are looking to turn over ownership of these libraries to the community. If you are interested, please contact our partner-engineering team at tech-support@clever.com.

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

## Usage

Get started by importing the `clever` module and setting your authentication method:

```python
    import clever
    clever.set_token('YOUR_OAUTH_TOKEN')
    # or if you're using API key auth
    # clever.set_api_key('YOUR_API_KEY')
```

The `clever` module exposes classes corresponding to resources:

* Contact
* District
* DistrictAdmin
* School
* SchoolAdmin
* Section
* Student
* Teacher
* Event

Each exposes a class method `all` that returns a list of all data in that resource that you have access to. Keyword arguments correspond to the same query parameters supported in the HTTP API, except that `limit` and `page` are not supported (pagination is handled automatically).

```python
    schools = clever.School.all() # gets information about all schools you have access to
    schools = clever.School.all(where=json.dumps({'name': 'Of Hard Knocks'}))
    schools = clever.School.all(sort='state')
```

If you'd like more control over pagination, or to limit the number of resources returned, use the `iter` class method:

```python
    students = clever.Student.iter()
    for i in range(0,2000):
        print students.next()
```

You may also use the `starting_after` or `ending_before` parameters with the `iter` method:

```python
    students = clever.Student.iter(starting_after="530e5960049e75a9262cff1d")
    for s in students:
        print students.next()
```

The `retrieve` class method takes in a Clever ID and returns a specific resource. The object (or list of objects in the case of `all`) supports accessing properties using either dot notation or dictionary notation:

```python
    demo_school = clever.School.retrieve("4fee004cca2e43cf27000001")
    assert demo_school.name == 'Clever Academy'
    assert demo_school['name'] == 'Clever Academy'
```

## CLI

The library comes with a basic command-line interface:

```bash
    $ export CLEVER_API_KEY=DEMO_KEY
    $ clever districts all
    Running the equivalent of:
    --
    curl https://api.clever.com/v1.1/districts -H "Authorization: Basic REVNT19LRVk="
    --
    Starting new HTTPS connection (1): api.clever.com
    API request to https://api.clever.com/v1.1/districts returned (response code, response body)     of (200, '{"data":[{"data":{"name":"Demo District","id":"4fd43cc56d11340000000005"},"uri":"/v1.1/districts/4fd43cc56d11340000000005"}],"links":[{"rel":"self","uri":"/v1.1/districts"}]}')
    Result (HTTP status code 200):
    --
    {"data":[{"data":{"name":"Demo District","id":"4fd43cc56d11340000000005"},"uri":"/v1.1/districts/4fd43cc56d11340000000005"}],"links":[{"rel":"self","uri":"/v1.1/districts"}]}
    --
```

Run `clever -h` to see a full list of commands.

## Feedback

Questions, feature requests, or feedback of any kind is always welcome! We're available at [tech-support@clever.com](mailto:tech-support@clever.com).

## Development

### Dependencies

    pip install -r requirements.txt

### Testing

    python -m unittest discover test

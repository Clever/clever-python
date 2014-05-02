import pkg_resources

version_file = pkg_resources.resource_stream(__name__, "VERSION")
VERSION = version_file.readline().strip()

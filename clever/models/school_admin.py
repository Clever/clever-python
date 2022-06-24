# coding: utf-8

"""
    Clever API

    The Clever API

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class SchoolAdmin(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'credentials': 'Credentials',
        'district': 'str',
        'email': 'str',
        'id': 'str',
        'name': 'Name',
        'schools': 'list[str]',
        'staff_id': 'str',
        'title': 'str'
    }

    attribute_map = {
        'credentials': 'credentials',
        'district': 'district',
        'email': 'email',
        'id': 'id',
        'name': 'name',
        'schools': 'schools',
        'staff_id': 'staff_id',
        'title': 'title'
    }

    def __init__(self, credentials=None, district=None, email=None, id=None, name=None, schools=None, staff_id=None, title=None):
        """
        SchoolAdmin - a model defined in Swagger
        """

        self._credentials = None
        self._district = None
        self._email = None
        self._id = None
        self._name = None
        self._schools = None
        self._staff_id = None
        self._title = None
        self.discriminator = None

        if credentials is not None:
          self.credentials = credentials
        if district is not None:
          self.district = district
        if email is not None:
          self.email = email
        if id is not None:
          self.id = id
        if name is not None:
          self.name = name
        if schools is not None:
          self.schools = schools
        if staff_id is not None:
          self.staff_id = staff_id
        if title is not None:
          self.title = title

    @property
    def credentials(self):
        """
        Gets the credentials of this SchoolAdmin.

        :return: The credentials of this SchoolAdmin.
        :rtype: Credentials
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """
        Sets the credentials of this SchoolAdmin.

        :param credentials: The credentials of this SchoolAdmin.
        :type: Credentials
        """

        self._credentials = credentials

    @property
    def district(self):
        """
        Gets the district of this SchoolAdmin.

        :return: The district of this SchoolAdmin.
        :rtype: str
        """
        return self._district

    @district.setter
    def district(self, district):
        """
        Sets the district of this SchoolAdmin.

        :param district: The district of this SchoolAdmin.
        :type: str
        """

        self._district = district

    @property
    def email(self):
        """
        Gets the email of this SchoolAdmin.

        :return: The email of this SchoolAdmin.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this SchoolAdmin.

        :param email: The email of this SchoolAdmin.
        :type: str
        """

        self._email = email

    @property
    def id(self):
        """
        Gets the id of this SchoolAdmin.

        :return: The id of this SchoolAdmin.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SchoolAdmin.

        :param id: The id of this SchoolAdmin.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this SchoolAdmin.

        :return: The name of this SchoolAdmin.
        :rtype: Name
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SchoolAdmin.

        :param name: The name of this SchoolAdmin.
        :type: Name
        """

        self._name = name

    @property
    def schools(self):
        """
        Gets the schools of this SchoolAdmin.

        :return: The schools of this SchoolAdmin.
        :rtype: list[str]
        """
        return self._schools

    @schools.setter
    def schools(self, schools):
        """
        Sets the schools of this SchoolAdmin.

        :param schools: The schools of this SchoolAdmin.
        :type: list[str]
        """

        self._schools = schools

    @property
    def staff_id(self):
        """
        Gets the staff_id of this SchoolAdmin.

        :return: The staff_id of this SchoolAdmin.
        :rtype: str
        """
        return self._staff_id

    @staff_id.setter
    def staff_id(self, staff_id):
        """
        Sets the staff_id of this SchoolAdmin.

        :param staff_id: The staff_id of this SchoolAdmin.
        :type: str
        """

        self._staff_id = staff_id

    @property
    def title(self):
        """
        Gets the title of this SchoolAdmin.

        :return: The title of this SchoolAdmin.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this SchoolAdmin.

        :param title: The title of this SchoolAdmin.
        :type: str
        """

        self._title = title

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, SchoolAdmin):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
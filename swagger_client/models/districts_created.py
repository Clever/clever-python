# coding: utf-8

"""
    Clever API

    The Clever API

    OpenAPI spec version: 1.2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class DistrictsCreated(object):
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
        'created': 'str',
        'id': 'str',
        'type': 'str',
        'data': 'DistrictObject'
    }

    attribute_map = {
        'created': 'created',
        'id': 'id',
        'type': 'type',
        'data': 'data'
    }

    def __init__(self, created=None, id=None, type=None, data=None):
        """
        DistrictsCreated - a model defined in Swagger
        """

        self._created = None
        self._id = None
        self._type = None
        self._data = None

        if created is not None:
          self.created = created
        if id is not None:
          self.id = id
        self.type = type
        if data is not None:
          self.data = data

    @property
    def created(self):
        """
        Gets the created of this DistrictsCreated.

        :return: The created of this DistrictsCreated.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this DistrictsCreated.

        :param created: The created of this DistrictsCreated.
        :type: str
        """

        self._created = created

    @property
    def id(self):
        """
        Gets the id of this DistrictsCreated.

        :return: The id of this DistrictsCreated.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DistrictsCreated.

        :param id: The id of this DistrictsCreated.
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """
        Gets the type of this DistrictsCreated.

        :return: The type of this DistrictsCreated.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this DistrictsCreated.

        :param type: The type of this DistrictsCreated.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def data(self):
        """
        Gets the data of this DistrictsCreated.

        :return: The data of this DistrictsCreated.
        :rtype: DistrictObject
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this DistrictsCreated.

        :param data: The data of this DistrictsCreated.
        :type: DistrictObject
        """

        self._data = data

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
        if not isinstance(other, DistrictsCreated):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

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


class Term(object):
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
        'end_date': 'str',
        'id': 'str',
        'name': 'str',
        'start_date': 'str'
    }

    attribute_map = {
        'end_date': 'end_date',
        'id': 'id',
        'name': 'name',
        'start_date': 'start_date'
    }

    def __init__(self, end_date=None, id=None, name=None, start_date=None):
        """
        Term - a model defined in Swagger
        """

        self._end_date = None
        self._id = None
        self._name = None
        self._start_date = None
        self.discriminator = None

        if end_date is not None:
          self.end_date = end_date
        if id is not None:
          self.id = id
        if name is not None:
          self.name = name
        if start_date is not None:
          self.start_date = start_date

    @property
    def end_date(self):
        """
        Gets the end_date of this Term.

        :return: The end_date of this Term.
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """
        Sets the end_date of this Term.

        :param end_date: The end_date of this Term.
        :type: str
        """

        self._end_date = end_date

    @property
    def id(self):
        """
        Gets the id of this Term.

        :return: The id of this Term.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Term.

        :param id: The id of this Term.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Term.

        :return: The name of this Term.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Term.

        :param name: The name of this Term.
        :type: str
        """

        self._name = name

    @property
    def start_date(self):
        """
        Gets the start_date of this Term.

        :return: The start_date of this Term.
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """
        Sets the start_date of this Term.

        :param start_date: The start_date of this Term.
        :type: str
        """

        self._start_date = start_date

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
        if not isinstance(other, Term):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BackendSet(object):

    def __init__(self, **kwargs):
        """
        Initializes a new BackendSet object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param backends:
            The value to assign to the backends property of this BackendSet.
        :type backends: list[Backend]

        :param health_checker:
            The value to assign to the health_checker property of this BackendSet.
        :type health_checker: HealthChecker

        :param name:
            The value to assign to the name property of this BackendSet.
        :type name: str

        :param policy:
            The value to assign to the policy property of this BackendSet.
        :type policy: str

        :param session_persistence_configuration:
            The value to assign to the session_persistence_configuration property of this BackendSet.
        :type session_persistence_configuration: SessionPersistenceConfigurationDetails

        :param ssl_configuration:
            The value to assign to the ssl_configuration property of this BackendSet.
        :type ssl_configuration: SSLConfiguration

        """
        self.swagger_types = {
            'backends': 'list[Backend]',
            'health_checker': 'HealthChecker',
            'name': 'str',
            'policy': 'str',
            'session_persistence_configuration': 'SessionPersistenceConfigurationDetails',
            'ssl_configuration': 'SSLConfiguration'
        }

        self.attribute_map = {
            'backends': 'backends',
            'health_checker': 'healthChecker',
            'name': 'name',
            'policy': 'policy',
            'session_persistence_configuration': 'sessionPersistenceConfiguration',
            'ssl_configuration': 'sslConfiguration'
        }

        self._backends = None
        self._health_checker = None
        self._name = None
        self._policy = None
        self._session_persistence_configuration = None
        self._ssl_configuration = None

    @property
    def backends(self):
        """
        **[Required]** Gets the backends of this BackendSet.

        :return: The backends of this BackendSet.
        :rtype: list[Backend]
        """
        return self._backends

    @backends.setter
    def backends(self, backends):
        """
        Sets the backends of this BackendSet.

        :param backends: The backends of this BackendSet.
        :type: list[Backend]
        """
        self._backends = backends

    @property
    def health_checker(self):
        """
        **[Required]** Gets the health_checker of this BackendSet.

        :return: The health_checker of this BackendSet.
        :rtype: HealthChecker
        """
        return self._health_checker

    @health_checker.setter
    def health_checker(self, health_checker):
        """
        Sets the health_checker of this BackendSet.

        :param health_checker: The health_checker of this BackendSet.
        :type: HealthChecker
        """
        self._health_checker = health_checker

    @property
    def name(self):
        """
        **[Required]** Gets the name of this BackendSet.
        A friendly name for the backend set. It must be unique and it cannot be changed.

        Valid backend set names include only alphanumeric characters, dashes, and underscores. Backend set names cannot
        contain spaces. Avoid entering confidential information.

        Example: `My_backend_set`


        :return: The name of this BackendSet.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this BackendSet.
        A friendly name for the backend set. It must be unique and it cannot be changed.

        Valid backend set names include only alphanumeric characters, dashes, and underscores. Backend set names cannot
        contain spaces. Avoid entering confidential information.

        Example: `My_backend_set`


        :param name: The name of this BackendSet.
        :type: str
        """
        self._name = name

    @property
    def policy(self):
        """
        **[Required]** Gets the policy of this BackendSet.
        The load balancer policy for the backend set. To get a list of available policies, use the
        :func:`list_policies` operation.

        Example: `LEAST_CONNECTIONS`


        :return: The policy of this BackendSet.
        :rtype: str
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """
        Sets the policy of this BackendSet.
        The load balancer policy for the backend set. To get a list of available policies, use the
        :func:`list_policies` operation.

        Example: `LEAST_CONNECTIONS`


        :param policy: The policy of this BackendSet.
        :type: str
        """
        self._policy = policy

    @property
    def session_persistence_configuration(self):
        """
        Gets the session_persistence_configuration of this BackendSet.

        :return: The session_persistence_configuration of this BackendSet.
        :rtype: SessionPersistenceConfigurationDetails
        """
        return self._session_persistence_configuration

    @session_persistence_configuration.setter
    def session_persistence_configuration(self, session_persistence_configuration):
        """
        Sets the session_persistence_configuration of this BackendSet.

        :param session_persistence_configuration: The session_persistence_configuration of this BackendSet.
        :type: SessionPersistenceConfigurationDetails
        """
        self._session_persistence_configuration = session_persistence_configuration

    @property
    def ssl_configuration(self):
        """
        Gets the ssl_configuration of this BackendSet.

        :return: The ssl_configuration of this BackendSet.
        :rtype: SSLConfiguration
        """
        return self._ssl_configuration

    @ssl_configuration.setter
    def ssl_configuration(self, ssl_configuration):
        """
        Sets the ssl_configuration of this BackendSet.

        :param ssl_configuration: The ssl_configuration of this BackendSet.
        :type: SSLConfiguration
        """
        self._ssl_configuration = ssl_configuration

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

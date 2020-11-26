# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.observation_data import ObservationData  # noqa: E501
from swagger_server.test import BaseTestCase


class TestObservationsController(BaseTestCase):
    """ObservationsController integration test stubs"""

    def test_observation_post(self):
        """Test case for observation_post

        adds noise observations to UoP
        """
        observation = ObservationData()
        response = self.client.open(
            '/FinEst-Twins/Observations-To-Kafka/1.0.0/observation',
            method='POST',
            data=json.dumps(observation),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

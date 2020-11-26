import connexion
import six

from swagger_server.models.observation_data import ObservationData  # noqa: E501
from swagger_server import util


def observation_post(observation=None):  # noqa: E501
    """adds noise observations to UoP

     # noqa: E501

    :param observation: Observations from Sensors
    :type observation: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        observation = ObservationData.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'

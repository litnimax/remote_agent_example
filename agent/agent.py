import logging
from random import random
from remote_agent import GeventAgent, public


class FactoryAgent(GeventAgent):
    rooms = ['room1', 'room2']

    def _get_room_sensors(self, room):
        # Simulate sensors :-)
        return {
            'temperature': '{0}'.format(int(random() * 100)),
            'noise': '{}'.format(int(random() * 100))
        }

    @public  # Public methods - can be called from Odoo
    def get_sensors(self):
        result = {}
        for room in self.rooms:
            result[room] = self._get_room_sensors(room)
        return result


if __name__ == '__main__':
    logging.basicConfig(
                level=logging.INFO,
                format='%(asctime)s - %(levelname)s - '
                       '%(name)s.%(funcName)s:%(lineno)d - %(message)s')
    fa = FactoryAgent()
    fa.start()

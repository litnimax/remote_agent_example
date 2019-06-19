# Remote Agent example
## Introduction
This is an example of how to use the **[remote_agent](https://github.com/litnimax/remote_agent)** Odoo module for both side connection
between Odoo and remote system. Odoo does not connect to remote system and even does not know its address.

In this example project we created an IoT app on Raspberry Pi that will monitor factory sensors (room temperature and noise level).

[![Remote Agent Example Demo](https://img.youtube.com/vi/nt8bLYfNlK4/0.jpg)](https://www.youtube.com/watch?v=nt8bLYfNlK4)

## Code example
## Remote side (Raspberry Pi script)
From *remote_agent* module copy *agent* folder to your system and rename it to *remote_agent*.

Install requirements ```pip install -r requirements.txt```

Copy remote_agent/start_agent.sh to the upper level where your agent.py is located.

See *install.sh* inside which automates the above.

Adjust start_agent.sh environment and start it.


**agent.py**
```python
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
    fa = FactoryAgent()
    fa.start()


```

### Odoo side
Here is an example of an Odoo model:

**room.py:**
```python
class Room(models.Model):
    _name = 'remote_agent_example.room'
    _description = 'Factory Room'

    name = fields.Char(required=True)
    agent_uid = fields.Char(required=True)
    temperature = fields.Integer(compute='_get_sensors')
    noise = fields.Integer(compute='_get_sensors')
    status = fields.Char(compute='_get_sensors')
    last_update = fields.Char(compute='_get_sensors')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', _('The name must be unique !')),
    ]

    @api.multi
    def _get_sensors(self):
        # This method is called on every open of room list view.
        # All values are computed at the same time. 
        # If you don't want to update sensors on every request you can remove
        # compute attribute from models and update it from refresh method.
        agents = self.mapped('agent_uid')
        for agent in agents:
            # Get all rooms sensors from agent
            try:
                sensors = self.env['remote_agent.agent'].execute_agent(
                                    agent, 'get_sensors',
                                    timeout=2)  # Do not block UI much if agent is offline
            except AgentOffline:
                # We got nothing
                sensors = {}
            for rec in self:
                if not sensors:
                    # Agent was offline
                    rec.status = 'offline'
                elif not sensors.get(rec.name):
                    # Room name not found on agent
                    rec.last_update = 'no such room'
                else:
                    rec.temperature = sensors[rec.name]['temperature']
                    rec.noise = sensors[rec.name]['noise']
                    rec.status = 'ok'
                    rec.last_update = datetime.now()

```



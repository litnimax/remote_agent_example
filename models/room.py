from datetime import datetime
import logging
from openerp import models, fields, api, _
from openerp.addons.remote_agent.models.agent import AgentOffline

logger = logging.getLogger(__name__)


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
                    rec.status = 'no such room'
                else:
                    rec.temperature = sensors[rec.name]['temperature']
                    rec.noise = sensors[rec.name]['noise']
                    rec.status = 'ok'
                    rec.last_update = datetime.now()


    @api.multi
    def refresh(self):
        return True

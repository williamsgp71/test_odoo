# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Visit(models.Model):
    '''
    Developer Williasm Guerrero  Plaza
    Se creo este modelo como test
    '''
    
    _name ='custom_crm.visit'
    _descripcion = 'Visit'

    name = fields.Char(string = 'Descripcion')
    customer = fields.Char(string = 'Cliente')
    date = fields.Datetime(string = 'Fecha')
    type = fields.Selection([('P','Presencia'),('W','Whatsapp'),('T','telefonico')], string = 'Tipo', Required = True)
    done = fields.Boolean(string = 'Realizadaaa')

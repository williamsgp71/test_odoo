# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Visit(models.Model):
    _name ='custom_crm.visit'
    _descripcion = 'Visit'

    name = fields.Char(string = 'Descripcion')

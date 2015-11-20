# -*- coding:utf-8 –*-
from openerp import models, fields, api, exceptions, _


class ProductionRecord(models.Model):
    _name = 'mrpext.productionrecord'
    name = fields.Char(compute='_compute_Name')

    workorder = fields.Many2one('mrp.production.workcenter.line', domain=[("state", 'not in', ['draft', 'cancel'])],
                                required=False)
    date = fields.Date(default=fields.Date.today, required=True)
    worker = fields.Many2one('res.users', default=lambda self: self.env.user)

    #product_id = fields.Many2one('res.users', default=lambda self: self.env.user)

    goodproducts = fields.Integer(required=True)
    badproducts = fields.Integer(required=True)



    totalproducts = fields.Integer(compute='_compute_badrate', store=True)
    badrate = fields.Float(compute='_compute_badrate', store=True)
    badratePercentage = fields.Integer(compute='_compute_badrate', store=True)
    badratePercentageString = fields.Char(compute='_compute_badrate', store=True)
    totalproducts = fields.Integer(compute='_compute_badrate', store=True)

    @api.depends('goodproducts', 'badproducts')
    @api.one
    def _compute_badrate(self):
        total = self.goodproducts + self.badproducts
        self.totalproducts = total
        if total != 0:
            self.badrate = float(self.badproducts) / float(total)
            self.badratePercentage = self.badrate * 100
            self.badratePercentageString = "%d%%" % self.badratePercentage
        else:
            self.badrate = None
            self.badratePercentage = None
            self.badratePercentageString = _("N/A")

    @api.depends('workorder', 'date')
    def _compute_Name(self):
        self.name = '%s @ %s' % (self.workorder.name, self.date)

    @api.one
    @api.constrains('goodproducts', 'badproducts')
    def _check_inputs(self):
        if self.goodproducts < 0:
            raise exceptions.ValidationError(_("Good products can not be negative!"))
        if self.badproducts < 0:
            raise exceptions.ValidationError(_("Bad products can not be negative!"))
        if self.goodproducts + self.badproducts == 0:
            raise exceptions.ValidationError(_("Total products can not equals zero!"))


class WorkorderLineWithProductionRecord(models.Model):
    _inherit = 'mrp.production.workcenter.line'

    productionrecords = fields.One2many('mrpext.productionrecord', 'workorder')

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ContactRelation(models.Model):
    _name = "contact.relation"
    _description = "Contact Relation"

    survey_relation_id = fields.Many2one("survey.survey", string="survey")
    question_id = fields.Many2one("survey.question", string="Survey Question",
                                  domain="[('survey_id', '=', survey_relation_id)]")
    contact_id = fields.Many2one("ir.model.fields", domain=[('model', '=', 'res.partner')])

    @api.onchange('contact_id')
    def question(self):
        self.survey_relation_id = self.survey_relation_id._origin


class SurveyInherit(models.Model):
    _inherit = "survey.survey"

    contact_ids = fields.One2many("contact.relation", "survey_relation_id", string="Contact Relation")


class SurveyUserInput(models.Model):
    _inherit = "survey.user_input"

    def _mark_done(self):
        values = {}
        for record in self.survey_id.contact_ids:
            values.update({record.contact_id.name: rec.display_name for rec in self.user_input_line_ids if
                           rec.question_id in record.question_id})
        print(values)
        if values["name"] == "Skipped":
            raise ValidationError("Name is mandatory")
        else:
            self.env['res.partner'].create(values)
        super(SurveyUserInput, self)._mark_done()

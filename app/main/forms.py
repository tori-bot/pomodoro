from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField
from wtforms.validators import DataRequired


class WorkForm(FlaskForm):
  time_to_work = SelectField('Select amount of time to work(Mins):', choices=[('10'), ('20'), ('30'), ('40'), ('50'), ('60')], validators=[(DataRequired())])
  time_to_break = SelectField('Select amount of time to break(Mins)', choices=[('5'), ('6'), ('7'), ('8'), ('9'), ('10')], validators=[(DataRequired())])
  activity_at_break = StringField('Enter what to do with you break:', validators=[(DataRequired())])
  submit = SubmitField('Submit')

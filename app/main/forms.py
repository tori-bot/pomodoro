from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField
from wtforms.validators import DataRequired


class WorkForm(FlaskForm):
  time_to_work = SelectField('Select amount of time to work:', choices=[('10 mins'), ('20 mins'), ('30 mins'), ('40 mins'), ('50 mins'), ('1 hr')], validators=[(DataRequired())])
  time_to_break = SelectField('Select amount of time to break', choices=[('5 mins'), ('6 mins'), ('7 mins'), ('8 mins'), ('9 mins'), ('10 mins')], validators=[(DataRequired())])
  activity_at_break = StringField('Enter what to do with you break:', validators=[(DataRequired())])
  submit = SubmitField('Submit')

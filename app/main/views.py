
from flask import render_template, redirect, url_for
from app.models import Work, Break
from .forms import WorkForm
from . import main
from flask_login import current_user, login_required



@main.route('/')
def index():
  return render_template('index.html')





@main.route('/Work Form', methods=['GET', 'POST'])
# @login_required
def work_form():
  form = WorkForm()
  if form.validate_on_submit():
    time_to_work = form.time_to_work.data
    time_to_break = form.time_to_break.data
    activity_at_break = form.activity_at_break.data

    work_schedule = Work(work_time = time_to_work, user_id = current_user._get_current_object().id)
    break_schedule = Break(categoryb=activity_at_break, break_time=time_to_break, user_id=current_user._get_current_object.id)

    work_schedule.save_work()
    break_schedule.save_break()

    return redirect(url_for('main.index'))

  return render_template('work_form.html', form=form)


@main.route('/sessions')
def table():
  return render_template('session_res.html')

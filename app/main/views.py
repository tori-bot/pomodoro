
from flask import render_template, redirect, url_for
from app.models import User, Break
from .forms import WorkForm
from . import main
from flask_login import current_user, login_required



@main.route('/')
def index():
  title = 'Welcome to Pomodoro | Your time manager.'
  return render_template('index.html', title=title)





@main.route('/work-form', methods=['GET','POST'])
@login_required
def work_form():
  # user = User.query.filter(user_id = current_user._get_current_object.id)
  form = WorkForm()
  if form.validate_on_submit():
    time_to_work = form.time_to_work.data
    time_to_break = form.time_to_break.data
    activity_at_break = form.activity_at_break.data

    # work_schedule = Work(work_time = time_to_work, user_id = current_user.id)
    break_schedule = Break(categoryb=activity_at_break,work_time = time_to_work, break_time=time_to_break, user_id=current_user.id)

    # work_schedule.save_work()
    break_schedule.save_break()

    return redirect(url_for('main.table'))

  return render_template('work_form.html', form=form)


@main.route('/sessions')
def table():
  # work_session = Work.query.filter_by(user_id = current_user._get_current_object().id).all()
  breaks_session = Break.query.filter_by(user_id = current_user._get_current_object().id).all()

  return render_template('session_res.html', breaks=breaks_session)

from multiprocessing import managers
from app import create_app,db
#from app.models
from flask_script import Manager,Server
from flask_migrate import Migrate,MigrateCommand

app=create_app('deelopment')
manager=Manager(app)
manager.add_command('serve',Server)

migrate=Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app=app,db=db)
    #add classes in this dict

if __name__=='__main__':
    manager.run()


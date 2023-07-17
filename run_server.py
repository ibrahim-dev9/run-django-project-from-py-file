import os
import sys
from django.core.management import execute_from_command_line

def run_django_server():
    # 1- Change to your Django project's directory
    project_directory = 'path/to/your/project'
    os.chdir(project_directory)

    # 2- Add your Django project to the sys.path
    sys.path.append(project_directory)

    # 3- Set up Django's settings module
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

    try:
        # 4- Run the Django server
        execute_from_command_line(['manage.py', 'runserver'])
    except Exception as e:
        print(f"Error: {e}")

 
if __name__ == '__main__':
    run_django_server()

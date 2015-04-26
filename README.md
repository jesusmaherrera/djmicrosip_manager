# djmicrosip_manager
manejador de instalaciones

#Start now
cd /d %0\..
virtualenv --no-site-packages env
env\scripts\activate
pip install -r requirements.txt
python manage.py runserver

export SECRET_KEY='pitch'
export MAIL_PASSWORD='EMAIL_PASS'
export MAIL_USERNAME='MAIL_USER'

python3.8 manage.py server

heroku config:set MAIL_USERNAME='zephon.makalle@gmail.com'
heroku config:set SECRET_KEY='pitch'

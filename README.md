# docker_django_sns

■コメント画像投稿サイト

■URLXXX


■サイト説明XXX
コメントと画像を投稿できるサイトです。
また、画像とコメントに対してもコメントできます。

■サイト画像XXX

■使用技術
Python 3.7.4
Django 3.1.6
postgresql
Heroku
Docker/Docker-compose
CircleCi CI/CD
bootstrap
jQuery
Paginator

■ライブラリ
django-allauth 0.44.0
Pillow 6.2.0
psycopg2
psycopg2-binary
django-allauth>=0.32.0
Pillow==7.2.0

■ライブラリインストールコマンド(dockerを使用しているため実行の必要なし)
pip install -r requirements.txt --user
pip install django-bootstrap4
pip install gunicorn
pip install django-heroku

Bootstrap - http://getbootstrap.com/ (v4.0.0)
jQuery - http://jquery.com/ (v3.4.1)

■機能一覧
・ユーザー登録、ログイン機能(django-allauth)
・投稿機能
　コメント
　画像投稿(Pillow)
・投稿に対してのコメント機能
・ページネーション機能(Paginator) 

■gitリポジトリ名
https://github.com/uenotomoki/docker_django_sns.git

■gitクローンからdocker-composeよりdjango実行
git clone https://github.com/uenotomoki/docker_django_sns.git

docker-compose -f myproject/docker-compose.yml run --rm web python3 manage.py makemigrations
docker-compose -f myproject/docker-compose.yml run --rm web python3 manage.py migrate
docker-compose -f myproject/docker-compose.yml build
docker-compose -f myproject/docker-compose.yml up

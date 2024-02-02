from flask import Flask
from flask_mysqldb import MySQL
from app import connect

# 数据库配置
app = Flask(__name__)
app.config['SECRET_KEY'] = 'moviemagicsecretkey'

app.config['MYSQL_HOST'] = connect.host
app.config['MYSQL_USER'] = connect.user
app.config['MYSQL_PASSWORD'] = connect.dbpw
app.config['MYSQL_DB'] = connect.db
app.config['MYSQL_PORT'] = connect.port


# 初始化MySQL
mysql = MySQL(app)


# 从app包中导入蓝图
from app.home.views import home


# 蓝图注册
app.register_blueprint(home)
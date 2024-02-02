from app import mysql
from flask import Blueprint, render_template, url_for, redirect, session, request, flash
import MySQLdb.cursors
from datetime import date, datetime, timedelta
from pytz import timezone

home = Blueprint('home', __name__)

@home.route('/')
def index():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    sql = """
        select 
            a.accountid,
            a.username  
            from accounts a
        """
    cursor.execute(sql)
    accounts = cursor.fetchall()
    return render_template('index.html', accounts=accounts)
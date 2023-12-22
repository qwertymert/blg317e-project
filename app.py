from flask import Flask, render_template, request, redirect, url_for, flash
import views
import viewDriver
import mysql.connector
import os
import yaml


def create_app():
    app = Flask(__name__)

    app.add_url_rule("/", view_func=views.home_page)
    app.add_url_rule("/select_table", view_func=views.select_table, methods=["GET", "POST"])
    app.add_url_rule("/filter_table", view_func=views.filter_table, methods=["GET", "POST"])
    app.add_url_rule("/drivers", view_func=viewDriver.drivers_page, methods=["GET", "POST"])
    app.register_blueprint(viewDriver.viewDriver)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

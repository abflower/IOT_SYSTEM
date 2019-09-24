# this file is intended to test the interaction between threading and flask

import threading
from flask import Flask, make_response, redirect, render_template, request
import atexit

import time

def print_msg(self, delay):
    while not self._stopevent.isSet(  ):
        print('Hello')
        time.sleep(delay)


class myThread (threading.Thread):
    def __init__(self, threadID, name, function, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.function = function
        self.delay = delay

        self._stopevent = threading.Event(  )
        
    def run(self):
        print('Starting thread: ' + self.name)
        self.function(self, self.delay)   
        print('Exiting thread: ' + self.name)

    def kill(self):
        self._stopevent.set(  )


config_thread = myThread(1, "config_thread", print_msg, 3)
config_thread.start()

def create_app():
    app = Flask(__name__)

    def start_thread():
        global config_thread
        config_thread.start()

    def kill():
        config_thread.kill()

    def recreate():
        global config_thread
        config_thread = myThread(1, "config_thread", print_msg, 2)

    def restart():
        recreate()
        start_thread()


    @app.route('/')
    def index():
        response = make_response(render_template("home.html"))
        return response

    @app.route('/reading_off')
    def reading_off():
        print('click')
        kill()
        return redirect('/')
    
    @app.route('/reading_restart')
    def reading_restart():
        print('click')
        restart()
        return redirect('/')
 

    return app

app = create_app()   
app.run()
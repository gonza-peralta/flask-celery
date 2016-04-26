# Flask - Celery. HOW TO USE - Example

## Getting Started

This code aims to show how execute flask with celery in the same app context

Packages included:

* app: Contains everything about a prototype Flask application.
  Include model, view, config, factory and populate script.
* celerytask: Includes a celery factory and a module with tasks code.
* executerrequest: Contains an executer who sends put requests to our app view
* executertask: Contains an executer who sends tasks to celery workers

## How to execute

First, ensure you have a user with name = John and surname = Connor

After that, we need to execute four modules:

* '$> python -m app.manage' : This executes our flask app
* 'celery -A celerytask.tasks:celery worker --loglevel=info': This executes our
  celery workers who dispatches our task

Then, at the same time, execute:
* '$> python -m executertask.executer' & '$> python -m executerrequest.executer'


# Flask - Celery. HOW TO USE - Example

## Getting Started

This code aim to show how execute flask with celery in the same app context

Packages include:

* app: Package that contain everything about a prototype Flask application.
  Include model, view, config, factory and populate script.
* celerytask: This package include a celery factory and a module with task code.
* executerrequest: That contain a executer who send put request to our app view
* executertask: That contain a executer who send task to celery workers

## How to execute

Before, ensure you have a user with name = John and surname = Connor

After that, we need execute four modules:

* '$> python -m app.manage' : This execute our flask app
* 'celery -A celerytask.tasks:celery worker --loglevel=info': This execute our
  celery workers who dispatch our task

Then, at the same time execute:
* '$> python -m executertask.executer' & '$> python -m executerrequest.executer'


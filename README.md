# FinFlux Hackathon

Guide on how to setup the application.
This project was generated with [Angular CLI](https://github.com/angular/angular-cli) version 7.3.0.



## Quick Start

This project has following prerequisites which needs to be installed on your system in order to proceed.
<ul>
<li> <a href="https://nodejs.org/en/download/">Node.js</a>
<li> <a href="http://flask.pocoo.org/docs/1.0/installation/">Flask</a>
<li> <a href="https://pypi.org/project/SQLAlchemy/">SQLAlchemy</a>
<li> <a href="https://github.com/angular/angular-cli/">Angular cli</a>
</ul>

## Setup Flask and SQLAlchemy
1. cd into the given directory
2. Run command `pip install SQLAlchemy`for creating connection between SQL and Python
3. `pip install -U flask-cors` so as to enable request across Cross-Origins

## Installing Node dependencies
1. cd into the given folder in terminal
2. Run `npm install`

## Steps to run the web application
1. Make sure all the required libraries and dependecies are installed.
2. cd into the server folder and run `python databaseSetup.py`. This would create a Sqlite db file so as to setup the database.
3. Run `python data.py`. This would fetch all the data from the given CSV file and store it into the database.
4. Run `python application.py` to start the server.
5. Now cd .. to go back into the root folder and ng serve to run the Angular Application

*Since, Angular App and server are running on different ports, make sure flask-cors is installed or, server would decline the request from client.* 
  
  
## Development server

Run `ng serve` for a dev server. Navigate to `http://localhost:4200/`. The app will automatically reload if you change any of the source files.

## Code scaffolding

Run `ng generate component component-name` to generate a new component. You can also use `ng generate directive|pipe|service|class|guard|interface|enum|module`.

## Build

Run `ng build` to build the project. The build artifacts will be stored in the `dist/` directory. Use the `--prod` flag for a production build.

## Running unit tests

Run `ng test` to execute the unit tests via [Karma](https://karma-runner.github.io).

## Running end-to-end tests

Run `ng e2e` to execute the end-to-end tests via [Protractor](http://www.protractortest.org/).

## Further help

To get more help on the Angular CLI use `ng help` or go check out the [Angular CLI README](https://github.com/angular/angular-cli/blob/master/README.md).

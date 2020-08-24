# SFIA-2-Strat-Roulette
2nd SFIA project for QA Consulting Academy. This project is my own copy of the popular Strat Roulette game for CSGO!

## Contents
1. [Project Details](#Project-Details)
   * [Brief](#Brief)
   * [Project Requirements](#Project-Requirements)
2. [Design](#Design)
   * [Technologies](#Technologies)
   * [Database ERD](#Database-Erd)
   * [CI Pipeline](#CI-Pipeline)
   * [Deployment](#Deployment)
3. [Project Management](#Project-Tracking)
   * [Agile Board](#Agile-Board)
   * [Version Control](#Version-Control)
4. [Risk Assessments](#Risk-Assessments)
5. [Testing](#Testing)
7. [Project Postmortem](#Project-Postmortem)
   * [Known Issues](#Known-Issues)
   * [Positives](#Positives)
   * [Negatives](#Negatives)
   * [Future Improvements](#Future-Improvements)
8. [Author](#Author)
9. [License](#License0)

# Project Details
## Brief
Similar to the Fundamental Project (SFIA 1), this project is designed so that you can be creative, however, there are certain rules you need to abide by that will be explained later.
At its core, you are creating an application that generates “Objects” upon a set of predefined rules.
These “Objects” can be from whatever domain you wish.

## Project Requirements
- 4 services (3 producing data, one displaying the data on the front-end with backend rules that affect the displayed data in the views)
- Use of agile methodologies
- Version control system using the feature-branch model
- CI Server (Jenkins) used for automatic testing and deployment based on commits to the master branch of the version control system using webhooks
- Application must be deployed using a containerisation and orchestration tool (Docker)
- Use of ansible to automatically provision each hosting environment with the services required to run the application
- Use of a reverse proxy (NGINX) to make the application accessible to the user
- Bcrypt used for the secure hashing of each user's password within the database
- Pytest and selenium for testing of the application
# Design
## Technologies
- Git (GitHub) for version control and version control service provider
- Jira for the agile planning and development process of the project (Kanban board)
- Flask python framework for the codebase of the application
- Jenkins CI Server for automatic testing and building of the application every time a new commit is made to the master branch of the project repository
- Docker for containerisation and orchestration of the application across multiple host VM's
- Ansible for the autromatic provisioning of each host VM with the requirements to allow the application to run
- NGINX used as the reverse proxy to allow the user to access the application online
## Database ERD
This project will have a database used for the login functionality of the application. This will comprise of one table:
![](README_Assets/Database-table.png)
## CI Pipleine
Using Jenkins, every new commit to the master branch of the application repository will trigger a new build by the Jenkins server. This new build will be tested and, provided the new build passes the tests, built in order to be deployed to the host machines.
## Deployment
Using Docker and Ansible, the application will be deployed automatically to multiple host VM's

# Project Management
## Agile Board
For this project I have used the Atlissian Jira agile suite to plan out my application. I have used the Kanban board to create a backlog of tasks using the MoSCoW method. Each issue in the backlog is colour coded for priority to achieve the Minimal Viable Product (MVP) for this project. Red = Must Have, Should Have (Orange), Could Have (Green).

## Version Control
The application codebase uses Git version control (hosted on its own GitHub repository). Each feature of the application is built in its own individual branch using the feature-branch method. Each branch is tested to see if it works as expected within the development branch and merged into the master branch only when it works. Every time a task from the Jira backlog is completed, the commit will include the issue number (e.g. QS2-1) in order to move the issue from the "in progress" section of the board to the "done" section automatically. 

# Risk Assessments
In order to plan for possible issues that could be encountered during the development lifecycle of this project, 2 risk assessments have been undertaken. The first before the project development starts and the second after the first development sprint based on the issues faced during the first sprint. 
## Preliminary Risk Assessment

## Development Risk Assessment

# Testing
In order to ensure the application works as expected, rigorous testing will be undertaken before each build of the application is deployed. 

**Version control testing**
Every time development of a feature on a branch is complete, the branch will be merged into the development branch. This branch is there to test the new feature with the previously developed features to ensure all is working as expected. This is a safety measure before creating a pull request into the master branch to avoid any critical errors that could break the application.

**Pytest**
Pytest is a form of unit testing that will be undertaken to test the code of each service (unit) within the application. These tests will generate a coverage report and the minimum coverage required is 75%.

**Selenium**
Selenium is the integration testing tool that will be used for this project. This will test all the services (units) as a collective to make sure the application, once complete, works in harmony without errors. This testing will follow the user storys defined in the project planning and see if the flow of the application matches the flow a user of the application would follow to use the service

# Project Post-mortem



# Author
Steven Michael Thomas Bore - Trainee DevOps Consultant (QA Consulting)

# License
This project is licensed using [The Unlicense](https://unlicense.org/)
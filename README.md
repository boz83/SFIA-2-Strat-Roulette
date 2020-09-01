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
3. [Project Management](#Project-Management)
   * [Agile Board](#Agile-Board)
   * [Version Control](#Version-Control)
4. [Risk Assessment](#Risk-Assessment)
5. [Testing](#Testing)
7. [Project Postmortem](#Project-Postmortem)
8. [Author](#Author)
9. [License](#License)

# Project Details
## Useful Links
**Jira Board:** https://qa-sfia-2.atlassian.net/jira/software/projects/QS2/boards/1
**GitHub Repository:** https://github.com/boz83/SFIA-2-Strat-Roulette/
**Presentation:** 
**Risk Assessment:** https://docs.google.com/spreadsheets/d/12J0revuwPM-79DD4oLNpypp2PxU9c09abv-K5zv_Yv8/edit#gid=0
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
- Use of NGINX web server to act as a reverse proxy to make the application accessible to the user without accessing port 5000
- Pytest for unit testing of the application
# Design
## Technologies
- Git (GitHub) for version control and version control service provider
- Jira for the agile planning and development process of the project (Kanban board)
- Flask python framework for the codebase of the application
- Jenkins CI Server for automatic testing and building of the application every time a new commit is made to the master branch of the project repository
- Docker & Docker swarm for containerisation and orchestration of the application across multiple host VM's
- Ansible for the automatic provisioning of each host VM with the requirements to allow the application to run
- NGINX web server used as the reverse proxy to allow the user to access the application online as well as load balancer for docker swarm nodes
![alt text](README_Assets/infrastructure_design.PNG)
This is a basic infrastructure flow of how the app will go from version control system to deployment
## Database ERD
This project will have a database used. For every 
![alt text](README_Assets/erd.PNG)
## CI Pipleine
Using Jenkins, every new commit to the master branch of the application repository will trigger a new build by the Jenkins server. This new build will be tested and, provided the new build passes the tests, built in order to be deployed to the host machines.
![alt text](https://raw.githubusercontent.com/boz83/SFIA-2-Strat-Roulette/master/README_Assests/CI_pipeline.png)
This diagram illustrates every step in the CI pipeline with all technologies incorporated for the application to be deployed successfully.
## Deployment
Using Docker and Ansible, the application will be deployed automatically to multiple host VM's. Ansible will be used to provision each machine in the docker swarm with the required processes to host the application within docker swarm. Docker will be used to build a new image of the containers and push it to dockerhub. These latest versions will then be pulled down every time the application is built

# Project Management
## Agile Board
For this project I have used the Atlissian Jira agile suite to plan out my application. I have used the Kanban board to create a backlog of tasks. The backlog contains user storys that are part of an epicto achieve the Minimal Viable Product (MVP) for this project. Each user story has issues assigned to them.
![alt text](README_Assets/jira_board.PNG)

## Version Control
The application codebase uses Git version control (hosted on its own GitHub repository). Each feature of the application is built in its own individual branch using the feature-branch method. Each branch is tested to see if it works as expected within the development branch and merged into the master branch only when it works. Every time a task from the Jira backlog is completed, the commit will include the issue number (e.g. QS2-1) in order to move the issue from the "in progress" section of the board to the "done" section automatically. 
![alt text](README_Assets/version_branches.PNG)
Screenshot of the github repository branches used to develop every component of this project folling the feature/branch version control workflow. Each feature is coded in its own branch befor ebeing merged into development for testing with the rest of the application before being merged into master for the final build.
![alt text](README_Assets/git_commits.PNG)
![alt text](README_Assets/Jira_issues.PNG)
These 2 images show that I have used the Jira software GitHub integration. When a feature is complete, the commit message will be representative of issue key(s) from the jira board to show which issues/user storys have been completed.
# Risk Assessment
In order to plan for possible issues that could be encountered during the development lifecycle of this project, a risk assessments have been undertaken. This was undertaken before the project began to ensure all major possible issues could be accounted for and preventive measures put in place.

![alt text](README_Assets/risk_assessment.PNG)

# Testing
In order to ensure the application works as expected, rigorous testing will be undertaken before each build of the application is deployed. 

**Version control testing**
Every time development of a feature on a branch is complete, the branch will be merged into the development branch. This branch is there to test the new feature with the previously developed features to ensure all is working as expected. This is a safety measure before creating a pull request into the master branch to avoid any critical errors that could break the application.
![alt text](README_Assets/gitkraken.PNG)
The circled points show where I have merged a feature/branch into the development branch.
![alt text](README_Assets/CI_pipeline.PNG)
Every time development is to be merged into the master branch, a full pull request must be opened on GitHub and manually reviewed. This is to prevent faulty code form being incorporated into the master branch the application is building from.

**Pytest**
Pytest is a form of unit testing that will be undertaken to test the code of each service (unit) within the application. These tests will generate a coverage report and the minimum overall coverage required is 75% for each of the 4 services. 
![alt text](README_Assets/test_result_service_1.PNG)
Service 1 Test Results. 100% test coverage for first API
![alt text](README_Assets/test_result_service_2.PNG)
Service 2 Test Results. 100% test coverage for second api
![alt text](README_Assets/test_result_service_3.PNG)
Service 3 Test Results. 100% test coverage for third api
![alt text](README_Assets/test_result_service_4.PNG)
Service 4 Test Results. Overall 79% test coverage for service 4: database is tested but the posting of database data within the view (all_strategys page).


# Project Post-mortem
In review, this project has been a major learning curve


# Author
Steven Michael Thomas Bore - Trainee DevOps Consultant (QA Consulting)

# License
This project is licensed using [The Unlicense](https://unlicense.org/)

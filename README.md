# QA-Assignment [![Build Status](https://travis-ci.org/SpencerWBarnes/QA-Assignment.svg?branch=master)](https://travis-ci.org/SpencerWBarnes/QA-Assignment) [![Heroku](http://heroku-badge.herokuapp.com/?app=qa-assignment-sb2726)](https://qa-assignment-sb2726.herokuapp.com/) [![Coverage Status](https://coveralls.io/repos/github/SpencerWBarnes/QA-Assignment/badge.svg?branch=master)](https://coveralls.io/github/SpencerWBarnes/QA-Assignment?branch=master)

This is a repository for the application developed for the assignments given for the course CSE 4283 Software Testing and Quality Assurance.

**Assignment 2:**
Goals of the assignment are to build a command line interface that can execute a few functions (_calculate BMI_, _calculate age of retirment_) while following Test Driven Development principals. Further details on the assignment can be found under [Docs/Assignment-2-Spring2020.pdf](/Docs/Assignment-2-Spring2020.pdf).

**Assignments 3 and 4:**
Goals of the assignment are to implement a web interface, deploy it online, make a continuous integration pipeline, and set of delivery tools. Further details on the assignment can be found under [Docs/Assignment-3-4-Spring2020.pdf](/Docs/Assignment-3-4-Spring2020.pdf).
Required steps are:
- [x] Source control
- [x] Continuous integration
- [x] Static analysis
- [x] Automated unit tests
- [x] Automated end-to-end tests
- [x] Automated deploy to staging
- [x] Manual push to production
- [x] 3rd party code coverage

## Tools used:
- GitHub <sub> <sup> surprise </sup> </sub> for source control and continuous integration  
- Sider for static code analysis and linting  
- Travis CI runs Python's unittest module for automated unit testing  
- Heroku and GitHub Pages for automated web deployment  
- Travis CI runs a local PHP server and runs SeleniumBase(_a Selenium wrapper for Python_) for automated end to end tests  
- GitHub allows for a manual push from Staging to Production  
- Coverage(_the Coveralls runner for Python_) for the unit tests' code coverage  

## Tests
If you wish to see a list of all tests assocciated with each function as well their result, go to the test doc in [Docs/Tests.md](/Docs/Tests.md)

## Statuses
Production: [![Build Status](https://travis-ci.org/SpencerWBarnes/QA-Assignment.svg?branch=master)](https://travis-ci.org/SpencerWBarnes/QA-Assignment) [![Heroku](http://heroku-badge.herokuapp.com/?app=qa-assignment-sb2726)](https://qa-assignment-sb2726.herokuapp.com/) [![Coverage Status](https://coveralls.io/repos/github/SpencerWBarnes/QA-Assignment/badge.svg?branch=master)](https://coveralls.io/github/SpencerWBarnes/QA-Assignment?branch=master)

Staging: [![Build Status](https://travis-ci.org/SpencerWBarnes/QA-Assignment.svg?branch=staging)](https://travis-ci.org/SpencerWBarnes/QA-Assignment) [![Heroku](http://heroku-badge.herokuapp.com/?app=qa-assignment-sb2726-staging)](https://qa-assignment-sb2726-staging.herokuapp.com/) [![Coverage Status](https://coveralls.io/repos/github/SpencerWBarnes/QA-Assignment/badge.svg?branch=staging)](https://coveralls.io/github/SpencerWBarnes/QA-Assignment?branch=staging)
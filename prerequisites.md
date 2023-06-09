<img src="images/prereq/phData_banner.png" width=1200px>


## GITHUB PREREQUISITES

### Fork and Clone Repository for Quickstart
You’ll need to create a fork of the repository for this lab in your GitHub account, which if you are reading this file you've likely already done that. However, you can check for updates to the repository and lab by visiting phData’s
[Data Engineering Pipelines with Snowpark Python](https://github.com/phdata/sfguide-data-engineering-with-snowpark-python/) associated GitHub Repository and click on the Fork
button near the top right. Complete any required fields and click Create Fork.

<img src="images/prereq/fork.png" width=800px>

By default GitHub Actions disables any workflows (or CI/CD pipelines) defined in the forked repository.
This repository contains a workflow to deploy your Snowpark Python UDF and stored procedures, which
we’ll use later on. So for now enable this workflow by opening your forked repository in GitHub, clicking on
the Actions tab near the top middle of the page, and then clicking on the I understand my workflows, go
ahead and enable them green button.


### Create a GitHub Codespace

Note: This development can be done on your desktop with VS Code, however Codespaces greatly simplifies the prerequisites and complexities of local development.

<img src="images/prereq/create_codespace.png" width=600px>

- If you’ve already created a Codespace, it can be launched and stopped from this window as well.

    <img src="images/prereq/launch_codespace.png" width=600px>

- Once the Codespace is launched, you will need to install python and Snowflake extensions

    <img src="images/prereq/extensions.png" width=400px>

- Python extension installed. Search for and install the “Python” extension (from Microsoft) in the
Extensions pane in the Codespace.
- Snowflake extension installed. Search for and install the “Snowflake” extension (from Snowflake) in the
Extensions pane in the Codespace.




### Create Anaconda Environment
This lab will take place inside an Anaconda virtual environment running in the Codespace. You will create and activate an Anaconda environment for this lab using the supplied conda_env.yml file.  You'll need to run commands in a terminal, so open a terminal as seen in the screenshot below.

<img src="images/prereq/terminal.png" width=400px>

Run these commands from a terminal in the root of your local forked repository.
```
conda env create -f conda_env.yml
conda init bash
```
You will need to close and reopen the terminal, then execute:
```
conda activate pysnowpark
```
Once activated you should see `(pysnowpark)` in front of the host name
 
 <img src="images/prereq/activate_pysnowpark.png" width=800px>


### Shutdown codespace
If you have successfully completed all the steps, congratulations you are ready for the Hands on Lab! If you completed these prerequisites prior to attending the Hands on Lab, you can stop the Codespace in Github where you launched it from, or it will automatically stop after 30 mintues
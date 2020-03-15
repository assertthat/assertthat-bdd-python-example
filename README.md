**assertthat-bdd**
Python example project for integration with assertthat-bdd-python and AssertThat BDD & Cucumber for Jira plugin.

**Main features:**
1. Download feature files before test run.
2. Run dummy Cucumber tests using Behave(https://behave.readthedocs.io/en/latest/install.html)
3. Import test results into Jira instance.

**Instructions:**
1. Before the run you will need to provide the Jira and AssertThat connection details which are used to download and 
upload the cucumber test results.  Replace ASSERTTHAT_ACCESSKEY, ASSERTTHAT_SECRET_KEY and PROJECT _ID in the files 
with download_steps.py and upload_results.py with the corresponding values from 
[https://assertthat.atlassian.net/wiki/spaces/ABTM/pages/725385217/Configuration][project configuration page].  
2. Run the following to import dependencies:
`make init`
3. Run the following to download the feature files
`make download`
4. Run the following to execute the dummy behave test steps:
`make test`
5. Run the following to upload the results into Jira
`make upload` 

Test results can be viewed in the plugin from the locations as detailed:
[https://assertthat.atlassian.net/wiki/spaces/ABTM/pages/728629316/Access+the+Automated+Test+Reports][AssertThat Reports]
 

[AssertThat Reports]: https://assertthat.atlassian.net/wiki/spaces/ABTM/pages/728629316/Access+the+Automated+Test+Reports

[project configuration page]: https://assertthat.atlassian.net/wiki/spaces/ABTM/pages/725385217/Configuration
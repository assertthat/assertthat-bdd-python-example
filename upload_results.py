from assertthat_bdd.jira_integration import JiraConnector

JiraConnector.upload_report(
    # Jira project id e.g. 10001
    project_id='PROJECT_ID',
    # Optional can be supplied as environment variable ASSERTTHAT_ACCESS_KEY
    access_key='ASSERTTHAT_ACCESS_KEY',
    # Optional can be supplied as environment variable ASSERTTHAT_SECRET_KEY
    secret_key='ASSERTTHAT_SECRET_KEY',
    # Optional can be supplied as environment variable ASSERTTHAT_TOKEN for Server and Data Center only
    # token='ASSERTTHAT_TOKEN',
    # The name of the run - default 'Test run dd MMM yyyy HH:mm:ss'
    run_name= 'Python Tests Run',
    # Required for Jira Server only. Omit if using Jira Cloud version
    # jira_server_url='https://mycompanyjira.com'
    # Json report folder - default ./reports
    # json_report_folder='./reports',
    # Regex to search for cucumber reports - default "\.json$"
    # json_report_include_pattern='\.json$',
    # Optional - default cucumber (can be one of: cucumber/karate)
    # type='cucumber',
    # Optional - Detail the proxy with the specific scheme e.g.'10.10.10.10:1010'
    # proxy_uri='proxyip:port',
    # Optional - user name which will be used for proxy authentication.*/
    # proxy_username='username',
    # Optional - password which will be used for proxy authentication.*/
    # proxy_password='password'
    )

from assertthat_bdd.jira_integration import JiraConnector

JiraConnector.download_features(
    # Jira project id e.g. 10001
    project_id='PROJECT_ID',
    # Optional can be supplied as environment variable ASSERTTHAT_ACCESS_KEY
    access_key='ASSERTTHAT_ACCESS_KEY',
    # Optional can be supplied as environment variable ASSERTTHAT_SECRET_KEY
    secret_key='ASSERTTHAT_SECRET_KEY',
    # Optional - default ./features
    output_folder='./features',
    # Optional - all features downloaded by default - should be a valid JQL
    # jql = 'project = XX AND key in ('XXX-1')',
    # Optional - default automated (can be one of: manual/automated/both)
    # mode='both',
    # Optional - Detail the proxy with the specific scheme e.g.'10.10.10.10:1010'
    # proxy_uri='proxyip:port',
    # proxy_uri= 'proxy_uri',
    # Optional - user name which will be used for proxy authentication.*/
    # proxy_username='username',
    # Optional - password which will be used for proxy authentication.*/
    # proxy_password='password'
)


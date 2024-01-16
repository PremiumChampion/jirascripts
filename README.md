# Export jira worklogs by user and issue

1. create and activate the
   venv [https://docs.python.org/3/library/venv.html#creating-virtual-environments](https://docs.python.org/3/library/venv.html#creating-virtual-environments)
2. install requirements

```shell
pip install -r requirements.txt
```

3. Fill in the parameters in the `export_jira_worklogs.py` file

```python
auth_jira = JIRA(server="https://...",  # fill in url of your jira instance
                 basic_auth=('username', 'password'))  # fill in your username and password
# fill in the project key found in the URL
# {instanceurl}/projects/{projectkey}/....
projectname = ""

# base filename for the output worklogs will be exported to this file
base_filename = "jira_worklog_output"
```

4. Run the main script

```shell
python export_jira_worklogs.py
```

5. view your export @`jira_worklog_output.csv`

# Export confluence to pdf

1. create and activate the
   venv [https://docs.python.org/3/library/venv.html#creating-virtual-environments](https://docs.python.org/3/library/venv.html#creating-virtual-environments)
2. install requirements

```shell
pip install -r requirements.txt
```

3. Fill in the parameters in the `export_confluence.py` file

```python
confluence = Confluence(url='https://...',
                        username='username',
                        password='password'
                        )

# get the filename by going to your homepage and opening the page information in the "..." menu
confluence_home_page_id = 1234

# export directory in cwd ./export_root_folder
export_root_folder = "export"
```

4. Run the main script

```shell
python export_confluence.py
```

5. view your export @`./export_root_folder`
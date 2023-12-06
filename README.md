# Export jira worklogs by user and issue

1. create and activate the
   venv [https://docs.python.org/3/library/venv.html#creating-virtual-environments](https://docs.python.org/3/library/venv.html#creating-virtual-environments)
2. install requirements

```shell
pip install -r requirements.txt
```

3. Fill in the parameters in the `main.py` file

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
python main.py
```

5. view your export @`jira_worklog_output.csv`
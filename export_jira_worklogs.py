# This is a sample Python script.

import csv
from jira import JIRA


auth_jira = JIRA(server="https://jira-student.it.hs-heilbronn.de",  # fill in url of your jira instance
                 basic_auth=('', ''))  # fill in your username and password



# fill in the project key found in the URL
# {instanceurl}/projects/{projectkey}/....
projectname = ""

# base filename for the output worklogs will be exported to this file
base_filename = "jira_worklog_output"



def export_jira_issues():
    print(f"getting all issues for project {projectname}")
    issues = auth_jira.search_issues(f"project={projectname}", maxResults=False)  # False to gett all results in batch
    issue_count = len(issues)
    print(f"got {issue_count} issues for project")
    output = []
    i = 1
    for issue in issues:
        print(f"getting worklogs for issue {i} from {issue_count}")
        i = i + 1
        worklogs = auth_jira.worklogs(issue.id)
        for worklog in worklogs:
            output.append({
                "project": issue.fields.project.name,
                "id": issue.key,
                "author": worklog.author.displayName,
                "timeSpent": worklog.timeSpent,
                "timeSpentSeconds": worklog.timeSpentSeconds,
                "name": issue.fields.summary,
                "started": worklog.started,
                # "path": worklog.
            })
    # uncomment to write export worklogs as json
    # with open(f"{base_filename}.json", "w") as file:
    #     json.dump(output, file)

    # uncomment to write export worklogs as csv
    print(f"writing all worklogs into csv file."
          f" import the data into excel and filter by username  and timespan to get the worked hours.")
    with open(f"{base_filename}.csv", "w", newline='') as file:
        fieldnames = ["project", "id", "author", "timeSpent", "timeSpentSeconds",
                      "name", "started"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for out in output:
            writer.writerow(out)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    export_jira_issues()

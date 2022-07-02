'''
a script to call the sonarcloud web api to analyze a set of projects
based on the keys provided in the file called "filtered_project_keys.txt"
'''

import json
import requests

url_root = 'https://sonarcloud.io/api/measures/component?component='
url_suffix = '&metricKeys=bugs,vulnerabilities,security_hotspots,code_smells,coverage,lines_to_cover,uncovered_lines,line_coverage,tests,test_execution_time,test_errors,test_failures,test_success_density,skipped_tests,uncovered_conditions,branch_coverage,conditions_by_line,covered_conditions_by_line,duplicated_lines,duplicated_blocks,duplicated_files,ncloc,lines,ncloc_language_distribution,statements,functions,classes,directories,files,comment_lines,complexity,cognitive_complexity,violations,open_issues,reopened_issues,confirmed_issues,false_positive_issues'

file = open("filtered_project_keys.txt", "r")
keys = file.readlines()

data = []
i = 0
for key in keys:
    i = i + 1
    print("Added projec metric no.{} to the list".format(i))
    r = requests.get(url=url_root + key + url_suffix) # construct the url for the current project
    metrics_dict = r.json()
    data.append(metrics_dict)

with open('data.json', 'w') as outfile:
    json.dump(data, outfile) # save the list as json file
print("JSON file created")
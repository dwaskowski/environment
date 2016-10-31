#!/usr/bin/python

# import system libraries
import sys, getopt, urllib

#import modules
from api import JiraAPI
from api import DWJenkinsAPI
from library import Logger

logger = Logger.Logger()

def main(argv):
    jiraStatus = 'Code Review'
    getoptComunicate = sys.argv[0] + " -h [-s <status>]"
    try:
        opts, args = getopt.getopt(argv,"hs:",["status="])
    except getopt.GetoptError:
        logger.log(getoptComunicate)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            logger.log(getoptComunicate)
            sys.exit()
        elif opt in ("-s", "--status"):
            jiraStatus = arg
    return {
        'jiraStatus': urllib.quote(jiraStatus)
    }

if __name__ == "__main__":
    args = main(sys.argv[1:])

jiraAPI = JiraAPI.JiraAPI()
jenkinsAPI = DWJenkinsAPI.DWJenkinsAPI()

wasBuildet = []
builds_info = jenkinsAPI.getJobInfo('CodeReview')
for build in builds_info['builds']:
    if build['result'] == 'SUCCESS' or build['building'] == True:
        wasBuildet.append(build['actions'][0]['parameters'][0]['value'])


def checkTicketsStatus():
    response = jiraAPI.getIssues(args['jiraStatus'])
    for item in response['issues']:
        itemDetails = jiraAPI.getTicketDetailsInfo(item['id'])
        if (item['key'] not in wasBuildet) and (len(itemDetails['detail'][0]['pullRequests']) < 1):
            logger.log('Build for ' + item['key'] + ' in progress ...', logger.LEVEL_OK)
            jenkinsAPI.buildJob('CodeReview', {'JIRA_KEY': item['key'], 'JIRA_ID': item['id']})
        else:
            logger.log('Build for ' + item['key'] + ' already exist', logger.LEVEL_INFO)

checkTicketsStatus()

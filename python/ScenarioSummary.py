
# Collate and summarize the json output from cucumber to something comparable
# Expect two filenames as input


# Dry run each repo
# Copy/point this to each of report files

import json

import os
import sys


def getFeatures(json_in):
    """Parse the Json for all Feature Names"""
    feature_list = []
    for feature in json_in:

        """Get the Tags for feature file"""
        taglist = []
        tags = feature.get("tags")
        for tag_element in tags:
            taglist.append(tag_element.get("name"))

        """Build a dictionary of the simplified data"""
        feature_dict = {
            "name": feature.get("name"),
            "file": feature.get("uri"),
            "tags": taglist
        }

        feature_list.append(feature_dict)
    return feature_list


def getPendingFeature(monoFeatureList, pocFeatureList):
    pendingFromMonoRepo = monoFeatureList

    for pocItem in pocFeatureList:
        featureFound = pocItem['name']
        for monoItem in pendingFromMonoRepo:
            if monoItem['name'] == featureFound:
                pendingFromMonoRepo.remove(monoItem)

    return pendingFromMonoRepo


def getScenarios(json_in):
    """ Setup for list of Scenarios """
    scenarioList = []
    for feature in json_in:
        for element in feature.get('elements'):
            if (element.get('keyword') == "Scenario") | (element.get('keyword') == "Scenario Outline"):
                # Stash the name, and grab the tags
                taglist = []
                tags = element.get("tags")
                for tag_element in tags:
                    taglist.append(tag_element.get("name"))

                scenario = {"name": element['name'], "tags": taglist}
            scenarioList.append(scenario)

    return scenarioList


def getPendingScenarios(monoScenarios, pocScenarios):
    pendingFromMonoRepo = monoScenarios
    for pocItem in pocScenarios:
        scenarioName = pocItem['name']
        if scenarioName == "Read existing library filter and making sure system filters are presents":
            print("Found BOGGY-1")
       # print('Searching on ', scenarioName)
        for monoItem in monoScenarios:
            if monoItem['name'] == scenarioName:
                # print("Removing: ", scenarioName)
                pendingFromMonoRepo.remove(monoItem)

    return pendingFromMonoRepo


def deDupe(list):
    outList = []
    for item in list:
        if len(outList) < 1:
            outList.append(item)
        else:
            found = False
            for outItem in outList:
                if item['name'] == outItem['name']:
                    found = True
            if found == False:
                outList.append(item)

    return outList


def main():
    '''Main Function'''


args = sys.argv
useageMessage = '''Parses json files from MonoReport Dry Run and POC Repo Dry Run to produce results
                    Run as  {args[0]} MonoRepoFile.json POCRepoFile.json'''

if len(args) < 3:
    print(useageMessage)
    sys.exit(1)


# At this point we should have the file paths to open

with open(args[1]) as f:
    monoRepoJson = json.load(f)

with open(args[2]) as f:

    pocRepoJson = json.load(f)

monoFeatureList = getFeatures(monoRepoJson)
pocFeatureList = getFeatures(pocRepoJson)

print("MonoRepo FeatureSize ", len(monoFeatureList))
print("POC FeatureSize ", len(pocFeatureList))

pendingFromMonoRepo = getPendingFeature(monoFeatureList, pocFeatureList)
print("Pending List", len(pendingFromMonoRepo))


print("Scenarios Comparisons")
monoScenarios = getScenarios(monoRepoJson)
pocScenarios = getScenarios(pocRepoJson)

pendingScenarios = getPendingScenarios(monoScenarios, pocScenarios)
# Scenario Outlines Cause duplicates
print("Dedeuping Scenario Outlines")
pendingScenarios = deDupe(pendingScenarios)

print("pending Scenarios: ", len(pendingScenarios))
print("Done Crunching Data!")

# print(pendingFromMonoRepo)

# Need to ouput to useable format
with open("output.txt", "w") as file_object:
    for record in pendingFromMonoRepo:
        line = "Feature +  {}+{}+{}\n".format(
            record['name'], record['file'], record['tags'])
        file_object.write(line)

    for record in pendingScenarios:
        line = "Scenario, {}:{}\n".format(record['name'],  record['tags'])
        file_object.write(line)

print("Done Output")

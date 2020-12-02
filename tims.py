""""
    TIMS domain
"""


from __utils__ import *
from domains.__domain_utils__ import *
# from collections import OrderedDict
# import enchant
# import requests
# import json
# import re
import xmltodict
import threading
from rauth import OAuth2Service
# import json


__author__ = "IRFAN PASHA K V <ikyalnoo@cisco.com>"


eng_dict = enchant.Dict("en_US")

"""
    Util Functions
"""



"""
scrubber_id_api = "https://wwwin-ottawa.cisco.com/tfoggoa/Scrubber/api/users/" + user
    scrubber_query_data = dict()
    scrubber_query_data[user] = []
    try:
        output = requests.request("GET",scrubber_id_api)
        json_content = json.loads(output.content.decode("utf-8","ignore"))
"""


def get_name_from_cec_id(user):
    try:
        service = OAuth2Service(client_id = "qk3gvxsvjkgkrnwtzjmzkpke",client_secret = "KecUpHsudjeA3XBju4ueNjuX",name = "irfan_dir",access_token_url = "https://cloudsso.cisco.com/as/token.oauth2")
        token = service.get_access_token(decoder=json.loads, data = {"grant_type": "client_credentials"})
        session = service.get_session(token)
        #prod_apr = "https://hrapi.cisco.com/hr/v1/data/worker?q=cec_id:"+
        response = session.get("https://hrapi.cisco.com/hr/v1/data/worker?q=cec_id:" + str(user),headers={'content-type': 'application/json'})
        output = json.loads(response.content)
        result = ""
        
        if output["status"] == "success":
            if len(output["data"]["results"]) == 1:    
                return format_full_name(output["data"]["results"][0]["person_full_name"]) + "(" + output["data"]["results"][0]["cec_id"] + ")"
            else:
                return False
        else: 
            return False
    except:
        return False 
def format_full_name(name):
    try:
        name = name.replace('Ms. ','').replace('Mr. ','').replace('Mrs. ','')
        full_name = name
        if ',' in name:
            if '(' in name:
                full_name = name.split('(')[1].split(')')[0]
            else:
                full_name = name.split(',')[1].split()[0]
            full_name += " " + name.split(',')[0]
        full_name = ' '.join([wd for wd in full_name.strip().split() if (len(wd) > 1 or full_name.strip().split().index(wd) > 0)])
        if full_name.count(' ') == 2:
            if len(full_name.split()[2]) > 1:
                full_name = " ".join([n for n in full_name.split() if full_name.split().index(n) in [0,2]])
        if full_name.isupper():
            full_name = " ".join([(wd[0].upper() + wd[1:].lower()) for wd in full_name.split()])
    except Exception as e:
        print('ERROR : ' + str(e))
        raw = os.popen("export LC_ALL='en_US.UTF-8'\n"+"/usr/cisco/bin/rchain -n " + str(user_cecid)).read()
        full_name = " ".join(raw.split("\n")[-2].split()[1:])
        
    return full_name
def get_title_for_report_id(report_id):

    tims_report_api = report_id
    "http://tims.cisco.com/xml/Txh219004d/results-summary-report.svc"
    output = requests.request("GET",tims_report_api)
    tims_xml_output = output.content.decode("utf-8")
    xmlDict = xmltodict.parse(tims_xml_output)
    json_data=json.dumps(xmlDict)
    timsoutput = json.loads(json_data)

    if timsoutput:
        if 'Error' in timsoutput['Tims'].keys():
            return False
        else:
            return timsoutput['Tims']['Folder']['Title']
    else:
        return False

def get_report_title(report_id):
    tims_report_api = report_id
    "http://tims.cisco.com/xml/Txh219004d/results-summary-report.svc"
    output = requests.request("GET",tims_report_api)
    tims_xml_output = output.content.decode("utf-8")
    xmlDict = xmltodict.parse(tims_xml_output)
    json_data=json.dumps(xmlDict)
    timsoutput = json.loads(json_data)
    results = ""
    
    if timsoutput:
        if 'Error' in timsoutput['Tims'].keys():
            return False
        else:
            results += "<p>Title: %s "%  timsoutput['Tims']['ResultsSummaryReport']['Title']
            "timsoutput['Tims']['ResultsSummaryReport']['Owner']['UserID']"
            if isinstance(timsoutput['Tims']['ResultsSummaryReport']['ResultSummary'],list):
                #for ResultSummary in timsoutput['Tims']['ResultsSummaryReport']['ResultSummary'][0]:
                    # result_summary_id = ResultSummary['ID']['@xlink:href']
                    # #title = get_title_for_report_id(result_summary_id)
                    # results += "<strong>%s</strong><<hr>"%  title if title else ""
                # results += "<p>"
                for ResultTicker in timsoutput['Tims']['ResultsSummaryReport']['ResultSummary'][0]['ResultTicker']: 
                    if ResultTicker['@category'] in ["passed", "failed","pending","quality","defects"]:
                        if 'Percentage' in ResultTicker.keys() and 'Count' in ResultTicker.keys():
                            results += f",{ ResultTicker['@category'][0].upper() + ResultTicker['@category'][1:] }: { str(int(float(ResultTicker['Count']))) } ({ str(float(ResultTicker['Percentage'])*100) }%)"
                        elif 'Percentage' in ResultTicker.keys():
                            results += f",{ ResultTicker['@category'][0].upper() + ResultTicker['@category'][1:] }: { str(float(ResultTicker['Percentage'])*100) }%"
                        elif 'Count' in ResultTicker.keys():
                            results += f",{ ResultTicker['@category'][0].upper() + ResultTicker['@category'][1:] }: { str(int(float(ResultTicker['Count']))) }"
                results += "</p>"
                    #result += "<br>For more details : " + ("http://tims.cisco.com/warp.cmd?ent=" + timsoutput['Tims']['ResultsSummaryReport']['ID']['#text'] if type=="webex" else ("<a href='"+ "https://wwwin-ottawa.cisco.com/tfoggoa/Scrubber/showquery.html?query=" + timsoutput['Tims']['ResultsSummaryReport']['ID']['#text']  +"'>" + "scrubber_id" + timsoutput['Tims']['ResultsSummaryReport']['ID']['#text']  + "</a>")) 
                #results += "<br>For more details : " + ("http://tims.cisco.com/warp.cmd?ent=" + timsoutput['Tims']['ResultsSummaryReport']['ID']['#text'] if type=="webex" else ("<a href='"+ "http://tims.cisco.com/warp.cmd?ent=" + timsoutput['Tims']['ResultsSummaryReport']['ID']['#text'] +"'>" + "http://tims.cisco.com/warp.cmd?ent=" + timsoutput['Tims']['ResultsSummaryReport']['ID']['#text']  + "</a>"))
                return results
            elif isinstance(timsoutput['Tims']['ResultsSummaryReport']['ResultSummary'],dict):

                # owner = get_name_from_cec_id(timsoutput['Tims']['ResultsSummaryReport']['Owner']['UserID'])
                # if owner:
                #     results = "<strong>Owner: </strong %s<br>"%owner
                # else:
                #     results = " "
                # results += "<strong>Title: </strong>%s<br>"%timsoutput['Tims']['ResultsSummaryReport']['Title']
                # results += "<strong>Project: </strong>%s<br>"%timsoutput['Tims']['DatabaseID']['#text']
                # results += "<strong>Project ID:  </strong>%s<br>"%timsoutput['Tims']['ProjectID']['#text']
                # results += "<strong>Summary Report ID: </strong>%s<br>"%timsoutput['Tims']['ResultsSummaryReport']['ID']['#text']
                #results += "<p>"
                for ResultTicker in timsoutput['Tims']['ResultsSummaryReport']['ResultSummary']['ResultTicker']: 
                    if ResultTicker['@category'] in ["passed", "failed","pending","quality","defects"]:
                        if 'Percentage' in ResultTicker.keys() and 'Count' in ResultTicker.keys():
                            results += f",{ ResultTicker['@category'][0].upper() + ResultTicker['@category'][1:] }: { str(int(float(ResultTicker['Count']))) } ({ str(float(ResultTicker['Percentage'])*100) }%)"
                        elif 'Percentage' in ResultTicker.keys():
                            results += f",{ ResultTicker['@category'][0].upper() + ResultTicker['@category'][1:] }: { str(float(ResultTicker['Percentage'])*100) }%"
                        elif 'Count' in ResultTicker.keys():
                            results += f",{ ResultTicker['@category'][0].upper() + ResultTicker['@category'][1:] }: { str(int(float(ResultTicker['Count']))) }"
                results += "</p>"
                #results += "<br>For more details : " + ("http://tims.cisco.com/warp.cmd?ent=" + timsoutput['Tims']['ResultsSummaryReport']['ID']['#text'] if type=="webex" else ("<a href='"+ "http://tims.cisco.com/warp.cmd?ent=" + timsoutput['Tims']['ResultsSummaryReport']['ID']['#text'] +"'>" + "http://tims.cisco.com/warp.cmd?ent=" + timsoutput['Tims']['ResultsSummaryReport']['ID']['#text']  + "</a>"))
                return results
    else:
        return False

def get_report_id_for_given_cec_id(cec_id):
    body_raw = f"""<Tims 
    xsi:schemaLocation="http://tims.cisco.com/namespace http://tims/xsd/Tims.xsd" 
    xmlns="http://tims.cisco.com/namespace" 
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
    xmlns:xlink="http://www.w3.org/1999/xlink">
    <SavedOperations type="summary-reports">
        <ListCriterion operator="is">
            <FieldName>Owners</FieldName><Value>{ cec_id }</Value>
        </ListCriterion>
    </SavedOperations>	
    </Tims>
    """
    # find_report = "http://tims.cisco.com/xml/Txh1p/find-reports-searches.svc"
    # output = requests.request("GET",find_report,data=body_raw)
    # tims_xml_output = output.content.decode("utf-8")
    # xmlDict = xmltodict.parse(tims_xml_output)
    # json_data=json.dumps(xmlDict)
    # timsoutput = json.loads(json_data)
    try:
        result = ""
        #name = get_name_from_cec_id(cec_id)
        name = cec_id
        database_id= {"NG-XR":"Txh1p","SP-Edge-Viking-DevTest-Manual":"Tsg1p","SP-Edge-Viking-SysTest":"Tsg11p","SP-Edge-Viking-DevTest-Automation":"Tsg11p"}
        #database_id= {"NG-XR":"Txh1p"}
        if name:
            result += f"<p>TIMS Reports for User: {name} </p>" 
        else:
            result += f"TIMS Reports for User: {cec_id} </p>"
        for database in database_id.keys():
            find_report = f"http://tims.cisco.com/xml/{ database_id[database] }/find-reports-searches.svc"
            output = requests.request("GET",find_report,data=body_raw)
            tims_xml_output = output.content.decode("utf-8")
            xmlDict = xmltodict.parse(tims_xml_output)
            json_data=json.dumps(xmlDict)
            timsoutput = json.loads(json_data)
            if timsoutput:
                if 'Error' in timsoutput['Tims'].keys():
                    if re.search("This user does not exist",timsoutput['Tims']["Error"]):
                        result += f"<p>{ cec_id }: user does not exist in  {database}</p>"
                    else:
                        return "<p>Not a valid CEC ID</p>"
                else:
                    if 'SearchHit' in timsoutput['Tims']['SavedOperations'].keys():
                        if isinstance(timsoutput['Tims']['SavedOperations']['SearchHit'],list):
                            if database == "NG-XR":
                                result += "<p>Database: NG-XR</p>"
                                result += "<p>Project:  NG-XR</p>"
                                repo_id = dict()
                                for report_id in timsoutput['Tims']['SavedOperations']['SearchHit']:
                                    id_ = str(re.search("(\d+)",report_id['#text']).group(0))
                                    repo_id[id_] = [report_id['#text'],report_id['@xlink:href']]
                                repo_id = dict(sorted(repo_id.items(),key= lambda t:t[0],reverse=True))
                                #for report_id in timsoutput['Tims']['SavedOperations']['SearchHit']:
                                for id_ in repo_id.keys():
                                    #result += f"<p>{report_id['#text']}: <ul>"
                                    result += f"<p><strong>{repo_id[id_][0]}:</strong> <ul>"
                                    #title = get_report_title(report_id['@xlink:href'])
                                    title = get_report_title(repo_id[id_][1])
                                    if title:
                                        result += f"<li>{title}</li>"
                                    result += "</ul>"
                                result += "<hr>"
                            elif database == "SP-Edge-Viking-DevTest-Manual":
                                result += "<p>Database: SP EDGE</p>"
                                result += "<p>Project:  Viking DevTest Manual</p>"
                                repo_id = dict()
                                for report_id in timsoutput['Tims']['SavedOperations']['SearchHit']:
                                    id_ = str(re.search("(\d+)",report_id['#text']).group(0))
                                    repo_id[id_] = [report_id['#text'],report_id['@xlink:href']]
                                repo_id = dict(sorted(repo_id.items(),key= lambda t:t[0],reverse=True))
                                #for report_id in timsoutput['Tims']['SavedOperations']['SearchHit']:
                                for id_ in repo_id.keys():
                                    #result += f"<p>{report_id['#text']}: <ul>"
                                    result += f"<p><strong>{repo_id[id_][0]}:</strong> <ul>"
                                    #title = get_report_title(report_id['@xlink:href'])
                                    title = get_report_title(repo_id[id_][1])
                                    if title:
                                        result += f"<li>{title}</li>"
                                    result += "</ul>"
                                result += "<hr>"
                            elif database == "SP-Edge-Viking-SysTest":
                                result += "<p>Database: SP EDGE</p>"
                                result += "<p>Project:  Viking SysTest</p>"
                                repo_id = dict()
                                for report_id in timsoutput['Tims']['SavedOperations']['SearchHit']:
                                    id_ = str(re.search("(\d+)",report_id['#text']).group(0))
                                    repo_id[id_] = [report_id['#text'],report_id['@xlink:href']]
                                repo_id = dict(sorted(repo_id.items(),key= lambda t:t[0],reverse=True))
                                #for report_id in timsoutput['Tims']['SavedOperations']['SearchHit']:
                                for id_ in repo_id.keys():
                                    #result += f"<p>{report_id['#text']}: <ul>"
                                    result += f"<p><strong>{repo_id[id_][0]}:</strong> <ul>"
                                    #title = get_report_title(report_id['@xlink:href'])
                                    title = get_report_title(repo_id[id_][1])
                                    if title:
                                        result += f"<li>{title}</li>"
                                    result += "</ul>"
                                result += "<hr>"
                            elif database == "SP-Edge-Viking-DevTest-Automation":
                                result += "<p>Database: SP EDGE</p>"
                                result += "<p>Project:  Viking DevTest Automation</p>"
                                repo_id = dict()
                                for report_id in timsoutput['Tims']['SavedOperations']['SearchHit']:
                                    id_ = str(re.search("(\d+)",report_id['#text']).group(0))
                                    repo_id[id_] = [report_id['#text'],report_id['@xlink:href']]
                                repo_id = dict(sorted(repo_id.items(),key= lambda t:t[0],reverse=True))
                                #for report_id in timsoutput['Tims']['SavedOperations']['SearchHit']:
                                for id_ in repo_id.keys():
                                    #result += f"<p>{report_id['#text']}: <ul>"
                                    result += f"<p><strong>{repo_id[id_][0]}:</strong> <ul>"
                                    #title = get_report_title(report_id['@xlink:href'])
                                    title = get_report_title(repo_id[id_][1])
                                    if title:
                                        result += f"<li>{title}</li>"
                                    result += "</ul>"
                                result += "<hr>"
                            
                        elif isinstance(timsoutput['Tims']['SavedOperations']['SearchHit'],dict):
                            if database == "NG-XR":
                                result += "<p>Database: NG-XR</p>"
                                result += "<p>Project:  NG-XR</p>"
                                result += f"<p>Report ID : {timsoutput['Tims']['SavedOperations']['SearchHit']['#text']}</p>"
                                #for report_id in timsoutput['Tims']['SavedOperations']['SearchHit']:
                                title = get_report_title(timsoutput['Tims']['SavedOperations']['SearchHit']['@xlink:href'])
                                if title:
                                    result += f"<p>{title}</p>"
                                result += "<hr>"
                            elif database == "SP-Edge-Viking-DevTest-Manual":
                                result += "<p>Database: SP EDGE</p>"
                                result += "<p>Project:  Viking DevTest Manual</p>"
                                result += f"<p>Report ID : {timsoutput['Tims']['SavedOperations']['SearchHit']['#text']}</p>"
                                #for report_id in timsoutput['Tims']['SavedOperations']['SearchHit']:
                                title = get_report_title(timsoutput['Tims']['SavedOperations']['SearchHit']['@xlink:href'])
                                if title:
                                    result += f"<p>{title}</p>"
                                result += "<hr>"
                            elif database == "SP-Edge-Viking-SysTest":
                                result += "<p>Database: SP EDGE</p>"
                                result += "<p>Project:  Viking SysTest</p>"
                                result += f"<p>Report ID :{timsoutput['Tims']['SavedOperations']['SearchHit']['#text']}</p>"
                                #for report_id in timsoutput['Tims']['SavedOperations']['SearchHit']:
                                title = get_report_title(timsoutput['Tims']['SavedOperations']['SearchHit']['@xlink:href'])
                                if title:
                                    result += f"<p>{title}</p>"
                                result += "<hr>"
                            elif database == "SP-Edge-Viking-DevTest-Automation":
                                result += "<p>Database: SP EDGE</p>"
                                result += "<p>Project:  Viking DevTest Automation</p>"
                                result += f"<p>Report ID : {timsoutput['Tims']['SavedOperations']['SearchHit']['#text']}</p>"
                                #for report_id in timsoutput['Tims']['SavedOperations']['SearchHit']:
                                title = get_report_title(timsoutput['Tims']['SavedOperations']['SearchHit']['@xlink:href'])
                                if title:
                                    result += f"<p>{title}</p>"
                                result += "<hr>"
                    # else:
                    #     if database == "NG-XR":
                    #         result += "<p>No TIMS Report found in NG-XR database</p><hr>"
                    #     elif database == "SP-Edge-Viking-DevTest-Manual":
                    #         result += "<p>No TIMS Report found in SP-Edge Viking-DevTest-Manual</p><hr>"
                    #     elif database == "SP-Edge-Viking-SysTest":
                    #         result += "<p>No TIMS Report found in SP-Edge Viking-SysTest</p><hr>"
                    #     elif database == "SP-Edge-Viking-DevTest-Automation":
                    #         result += "<p>No TIMS Report found in SP-Edge Viking-DevTest-Automation</p><hr>"
                        
            else:
                return  "<p>TIMS Server is Down"
        return result
    except:
        return "<p>TIMS Server is DOWN</p>"


def get_report_details(timsoutput):
    "timsoutput['Tims']['ResultsSummaryReport']['Title']"
    i = 0
    columns = timsoutput['Tims']['ResultsSummaryReport']['Specifications']['ColumnSpecification']['Column']
    owner = get_name_from_cec_id(timsoutput['Tims']['ResultsSummaryReport']['Owner']['UserID'])
    if owner:
        results = "<strong>Owner: </strong>%s<br>"%owner
    else:
        results = "<strong>Owner: </strong> %s<br>"%timsoutput['Tims']['ResultsSummaryReport']['Owner']['UserID']
    results += "<strong>Title: </strong>%s <br>"%  timsoutput['Tims']['ResultsSummaryReport']['Title']
    results += "<strong>Project: </strong>%s<br>"%timsoutput['Tims']['DatabaseID']['#text']
    results += "<strong>Project ID:  </strong>%s<br>"%timsoutput['Tims']['ProjectID']['#text']
    results += "<strong>Summary Report ID: </strong>%s<br>"%timsoutput['Tims']['ResultsSummaryReport']['ID']['#text']
    
    "timsoutput['Tims']['ResultsSummaryReport']['Owner']['UserID']"
    if isinstance(timsoutput['Tims']['ResultsSummaryReport']['ResultSummary'],list):
        for ResultSummary in timsoutput['Tims']['ResultsSummaryReport']['ResultSummary']:
            result_summary_id = ResultSummary['ID']['@xlink:href']
            title = get_title_for_report_id(result_summary_id)
            results += "<strong>%s</strong><ul>"%  title if title else ""
            
            for ResultTicker in ResultSummary['ResultTicker']: 
                if 'Percentage' in ResultTicker.keys() and 'Count' in ResultTicker.keys():
                    results += f"<li><strong>{ ResultTicker['@category'][0].upper() + ResultTicker['@category'][1:] }: </strong> { str(int(float(ResultTicker['Count']))) } ({ str(float(ResultTicker['Percentage'])*100) }%)</li>"
                elif 'Percentage' in ResultTicker.keys():
                    results += f"<li><strong>{ ResultTicker['@category'][0].upper() + ResultTicker['@category'][1:] }: </strong> { str(float(ResultTicker['Percentage'])*100) }%</li>"
                elif 'Count' in ResultTicker.keys():
                    results += f"<li><strong>{ ResultTicker['@category'][0].upper() + ResultTicker['@category'][1:] }: </strong> { str(int(float(ResultTicker['Count']))) }</li>"
            results += "</ul><hr>"
            #result += "<br>For more details : " + ("http://tims.cisco.com/warp.cmd?ent=" + timsoutput['Tims']['ResultsSummaryReport']['ID']['#text'] if type=="webex" else ("<a href='"+ "https://wwwin-ottawa.cisco.com/tfoggoa/Scrubber/showquery.html?query=" + timsoutput['Tims']['ResultsSummaryReport']['ID']['#text']  +"'>" + "scrubber_id" + timsoutput['Tims']['ResultsSummaryReport']['ID']['#text']  + "</a>")) 
        results += "<br>For more details : " + ("http://tims.cisco.com/warp.cmd?ent=" + timsoutput['Tims']['ResultsSummaryReport']['ID']['#text'] if type=="webex" else ("<a href='"+ "http://tims.cisco.com/warp.cmd?ent=" + timsoutput['Tims']['ResultsSummaryReport']['ID']['#text'] +"'>" + "http://tims.cisco.com/warp.cmd?ent=" + timsoutput['Tims']['ResultsSummaryReport']['ID']['#text']  + "</a>"))
        return results
    elif isinstance(timsoutput['Tims']['ResultsSummaryReport']['ResultSummary'],dict):

        # owner = get_name_from_cec_id(timsoutput['Tims']['ResultsSummaryReport']['Owner']['UserID'])
        # if owner:
        #     results = "<strong>Owner: </strong %s<br>"%owner
        # else:
        #     results = " "
        # results += "<strong>Title: </strong>%s<br>"%timsoutput['Tims']['ResultsSummaryReport']['Title']
        # results += "<strong>Project: </strong>%s<br>"%timsoutput['Tims']['DatabaseID']['#text']
        # results += "<strong>Project ID:  </strong>%s<br>"%timsoutput['Tims']['ProjectID']['#text']
        # results += "<strong>Summary Report ID: </strong>%s<br>"%timsoutput['Tims']['ResultsSummaryReport']['ID']['#text']
        for ResultTicker in timsoutput['Tims']['ResultsSummaryReport']['ResultSummary']['ResultTicker']: 
            if 'Percentage' in ResultTicker.keys() and 'Count' in ResultTicker.keys():
                results += f"<strong>{ ResultTicker['@category'][0].upper() + ResultTicker['@category'][1:] }: </strong> { str(int(float(ResultTicker['Count']))) } ({ str(float(ResultTicker['Percentage'])*100) }%)<br>"
            elif 'Percentage' in ResultTicker.keys():
                results += f"<strong>{ ResultTicker['@category'][0].upper() + ResultTicker['@category'][1:] }: </strong> { str(float(ResultTicker['Percentage'])*100) }%<br>"
            elif 'Count' in ResultTicker.keys():
                results += f"<strong>{ ResultTicker['@category'][0].upper() + ResultTicker['@category'][1:] }: </strong> { str(int(float(ResultTicker['Count']))) }<br>"
        results += "<br>For more details : " + ("http://tims.cisco.com/warp.cmd?ent=" + timsoutput['Tims']['ResultsSummaryReport']['ID']['#text'] if type=="webex" else ("<a href='"+ "http://tims.cisco.com/warp.cmd?ent=" + timsoutput['Tims']['ResultsSummaryReport']['ID']['#text'] +"'>" + "http://tims.cisco.com/warp.cmd?ent=" + timsoutput['Tims']['ResultsSummaryReport']['ID']['#text']  + "</a>"))
        return results
        
def api_to_get_tims_data(report_id):
    try:
        
        #tims_report_api = "http://tims.cisco.com/xml/Txh219004d/results-summary-report.svc"
        tims_report_api = "http://tims.cisco.com/xml/" + report_id + "/results-summary-report.svc"
        "http://tims.cisco.com/xml/Txh219004d/results-summary-report.svc"
        output = requests.request("GET",tims_report_api)
        tims_xml_output = output.content.decode("utf-8")
        xmlDict = xmltodict.parse(tims_xml_output)
        json_data=json.dumps(xmlDict)
        timsoutput = json.loads(json_data)
        owner = timsoutput['Tims']['ResultsSummaryReport']['Owner']['UserID']
        title = timsoutput['Tims']['ResultsSummaryReport']['Title']
        project = timsoutput['Tims']['DatabaseID']['#text']
        Project_id= timsoutput['Tims']['ProjectID']['#text']
        Summary_Report_Id = timsoutput['Tims']['ResultsSummaryReport']['ID']['#text']
        defects_summary = dict()
        defects_summary['title'] = timsoutput['Tims']['ResultsSummaryReport']['Title']
        defects_summary['owner'] = timsoutput['Tims']['ResultsSummaryReport']['Owner']['UserID']
        defects_summary['database'] = timsoutput['Tims']['DatabaseID']['#text']
        defects_summary['project_id'] = timsoutput['Tims']['ProjectID']['#text']
        defects_summary['all_cdets_id'] = set()
        if isinstance(timsoutput['Tims']['ResultsSummaryReport']['ResultSummary'],list):
            for ResultTicker in timsoutput['Tims']['ResultsSummaryReport']['ResultSummary'][0]['ResultTicker']:
                if ResultTicker['@category'] == "defects" :
                    defects_summary['total_defects'] = str(int(float(ResultTicker['Count'])))
                    #total = str(int(float(ResultTicker['Count'])))
                    #defects_summary['ids'] = dict() 
                    for test_case in ResultTicker['ID']:
                        #test_case_id = test_case['#text']
                        test_case_details = get_test_case_details(test_case['@xlink:href'])
                        if test_case_details:
                            if len(test_case_details['bugs']) == 1:
                                defects_summary['all_cdets_id'].add(test_case_details['bugs'][0]['cdet_id'])
                                if test_case_details['bugs'][0]['cdet_id'] in defects_summary.keys():
                                    test_case = {"test_case_title":test_case_details['test_case_title'],"test_cases_status":test_case_details['test_cases_status'],"test_case_id":test_case_details['test_case_id']}
                                    defects_summary[test_case_details['bugs'][0]['cdet_id']]["test_case"].append(test_case)
                                    defects_summary[test_case_details['bugs'][0]['cdet_id']]["cdet_severity"] = test_case_details['bugs'][0]["cdet_sev"]
                                    defects_summary[test_case_details['bugs'][0]['cdet_id']]["cdet_state"] = test_case_details['bugs'][0]["cdet_state"]
                                else:
                                    defects_summary[test_case_details['bugs'][0]['cdet_id']] = dict()
                                    test_case = {"test_case_title":test_case_details['test_case_title'],"test_cases_status":test_case_details['test_cases_status'],"test_case_id":test_case_details['test_case_id']}
                                    defects_summary[test_case_details['bugs'][0]['cdet_id']]["test_case"] = [test_case]
                                    defects_summary[test_case_details['bugs'][0]['cdet_id']]["cdet_severity"] = test_case_details['bugs'][0]["cdet_sev"]
                                    defects_summary[test_case_details['bugs'][0]['cdet_id']]["cdet_state"] = test_case_details['bugs'][0]["cdet_state"]
                            elif len(test_case_details['bugs']) > 1:
                                for cdet in test_case_details['bugs']:
                                    defects_summary['all_cdets_id'].add(cdet['cdet_id'])
                                    if cdet['cdet_id'] in defects_summary.keys():
                                        test_case = {"test_case_title":test_case_details['test_case_title'],"test_cases_status":test_case_details['test_cases_status'],"test_case_id":test_case_details['test_case_id']}
                                        defects_summary[cdet['cdet_id']]["test_case"].append(test_case)
                                        defects_summary[cdet['cdet_id']]["cdet_severity"] = test_case_details['bugs'][0]["cdet_sev"]
                                        defects_summary[cdet['cdet_id']]["cdet_state"] = test_case_details['bugs'][0]["cdet_state"]
                                    else:
                                        defects_summary[cdet['cdet_id']] = dict()
                                        test_case = {"test_case_title":test_case_details['test_case_title'],"test_cases_status":test_case_details['test_cases_status'],"test_case_id":test_case_details['test_case_id']}
                                        defects_summary[cdet['cdet_id']]["test_case"] = [test_case]
                                        defects_summary[cdet['cdet_id']]["cdet_severity"] = cdet["cdet_sev"]
                                        defects_summary[cdet['cdet_id']]["cdet_state"] = cdet["cdet_state"]
                            else:
                                return False
                        else:
                            return False
            return defects_summary
        elif isinstance(timsoutput['Tims']['ResultsSummaryReport']['ResultSummary'],dict):
            for ResultTicker in timsoutput['Tims']['ResultsSummaryReport']['ResultSummary']['ResultTicker']:
                if ResultTicker['@category'] == "defects" :
                    defects_summary['total_defects'] = str(int(float(ResultTicker['Count'])))
                    #total = str(int(float(ResultTicker['Count'])))
                    #defects_summary['ids'] = dict() 
                    for test_case in ResultTicker['ID']:
                        #test_case_id = test_case['#text']
                        test_case_details = get_test_case_details(test_case['@xlink:href'])
                        if test_case_details:
                            if len(test_case_details['bugs']) == 1:
                                defects_summary['all_cdets_id'].add(test_case_details['bugs'][0]['cdet_id'])
                                if test_case_details['bugs'][0]['cdet_id'] in defects_summary.keys():
                                    test_case = {"test_case_title":test_case_details['test_case_title'],"test_cases_status":test_case_details['test_cases_status'],"test_case_id":test_case_details['test_case_id']}
                                    defects_summary[test_case_details['bugs'][0]['cdet_id']]["test_case"].append(test_case)
                                    defects_summary[test_case_details['bugs'][0]['cdet_id']]["cdet_severity"] = test_case_details['bugs'][0]["cdet_sev"]
                                    defects_summary[test_case_details['bugs'][0]['cdet_id']]["cdet_state"] = test_case_details['bugs'][0]["cdet_state"]
                                else:
                                    defects_summary[test_case_details['bugs'][0]['cdet_id']] = dict()
                                    test_case = {"test_case_title":test_case_details['test_case_title'],"test_cases_status":test_case_details['test_cases_status'],"test_case_id":test_case_details['test_case_id']}
                                    defects_summary[test_case_details['bugs'][0]['cdet_id']]["test_case"] = [test_case]
                                    defects_summary[test_case_details['bugs'][0]['cdet_id']]["cdet_severity"] = test_case_details['bugs'][0]["cdet_sev"]
                                    defects_summary[test_case_details['bugs'][0]['cdet_id']]["cdet_state"] = test_case_details['bugs'][0]["cdet_state"]
                            elif len(test_case_details['bugs']) > 1:
                                for cdet in test_case_details['bugs']:
                                    defects_summary['all_cdets_id'].add(cdet['cdet_id'])
                                    if cdet['cdet_id'] in defects_summary.keys():
                                        test_case = {"test_case_title":test_case_details['test_case_title'],"test_cases_status":test_case_details['test_cases_status'],"test_case_id":test_case_details['test_case_id']}
                                        defects_summary[cdet['cdet_id']]["test_case"].append(test_case)
                                        defects_summary[cdet['cdet_id']]["cdet_severity"] = test_case_details['bugs'][0]["cdet_sev"]
                                        defects_summary[cdet['cdet_id']]["cdet_state"] = test_case_details['bugs'][0]["cdet_state"]
                                    else:
                                        defects_summary[cdet['cdet_id']] = dict()
                                        test_case = {"test_case_title":test_case_details['test_case_title'],"test_cases_status":test_case_details['test_cases_status'],"test_case_id":test_case_details['test_case_id']}
                                        defects_summary[cdet['cdet_id']]["test_case"] = [test_case]
                                        defects_summary[cdet['cdet_id']]["cdet_severity"] = cdet["cdet_sev"]
                                        defects_summary[cdet['cdet_id']]["cdet_state"] = cdet["cdet_state"]
                            else:
                                return False
                        else:
                            return False
            return defects_summary
        else:
            return False
    except:
        return False

def get_test_cases_using_threads(ResultTicker,defects_summary):
    result_tickers = ResultTicker
    testcases_count = len(result_tickers)
    defects_summary = defects_summary
    defects_summary['all_cdets_id'] = set()
    defects_summary['no_bug_test'] = list()
    all_cdets_id = dict()
    THREAD_COUNT = 15
    THREAD_COUNT = testcases_count if THREAD_COUNT > testcases_count else THREAD_COUNT
    class myThread (threading.Thread):
        def __init__(self, result_tickers):
            threading.Thread.__init__(self)
            self.result_tickers  = result_tickers
        def run(self):
            for test_case in self.result_tickers:
                #test_case_id = test_case['#text']
                test_case_details = get_test_case_details(test_case['@xlink:href'])
                if test_case_details:
                    if len(test_case_details['bugs']) == 1:
                        #defects_summary['all_cdets_id'].add(test_case_details['bugs'][0]['cdet_id'])
                        if test_case_details['bugs'][0]['cdet_id'] in all_cdets_id.keys():
                            all_cdets_id[test_case_details['bugs'][0]['cdet_id']] += 1
                        else:
                            all_cdets_id[test_case_details['bugs'][0]['cdet_id']]= 1 
                        
                        if test_case_details['bugs'][0]['cdet_id'] in defects_summary.keys():
                            test_case = {"test_case_title":test_case_details['test_case_title'],"test_case_id":test_case_details['test_case_id'],"test_cases_status":test_case_details['test_cases_status']}
                            defects_summary[test_case_details['bugs'][0]['cdet_id']]["test_case"].append(test_case)
                            defects_summary[test_case_details['bugs'][0]['cdet_id']]["cdet_severity"] = test_case_details['bugs'][0]["cdet_sev"]
                            defects_summary[test_case_details['bugs'][0]['cdet_id']]["cdet_state"] = test_case_details['bugs'][0]["cdet_state"]
                        else:
                            defects_summary[test_case_details['bugs'][0]['cdet_id']] = dict()
                            test_case = {"test_case_title":test_case_details['test_case_title'],"test_case_id":test_case_details['test_case_id'],"test_cases_status":test_case_details['test_cases_status']}
                            defects_summary[test_case_details['bugs'][0]['cdet_id']]["test_case"] = [test_case]
                            defects_summary[test_case_details['bugs'][0]['cdet_id']]["cdet_severity"] = test_case_details['bugs'][0]["cdet_sev"]
                            defects_summary[test_case_details['bugs'][0]['cdet_id']]["cdet_state"] = test_case_details['bugs'][0]["cdet_state"]
                        
                    elif len(test_case_details['bugs']) > 1:
                        for cdet in test_case_details['bugs']:
                            defects_summary['all_cdets_id'].add(cdet['cdet_id'])
                            if cdet['cdet_id'] in all_cdets_id.keys():
                                all_cdets_id[cdet['cdet_id']] += 1
                            else:
                                all_cdets_id[cdet['cdet_id']]= 1
                            if cdet['cdet_id'] in defects_summary.keys():
                                test_case = {"test_case_title":test_case_details['test_case_title'],"test_case_id":test_case_details['test_case_id'],"test_cases_status":test_case_details['test_cases_status']}
                                defects_summary[cdet['cdet_id']]["test_case"].append(test_case)
                                defects_summary[cdet['cdet_id']]["cdet_severity"] = test_case_details['bugs'][0]["cdet_sev"]
                                defects_summary[cdet['cdet_id']]["cdet_state"] = test_case_details['bugs'][0]["cdet_state"]
                            else:
                                defects_summary[cdet['cdet_id']] = dict()
                                test_case = {"test_case_title":test_case_details['test_case_title'],"test_case_id":test_case_details['test_case_id'],"test_cases_status":test_case_details['test_cases_status']}
                                defects_summary[cdet['cdet_id']]["test_case"] = [test_case]
                                defects_summary[cdet['cdet_id']]["cdet_severity"] = cdet["cdet_sev"]
                                defects_summary[cdet['cdet_id']]["cdet_state"] = cdet["cdet_state"]
                    elif len(test_case_details['bugs']) == 0:
                        test_case = {"test_case_title":test_case_details['test_case_title'],"test_case_id":test_case_details['test_case_id'],"test_cases_status":test_case_details['test_cases_status']}
                        defects_summary['no_bug_test'].append(test_case)                
                else:
                    return False
            
    threads = []
    group = []
    if not isinstance(result_tickers, list):
        result_tickers = [result_tickers]
    for i in range(0, testcases_count - (testcases_count % THREAD_COUNT), int(testcases_count/THREAD_COUNT)):
        group.append(result_tickers[i:i+int(testcases_count/THREAD_COUNT)])
    for x in range(i + int(testcases_count/THREAD_COUNT), testcases_count):
        group[x % len(group)].append(result_tickers[x])
    for g in group:
        threads.append(myThread(g))
    print(f'{len(threads)} TIMS threads')

    # Start new Threads
    for t in threads:
        t.start()

    # Wait for threads to be over
    for t in threads:
        t.join()
    return defects_summary,all_cdets_id

def get_tims_status_data(timsoutput,status):
    try:
        
        # #tims_report_api = "http://tims.cisco.com/xml/Txh219004d/results-summary-report.svc"
        # tims_report_api = "http://tims.cisco.com/xml/" + report_id + "/results-summary-report.svc"
        # "http://tims.cisco.com/xml/Txh219004d/results-summary-report.svc"
        # output = requests.request("GET",tims_report_api)
        # tims_xml_output = output.content.decode("utf-8")
        # xmlDict = xmltodict.parse(tims_xml_output)
        # json_data=json.dumps(xmlDict)
        # timsoutput = json.loads(json_data)
        owner = timsoutput['Tims']['ResultsSummaryReport']['Owner']['UserID']
        title = timsoutput['Tims']['ResultsSummaryReport']['Title']
        project = timsoutput['Tims']['DatabaseID']['#text']
        Project_id= timsoutput['Tims']['ProjectID']['#text']
        summary_report_id = timsoutput['Tims']['ResultsSummaryReport']['ID']['#text']
        defects_summary = dict()
        defects_summary['title'] = timsoutput['Tims']['ResultsSummaryReport']['Title']
        defects_summary['owner'] = timsoutput['Tims']['ResultsSummaryReport']['Owner']['UserID']
        defects_summary['database'] = timsoutput['Tims']['DatabaseID']['#text']
        defects_summary['project_id'] = timsoutput['Tims']['ProjectID']['#text']
        defects_summary['summary_report_id'] = timsoutput['Tims']['ResultsSummaryReport']['ID']['#text']
        defects_summary['all_cdets_id'] = set()
        defects_summary['no_bug_test'] = list()
        all_cdets_id = dict()
        results = ""
        
        #if status == 'failed':
        if isinstance(timsoutput['Tims']['ResultsSummaryReport']['ResultSummary'],list):
            for ResultTicker in timsoutput['Tims']['ResultsSummaryReport']['ResultSummary'][0]['ResultTicker']:
                if ResultTicker['@category'] == status :
                    if int(float(ResultTicker['Count'])) == 0:
                        return f"no {status}"
                    defects_summary['total'] = str(int(float(ResultTicker['Count'])))
                    if isinstance(ResultTicker['ID'], dict):
                        test_case_details = get_test_case_details(ResultTicker['ID']['@xlink:href'])
                        if test_case_details:
                            if len(test_case_details['bugs']) == 1:
                                #defects_summary['all_cdets_id'].add(test_case_details['bugs'][0]['cdet_id'])
                                if test_case_details['bugs'][0]['cdet_id'] in all_cdets_id.keys():
                                    all_cdets_id[test_case_details['bugs'][0]['cdet_id']] += 1
                                else:
                                    all_cdets_id[test_case_details['bugs'][0]['cdet_id']]= 1 
                                
                                if test_case_details['bugs'][0]['cdet_id'] in defects_summary.keys():
                                    test_case = {"test_case_title":test_case_details['test_case_title'],"test_case_id":test_case_details['test_case_id']}
                                    defects_summary[test_case_details['bugs'][0]['cdet_id']]["test_case"].append(test_case)
                                    defects_summary[test_case_details['bugs'][0]['cdet_id']]["cdet_severity"] = test_case_details['bugs'][0]["cdet_sev"]
                                    defects_summary[test_case_details['bugs'][0]['cdet_id']]["cdet_state"] = test_case_details['bugs'][0]["cdet_state"]
                                else:
                                    defects_summary[test_case_details['bugs'][0]['cdet_id']] = dict()
                                    test_case = {"test_case_title":test_case_details['test_case_title'],"test_case_id":test_case_details['test_case_id']}
                                    defects_summary[test_case_details['bugs'][0]['cdet_id']]["test_case"] = [test_case]
                                    defects_summary[test_case_details['bugs'][0]['cdet_id']]["cdet_severity"] = test_case_details['bugs'][0]["cdet_sev"]
                                    defects_summary[test_case_details['bugs'][0]['cdet_id']]["cdet_state"] = test_case_details['bugs'][0]["cdet_state"]
                            elif len(test_case_details['bugs']) > 1:
                                for cdet in test_case_details['bugs']:
                                    defects_summary['all_cdets_id'].add(cdet['cdet_id'])
                                    if cdet['cdet_id'] in all_cdets_id.keys():
                                        all_cdets_id[cdet['cdet_id']] += 1
                                    else:
                                        all_cdets_id[cdet['cdet_id']]= 1
                                    if cdet['cdet_id'] in defects_summary.keys():
                                        test_case = {"test_case_title":test_case_details['test_case_title'],"test_case_id":test_case_details['test_case_id']}
                                        defects_summary[cdet['cdet_id']]["test_case"].append(test_case)
                                        defects_summary[cdet['cdet_id']]["cdet_severity"] = test_case_details['bugs'][0]["cdet_sev"]
                                        defects_summary[cdet['cdet_id']]["cdet_state"] = test_case_details['bugs'][0]["cdet_state"]
                                    else:
                                        defects_summary[cdet['cdet_id']] = dict()
                                        test_case = {"test_case_title":test_case_details['test_case_title'],"test_case_id":test_case_details['test_case_id']}
                                        defects_summary[cdet['cdet_id']]["test_case"] = [test_case]
                                        defects_summary[cdet['cdet_id']]["cdet_severity"] = cdet["cdet_sev"]
                                        defects_summary[cdet['cdet_id']]["cdet_state"] = cdet["cdet_state"]
                            elif len(test_case_details['bugs']) == 0:
                                test_case = {"test_case_title":test_case_details['test_case_title'],"test_case_id":test_case_details['test_case_id']}
                                defects_summary['no_bug_test'].append(test_case) 
                            else:
                                return False
                        else:
                            return False
                    elif isinstance(ResultTicker['ID'],list):
                        #import pdb ; pdb.set_trace()
                        defects_summary,all_cdets_id = get_test_cases_using_threads(ResultTicker['ID'],defects_summary)
                        # for test_case in ResultTicker['ID']:
                        #     #test_case_id = test_case['#text']
                        #     test_case_details = get_test_case_details(test_case['@xlink:href'])
                        #     if test_case_details:
                        #         if len(test_case_details['bugs']) == 1:
                        #             #defects_summary['all_cdets_id'].add(test_case_details['bugs'][0]['cdet_id'])
                        #             if test_case_details['bugs'][0]['cdet_id'] in all_cdets_id.keys():
                        #                 all_cdets_id[test_case_details['bugs'][0]['cdet_id']] += 1
                        #             else:
                        #                 all_cdets_id[test_case_details['bugs'][0]['cdet_id']]= 1 
                                    
                        #             if test_case_details['bugs'][0]['cdet_id'] in defects_summary.keys():
                        #                 test_case = {"test_case_title":test_case_details['test_case_title'],"test_case_id":test_case_details['test_case_id']}
                        #                 defects_summary[test_case_details['bugs'][0]['cdet_id']]["test_case"].append(test_case)
                        #                 defects_summary[test_case_details['bugs'][0]['cdet_id']]["cdet_severity"] = test_case_details['bugs'][0]["cdet_sev"]
                        #                 defects_summary[test_case_details['bugs'][0]['cdet_id']]["cdet_state"] = test_case_details['bugs'][0]["cdet_state"]
                        #             else:
                        #                 defects_summary[test_case_details['bugs'][0]['cdet_id']] = dict()
                        #                 test_case = {"test_case_title":test_case_details['test_case_title'],"test_case_id":test_case_details['test_case_id']}
                        #                 defects_summary[test_case_details['bugs'][0]['cdet_id']]["test_case"] = [test_case]
                        #                 defects_summary[test_case_details['bugs'][0]['cdet_id']]["cdet_severity"] = test_case_details['bugs'][0]["cdet_sev"]
                        #                 defects_summary[test_case_details['bugs'][0]['cdet_id']]["cdet_state"] = test_case_details['bugs'][0]["cdet_state"]
                        #         elif len(test_case_details['bugs']) > 1:
                        #             for cdet in test_case_details['bugs']:
                        #                 defects_summary['all_cdets_id'].add(cdet['cdet_id'])
                        #                 if cdet['cdet_id'] in all_cdets_id.keys():
                        #                     all_cdets_id[cdet['cdet_id']] += 1
                        #                 else:
                        #                     all_cdets_id[cdet['cdet_id']]= 1
                        #                 if cdet['cdet_id'] in defects_summary.keys():
                        #                     test_case = {"test_case_title":test_case_details['test_case_title'],"test_case_id":test_case_details['test_case_id']}
                        #                     defects_summary[cdet['cdet_id']]["test_case"].append(test_case)
                        #                     defects_summary[cdet['cdet_id']]["cdet_severity"] = test_case_details['bugs'][0]["cdet_sev"]
                        #                     defects_summary[cdet['cdet_id']]["cdet_state"] = test_case_details['bugs'][0]["cdet_state"]
                        #                 else:
                        #                     defects_summary[cdet['cdet_id']] = dict()
                        #                     test_case = {"test_case_title":test_case_details['test_case_title'],"test_case_id":test_case_details['test_case_id']}
                        #                     defects_summary[cdet['cdet_id']]["test_case"] = [test_case]
                        #                     defects_summary[cdet['cdet_id']]["cdet_severity"] = cdet["cdet_sev"]
                        #                     defects_summary[cdet['cdet_id']]["cdet_state"] = cdet["cdet_state"]
                        #         elif len(test_case_details['bugs']) == 0:
                        #             test_case = {"test_case_title":test_case_details['test_case_title'],"test_case_id":test_case_details['test_case_id']}
                        #             defects_summary['no_bug_test'].append(test_case)
                        #         else:
                        #             return False
                        #     else:
                        #         return False       
                    else:
                        return False
            #I_state = dict(sorted(I_state.items(),key=lambda t:t[1],reverse=True))
            #import pdb ; pdb.set_trace()
            all_cdets_id = dict(sorted(all_cdets_id.items(),key=lambda t:t[1],reverse=True))
            results += f"<p>Title: {defects_summary['title']}"
            results += f"<p>Owner: {defects_summary['owner']}"
            results += f"<p>Report Id: {defects_summary['summary_report_id']}"
            if status == "defects" :
                results += f"<p>Total {status} : {defects_summary['total']}</p>"
            else:
                results += f"<p>Total {status} test cases: {defects_summary['total']}</p>"
            for defect in all_cdets_id.keys():
                results += f"<p><strong> {defect}[Sev: {defects_summary[defect]['cdet_severity']},Status: {defects_summary[defect]['cdet_state']}]</strong></p><ul>"
                #results += f"<li>Total Test Tagged: {all_cdets_id[defect]}, Bus Severity : {defects_summary[defect]['cdet_severity']} and Bug state : {defects_summary[defect]['cdet_state']}</li>"
                results += f"<li>Total Test Tagged: {all_cdets_id[defect]}</li>"
                #results += f"<li>Total Test Tagged: {all_cdets_id[defect]['coun']}</li>"
                for test_case in defects_summary[defect]["test_case"]:
                    results += f"<li>Title: {test_case['test_case_title']}"
                    results += f" , Id: {test_case['test_case_id']}"
                    results += f" , Status: {test_case['test_cases_status']}</li>" if status == "defects" else "</li>"
                    
                results += "</ul><hr>"
            if len(defects_summary['no_bug_test']) > 0:
                results += f"<p> Test cases does not have any defects ID tagged</p> <ul>"
                for test_case in defects_summary['no_bug_test']:
                    results += f"<li>Title: {test_case['test_case_title']}"
                    results += f" , Id: {test_case['test_case_id']}"
                    results += f" , Status: {test_case['test_cases_status']}</li>" if status == "defects" else "</li>"
                results += "</ul><hr>"
            # else:
            #     results += "<hr>"
            return results
            #return defects_summary
        elif isinstance(timsoutput['Tims']['ResultsSummaryReport']['ResultSummary'],dict):
            for ResultTicker in timsoutput['Tims']['ResultsSummaryReport']['ResultSummary']['ResultTicker']:
                if ResultTicker['@category'] == status :
                    if int(float(ResultTicker['Count'])) == 0:
                        return f"no {status}"
                    defects_summary['total'] = str(int(float(ResultTicker['Count'])))
                    #total = str(int(float(ResultTicker['Count'])))
                    #defects_summary['ids'] = dict()
                    if isinstance(ResultTicker['ID'], dict):
                        test_case_details = get_test_case_details(ResultTicker['ID']['@xlink:href'])
                        if test_case_details:
                            if len(test_case_details['bugs']) == 1:
                                if test_case_details['bugs'][0]['cdet_id'] in all_cdets_id.keys():
                                    all_cdets_id[test_case_details['bugs'][0]['cdet_id']] += 1
                                else:
                                    all_cdets_id[test_case_details['bugs'][0]['cdet_id']]= 1
                                defects_summary['all_cdets_id'].add(test_case_details['bugs'][0]['cdet_id'])
                                if test_case_details['bugs'][0]['cdet_id'] in defects_summary.keys():
                                    test_case = {"test_case_title":test_case_details['test_case_title'],"test_cases_status":test_case_details['test_cases_status'],"test_case_id":test_case_details['test_case_id']}
                                    defects_summary[test_case_details['bugs'][0]['cdet_id']]["test_case"].append(test_case)
                                    defects_summary[test_case_details['bugs'][0]['cdet_id']]["cdet_severity"] = test_case_details['bugs'][0]["cdet_sev"]
                                    defects_summary[test_case_details['bugs'][0]['cdet_id']]["cdet_state"] = test_case_details['bugs'][0]["cdet_state"]
                                else:
                                    defects_summary[test_case_details['bugs'][0]['cdet_id']] = dict()
                                    test_case = {"test_case_title":test_case_details['test_case_title'],"test_cases_status":test_case_details['test_cases_status'],"test_case_id":test_case_details['test_case_id']}
                                    defects_summary[test_case_details['bugs'][0]['cdet_id']]["test_case"] = [test_case]
                                    defects_summary[test_case_details['bugs'][0]['cdet_id']]["cdet_severity"] = test_case_details['bugs'][0]["cdet_sev"]
                                    defects_summary[test_case_details['bugs'][0]['cdet_id']]["cdet_state"] = test_case_details['bugs'][0]["cdet_state"]
                            elif len(test_case_details['bugs']) > 1:
                                for cdet in test_case_details['bugs']:
                                    defects_summary['all_cdets_id'].add(cdet['cdet_id'])
                                    for cdet in test_case_details['bugs']:
                                        if cdet['cdet_id'] in all_cdets_id.keys():
                                            all_cdets_id[cdet['cdet_id']] += 1
                                        else:
                                            all_cdets_id[cdet['cdet_id']]= 1
                                        if cdet['cdet_id'] in defects_summary.keys():
                                            test_case = {"test_case_title":test_case_details['test_case_title'],"test_cases_status":test_case_details['test_cases_status'],"test_case_id":test_case_details['test_case_id']}
                                            defects_summary[cdet['cdet_id']]["test_case"].append(test_case)
                                            defects_summary[cdet['cdet_id']]["cdet_severity"] = test_case_details['bugs'][0]["cdet_sev"]
                                            defects_summary[cdet['cdet_id']]["cdet_state"] = test_case_details['bugs'][0]["cdet_state"]
                                        else:
                                            defects_summary[cdet['cdet_id']] = dict()
                                            test_case = {"test_case_title":test_case_details['test_case_title'],"test_cases_status":test_case_details['test_cases_status'],"test_case_id":test_case_details['test_case_id']}
                                            defects_summary[cdet['cdet_id']]["test_case"] = [test_case]
                                            defects_summary[cdet['cdet_id']]["cdet_severity"] = cdet["cdet_sev"]
                                            defects_summary[cdet['cdet_id']]["cdet_state"] = cdet["cdet_state"]
                            elif len(test_case_details['bugs']) == 0:
                                test_case = {"test_case_title":test_case_details['test_case_title'],"test_case_id":test_case_details['test_case_id']}
                                defects_summary['no_bug_test'].append(test_case)
                            else:
                                return False
                        else:
                            return False
                    elif isinstance(ResultTicker['ID'],list):
                        defects_summary,all_cdets_id = get_test_cases_using_threads(ResultTicker['ID'],defects_summary)
                        # for test_case in ResultTicker['ID']:
                        #     #test_case_id = test_case['#text']
                        #     test_case_details = get_test_case_details(test_case['@xlink:href'])
                        #     if test_case_details:
                        #         if len(test_case_details['bugs']) == 1:
                        #             if test_case_details['bugs'][0]['cdet_id'] in all_cdets_id.keys():
                        #                 all_cdets_id[test_case_details['bugs'][0]['cdet_id']] += 1
                        #             else:
                        #                 all_cdets_id[test_case_details['bugs'][0]['cdet_id']]= 1
                        #             defects_summary['all_cdets_id'].add(test_case_details['bugs'][0]['cdet_id'])
                        #             if test_case_details['bugs'][0]['cdet_id'] in defects_summary.keys():
                        #                 test_case = {"test_case_title":test_case_details['test_case_title'],"test_cases_status":test_case_details['test_cases_status'],"test_case_id":test_case_details['test_case_id']}
                        #                 defects_summary[test_case_details['bugs'][0]['cdet_id']]["test_case"].append(test_case)
                        #                 defects_summary[test_case_details['bugs'][0]['cdet_id']]["cdet_severity"] = test_case_details['bugs'][0]["cdet_sev"]
                        #                 defects_summary[test_case_details['bugs'][0]['cdet_id']]["cdet_state"] = test_case_details['bugs'][0]["cdet_state"]
                        #             else:
                        #                 defects_summary[test_case_details['bugs'][0]['cdet_id']] = dict()
                        #                 test_case = {"test_case_title":test_case_details['test_case_title'],"test_cases_status":test_case_details['test_cases_status'],"test_case_id":test_case_details['test_case_id']}
                        #                 defects_summary[test_case_details['bugs'][0]['cdet_id']]["test_case"] = [test_case]
                        #                 defects_summary[test_case_details['bugs'][0]['cdet_id']]["cdet_severity"] = test_case_details['bugs'][0]["cdet_sev"]
                        #                 defects_summary[test_case_details['bugs'][0]['cdet_id']]["cdet_state"] = test_case_details['bugs'][0]["cdet_state"]
                        #         elif len(test_case_details['bugs']) > 1:
                        #             for cdet in test_case_details['bugs']:
                        #                 defects_summary['all_cdets_id'].add(cdet['cdet_id'])
                        #                 if cdet['cdet_id'] in all_cdets_id.keys():
                        #                     all_cdets_id[cdet['cdet_id']] += 1
                        #                 else:
                        #                     all_cdets_id[cdet['cdet_id']]= 1
                        #                 if cdet['cdet_id'] in defects_summary.keys():
                        #                     test_case = {"test_case_title":test_case_details['test_case_title'],"test_cases_status":test_case_details['test_cases_status'],"test_case_id":test_case_details['test_case_id']}
                        #                     defects_summary[cdet['cdet_id']]["test_case"].append(test_case)
                        #                     defects_summary[cdet['cdet_id']]["cdet_severity"] = test_case_details['bugs'][0]["cdet_sev"]
                        #                     defects_summary[cdet['cdet_id']]["cdet_state"] = test_case_details['bugs'][0]["cdet_state"]
                        #                 else:
                        #                     defects_summary[cdet['cdet_id']] = dict()
                        #                     test_case = {"test_case_title":test_case_details['test_case_title'],"test_cases_status":test_case_details['test_cases_status'],"test_case_id":test_case_details['test_case_id']}
                        #                     defects_summary[cdet['cdet_id']]["test_case"] = [test_case]
                        #                     defects_summary[cdet['cdet_id']]["cdet_severity"] = cdet["cdet_sev"]
                        #                     defects_summary[cdet['cdet_id']]["cdet_state"] = cdet["cdet_state"]
                        #         elif len(test_case_details['bugs']) == 0:
                        #             test_case = {"test_case_title":test_case_details['test_case_title'],"test_case_id":test_case_details['test_case_id']}
                        #             defects_summary['no_bug_test'].append(test_case)
                        #         else:
                        #             return False
                        #     else:
                        #         return False
                    else:
                        return False
            all_cdets_id = dict(sorted(all_cdets_id.items(),key=lambda t:t[1],reverse=True))
            results += f"<p>Title: {defects_summary['title']}"
            results += f"<p>Owner: {defects_summary['owner']}"
            results += f"<p>Report Id: {defects_summary['summary_report_id']}"
            if status == "defects" :
                results += f"<p>Total {status} : {defects_summary['total']}</p>"
            else:
                results += f"<p>Total {status} test cases: {defects_summary['total']}</p>"
            for defect in all_cdets_id.keys():
                #results += f"<p> {defect}<ul>"
                results += f"<p><strong> {defect}[Sev: {defects_summary[defect]['cdet_severity']},Status: {defects_summary[defect]['cdet_state']}]</strong></p><ul>"
                #results += f"<li>Total Test Cases Tagged: {all_cdets_id[defect]}, Bus Severity : {defects_summary[defect]['cdet_severity']} and Bug state : {defects_summary[defect]['cdet_state']}</li>"
                results += f"<li>Total Test Cases Tagged: {all_cdets_id[defect]},</li>"
                #results += f"<li>Total Test Tagged: {all_cdets_id[defect]['coun']}</li>"
                for test_case in defects_summary[defect]["test_case"]:
                    results += f"<li>Title: {test_case['test_case_title']}"
                    results += f" , Id: {test_case['test_case_id']}"
                    results += f" , Status: {test_case['test_cases_status']}</li>" if status == "defects" else "</li>"
                results += "</ul><hr>"
            if len(defects_summary['no_bug_test']) > 1:
                results += f"<p> Test cases does not have any defects ID tagged</p> <ul>"
                for test_case in defects_summary['no_bug_test']:
                    results += f"<li>Title: {test_case['test_case_title']}"
                    results += f" , Id: {test_case['test_case_id']}"
                    results += f" , Status: {test_case['test_cases_status']}</li>" if status == "defects" else "</li>"
                results += "</ul><hr>"
            return results
            
            #return defects_summary
    except:
        return False


def get_test_case_details(test_case_id):
    try:
        #tims_report_api = "http://tims.cisco.com/xml/Txh219004d/results-summary-report.svc"
        "http://tims.cisco.com/xml/Tsg1587299r/entity.svc"
        #tims_report_api = "http://tims.cisco.com/xml/" + report_id + "/results-summary-report.svc"
        tims_report_api = test_case_id
        #"http://tims.cisco.com/xml/Txh219004d/results-summary-report.svc"
        output = requests.request("GET",tims_report_api)
        tims_xml_output = output.content.decode("utf-8")
        xmlDict = xmltodict.parse(tims_xml_output)
        json_data=json.dumps(xmlDict)
        timsoutput = json.loads(json_data)
        test_case_title = timsoutput['Tims']['Result']['Title']
        test_cases_status = timsoutput['Tims']['Result']['Status']
        test_case_id = timsoutput['Tims']['Result']['LogicalID']
        for test_data in timsoutput['Tims']['Result']['ListFieldValue']:
            if test_data['FieldName'] == 'Defects':
                # cd_id = test_data['Value']['#text']
                bugs = []
                if isinstance(test_data['Value'],list) :
                    bugs = []
                    for cdet in test_data['Value']:
                        if re.search("(\w+)\s\((\d)\|(\w)\)",cdet['#text']):
                            cdets = re.search("(\w+)\s\((\d)\|(\w)\)",cdet['#text']).groups()
                            cdet_id = cdets[0]
                            cdet_sev = cdets[1]
                            cdet_state = cdets[2]
                            bugs.append({"cdet_id":cdet_id,"cdet_sev":cdet_sev,"cdet_state":cdet_state})
                    test_case_details = {"test_case_id":test_case_id,"test_cases_status":test_cases_status,"test_case_title":test_case_title,"bugs":bugs}    
                    return test_case_details
                else:
                    if re.search("(\w+)\s\((\d)\|(\w)\)",test_data['Value']['#text']):
                        cdets = re.search("(\w+)\s\((\d)\|(\w)\)",test_data['Value']['#text']).groups()
                        cdet_id = cdets[0]
                        cdet_sev = cdets[1]
                        cdet_state = cdets[2]
                        bugs.append({"cdet_id":cdet_id,"cdet_sev":cdet_sev,"cdet_state":cdet_state})
                    test_case_details = {"test_case_id":test_case_id,"test_cases_status":test_cases_status,"test_case_title":test_case_title,"bugs":bugs}    
                    return test_case_details
        bugs = []
        test_case_details = {"test_case_id":test_case_id,"test_cases_status":test_cases_status,"test_case_title":test_case_title,"bugs":bugs}
        return test_case_details
    except:
        return False

def get_tims_report_summary(report_id):
    try:
        #tims_report_api = "http://tims.cisco.com/xml/Txh219004d/results-summary-report.svc"
        tims_report_api = "http://tims.cisco.com/xml/" + report_id + "/results-summary-report.svc"
        "http://tims.cisco.com/xml/Txh219004d/results-summary-report.svc"
        output = requests.request("GET",tims_report_api)
        tims_xml_output = output.content.decode("utf-8")
        xmlDict = xmltodict.parse(tims_xml_output)
        json_data=json.dumps(xmlDict)
        timsoutput = json.loads(json_data)
        return timsoutput
    except:
        return False

def get_tims_data(question,user,type="web"):
    "['blocked', 'total', 'executed', 'quality', 'passx', 'dropped', 'failed', 'passed', 'pending', 'defects']"
    question = question.lower()
    question = question.strip()
    content = dict()
    qwords = re.split("\s+",question)
    try:
        qwords.remove(" ")
    except :
        pass
    question = " ".join(qwords)
    result = ""
    if re.search("bugs|fail|failing|block|blocking|defect|defects",question):
        tims_report_id = re.search("(t[a-z][a-z]\d+d)" , question).group(1)
        timsoutput = get_tims_report_summary(tims_report_id)
        if timsoutput:
            if 'Error' in timsoutput['Tims'].keys():
                if isinstance(timsoutput['Tims']['Error'],str) :
                    result = "<strong>" + timsoutput['Tims']['Error'] + "</strong>"
                    #return result
                elif isinstance(timsoutput['Tims']['Erro'],list):
                    result = "<strong>" + " ".join(timsoutput['Tims']['Erro']) + "</strong>"
                    #return result
                else:
                    result = "<strong>Error:The specified Report ID does not exist</strong>"
            else:
                if re.search("fail",question):
                    results = get_tims_status_data(timsoutput,"failed")
                    if results == "no failed" :
                        result = f"<p>No failed test cases in given report </p>"
                    elif results:
                        result = results
                    else:
                        result = f"<p>Not able to fetch failed test cases in given report</p>"
                if re.search("block",question):
                    results = get_tims_status_data(timsoutput,"blocked")
                    if results == "no blocked" :
                        result = f"<p>No blocked test cases in given report </p>"
                    elif results:
                        result = results
                    else:
                        result = f"<p>Not able to fetch blocked test cases in given report</p>"
                if re.search("drop",question):
                    results = get_tims_status_data(timsoutput,"dropped")
                    if results == "no dropped" :
                        result = f"<p>No dropped test cases in given report </p>"
                    elif results:
                        result = results
                    else:
                        result = f"<p>Not able to fetch dropped test cases in given report</p>"
                if re.search("defect|report",question):
                    results = get_tims_status_data(timsoutput,"defects")
                    if results == "no defect" :
                        result = f"<p>No Defects in given report </p>"
                    elif results:
                        result = results
                    else:
                        result = f"<p>Not able to fetch defects in given report</p>"
                        
        else:
            result = "<strong>TIMS Server is not reachable Please try after some time</strong> "
    elif re.search("(t[a-z][a-z]\d+d)" , question):
        tims_report_id = re.search("(t[a-z][a-z]\d+d)" , question).group(1)
        timsoutput = get_tims_report_summary(tims_report_id)
        if timsoutput:
            if 'Error' in timsoutput['Tims'].keys():
                if isinstance(timsoutput['Tims']['Error'],str) :
                    result = "<strong>" + timsoutput['Tims']['Error'] + "</strong>"
                    #return result
                elif isinstance(timsoutput['Tims']['Erro'],list):
                    result = "<strong>" + " ".join(timsoutput['Tims']['Erro']) + "</strong>"
                    #return result
                else:
                    result = "<strong>Error:The specified Report ID does not exist</strong>"
            else:
                result = get_report_details(timsoutput)
                #return result
        else:
            result = "<strong>TIMS Server is not reachable Please try after some time</strong> "
    elif re.search("tims|report|id|user|reports",question):
        if "my" in question.lower().split():
            cec_id = user
            result = get_report_id_for_given_cec_id(cec_id)
        else:
            cec_id = "all"
            for word in qwords:
                # if word == "":
                #     qwords.remove(" ")
                if not eng_dict.check(word) and word not in ["tims","id"]:
                    cec_id = word
            if cec_id != "all":
                result = get_report_id_for_given_cec_id(cec_id)
                if not result:
                    result = "<strong>No TIMS reports found in NG-XR and SP-Edge Databases</strong>"
            else:
                result += "<p>Not able to get the CEC ID from quetion"  
    else:
        result += "<strong>Could not find  TIME report ID, please provide valid TIMS report ID</strong>" 
    content["title"] = "TIMS Details"
    content["results"] = ([result+"<br>"+"<br>"] if type=="webex" else result+"<br>"+"<br>")
    return content

if __name__ == "__main__":
    print(get_tims_data("get me defects report in Txh214186d","ikyalnoo","web"))
    #print(api_to_get_tims_data("Txh214186d"))

#Txh219004d
#Txh218786d  
#Tsg364967d
#Txh214186d
"timsoutput['Tims']['ResultsSummaryReport']['Specifications']['ColumnSpecification']['Column'] = ['blocked', 'total', 'executed', 'quality', 'passx', 'dropped', 'failed', 'passed', 'pending']"
"timsoutput['Tims']['ResultsSummaryReport']['ResultSummary']['ResultTicker'][0]"
"timsoutput['Tims']['ResultsSummaryReport']['ResultSummary']['ResultTicker'][3]['@category']"
"Dabase ID timsoutput['Tims']['DatabaseID']['#text'] = NG-XR"
"timsoutput['Tims']['ProjectID']['#text'] = Txh1p"
"timsoutput['Tims']['ResultsSummaryReport']['ID']['#text']"
"timsoutput['Tims']['ResultsSummaryReport']['Title']  name LACP-hotstandby-result"

"""
 "http://tims.cisco.com/xml/Txh219004d/results-summary-report.svc"
output = requests.request("GET","http://tims.cisco.com/xml/Tsg1587247f/entity.svc")
tims_xml_output = output.content.decode("utf-8")
xmlDict = xmltodict.parse(tims_xml_output)
json_data=json.dumps(xmlDict)
timsoutput = json.loads(json_data)

Txh219004d = (Pdb) type(timsoutput['Tims']['ResultsSummaryReport']['ResultSummary'])
<class 'dict'>
"""
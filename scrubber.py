"""
    Scrubber domain
"""

<<<<<<< HEAD
from __utils__ import *
from domains.__domain_utils__ import *
# from collections import OrderedDict
# import enchant
# import requests
# import json
# import re
=======
# from __utils__ import *
# from domains.__domain_utils__ import *
import enchant
import requests
import json
import re
>>>>>>> origin/master-live
__author__ = "IRFAN PASHA K V <ikyalnoo@cisco.com>"


eng_dict = enchant.Dict("en_US")

"""
    Util Functions
"""
<<<<<<< HEAD

def state_wise_bugs(scrubber_id,scrubber_state,state):
    result = ""
    if state == "i" :
        if "total_I" in scrubber_state["status"]["I_status"].keys():
            result += "<p> I State Bugs Summary for scrubber : <strong>%s</strong>"%scrubber_id
            #state_bugs["I"] = scrubber_output["status"]["I_status"]["total_I"]
            result += "<p><strong>Total I state bugs: %s</strong></p>"%scrubber_state["status"]["I_status"]["total_I"]
            #result += "<strong>Per Submitter Count:</strong>"
            result += "<hr>"
            I_state = dict()
            for i_submitter in scrubber_state["status"]["I_Submitter"].keys():
                I_state[i_submitter] = scrubber_state["status"]["I_Submitter"][i_submitter]["count"]
            I_state = dict(sorted(I_state.items(),key=lambda t:t[1],reverse=True))
            for i_submitter in I_state.keys():
                result += "For Submitter: <strong>%s</strong><ul>"%i_submitter
                result += "<li>Count: <strong>%s</strong></li>"%I_state[i_submitter]
                
                i_bug = ""
                for bug in scrubber_state["status"]["I_Submitter"][i_submitter]["bugids"]:
                    i_bug += bug + ","
                
                result += "<li>I State Bugs: <strong>%s</strong></li>"%i_bug
                result += "</ul><hr>"
            result += "<br>For more details : " + ("https://wwwin-ottawa.cisco.com/tfoggoa/Scrubber/showquery.html?query=" + scrubber_id if type=="webex" else ("<a href='"+ "https://wwwin-ottawa.cisco.com/tfoggoa/Scrubber/showquery.html?query=" + scrubber_id  +"'>" + "scrubber_id" + scrubber_id  + "</a>")) 
        else:
            result += "<strong>No I state Bugs Found</strong>"
        return result
    elif state=="a":
        
        if "total_A" in scrubber_state["status"]["A_status"].keys():
            #state_bugs["I"] = scrubber_output["status"]["I_status"]["total_I"]
            result += "<p> A State Bugs Summary for scrubber : <strong>%s</strong>"%scrubber_id
            result += "<p><strong>Total A state bugs: %s</strong></p>"%scrubber_state["status"]["A_status"]["total_A"]
            #result += "<strong>Per Submitter Count:</strong>"
            result += "<hr>"
            I_state = dict()
            for i_submitter in scrubber_state["status"]["A_Submitter"].keys():
                I_state[i_submitter] = scrubber_state["status"]["A_Submitter"][i_submitter]["count"]
            I_state = dict(sorted(I_state.items(),key=lambda t:t[1],reverse=True))
            for i_submitter in I_state.keys():
                result += "For Submitter: <strong>%s</strong><ul>"%i_submitter
                result += "<li>Count: <strong>%s</strong></li>"%I_state[i_submitter]
                
                i_bug = ""
                for bug in scrubber_state["status"]["A_Submitter"][i_submitter]["bugids"]:
                    i_bug += bug + ","
                
                result += "<li>A State Bugs: <strong>%s</strong></li>"%i_bug
                result += "</ul><hr>"
            result += "<br>For more details : " + ("https://wwwin-ottawa.cisco.com/tfoggoa/Scrubber/showquery.html?query=" + scrubber_id if type=="webex" else ("<a href='"+ "https://wwwin-ottawa.cisco.com/tfoggoa/Scrubber/showquery.html?query=" + scrubber_id  +"'>" + "scrubber_id" + scrubber_id  + "</a>")) 
        else:
            result += "<strong>No A state Bugs Found</strong>"
        return result
    elif state =="r":
        if "total_R" in scrubber_state["status"]["R_status"].keys():
            #state_bugs["I"] = scrubber_output["status"]["I_status"]["total_I"]
            result += "<p>R State Bugs Summary for scrubber : <strong>%s</strong>"%scrubber_id
            result += "<p><strong>Total R state bugs: %s</strong></p>"%scrubber_state["status"]["R_status"]["total_R"]
            #result += "<strong>Per Submitter Count:</strong>"
            result += "<hr>"
            I_state = dict()
            for i_submitter in scrubber_state["status"]["R_Submitter"].keys():
                I_state[i_submitter] = scrubber_state["status"]["R_Submitter"][i_submitter]["count"]
            I_state = dict(sorted(I_state.items(),key=lambda t:t[1],reverse=True))
            for i_submitter in I_state.keys():
                result += "For Submitter: <strong>%s</strong><ul>"%i_submitter
                result += "<li>Count: <strong>%s</strong></li>"%I_state[i_submitter]
                
                i_bug = ""
                for bug in scrubber_state["status"]["R_Submitter"][i_submitter]["bugids"]:
                    i_bug += bug + ","
                
                result += "<li>R State Bugs: <strong>%s</strong></li>"%i_bug
                result += "</ul><hr>"
            result += "<br>For more details : " + ("https://wwwin-ottawa.cisco.com/tfoggoa/Scrubber/showquery.html?query=" + scrubber_id if type=="webex" else ("<a href='"+ "https://wwwin-ottawa.cisco.com/tfoggoa/Scrubber/showquery.html?query=" + scrubber_id  +"'>" + "scrubber_id" + scrubber_id  + "</a>")) 
        else:
            result += "<strong>No R state Bugs Found</strong>"
        return result
    elif state =="m":
        if "total_M" in scrubber_state["status"]["M_status"].keys():
            result += "<p>M State Bugs Summary for scrubber : <strong>%s</strong>"%scrubber_id
            #state_bugs["I"] = scrubber_output["status"]["I_status"]["total_I"]
            result += "<p><strong>Total M state bugs: %s</strong></p>"%scrubber_state["status"]["M_status"]["total_M"]
            #result += "<strong>Per Submitter Count:</strong>"
            result += "<hr>"
            I_state = dict()
            for i_submitter in scrubber_state["status"]["M_Submitter"].keys():
                I_state[i_submitter] = scrubber_state["status"]["M_Submitter"][i_submitter]["count"]
            I_state = dict(sorted(I_state.items(),key=lambda t:t[1],reverse=True))
            for i_submitter in I_state.keys():
                result += "For Submitter: <strong>%s</strong><ul>"%i_submitter
                result += "<li>Count: <strong>%s</strong></li>"%I_state[i_submitter]
                
                i_bug = ""
                for bug in scrubber_state["status"]["M_Submitter"][i_submitter]["bugids"]:
                    i_bug += bug + ","
                
                result += "<li>M State Bugs: <strong>%s</strong></li>"%i_bug
                result += "</ul><hr>"
            result += "<br>For more details : " + ("https://wwwin-ottawa.cisco.com/tfoggoa/Scrubber/showquery.html?query=" + scrubber_id if type=="webex" else ("<a href='"+ "https://wwwin-ottawa.cisco.com/tfoggoa/Scrubber/showquery.html?query=" + scrubber_id  +"'>" + "scrubber_id" + scrubber_id  + "</a>")) 
        else:
            result += "<strong>No M state Bugs Found</strong>"
        return result
    elif state =="v":
        if "total_V" in scrubber_state["status"]["V_status"].keys():
            result += "<p>V State Bugs Summary for scrubber : <strong>%s</strong>"%scrubber_id
            #state_bugs["I"] = scrubber_output["status"]["I_status"]["total_I"]
            result += "<p><strong>Total V state bugs: %s</strong></p>"%scrubber_state["status"]["V_status"]["total_V"]
            #result += "<strong>Per Submitter Count:</strong>"
            result += "<hr>"
            I_state = dict()
            for i_submitter in scrubber_state["status"]["V_Submitter"].keys():
                I_state[i_submitter] = scrubber_state["status"]["V_Submitter"][i_submitter]["count"]
            I_state = dict(sorted(I_state.items(),key=lambda t:t[1],reverse=True))
            for i_submitter in I_state.keys():
                result += "For Submitter: <strong>%s</strong><ul>"%i_submitter
                result += "<li>Count: <strong>%s</strong></li>"%I_state[i_submitter]
                
                i_bug = ""
                for bug in scrubber_state["status"]["V_Submitter"][i_submitter]["bugids"]:
                    i_bug += bug + ","
                
                result += "<li>V State Bugs: <strong>%s</strong></li>"%i_bug
                result += "</ul><hr>"
            result += "<br>For more details : " + ("https://wwwin-ottawa.cisco.com/tfoggoa/Scrubber/showquery.html?query=" + scrubber_id if type=="webex" else ("<a href='"+ "https://wwwin-ottawa.cisco.com/tfoggoa/Scrubber/showquery.html?query=" + scrubber_id  +"'>" + "scrubber_id" + scrubber_id  + "</a>")) 
        else:
            result += "<strong>No V state Bugs Found</strong>"
        return result
    elif state =="w":
        if "total_W" in scrubber_state["status"]["W_status"].keys():
            result += "<p>W State Bugs Summary for scrubber : <strong>%s</strong>"%scrubber_id
            #state_bugs["I"] = scrubber_output["status"]["I_status"]["total_I"]
            result += "<p><strong>Total W state bugs: %s</strong></p>"%scrubber_state["status"]["W_status"]["total_W"]
            #result += "<strong>Per Submitter Count:</strong>"
            result += "<hr>"
            I_state = dict()
            for i_submitter in scrubber_state["status"]["W_Submitter"].keys():
                I_state[i_submitter] = scrubber_state["status"]["W_Submitter"][i_submitter]["count"]
            I_state = dict(sorted(I_state.items(),key=lambda t:t[1],reverse=True))
            for i_submitter in I_state.keys():
                result += "For Submitter: <strong>%s</strong><ul>"%i_submitter
                result += "<li>Count: <strong>%s</strong></li>"%I_state[i_submitter]
                
                i_bug = ""
                for bug in scrubber_state["status"]["W_Submitter"][i_submitter]["bugids"]:
                    i_bug += bug + ","
                
                result += "<li>W State Bugs: <strong>%s</strong></li>"%i_bug
                result += "</ul><hr>"
            result += "<br>For more details : " + ("https://wwwin-ottawa.cisco.com/tfoggoa/Scrubber/showquery.html?query=" + scrubber_id if type=="webex" else ("<a href='"+ "https://wwwin-ottawa.cisco.com/tfoggoa/Scrubber/showquery.html?query=" + scrubber_id  +"'>" + "scrubber_id" + scrubber_id  + "</a>")) 
        else:
            result += "<strong>No W state Bugs Found</strong>"
        return result
    elif state =="n":
        if "total_N" in scrubber_state["status"]["N_status"].keys():
            #state_bugs["I"] = scrubber_output["status"]["I_status"]["total_I"]
            result += "<p>N State Bugs Summary for scrubber : <strong>%s</strong>"%scrubber_id
            result += "<p><strong>Total N state bugs: %s</strong></p>"%scrubber_state["status"]["N_status"]["total_N"]
            #result += "<strong>Per Submitter Count:</strong>"
            result += "<hr>"
            I_state = dict()
            for i_submitter in scrubber_state["status"]["N_Submitter"].keys():
                I_state[i_submitter] = scrubber_state["status"]["N_Submitter"][i_submitter]["count"]
            I_state = dict(sorted(I_state.items(),key=lambda t:t[1],reverse=True))
            for i_submitter in I_state.keys():
                result += "For Submitter: <strong>%s</strong><ul>"%i_submitter
                result += "<li>Count: <strong>%s</strong></li>"%I_state[i_submitter]
                
                i_bug = ""
                for bug in scrubber_state["status"]["N_Submitter"][i_submitter]["bugids"]:
                    i_bug += bug + ","
                
                result += "<li>N State Bugs: <strong>%s</strong></li>"%i_bug
                result += "</ul><hr>"
            result += "<br>For more details : " + ("https://wwwin-ottawa.cisco.com/tfoggoa/Scrubber/showquery.html?query=" + scrubber_id if type=="webex" else ("<a href='"+ "https://wwwin-ottawa.cisco.com/tfoggoa/Scrubber/showquery.html?query=" + scrubber_id  +"'>" + "scrubber_id" + scrubber_id  + "</a>")) 
        else:
            result += "<strong>No N state Bugs Found</strong>"
        return result
    elif state =="p":
        if "total_P" in scrubber_state["status"]["P_status"].keys():
            result += "<p>P State Bugs Summary for scrubber : <strong>%s</strong>"%scrubber_id
            #state_bugs["I"] = scrubber_output["status"]["I_status"]["total_I"]
            result += "<p><strong>Total P state bugs: %s</strong></p>"%scrubber_state["status"]["P_status"]["total_P"]
            #result += "<strong>Per Submitter Count:</strong>"
            result += "<hr>"
            I_state = dict()
            for i_submitter in scrubber_state["status"]["P_Submitter"].keys():
                I_state[i_submitter] = scrubber_state["status"]["P_Submitter"][i_submitter]["count"]
            I_state = dict(sorted(I_state.items(),key=lambda t:t[1],reverse=True))
            for i_submitter in I_state.keys():
                result += "For Submitter: <strong>%s</strong><ul>"%i_submitter
                result += "<li>Count: <strong>%s</strong></li>"%I_state[i_submitter]
                
                i_bug = ""
                for bug in scrubber_state["status"]["P_Submitter"][i_submitter]["bugids"]:
                    i_bug += bug + ","
                
                result += "<li>P State Bugs: <strong>%s</strong></li>"%i_bug
                result += "</ul><hr>"
            result += "<br>For more details : " + ("https://wwwin-ottawa.cisco.com/tfoggoa/Scrubber/showquery.html?query=" + scrubber_id if type=="webex" else ("<a href='"+ "https://wwwin-ottawa.cisco.com/tfoggoa/Scrubber/showquery.html?query=" + scrubber_id  +"'>" + "scrubber_id" + scrubber_id  + "</a>")) 
        else:
            result += "<strong>No P state Bugs Found</strong>"
        return result
    elif state =="o":
        if "total_O" in scrubber_state["status"]["O_status"].keys():
            result += "<p>O State Bugs Summary for scrubber : <strong>%s</strong>"%scrubber_id
            #state_bugs["I"] = scrubber_output["status"]["I_status"]["total_I"]
            result += "<p><strong>Total O state bugs: %s</strong></p>"%scrubber_state["status"]["O_status"]["total_O"]
            #result += "<strong>Per Submitter Count:</strong>"
            result += "<hr>"
            I_state = dict()
            for i_submitter in scrubber_state["status"]["O_Submitter"].keys():
                I_state[i_submitter] = scrubber_state["status"]["O_Submitter"][i_submitter]["count"]
            I_state = dict(sorted(I_state.items(),key=lambda t:t[1],reverse=True))
            for i_submitter in I_state.keys():
                result += "For Submitter: <strong>%s</strong><ul>"%i_submitter
                result += "<li>Count: <strong>%s</strong></li>"%I_state[i_submitter]
                
                i_bug = ""
                for bug in scrubber_state["status"]["O_Submitter"][i_submitter]["bugids"]:
                    i_bug += bug + ","
                
                result += "<li>O State Bugs: <strong>%s</strong></li>"%i_bug
                result += "</ul><hr>"
            result += "<br>For more details : " + ("https://wwwin-ottawa.cisco.com/tfoggoa/Scrubber/showquery.html?query=" + scrubber_id if type=="webex" else ("<a href='"+ "https://wwwin-ottawa.cisco.com/tfoggoa/Scrubber/showquery.html?query=" + scrubber_id  +"'>" + "scrubber_id" + scrubber_id  + "</a>")) 
        else:
            result += "<strong>No O state Bugs Found</strong>"
        return result   
    elif state =="d":
        if "total_D" in scrubber_state["status"]["D_status"].keys():
            result += "<p> D State Bugs Summary for scrubber : <strong>%s</strong>"%scrubber_id
            #state_bugs["I"] = scrubber_output["status"]["I_status"]["total_I"]
            result += "<p><strong>Total D state bugs: %s</strong></p>"%scrubber_state["status"]["D_status"]["total_D"]
            #result += "<strong>Per Submitter Count:</strong>"
            result += "<hr>"
            I_state = dict()
            for i_submitter in scrubber_state["status"]["D_Submitter"].keys():
                I_state[i_submitter] = scrubber_state["status"]["D_Submitter"][i_submitter]["count"]
            I_state = dict(sorted(I_state.items(),key=lambda t:t[1],reverse=True))
            for i_submitter in I_state.keys():
                result += "For Submitter: <strong>%s</strong><ul>"%i_submitter
                result += "<li>Count: <strong>%s</strong></li>"%I_state[i_submitter]
                
                i_bug = ""
                for bug in scrubber_state["status"]["D_Submitter"][i_submitter]["bugids"]:
                    i_bug += bug + ","
                
                result += "<li>D State Bugs: <strong>%s</strong></li>"%i_bug
                result += "</ul><hr>"
            result += "<br>For more details : " + ("https://wwwin-ottawa.cisco.com/tfoggoa/Scrubber/showquery.html?query=" + scrubber_id if type=="webex" else ("<a href='"+ "https://wwwin-ottawa.cisco.com/tfoggoa/Scrubber/showquery.html?query=" + scrubber_id  +"'>" + "scrubber_id" + scrubber_id  + "</a>")) 
        else:
            result += "<strong>No D state Bugs Found</strong>"
        return result

def get_last_scrubber_id(user):
    
=======
def get_last_scrubber_id(user):
    import pdb; pdb.set_trace()
>>>>>>> origin/master-live
    scrubber_user_api = "https://wwwin-ottawa.cisco.com/tfoggoa/Scrubber/api/users/" + user
    try:
        scrubber_user_api = requests.request("GET",f"{scrubber_user_api}")
        scrubber_user_data = json.loads(scrubber_user_api.content)
        if scrubber_user_data["status"] == "success":
            #print(scrubber_user_data[user])
            return scrubber_user_data[user][0]["datafile"]
        else:
            return False
    except:
        return False
<<<<<<< HEAD
def get_bugs_from_scrubber(scrubber_id):

    scrubber_id_api = "https://wwwin-ottawa.cisco.com/tfoggoa/Scrubber/api/queries/" + scrubber_id
    scrubber_data = dict()
    
    try:
        output = requests.request("GET",scrubber_id_api)
        
        json_content = json.loads(output.content.decode("utf-8","ignore"))
        if json_content["status"] == "success":
            #if "total_bugs" in scrubber_data.keys():
            #
            scrubber_data["total_bugs"] = len(json_content[scrubber_id]["bug"])
            scrubber_data["name"] = json_content[scrubber_id]["queryinfo"]["name"]
            scrubber_data["query"] = json_content[scrubber_id]["queryinfo"]["string"]
            scrubber_data["submitter"] = dict()
            scrubber_data["director"] = dict()
            scrubber_data["sev"] = dict()
            scrubber_data["status"] = dict()
            scrubber_data["status"]["I_status"] = dict()
            scrubber_data["status"]["I_Submitter"] = dict()
            #scrubber_data["status"]["I_status"]["submitter_count"] = dict()
            scrubber_data["status"]["A_status"] = dict()
            scrubber_data["status"]["A_Submitter"] = dict()
            #scrubber_data["status"]["A_status"]["submitter_count"] = dict()
            scrubber_data["status"]["M_status"] = dict()
            scrubber_data["status"]["M_Submitter"] = dict()
            #scrubber_data["status"]["M_status"]["submitter_count"] = dict()
            scrubber_data["status"]["N_status"] = dict()
            scrubber_data["status"]["N_Submitter"] = dict()
            #scrubber_data["status"]["N_status"]["submitter_count"] = dict()
            scrubber_data["status"]["R_status"] = dict()
            scrubber_data["status"]["R_Submitter"] = dict()
            #scrubber_data["status"]["R_status"]["submitter_count"] = dict()
            
            scrubber_data["status"]["V_status"] = dict()
            scrubber_data["status"]["V_Submitter"] = dict()
            #scrubber_data["status"]["I_status"]["submitter_count"] = dict()
            scrubber_data["status"]["C_status"] = dict()
            scrubber_data["status"]["C_Submitter"] = dict()
            #scrubber_data["status"]["A_status"]["submitter_count"] = dict()
            scrubber_data["status"]["J_status"] = dict()
            scrubber_data["status"]["J_Submitter"] = dict()
            #scrubber_data["status"]["M_status"]["submitter_count"] = dict()
            scrubber_data["status"]["U_status"] = dict()
            scrubber_data["status"]["U_Submitter"] = dict()
            #scrubber_data["status"]["N_status"]["submitter_count"] = dict()
            scrubber_data["status"]["D_status"] = dict()
            scrubber_data["status"]["D_Submitter"] = dict()
            scrubber_data["status"]["O_status"] = dict()
            scrubber_data["status"]["O_Submitter"] = dict()
            scrubber_data["status"]["W_status"] = dict()
            scrubber_data["status"]["W_Submitter"] = dict()
            scrubber_data["status"]["P_status"] = dict()
            scrubber_data["status"]["P_Submitter"] = dict()
            #scrubber_data["status"]["R_status"]["submitter_count"] = dict()
            scrubber_data["manager"] = dict()
            scrubber_data["engineer"] = dict()
            scrubber_data["comp"] = dict()
            scrubber_data["product"] = dict()
            scrubber_data["regression"] = dict()
            scrubber_data["all_cdets"] = []
            scrubber_data["eta"] = dict()
            scrubber_data["non_eta"] = dict()
            scrubber_data["found"] = dict()
            if len(json_content[scrubber_id]["bug"]) > 0:
                for cdet in json_content[scrubber_id]["bug"]:
                    all_keys = cdet.keys()
                    if "bugid" in all_keys:
                        scrubber_data["all_cdets"].append(cdet["bugid"])
                    if "submitter" in all_keys:
                        if cdet["submitter"] in scrubber_data["submitter"].keys():
                            scrubber_data["submitter"][cdet["submitter"]]["count"] += 1
                            scrubber_data["submitter"][cdet["submitter"]]["bug_ids"].append(cdet["bugid"])
                        else:
                            scrubber_data["submitter"][cdet["submitter"]] = dict()
                            scrubber_data["submitter"][cdet["submitter"]]["count"] = 1
                            scrubber_data["submitter"][cdet["submitter"]]["bug_ids"] = [cdet["bugid"]]
                    # if "all_cdets" in scrubber_data["submitter"].keys():
                    #     scrubber_data["submitter"][cdet["submitter"]]["count"] += 1
                    #     scrubber_data["submitter"][cdet["submitter"]]["bug_ids"].append(cdet["bugid"])
                    # else:
                    #     scrubber_data["submitter"][cdet["submitter"]] = dict()
                    #     scrubber_data["submitter"][cdet["submitter"]]["count"] = 1
                    #     scrubber_data["submitter"][cdet["submitter"]]["bug_ids"] = [cdet["bugid"]]
                    #
                    if "found" in all_keys:
                        if cdet["found"] in scrubber_data["found"].keys():
                            scrubber_data["found"][cdet["found"]]["count"] += 1
                            scrubber_data["found"][cdet["found"]]["bug_ids"].append(cdet["bugid"])
                        else:
                            scrubber_data["found"][cdet["found"]] = dict()
                            scrubber_data["found"][cdet["found"]]["count"] = 1
                            scrubber_data["found"][cdet["found"]]["bug_ids"] = [cdet["bugid"]]
                    if "estfix" in all_keys:
                        if re.search("\d+",cdet["estfix"]):
                            if "eta_bugs" in scrubber_data["eta"].keys():
                                scrubber_data["eta"]["count"] += 1
                                scrubber_data["eta"]["eta_bugs"].append(cdet["bugid"])
                            else:
                                scrubber_data["eta"]= {"count":1}
                                scrubber_data["eta"]["eta_bugs"] = [cdet["bugid"]]
                        else:
                            if "non_eta_bugs" in scrubber_data["non_eta"].keys():
                                scrubber_data["non_eta"]["count"] += 1
                                scrubber_data["non_eta"]["non_eta_bugs"].append(cdet["bugid"])
                            else:
                                scrubber_data["non_eta"] = {"count":1}
                                scrubber_data["non_eta"]["non_eta_bugs"] = [cdet["bugid"]]

                    if "director" in all_keys:  
                        if cdet["director"] in scrubber_data["director"].keys():
                            scrubber_data["director"][cdet["director"]]["count"] += 1
                            scrubber_data["director"][cdet["director"]]["bug_ids"].append(cdet["bugid"])
                        else:
                            scrubber_data["director"][cdet["director"]] = dict()
                            scrubber_data["director"][cdet["director"]]["count"] = 1
                            scrubber_data["director"][cdet["director"]]["bug_ids"] = [cdet["bugid"]]
                    if "manager" in all_keys:  
                        if cdet["manager"] in scrubber_data["manager"].keys():
                            scrubber_data["manager"][cdet["manager"]]["count"] += 1
                            scrubber_data["manager"][cdet["manager"]]["bug_ids"].append(cdet["bugid"])
                        else:
                            scrubber_data["manager"][cdet["manager"]] = dict()
                            scrubber_data["manager"][cdet["manager"]]["count"] = 1
                            scrubber_data["manager"][cdet["manager"]]["bug_ids"] = [cdet["bugid"]]
                    if "comp" in all_keys:
                        if cdet["comp"] in scrubber_data["comp"].keys():
                            scrubber_data["comp"][cdet["comp"]]["count"] += 1
                            scrubber_data["comp"][cdet["comp"]]["bug_ids"].append(cdet["bugid"])
                        else:
                            scrubber_data["comp"][cdet["comp"]] = dict()
                            scrubber_data["comp"][cdet["comp"]]["count"] = 1
                            scrubber_data["comp"][cdet["comp"]]["bug_ids"] = [cdet["bugid"]]
                    if "product" in all_keys:   
                        if cdet["product"] in scrubber_data["product"].keys():
                            scrubber_data["product"][cdet["product"]]["count"] += 1
                            scrubber_data["product"][cdet["product"]]["bug_ids"].append(cdet["bugid"])
                        else:
                            scrubber_data["product"][cdet["product"]] = dict()
                            scrubber_data["product"][cdet["product"]]["count"] = 1
                            scrubber_data["product"][cdet["product"]]["bug_ids"] = [cdet["bugid"]]

                    if "regression" in all_keys:
                        if cdet["regression"] == "Y":
                            if cdet["regression"] in scrubber_data["regression"].keys():
                                scrubber_data["regression"]["reg_count"] += 1
                                scrubber_data["regression"]["bug_ids"].append(cdet["bugid"])
                            else:
                                scrubber_data["regression"] = {"reg_count":1}
                                scrubber_data["regression"]["bug_ids"] = [cdet["bugid"]]

                    if "sev" in all_keys:
                        if int(cdet["sev"]) == 1:
                            if "sev1" in scrubber_data["sev"].keys():
                                scrubber_data["sev"]["sev1"]["count"] += 1
                                scrubber_data["sev"]["sev1"]["sev1_id"].append(cdet["bugid"])
                            else:
                                scrubber_data["sev"]["sev1"] = dict()
                                scrubber_data["sev"]["sev1"]["count"] = 1
                                scrubber_data["sev"]["sev1"]["sev1_id"] = [cdet["bugid"]]
                        elif int(cdet["sev"]) == 2:
                            if "sev2" in scrubber_data["sev"].keys():
                                scrubber_data["sev"]["sev2"]["count"] += 1
                                scrubber_data["sev"]["sev2"]["sev1_id"].append(cdet["bugid"])
                            else:
                                scrubber_data["sev"]["sev2"] = dict()
                                scrubber_data["sev"]["sev2"]["count"] = 1
                                scrubber_data["sev"]["sev2"]["sev1_id"] = [cdet["bugid"]]
                        elif int(cdet["sev"]) == 3:
                            if "sev3" in scrubber_data["sev"].keys():
                                scrubber_data["sev"]["sev3"]["count"] += 1
                                scrubber_data["sev"]["sev3"]["sev1_id"].append(cdet["bugid"])
                            else:
                                scrubber_data["sev"]["sev3"] = dict()
                                scrubber_data["sev"]["sev3"]["count"] = 1
                                scrubber_data["sev"]["sev3"]["sev1_id"] = [cdet["bugid"]]
                        elif int(cdet["sev"]) == 4:
                            if "sev4" in scrubber_data["sev"].keys():
                                scrubber_data["sev"]["sev4"]["count"] += 1
                                scrubber_data["sev"]["sev4"]["sev1_id"].append(cdet["bugid"])
                            else:
                                scrubber_data["sev"]["sev4"] = dict()
                                scrubber_data["sev"]["sev4"]["count"] = 1
                                scrubber_data["sev"]["sev4"]["sev1_id"] = [cdet["bugid"]]
                        elif int(cdet["sev"]) == 5:
                            if "sev5" in scrubber_data["sev"].keys():
                                scrubber_data["sev"]["sev5"]["count"] += 1
                                scrubber_data["sev"]["sev5"]["sev1_id"].append(cdet["bugid"])
                            else:
                                scrubber_data["sev"]["sev5"] = dict()
                                scrubber_data["sev"]["sev5"]["count"] = 1
                                scrubber_data["sev"]["sev5"]["sev1_id"] = [cdet["bugid"]]
                        elif int(cdet["sev"]) == 6:
                            if "sev6" in scrubber_data["sev"].keys():
                                scrubber_data["sev"]["sev6"]["count"] += 1
                                scrubber_data["sev"]["sev6"]["sev1_id"].append(cdet["bugid"])
                            else:
                                scrubber_data["sev"]["sev6"] = dict()
                                scrubber_data["sev"]["sev6"]["count"] = 1
                                scrubber_data["sev"]["sev6"]["sev1_id"] = [cdet["bugid"]]
                    
                    if "status" in all_keys:
                        if  cdet["status"] == "I":
                            #scrubber_data["status"]["I_status"] = 
                            if "total_I" in scrubber_data["status"]["I_status"].keys():
                                scrubber_data["status"]["I_status"]["total_I"] += 1
                            else:
                                scrubber_data["status"]["I_status"] = {"total_I":1}
                            
                            if cdet["submitter"] in scrubber_data["status"]["I_Submitter"].keys():
                                scrubber_data["status"]["I_Submitter"][cdet["submitter"]]["count"] += 1
                                scrubber_data["status"]["I_Submitter"][cdet["submitter"]]["bugids"].append(cdet["bugid"])
                            else:
                                scrubber_data["status"]["I_Submitter"][cdet["submitter"]] = dict()
                                scrubber_data["status"]["I_Submitter"][cdet["submitter"]] = {"count":1,"bugids":[cdet["bugid"]]}
                            # if "cdet_id" in scrubber_data["status"]["I_status"].keys():
                            #     scrubber_data["status"]["I_status"]["cdet_id"].append(cdet["bugid"])
                            # else :
                            #     scrubber_data["status"]["I_status"]["cdet_id"] = [cdet["bugid"]]
                            # if cdet["submitter"] in scrubber_data["status"]["I_status"]["submitter_count"].keys():

                            #     scrubber_data["status"]["I_status"]["submitter_count"][cdet["submitter"]]+=1
                            # else :
                            #     scrubber_data["status"]["I_status"]["submitter_count"] = dict()
                            #     scrubber_data["status"]["I_status"]["submitter_count"][cdet["submitter"]]= 1
                        if  cdet["status"] == "A":
                            #scrubber_data["status"]["I_status"] = 
                            if "total_A" in scrubber_data["status"]["A_status"].keys():
                                scrubber_data["status"]["A_status"]["total_A"] += 1
                            else:
                                scrubber_data["status"]["A_status"] = {"total_A":1}
                            if cdet["submitter"] in scrubber_data["status"]["A_Submitter"].keys():
                                scrubber_data["status"]["A_Submitter"][cdet["submitter"]]["count"] += 1
                                scrubber_data["status"]["A_Submitter"][cdet["submitter"]]["bugids"].append(cdet["bugid"])
                            else:
                                scrubber_data["status"]["A_Submitter"][cdet["submitter"]] = dict()
                                scrubber_data["status"]["A_Submitter"][cdet["submitter"]] = {"count":1,"bugids":[cdet["bugid"]]}
                            # if "cdet_id" in scrubber_data["status"]["A_status"].keys():
                            #     scrubber_data["status"]["A_status"]["cdet_id"].append(cdet["bugid"])
                            # else :
                            #     scrubber_data["status"]["A_status"]["cdet_id"] = [cdet["bugid"]]
                            # if cdet["submitter"] in scrubber_data["status"]["A_status"]["submitter_count"].keys():
                            #     scrubber_data["status"]["A_status"]["submitter_count"][cdet["submitter"]]+=1
                            # else :
                            #     scrubber_data["status"]["A_status"]["submitter_count"] = dict()
                            #     scrubber_data["status"]["A_status"]["submitter_count"][cdet["submitter"]]= 1
                        if  cdet["status"] == "N":
                            #scrubber_data["status"]["I_status"] = 
                            if "total_N" in scrubber_data["status"]["N_status"].keys():
                                scrubber_data["status"]["N_status"]["total_N"] += 1
                            else:
                                scrubber_data["status"]["N_status"] = {"total_N":1}
                            
                            if cdet["submitter"] in scrubber_data["status"]["N_Submitter"].keys():
                                scrubber_data["status"]["N_Submitter"][cdet["submitter"]]["count"] += 1
                                scrubber_data["status"]["N_Submitter"][cdet["submitter"]]["bugids"].append(cdet["bugid"])
                            else:
                                scrubber_data["status"]["N_Submitter"][cdet["submitter"]] = dict()
                                scrubber_data["status"]["N_Submitter"][cdet["submitter"]] = {"count":1,"bugids":[cdet["bugid"]]}
                            # if "cdet_id" in scrubber_data["status"]["N_status"].keys():
                            #     scrubber_data["status"]["N_status"]["cdet_id"].append(cdet["bugid"])
                            # else :
                            #     scrubber_data["status"]["N_status"]["cdet_id"] = [cdet["bugid"]]
                            # if cdet["submitter"] in scrubber_data["status"]["N_status"]["submitter_count"].keys():
                            #     scrubber_data["status"]["N_status"]["submitter_count"][cdet["submitter"]]+=1
                            # else :
                            #     scrubber_data["status"]["N_status"]["submitter_count"] = dict()
                            #     scrubber_data["status"]["N_status"]["submitter_count"][cdet["submitter"]]= 1
                        if  cdet["status"] == "R":
                            #scrubber_data["status"]["I_status"] = 
                            if "total_R" in scrubber_data["status"]["R_status"].keys():
                                scrubber_data["status"]["R_status"]["total_R"] += 1
                            else:
                                scrubber_data["status"]["R_status"] = {"total_R":1}
                            
                            if cdet["submitter"] in scrubber_data["status"]["R_Submitter"].keys():
                                scrubber_data["status"]["R_Submitter"][cdet["submitter"]]["count"] += 1
                                scrubber_data["status"]["R_Submitter"][cdet["submitter"]]["bugids"].append(cdet["bugid"])
                            else:
                                scrubber_data["status"]["R_Submitter"][cdet["submitter"]] = dict()
                                scrubber_data["status"]["R_Submitter"][cdet["submitter"]] = {"count":1,"bugids":[cdet["bugid"]]}
                            # if "cdet_id" in scrubber_data["status"]["R_status"].keys():
                            #     scrubber_data["status"]["R_status"]["cdet_id"].append(cdet["bugid"])
                            # else :
                            #     scrubber_data["status"]["R_status"]["cdet_id"] = [cdet["bugid"]]
                            # if cdet["submitter"] in scrubber_data["status"]["R_status"]["submitter_count"].keys():
                            #     scrubber_data["status"]["R_status"]["submitter_count"][cdet["submitter"]]+=1
                            # else :
                            #     #scrubber_data["status"]["R_status"]["submitter_count"] = dict()
                            #     scrubber_data["status"]["R_status"]["submitter_count"][cdet["submitter"]]= 1    
                        if  cdet["status"] == "M":
                            #scrubber_data["status"]["I_status"] = 
                            if "total_M" in scrubber_data["status"]["M_status"].keys():
                                scrubber_data["status"]["M_status"]["total_M"] += 1
                            else:
                                scrubber_data["status"]["M_status"] = {"total_M":1}
                            
                            if cdet["submitter"] in scrubber_data["status"]["M_Submitter"].keys():
                                scrubber_data["status"]["M_Submitter"][cdet["submitter"]]["count"] += 1
                                scrubber_data["status"]["M_Submitter"][cdet["submitter"]]["bugids"].append(cdet["bugid"])
                            else:
                                scrubber_data["status"]["M_Submitter"][cdet["submitter"]] = dict()
                                scrubber_data["status"]["M_Submitter"][cdet["submitter"]] = {"count":1,"bugids":[cdet["bugid"]]}
                            # if "cdet_id" in scrubber_data["status"]["M_status"].keys():
                            #     scrubber_data["status"]["M_status"]["cdet_id"].append(cdet["bugid"])
                            # else :
                            #     scrubber_data["status"]["M_status"]["cdet_id"] = [cdet["bugid"]]
                            # if cdet["submitter"] in scrubber_data["status"]["M_status"]["submitter_count"].keys():
                            #     scrubber_data["status"]["M_status"]["submitter_count"][cdet["submitter"]]+=1
                            # else :
                            #     scrubber_data["status"]["M_status"]["submitter_count"] = dict()
                            #     scrubber_data["status"]["M_status"]["submitter_count"][cdet["submitter"]]= 1
                        if  cdet["status"] == "V":
                            #scrubber_data["status"]["I_status"] = 
                            if "total_V" in scrubber_data["status"]["V_status"].keys():
                                scrubber_data["status"]["V_status"]["total_V"] += 1
                            else:
                                scrubber_data["status"]["V_status"] = {"total_V":1}
                            
                            if cdet["submitter"] in scrubber_data["status"]["V_Submitter"].keys():
                                scrubber_data["status"]["V_Submitter"][cdet["submitter"]]["count"] += 1
                                scrubber_data["status"]["V_Submitter"][cdet["submitter"]]["bugids"].append(cdet["bugid"])
                            else:
                                scrubber_data["status"]["V_Submitter"][cdet["submitter"]] = dict()
                                scrubber_data["status"]["V_Submitter"][cdet["submitter"]] = {"count":1,"bugids":[cdet["bugid"]]}
                        if  cdet["status"] == "P":
                            #scrubber_data["status"]["I_status"] = 
                            if "total_P" in scrubber_data["status"]["P_status"].keys():
                                scrubber_data["status"]["P_status"]["total_P"] += 1
                            else:
                                scrubber_data["status"]["P_status"] = {"total_P":1}
                            
                            if cdet["submitter"] in scrubber_data["status"]["P_Submitter"].keys():
                                scrubber_data["status"]["P_Submitter"][cdet["submitter"]]["count"] += 1
                                scrubber_data["status"]["P_Submitter"][cdet["submitter"]]["bugids"].append(cdet["bugid"])
                            else:
                                scrubber_data["status"]["P_Submitter"][cdet["submitter"]] = dict()
                                scrubber_data["status"]["P_Submitter"][cdet["submitter"]] = {"count":1,"bugids":[cdet["bugid"]]}                            
                        if  cdet["status"] == "W":
                            #scrubber_data["status"]["I_status"] = 
                            if "total_W" in scrubber_data["status"]["W_status"].keys():
                                scrubber_data["status"]["W_status"]["total_W"] += 1
                            else:
                                scrubber_data["status"]["W_status"] = {"total_W":1}
                            
                            if cdet["submitter"] in scrubber_data["status"]["W_Submitter"].keys():
                                scrubber_data["status"]["W_Submitter"][cdet["submitter"]]["count"] += 1
                                scrubber_data["status"]["W_Submitter"][cdet["submitter"]]["bugids"].append(cdet["bugid"])
                            else:
                                scrubber_data["status"]["W_Submitter"][cdet["submitter"]] = dict()
                                scrubber_data["status"]["W_Submitter"][cdet["submitter"]] = {"count":1,"bugids":[cdet["bugid"]]}
                        if  cdet["status"] == "O":
                            #scrubber_data["status"]["I_status"] = 
                            if "total_O" in scrubber_data["status"]["O_status"].keys():
                                scrubber_data["status"]["O_status"]["total_O"] += 1
                            else:
                                scrubber_data["status"]["O_status"] = {"total_O":1}
                            
                            if cdet["submitter"] in scrubber_data["status"]["O_Submitter"].keys():
                                scrubber_data["status"]["O_Submitter"][cdet["submitter"]]["count"] += 1
                                scrubber_data["status"]["O_Submitter"][cdet["submitter"]]["bugids"].append(cdet["bugid"])
                            else:
                                scrubber_data["status"]["O_Submitter"][cdet["submitter"]] = dict()
                                scrubber_data["status"]["O_Submitter"][cdet["submitter"]] = {"count":1,"bugids":[cdet["bugid"]]}
                        if  cdet["status"] == "D":
                            #scrubber_data["status"]["I_status"] = 
                            if "total_D" in scrubber_data["status"]["D_status"].keys():
                                scrubber_data["status"]["D_status"]["total_D"] += 1
                            else:
                                scrubber_data["status"]["D_status"] = {"total_D":1}
                            
                            if cdet["submitter"] in scrubber_data["status"]["D_Submitter"].keys():
                                scrubber_data["status"]["D_Submitter"][cdet["submitter"]]["count"] += 1
                                scrubber_data["status"]["D_Submitter"][cdet["submitter"]]["bugids"].append(cdet["bugid"])
                            else:
                                scrubber_data["status"]["D_Submitter"][cdet["submitter"]] = dict()
                                scrubber_data["status"]["D_Submitter"][cdet["submitter"]] = {"count":1,"bugids":[cdet["bugid"]]}                              
                return scrubber_data           
            else:
                return False                   
            #return json_content[scrubber_id]
        else:
            return False

    except Exception as e:
        return False
            

def get_all_scrubber_data(scrubber_id,scrubber_output):
    result = "<p>Statics for Scrubber:  <strong>%s</strong></p>"%scrubber_id
    result += "<p>Name: <strong>%s</strong></p>"%scrubber_output["name"]
    result += "<p>Total Bugs: <strong>%s</strong></p>"%str(scrubber_output["total_bugs"])
    result += "<p>Query: <strong>%s</strong></p>"%scrubber_output["query"]
    if "count" in scrubber_output["eta"].keys():
        result += "<p>ETA Bugs Count: <strong>%s</strong></p>"%scrubber_output["eta"]["count"]
    else:
        result += "<p>ETA Bugs Count: <strong>0</strong></p>"
    if "count" in scrubber_output["non_eta"].keys():
        result += "<p>Non ETA Bugs Count: <strong>%s</strong></p>"%scrubber_output["non_eta"]["count"]
    else:
        result += "<p>Non ETA Bugs Count: <strong>0</strong></p>"
    # result += "<li>Bug List: "
    # for bug in scrubber_output["all_cdets"]:
    #     result += "<strong>%s</strong>,"%bug
    # result += "</li>"
    result += "<hr>"
    state_bugs = dict()
    result += "<strong>Per Bug State Count</strong><ul>"
    if "total_I" in scrubber_output["status"]["I_status"].keys():
        state_bugs["I"] = scrubber_output["status"]["I_status"]["total_I"]
        #result += "<li>I State Bugs: <strong>%s</strong></li>"%scrubber_output["status"]["I_status"]["total_I"]
    if "total_A" in scrubber_output["status"]["A_status"].keys():
        state_bugs["A"] = scrubber_output["status"]["A_status"]["total_A"]
        #result += "<li>A State Bugs: <strong>%s</strong></li>"%scrubber_output["status"]["A_status"]["total_A"]
    if "total_R" in scrubber_output["status"]["R_status"].keys():
        state_bugs["R"] = scrubber_output["status"]["R_status"]["total_R"]
        #result += "<li>R State Bugs: <strong>%s</strong></li>"%scrubber_output["status"]["R_status"]["total_R"]
    if "total_N" in scrubber_output["status"]["N_status"].keys():
        state_bugs["N"] = scrubber_output["status"]["N_status"]["total_N"]
        #result += "<li>N State Bugs: <strong>%s</strong></li>"%scrubber_output["status"]["N_status"]["total_N"]
    if "total_M" in scrubber_output["status"]["M_status"].keys():
        state_bugs["M"] = scrubber_output["status"]["M_status"]["total_M"]
        #result += "<li>M State Bugs: <strong>%s</strong></li>"%scrubber_output["status"]["M_status"]["total_M"]
    #
    ord_bugs = dict(sorted(state_bugs.items(), key=lambda t: t[1],reverse=True))
    for state in ord_bugs.keys():
        if state == "I":
            result += "<li>I State Bugs: <strong>%s</strong></li>"%(ord_bugs["I"])
        if state == "A":
            result += "<li>A State Bugs: <strong>%s</strong></li>"%(ord_bugs["A"])
        if state == "R":
            result += "<li>R State Bugs: <strong>%s</strong></li>"%(ord_bugs["R"])
        if state == "N":
            result += "<li>N State Bugs: <strong>%s</strong></li>"%(ord_bugs["N"])
        if state == "M":
            result += "<li>M State Bugs: <strong>%s</strong></li>"%(ord_bugs["M"])
        
    result += "</ul><hr>"
    sev_bugs = dict()
    result += "<strong>Per Bug Severity Count</strong><ul>"
    if "sev1" in scrubber_output["sev"].keys():
        sev_bugs["sev1"] = scrubber_output["sev"]["sev1"]["count"]
        #result += "<li> Sev 1: <strong>%s</strong></li>"%scrubber_output["sev"]["sev1"]["count"]
    if "sev2" in scrubber_output["sev"].keys():
        sev_bugs["sev2"] = scrubber_output["sev"]["sev2"]["count"]
        #result += "<li> Sev 2: <strong>%s</strong></li>"%scrubber_output["sev"]["sev2"]["count"]
    if "sev3" in scrubber_output["sev"].keys():
        sev_bugs["sev3"] = scrubber_output["sev"]["sev3"]["count"]
        #result += "<li> Sev 3: <strong>%s</strong></li>"%scrubber_output["sev"]["sev3"]["count"]
    if "sev4" in scrubber_output["sev"].keys():
        sev_bugs["sev4"] = scrubber_output["sev"]["sev4"]["count"]
        #result += "<li> Sev 4: <strong>%s</strong></li>"%scrubber_output["sev"]["sev3"]["count"]
    sev_bugs = dict(sorted(sev_bugs.items(),key=lambda t:t[1], reverse=True))
    for sev in sev_bugs.keys():
        if sev == "sev1":
            result += "<li> Sev 1: <strong>%s</strong></li>"%sev_bugs["sev1"]
        if sev == "sev2":
            result += "<li> Sev 2: <strong>%s</strong></li>"%sev_bugs["sev2"]
        if sev == "sev3":
            result += "<li> Sev 3: <strong>%s</strong></li>"%sev_bugs["sev3"]
        if sev == "sev4":
            result += "<li> Sev 4: <strong>%s</strong></li>"%sev_bugs["sev3"]
    result += "</ul><hr>"

    
    found_count = dict()
    result += "<strong>Per Found Count</strong><ul>"
    if scrubber_output["found"] :
        for found in scrubber_output["found"].keys():
            found_count[found] = scrubber_output["found"][found]['count']
            #result += "<li> %s: <strong>%s</strong></li>"%(submitter,scrubber_output["submitter"][submitter]['count'])
        found_count = dict(sorted(found_count.items(),key=lambda t:t[1],reverse=True))
        for found in  found_count.keys():
            result += "<li> %s: <strong>%s</strong></li>"%(found,found_count[found])
    result += "</ul><hr>"
    submitter_count = dict()
    result += "<strong>Per Submitter Count</strong><ul>"
    if scrubber_output["submitter"] :
        for submitter in scrubber_output["submitter"].keys():
            submitter_count[submitter] = scrubber_output["submitter"][submitter]['count']
            #result += "<li> %s: <strong>%s</strong></li>"%(submitter,scrubber_output["submitter"][submitter]['count'])
        submitter_count = dict(sorted(submitter_count.items(),key=lambda t:t[1],reverse=True))
        for submitter in  submitter_count.keys():
            result += "<li> %s: <strong>%s</strong></li>"%(submitter,submitter_count[submitter])
    result += "</ul><hr>"
    director_count = dict()
    result += "<strong>Per Director Count</strong><ul>"
    if scrubber_output["director"] :
        # for director in scrubber_output["director"].keys():
        #     result += "<li> %s: <strong>%s</strong></li>"%(director,scrubber_output["director"][director]['count'])
        
        for director in scrubber_output["director"].keys():
            director_count[director] = scrubber_output["director"][director]['count']
            #result += "<li> %s: <strong>%s</strong></li>"%(submitter,scrubber_output["submitter"][submitter]['count'])
        director_count = dict(sorted(director_count.items(),key=lambda t:t[1],reverse=True))
        for director in  director_count.keys():
            result += "<li> %s: <strong>%s</strong></li>"%(director,director_count[director])
    
    result += "</ul><hr>"
    manager_count = dict()
    result += "<strong>Per Manager Count</strong><ul>"
    if scrubber_output["manager"] :
        for manager in scrubber_output["manager"].keys():
            manager_count[submitter] = scrubber_output["manager"][manager]['count']
            #result += "<li> %s: <strong>%s</strong></li>"%(submitter,scrubber_output["submitter"][submitter]['count'])
        manager_count = dict(sorted(manager_count.items(),key=lambda t:t[1],reverse=True))
        for manager in  manager_count.keys():
            result += "<li> %s: <strong>%s</strong></li>"%(manager,manager_count[manager])
    result += "</ul><hr>"
    comp_count = dict()
    result += "<strong>Per Componenet Count</strong><ul>"
    if scrubber_output["comp"] :
        for comp in scrubber_output["comp"].keys():
            comp_count[comp] = scrubber_output["comp"][comp]['count']
            #result += "<li> %s: <strong>%s</strong></li>"%(submitter,scrubber_output["submitter"][submitter]['count'])
        comp_count = dict(sorted(comp_count.items(),key=lambda t:t[1],reverse=True))
        for comp in  comp_count.keys():
            result += "<li> %s: <strong>%s</strong></li>"%(comp,comp_count[comp])
    result += "</ul><hr>"
    product_count = dict()
    result += "<strong>Per Product Count</strong><ul>"
    if scrubber_output["product"] :
        for product in scrubber_output["product"].keys():
            product_count[product] = scrubber_output["product"][product]['count']
            #result += "<li> %s: <strong>%s</strong></li>"%(submitter,scrubber_output["submitter"][submitter]['count'])
        product_count = dict(sorted(product_count.items(),key=lambda t:t[1],reverse=True))
        for product in  product_count.keys():
            result += "<li> %s: <strong>%s</strong></li>"%(product,product_count[product])
    result += "</ul><hr>"
    result += "<br>For more details : " + ("https://wwwin-ottawa.cisco.com/tfoggoa/Scrubber/showquery.html?query=" + scrubber_id if type=="webex" else ("<a href='"+ "https://wwwin-ottawa.cisco.com/tfoggoa/Scrubber/showquery.html?query=" + scrubber_id  +"'>" + "scrubber_id" + scrubber_id  + "</a>"))                
    return result                           



def get_scrubber_query(user):

    scrubber_id_api = "https://wwwin-ottawa.cisco.com/tfoggoa/Scrubber/api/users/" + user
    scrubber_query_data = dict()
    scrubber_query_data[user] = []
    try:
        output = requests.request("GET",scrubber_id_api)
        json_content = json.loads(output.content.decode("utf-8","ignore"))
        if json_content["status"] == "success":
            if len(json_content[user]) > 0:
                for query in json_content[user]:
                    # scrubber_query_data["name"] = query["name"]
                    # scrubber_query_data["scrubber_id"] = query["datafile"]
                    # scrubber_query_data["total_bugs"] = query["bugs"]
                    # scrubber_query_data["sev1"] = query["sevone"]
                    # scrubber_query_data["sev2"] = query["sevtwo"]
                    # scrubber_query_data["query"] = query["string"]
                    scrubber_query_data[user].append({"name":query["name"],"query":query["string"],"scrubber_id":query["datafile"],"total_bugs":query["bugs"],"sev1":query["sevone"],"sev2":query["sevtwo"]})
                return scrubber_query_data    
            else:
                return False
        else:
            return False
    except:
        return False
=======
def get_bugs_from_scrubber(scrubber_id,status):

    scrubber_id_api = "https://wwwin-ottawa.cisco.com/tfoggoa/Scrubber/api/queries/" + scrubber_id

    try:
        output = requests.request("GET",scrubber_id_api)
        if output["status"] == "success":
            


>>>>>>> origin/master-live
"""
    API Functions
"""

def get_scrubber_data(question,user,type="web"):

    """

    """

    question = question.lower()
<<<<<<< HEAD
    question = question.strip()
    content = dict()
    qwords = re.split("\s+",question)
    try:
        qwords.remove("scrubber")
        qwords.remove(" ")
    except :
        pass
    question = " ".join(qwords)
=======

>>>>>>> origin/master-live
    results = ""
    "https://wwwin-ottawa.cisco.com/tfoggoa/Scrubber/api/users/dpatwa"
    "https://wwwin-ottawa.cisco.com/tfoggoa/Scrubber/api/queries/dpatwa-172"
    "https://wwwin-ottawa/tfoggoa/Scrubber/api/notes/CSCvd43303"

<<<<<<< HEAD
    if re.search("statistics|statistic|stats",question):
        scrubber_id = False
        if re.search("last|latest",question):
            if "my" in qwords:
                cec_id = user
                
                scrubber_id = get_last_scrubber_id(user)
                result = ""
                if scrubber_id:
                    scrubber_output = get_bugs_from_scrubber(scrubber_id)
                    if scrubber_output:
                        result = get_all_scrubber_data(scrubber_id,scrubber_output)
                    else:
                        result = "<strong>Scrubber API server is Down</strong>"
                else:
                    result = "<strong> Not able to get scrubber information</strong>"
            else:
                #qwords = re.split("\s+",question)
                cec_id = "all"
                for word in qwords:
                    # if word == "":
                    #     qwords.remove(" ")
                    if not eng_dict.check(word):
                        cec_id = word
                question = " ".join(qwords)
                result = ""
                if cec_id != "all":
                    scrubber_id = get_last_scrubber_id(cec_id)
                    result = ""
                    if scrubber_id:
                        scrubber_output = get_bugs_from_scrubber(scrubber_id)
                        if scrubber_output:
                            result = get_all_scrubber_data(scrubber_id,scrubber_output)
                        else:
                            result = "<strong>Scrubber API server is Down</strong>"
                    else:
                        result = "<strong> Not able to get scrubber information</strong>"
                else:
                    cec_id = user
                    scrubber_id = get_last_scrubber_id(cec_id)
                    result = ""
                    if scrubber_id:
                        scrubber_output = get_bugs_from_scrubber(scrubber_id)
                        if scrubber_output:
                            result = get_all_scrubber_data(scrubber_id,scrubber_output)
                        else:
                            result = "<strong>Scrubber API server is Down</strong>"
                    else:
                        result = "<strong> Not able to get scrubber information</strong>"
        elif re.search("\w+-\d{,8}",question):
            
            scrubber_id = re.search("(\w+-\d{,8})",question).group(1)
            result = ""
            if scrubber_id:
                scrubber_output = get_bugs_from_scrubber(scrubber_id)
                if scrubber_output:
                    result = get_all_scrubber_data(scrubber_id,scrubber_output)
                else:
                        result = "<strong>Scrubber API server is Down</strong>"
            else:
                result = "<strong> Not able to get scrubber information</strong>"
        else:
            result= "<p>Not able to fetch scrubber, Please use help scrubber and reframe you question</p>"
    elif re.search("bugs|state|states|status|bug",question):
        scrubber_id = False
        if re.search("last|latest",question):
            if "my" in qwords:
                cec_id = user
                scrubber_id = get_last_scrubber_id(user)
                result = ""
                if scrubber_id:
                    scrubber_output = get_bugs_from_scrubber(scrubber_id)
                    words  = question.split(" ")
                    # if "state" in words:
                    if "i" in words:
                    #if re.search("i|i[\s+]?state",question):
                        result = state_wise_bugs(scrubber_id,scrubber_output,"i")
                    elif "r" in words:
                        result = state_wise_bugs(scrubber_id,scrubber_output,"r")
                    elif "a" in words:
                        result = state_wise_bugs(scrubber_id,scrubber_output,"a")
                    elif "m" in words:
                        result = state_wise_bugs(scrubber_id,scrubber_output,"m")
                    elif "v" in words:
                        result = state_wise_bugs(scrubber_id,scrubber_output,"v")
                    elif "n" in words:
                        result = state_wise_bugs(scrubber_id,scrubber_output,"n")
                    elif "p" in words:
                        result = state_wise_bugs(scrubber_id,scrubber_output,"p")
                    elif "w" in words:
                        result = state_wise_bugs(scrubber_id,scrubber_output,"w")
                    elif "o" in words:
                        result = state_wise_bugs(scrubber_id,scrubber_output,"o")
                    elif "d" in words:
                        result = state_wise_bugs(scrubber_id,scrubber_output,"d")
                    else:
                        result = "<strong>Details for scrubber%s:</strong>"%scrubber_id
                        result += "<p>Name: <strong>%s</strong></p>"%scrubber_output["name"]
                        result += "<p>Total Bugs: <strong>%s</strong></p>"%str(scrubber_output["total_bugs"])
                        result += "<p>Query: <strong>%s</strong></p>"%scrubber_output["query"]
                else:
                    result = "<strong>Scrubber API server is Down</strong>"
            else:
                #qwords = re.split("\s+",question)
                user = "all"
                
                for word in qwords:
                    # if word == "":
                    #     qwords.remove(" ")
                    if not eng_dict.check(word):
                        user = word
                question = " ".join(qwords)
                
                scrubber_id = get_last_scrubber_id(user)
                result = ""
                if scrubber_id:
                    scrubber_output = get_bugs_from_scrubber(scrubber_id)
                    words  = question.split(" ")
                    #if "state" in words:
                    if "i" in words:
                    #if re.search("i|i[\s+]?state",question):
                        result = state_wise_bugs(scrubber_id,scrubber_output,"i")
                    elif "r" in words:
                        result = state_wise_bugs(scrubber_id,scrubber_output,"r")
                    elif "a" in words:
                        result = state_wise_bugs(scrubber_id,scrubber_output,"a")
                    elif "m" in words:
                        result = state_wise_bugs(scrubber_id,scrubber_output,"m")
                    elif "v" in words:
                        result = state_wise_bugs(scrubber_id,scrubber_output,"v")
                    elif "n" in words:
                        result = state_wise_bugs(scrubber_id,scrubber_output,"n")
                    elif "p" in words:
                        result = state_wise_bugs(scrubber_id,scrubber_output,"p")
                    elif "w" in words:
                        result = state_wise_bugs(scrubber_id,scrubber_output,"w")
                    elif "o" in words:
                        result = state_wise_bugs(scrubber_id,scrubber_output,"o")
                    elif "d" in words:
                        result = state_wise_bugs(scrubber_id,scrubber_output,"d")
                    else:
                        result = "<strong>Details for scrubber%s:</strong>"%scrubber_id
                        result += "<p>Name: <strong>%s</strong></p>"%scrubber_output["name"]
                        result += "<p>Total Bugs: <strong>%s</strong></p>"%str(scrubber_output["total_bugs"])
                        result += "<p>Query: <strong>%s</strong></p>"%scrubber_output["query"]
                else:
                    result = "<strong>Scrubber API server is Down</strong>"
        elif re.search("\w+-\d{,8}",question):
            
            scrubber_id = re.search("(\w+-\d{,8})",question).group(1)
            #scrubber_id = get_last_scrubber_id(user)
            result = ""
            if scrubber_id:
                scrubber_output = get_bugs_from_scrubber(scrubber_id)
                words  = question.split(" ")
                
                #if "state" in words:
                if "i" in words:
                #if re.search("i|i[\s+]?state",question):
                    result = state_wise_bugs(scrubber_id,scrubber_output,"i")
                elif "r" in words:
                    result = state_wise_bugs(scrubber_id,scrubber_output,"r")
                elif "a" in words:
                    result = state_wise_bugs(scrubber_id,scrubber_output,"a")
                elif "m" in words:
                    result = state_wise_bugs(scrubber_id,scrubber_output,"m")
                elif "v" in words:
                    result = state_wise_bugs(scrubber_id,scrubber_output,"v")
                elif "n" in words:
                    result = state_wise_bugs(scrubber_id,scrubber_output,"n")
                elif "p" in words:
                    result = state_wise_bugs(scrubber_id,scrubber_output,"p")
                elif "w" in words:
                    result = state_wise_bugs(scrubber_id,scrubber_output,"w")
                elif "o" in words:
                    result = state_wise_bugs(scrubber_id,scrubber_output,"o")
                elif "d" in words:
                    result = state_wise_bugs(scrubber_id,scrubber_output,"d")
                else:
                    result = "<strong>Details for scrubber%s:</strong>"%scrubber_id
                    result += "<p>Name: <strong>%s</strong></p>"%scrubber_output["name"]
                    result += "<p>Total Bugs: <strong>%s</strong></p>"%str(scrubber_output["total_bugs"])
                    result += "<p>Query: <strong>%s</strong></p>"%scrubber_output["query"]
            else:
                result = "<strong>Scrubber API server is Down</strong>"                  
        else:
            result= "<p>Not able to fetch scrubber, Please use help scrubber and reframe you question</p>"
    elif re.search("queries|query",question):
        if "my" in qwords:
            cec_id = user
            
            scrubber_query_data = get_scrubber_query(user)
            if scrubber_query_data:
                result = ""
                result += "<p>Below are Scrubber Queries for: <strong>%s</strong>"%(user)
                result += "<hr>"
                for query in scrubber_query_data[user]:
                    result +=  "<p><strong>%s:</strong></p><ul>"%query["scrubber_id"]
                    result += "<li>Name: <strong>%s</strong></li>"%query["name"]
                    result += "<li>Query: <strong>%s</strong></li>"%query["query"]
                    result += "<li>Total Bugs: <strong>%s</strong></li>"%query["total_bugs"]
                    result += "<li>Sev1: <strong>%s</strong></li>"%query["sev1"]
                    result += "<li>Sev2: <strong>%s</strong></li>"%query["sev2"]
                    result += "</ul><hr>"
            else:
                result = "<p>No scrubber Query for user: <strong>%s</strong></p>"%user
        else:
            #qwords = re.split("\s+",question)
            user = "all"
            
            for word in qwords:
                # if word == "":
                #     qwords.remove(" ")
                if not eng_dict.check(word):
                    user = word
            question = " ".join(qwords)
            if user != "all":
                scrubber_query_data = get_scrubber_query(user)
                if scrubber_query_data:
                    result = ""
                    result += "<p>Below are Scrubber Queries for: <strong>%s</strong>"%(user)
                    result += "<hr>"
                    for query in scrubber_query_data[user]:
                        result +=  "<p><strong>%s:</strong></p><ul>"%query["scrubber_id"]
                        result += "<li>Name: <strong>%s</strong></li>"%query["name"]
                        result += "<li>Query: <strong>%s</strong></li>"%query["query"]
                        result += "<li>Total Bugs: <strong>%s</strong></li>"%query["total_bugs"]
                        result += "<li>Sev1: <strong>%s</strong></li>"%query["sev1"]
                        result += "<li>Sev2: <strong>%s</strong></li>"%query["sev2"]
                        result += "</ul><hr>"
                else:
                    result = "<p>No scrubber Query for user: <strong>%s</strong></p>"%user
            else:
                result = "<p>No able fetch cec id from question</p>"
    else:
        scrubber_id = False
        if re.search("last|latest",question):
            if "my" in qwords:
                cec_id = user
                
                scrubber_id = get_last_scrubber_id(user)
                result = ""
                if scrubber_id:
                    scrubber_output = get_bugs_from_scrubber(scrubber_id)
                    if scrubber_output:
                        result = get_all_scrubber_data(scrubber_id,scrubber_output)
                    else:
                        result = "<strong>Scrubber API server is Down</strong>"
                else:
                    result = "<strong> Not able to get scrubber information</strong>"
            else:
                #qwords = re.split("\s+",question)
                user = "all"
                for word in qwords:
                    # if word == "":
                    #     qwords.remove(" ")
                    if not eng_dict.check(word):
                        user = word
                question = " ".join(qwords)
                result = ""
                if user != "all":
                    scrubber_id = get_last_scrubber_id(user)
                    result = ""
                    if scrubber_id:
                        scrubber_output = get_bugs_from_scrubber(scrubber_id)
                        if scrubber_output:
                            result = get_all_scrubber_data(scrubber_id,scrubber_output)
                        else:
                            result = "<strong>Scrubber API server is Down</strong>"
                    else:
                        result = "<strong> Not able to get scrubber information</strong>"
                else:
                    result = "<strong>Not able get the cec_id</strong>"
        elif re.search("\w+-\d{,8}",question):
            
            scrubber_id = re.search("(\w+-\d{,8})",question).group(1)
            result = ""
            if scrubber_id:
                scrubber_output = get_bugs_from_scrubber(scrubber_id)
                if scrubber_output:
                    result = get_all_scrubber_data(scrubber_id,scrubber_output)
                else:
                        result = "<strong>Scrubber API server is Down</strong>"
            else:
                result = "<strong> Not able to get scrubber information</strong>"
        else:
            result= "<p>Not able to fetch scrubber, Please use help scrubber and reframe you question</p>"               
    content["title"] = "Scrubber Details"
    content["results"] = ([result+"<br>"+"<br>"] if type=="webex" else result+"<br>"+"<br>")
    # content = {
    #     "title": "CAFY",
    #     "results": [results]
    # }
=======
    if re.search("last|\w+-\d{,8}|break[-\s+]?up|state",question):
        scrubber_id = False
        if re.search("last|latest",question):
            if re.search("my|mine",question):
                cec_id = user
                
                output = get_last_scrubber_id(user)
                if output:
                    scrubber_id = output
            else:
                qwords = re.split("\s+",question)
                user = "all"
                for word in qwords:
                    if not eng_dict.check(word):
                        user = word
                question = " ".join(qwords)
                output = get_last_scrubber_id(user)
                if output:
                    scrubber_id = output
            
        elif re.search("\w+-\d{,8}",question):
            scrubber_id = re.search("(\w+-\d{,8})",question).group(1)
            print(scrubber_id)
            if scrubber_id:
                if re.search("all[\s+]?bugs|all",question):
                    results = get_bugs_from_scrubber(scrubber_id,status)



    content = {
        "title": "CAFY",
        "results": [results]
    }
>>>>>>> origin/master-live
    #log("irfan" , content)
    return content


if __name__ == "__main__":
<<<<<<< HEAD
    print(get_scrubber_data("mnamasev scrubber queries","ikyalnoo","web"))
    #pass
=======
    print(get_scrubber_data("show me all bugs in mnamasev-118 scrubber","ikyalnoo","web"))
>>>>>>> origin/master-live

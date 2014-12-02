##password needs to replace ******
import datetime
import os
#for xml retreval
from xml.dom import minidom
import urllib2
from datetime import datetime
#for getting the name of the admin
import Zope2
#for creating person within fsd object
from AccessControl.SecurityManagement import newSecurityManager
import sys 
from Products.CMFCore.utils import getToolByName
from zope.component.hooks import getSite
import time
container = []
awardContainer = []
certificationContainer = []
confPresContainer = []
educationContainer = []
facultyDevContainer = []
grantsContainer = []
otherTeachingContainer = []
priorContainer = []
ProfMembershipContainer = []
profPressContainer = []
publicationContainer = []
resignedContainer = []
scheduledTeachingContainer = []
serviceConsultinConatainer = []
travelContainer = []
import datetime
fullName = ""
fullNameUsers = []
globalBuilding = ""
globalFax = ""
globalEmail = ""
globalPhone = ""
curr_year = datetime.datetime.now()
curr_year = curr_year.year
prev_year = curr_year+1
school_year = str(curr_year)+"-"+str(prev_year)

password = ''



def populate_admin(name):
    ploneOnServer = False
    #if ploneOnServer == True:
        #t = open('/opt/Plone-4.3/zeocluster/Extensions/COB/pw.txt', 'r+')
    ##else:
        #t = open('/Users/cobstu01/Desktop/Plone/file.txt', 'r+')
    import datetime
    curr_year = datetime.datetime.now()
    curr_year = curr_year.year
    prev_year = curr_year-1
    school_year = str(prev_year)+"-"+str(curr_year)
    #j = 0
    #url to retrieve data from
    url = 'https://digitalmeasures.com/login/service/v4/SchemaData/INDIVIDUAL-ACTIVITIES-Business/ADMIN'

    password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

    # Add the username and password.
    username = "uwosh/fac_reports"
    ##t = open('/Users/cobstu01/Desktop/Plone/file.txt', 'r+')
    #line = "***"
    #password = line
    top_level_url = "http://digitalmeasures.com/login/service/v4/SchemaData/INDIVIDUAL-ACTIVITIES-Business"
    password_mgr.add_password(None, top_level_url, username, password)
    handler = urllib2.HTTPBasicAuthHandler(password_mgr)

    # create "opener" (OpenerDirector instance)
    opener = urllib2.build_opener(handler)

    # use the opener to fetch a URL
    opener.open(url)
    #logger.info('opened URL %s ok' % url)

    # Install the opener. Now all calls to urllib2.urlopen use our opener.
    urllib2.install_opener(opener)

    #retrieve the xml file and parse it
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    xml = response.read()
    dom = minidom.parse(urllib2.urlopen(url))

    #####################################################################
    ###Grabs information from Digital Measures from the award section   #
    ### 'j' is the id used for ID's, and increments after all of a users#
    ###awards are acounted forself.                                     #
    #####################################################################
    container = []
    user = []
    i = 0
    j = 0
    catPlusPos = ""
    categoryArray = []
    categoryOnly = []
    catHolder = []
    rank = ""
    nodeCount = 0
    index = 0
    for node in dom.getElementsByTagName('Record'):
        if name in node.getAttribute('username') and node.getAttribute("username").strip() == name:
            index = node.getAttribute('username').index(name)
            try:
                rank = node.getElementsByTagName('RANK')[index].childNodes[0].nodeValue.strip()
            except IndexError:
                rank = ''
            break

    for node2 in node.getElementsByTagName("ADMIN"):
        count = len(node2.getElementsByTagName("ADMIN_DIR"))  
        catHolder.append(count)
        catCount = 0
        error = "error"
    rightYearCount = 0
    
    try:
        while catCount<catHolder[nodeCount]:
            try:
                AC_YEAR = node.getElementsByTagName('AC_YEAR')[0].childNodes[0].nodeValue.strip()
            except IndexError:
                AC_YEAR = "no"
            try:
                CATEGORY = node.getElementsByTagName('CATEGORY')[j].childNodes[0].nodeValue.strip()
            except IndexError:
                CATEGORY = ""
            try:
                POSITION = node.getElementsByTagName('POSITION')[j].childNodes[0].nodeValue.strip() 
            except IndexError:
                POSITION = "  "
            catCount=catCount+1
            j=j+1
            if CATEGORY != "":
                if CATEGORY == "College of Business Dean's Office" and POSITION is not "  ":
                    catPlusPos = POSITION
                    if(CATEGORY not in categoryOnly):
                        categoryOnly.append(CATEGORY)
                    if(catPlusPos not in categoryArray):
                        categoryArray.append(catPlusPos)
                elif POSITION is "  " and CATEGORY is not "":
                    if(CATEGORY not in categoryOnly):
                        categoryOnly.append(CATEGORY)
                elif POSITION is not "  " and CATEGORY is not "":
                    catPlusPos = POSITION+", "+CATEGORY
                    if(CATEGORY not in categoryOnly and CATEGORY not in categoryArray):
                        categoryOnly.append(CATEGORY)
                    if(catPlusPos not in categoryArray):
                        categoryArray.append(catPlusPos)
    except IndexError:
        error = "error"
    nodeCount = nodeCount+1
    return categoryArray, rank, categoryOnly
             
def populate_users(us, userIdArray, userId):
    print "inside users "+userId
    ploneOnServer = False
    #if ploneOnServer == True:
        #t = open('/opt/Plone-4.3/zeocluster/Extensions/COB/pw.txt', 'r+')
    #else:
        #t = open('/Users/cobstu01/Desktop/Plone/file.txt', 'r+')

    #url to retrieve data from
    url = 'http://www.digitalmeasures.com/login/service/v4/SchemaData/INDIVIDUAL-ACTIVITIES-Business/PCI'
    password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

    # Add the username and password.
    # If we knew the realm, we could use it instead of ``None``.
    username = "uwosh/fac_reports"
    ##t = open('/Users/cobstu01/Desktop/Plone/file.txt', 'r+')
    #line = "***"
    #password = line
    top_level_url = "http://www.digitalmeasures.com/login/service/v4/SchemaData/INDIVIDUAL-ACTIVITIES-Business"
    password_mgr.add_password(None, top_level_url, username, password)
    handler = urllib2.HTTPBasicAuthHandler(password_mgr)

    # create "opener" (OpenerDirector instance)
    opener = urllib2.build_opener(handler)

    # use the opener to fetch a URL
    opener.open(url)

    # Install the opener. Now all calls to urllib2.urlopen use our opener.
    urllib2.install_opener(opener)

    #retrieve the xml file and parse it
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    xml = response.read()
    dom = minidom.parse(urllib2.urlopen(url))
    user2 = []
    user = []
    returnInfo = []
    categoryOnly = []
    identifier = []
    output = ""
    i = 0
    j = 0
    ID = ""
    for node in dom.getElementsByTagName('Record'):
        identifier.append(node.getAttribute("userId"))
        user.append(node)
    j = identifier.index(userId)
    try:
        tempFirstName = user[j].getElementsByTagName('FNAME')[0].childNodes[0].nodeValue.strip()
    except IndexError:
        tempFirstName = '  '.strip()
    try:
        tempLastName = user[j].getElementsByTagName('LNAME')[0].childNodes[0].nodeValue.strip()
    except IndexError:
        tempLastName = '  '.strip()
    try:
        prefix = user[j].getElementsByTagName('PREFIX')[0].childNodes[0].nodeValue.strip()
    except IndexError:
        prefix = '  '.strip()
    try:
        MNAME = user[j].getElementsByTagName('MNAME')[0].childNodes[0].nodeValue.strip()
    except IndexError:
        MNAME = "".strip()
    try:
        EMAIL = user[j].getElementsByTagName('EMAIL')[0].childNodes[0].nodeValue
        globalEmail = EMAIL
    except IndexError:
        EMAIL = "  "
        globalEmail = EMAIL
    expCount = 0
    otherCount = 0
    MoreEXPERTISE = ""
    temp = ""
    expertiseArray = []
    while (expCount < len(user[j].getElementsByTagName('PCI_EXPERTISE'))):
        try:
            EXPERTISE = user[j].getElementsByTagName('EXPERTISE')[expCount].childNodes[0].nodeValue
        except IndexError:
            EXPERTISE = ""
        if (EXPERTISE == "Other"):
            print "Expertise is "+EXPERTISE
            temp = temp+user[j].getElementsByTagName('EXPERTISE_OTHER')[otherCount].childNodes[0].nodeValue+", "
            otherCount= otherCount+1
        else:
            try:
                temp = temp+user[j].getElementsByTagName('EXPERTISE')[expCount].childNodes[0].nodeValue+", "
            except IndexError:
                temp = ""
        expCount = expCount+1
    EXPERTISE = temp
    try:
        EXPERTISE_OTHER = user[j].getElementsByTagName('EXPERTISE_OTHER')[0].childNodes[0].nodeValue
    except IndexError:
        EXPERTISE_OTHER = ""
    try:
        BUILDING = user[j].getElementsByTagName('BUILDING')[0].childNodes[0].nodeValue
        globalBuilding = BUILDING
    except IndexError:
        BUILDING = " "
        globalBuilding = BUILDING
    try:
        OPHONE = user[j].getElementsByTagName('OPHONE')[0].childNodes[0].nodeValue
        globalPhone = OPHONE
    except IndexError:
        OPHONE = " "
        globalPhone = OPHONE
    us = us.lower()
    #####################################################################
    ###Populates the faculty profile for each user, on the plone site.###
    ##################################################################### 
    fullname = tempFirstName+" "+tempLastName    
    if( "'" in fullname):
        fullname = fullname.replace("'", "")
    if(MNAME != ""):   
        ID = tempFirstName+" "+MNAME+" "+tempLastName    
    else:
        ID = tempFirstName+" "+tempLastName 
    error = ""
    index = 0
    categoryArray = populate_admin(us)[0]
    categoryOnly = populate_admin(us)[2]
    rank = populate_admin(us)[1]
    ploneOnServer = False
    output +="<div id = \"summary_page\">\n"
    portal = getSite();
    if hasattr(portal, 'portraits'):
        form_folder = getattr(portal, 'portraits')
        pictureName = user[j].getAttribute('username').strip()+".jpg"
        if hasattr(form_folder,pictureName):
            output +="<img  align = \"right\" src = http://www.uwosh.edu/cob/portraits/"+pictureName+"/image_mini><br>"
        else:
            output +="<img  align = \"right\" src = http://www.uwosh.edu/cob/portraits/default.jpg/image_mini><br>"

    output +="<a class =\"summaryName\" href=\"http://www.uwosh.edu/cob/directory/"+us+"\">"+ID+"</a>\n"
    education = populate_education(ID,us, userIdArray, userId)
    if education is not " ":
        output +="<br>"+education+"<br>"
        print "Education ="+education
    else:
        output +="<br>"
    if rank == '' or rank == "Staff" or rank == "Academic Staff":
        error = "no rank"
    else:
        output +=rank+"<br>"
        print "rank = "+rank
    categoryCount = 0
    categories = ""
    error = ""
    try:
        if len(categoryArray) is 0:
            error = "no category"
        else:
            output +=categoryArray[0]
            categoryCount=categoryCount+1
    except IndexError:
        error = "error"
    while len(categoryArray) > categoryCount:
        output +="<br>"+categoryArray[categoryCount]
        categories = categories+","+categoryArray[categoryCount]
        categoryCount= categoryCount+1

    output +="<table class = \"inner\">\n"
    output +="<tr>\n"
    output +="<td class =\"office-label\">\n"
    output +="Office:"
    output +="</td>\n"
    output +="<td class =\"building\">\n"
    output +=globalBuilding+"\n"
    print "office = "+globalBuilding
    output +="</td>\n"
    "</tr>\n"

    output +="<tr>\n"
    output +="<td class =\"phone-label\">\n"
    output +="Office Phone:  "
    output +="</td>\n"
    output +="<td class =\"phone\">\n"
    globalPhone+"\n"
    print "phone = "+globalPhone
    output +="</td>\n"
    output +="</tr>\n"
    globalEmail = us+"@uwosh.edu"
    print "email = "+globalEmail
    output +="<tr>\n"
    output +="<td class =\"email-label\">\n"
    output +="Email:\n"
    output +="</td>\n"
    output +="<td class =\"email\">\n"
    output +="<a href=mailto:"+globalEmail+">"+globalEmail+"</a>\n"
    output +="</td>\n"
    output +="</tr>\n"
    
    if len(EXPERTISE)>0:
        output +="<tr>\n"
        output +="<td class =\"expertise-label\">\n"
        output +="Expertise: "
        output +="</td>"
        output +="<td class =\"expertise\">\n"
        EXPERTISE = EXPERTISE.lstrip(",")
        EXPERTISE = EXPERTISE.rstrip()
        EXPERTISE = EXPERTISE.rstrip(",")
        output +=EXPERTISE
        print "expertise = "+EXPERTISE
        output +="</td>\n"
        output +="</tr>\n"
    output +="</table>\n"
    output +="</div>"
        
        
    
    returnInfo.append(ID)
    returnInfo.append(categoryOnly)
    returnInfo.append(output)
    error = ""
    return returnInfo

def populate_users_departmentPage(us, userIdArray, userId):
    ploneOnServer = False
    #if ploneOnServer == True:
        #t = open('/opt/Plone-4.3/zeocluster/Extensions/COB/pw.txt', 'r+')
    #else:
        #t = open('/Users/cobstu01/Desktop/Plone/file.txt', 'r+')
    url = 'http://www.digitalmeasures.com/login/service/v4/SchemaData/INDIVIDUAL-ACTIVITIES-Business/PCI'
    password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

    # Add the username and password.
    # If we knew the realm, we could use it instead of ``None``.
    username = "uwosh/fac_reports"
    ##t = open('/Users/cobstu01/Desktop/Plone/file.txt', 'r+')
    #line = "***"
    #password = line
    top_level_url = "http://www.digitalmeasures.com/login/service/v4/SchemaData/INDIVIDUAL-ACTIVITIES-Business"
    password_mgr.add_password(None, top_level_url, username, password)
    handler = urllib2.HTTPBasicAuthHandler(password_mgr)

    # create "opener" (OpenerDirector instance)
    opener = urllib2.build_opener(handler)

    # use the opener to fetch a URL
    opener.open(url)

    # Install the opener. Now all calls to urllib2.urlopen use our opener.
    urllib2.install_opener(opener)

    #retrieve the xml file and parse it
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    xml = response.read()
    dom = minidom.parse(urllib2.urlopen(url))
    user2 = []
    user = []
    returnInfo = []
    categoryOnly = []
    identifier = []
    output = ""
    i = 0
    j = 0
    ID = ""
    print "userID = "+userId
    for node in dom.getElementsByTagName('Record'):
        identifier.append(node.getAttribute("userId"))
        user.append(node)
    j = identifier.index(userId)
    try:
        tempFirstName = user[j].getElementsByTagName('FNAME')[0].childNodes[0].nodeValue.strip()
    except IndexError:
        tempFirstName = '  '.strip()
    try:
        tempLastName = user[j].getElementsByTagName('LNAME')[0].childNodes[0].nodeValue.strip()
    except IndexError:
        tempLastName = '  '.strip()
    try:
        prefix = user[j].getElementsByTagName('PREFIX')[0].childNodes[0].nodeValue.strip()
    except IndexError:
        prefix = '  '.strip()
    try:
        MNAME = user[j].getElementsByTagName('MNAME')[0].childNodes[0].nodeValue.strip()
    except IndexError:
        MNAME = "".strip()
    try:
        EMAIL = user[j].getElementsByTagName('EMAIL')[0].childNodes[0].nodeValue
        globalEmail = EMAIL
    except IndexError:
        EMAIL = "  "
        globalEmail = EMAIL
    expCount = 0
    otherCount = 0
    MoreEXPERTISE = ""
    temp = ""
    expertiseArray = []
    while (expCount < len(user[j].getElementsByTagName('PCI_EXPERTISE'))):
        try:
            EXPERTISE = user[j].getElementsByTagName('EXPERTISE')[expCount].childNodes[0].nodeValue
        except IndexError:
            EXPERTISE = ""
        if (EXPERTISE == "Other"):
            print "Expertise is "+EXPERTISE
            temp = temp+user[j].getElementsByTagName('EXPERTISE_OTHER')[otherCount].childNodes[0].nodeValue+", "
            otherCount= otherCount+1
        else:
            try:
                temp = temp+user[j].getElementsByTagName('EXPERTISE')[expCount].childNodes[0].nodeValue+", "
            except IndexError:
                temp = ""
        expCount = expCount+1
    EXPERTISE = temp
    try:
        EXPERTISE_OTHER = user[j].getElementsByTagName('EXPERTISE_OTHER')[0].childNodes[0].nodeValue
    except IndexError:
        EXPERTISE_OTHER = ""
    try:
        BUILDING = user[j].getElementsByTagName('BUILDING')[0].childNodes[0].nodeValue
        globalBuilding = BUILDING
    except IndexError:
        BUILDING = " "
        globalBuilding = BUILDING
    try:
        OPHONE = user[j].getElementsByTagName('OPHONE')[0].childNodes[0].nodeValue
        globalPhone = OPHONE
    except IndexError:
        OPHONE = " "
        globalPhone = OPHONE
    us = us.lower()
    #####################################################################
    ###Populates the faculty profile for each user, on the plone site.###
    ##################################################################### 
    fullname = tempFirstName+" "+tempLastName    
    if( "'" in fullname):
        fullname = fullname.replace("'", "")
    if(MNAME != ""):   
        ID = tempFirstName+" "+MNAME+" "+tempLastName    
    else:
        ID = tempFirstName+" "+tempLastName 
    error = ""
    index = 0
    categoryArray = populate_admin(us)[0]
    categoryOnly = populate_admin(us)[2]
    rank = populate_admin(us)[1]
    ploneOnServer = False
    output +="<div id = \"summary_page\">\n"
    portal = getSite();
    if hasattr(portal, 'portraits'):
        form_folder = getattr(portal, 'portraits')
        pictureName = user[j].getAttribute('username').strip()+".jpg"
        if hasattr(form_folder,pictureName):
            output +="<img  align = \"right\" src = http://www.uwosh.edu/cob/portraits/"+pictureName+"/image_thumb><br>"
        else:
            output +="<img  align = \"right\" src = http://www.uwosh.edu/cob/portraits/default.jpg/image_thumb><br>"

    output +="<a class =\"summaryName\" href=\"http://www.uwosh.edu/cob/directory/"+us+"\">"+ID+"</a>\n"
    education = populate_education(ID,us, userIdArray, userId)
    if education is not " ":
        output +="<br>"+education+"<br>"
        print "Education ="+education
    else:
        output +="<br>"
    if rank == '' or rank == "Staff" or rank == "Academic Staff":
        error = "no rank"
    else:
        output +=rank+"<br>"
        print "rank = "+rank
    categoryCount = 0
    categories = ""
    error = ""
    try:
        if len(categoryArray) is 0:
            error = "no category"
        else:
            output +=categoryArray[0]
            categoryCount=categoryCount+1
    except IndexError:
        error = "error"
    while len(categoryArray) > categoryCount:
        output +="<br>"+categoryArray[categoryCount]
        categories = categories+","+categoryArray[categoryCount]
        categoryCount= categoryCount+1

    output +="<table class = \"inner\">\n"
    output +="<tr>\n"
    output +="<td class =\"office-label\">\n"
    output +="Office:"
    output +="</td>\n"
    output +="<td class =\"building\">\n"
    output +=globalBuilding+"\n"
    print "office = "+globalBuilding
    output +="</td>\n"
    "</tr>\n"

    output +="<tr>\n"
    output +="<td class =\"phone-label\">\n"
    output +="Office Phone:  "
    output +="</td>\n"
    output +="<td class =\"phone\">\n"
    globalPhone+"\n"
    print "phone = "+globalPhone
    output +="</td>\n"
    output +="</tr>\n"
    globalEmail = us+"@uwosh.edu"
    print "email = "+globalEmail
    output +="<tr>\n"
    output +="<td class =\"email-label\">\n"
    output +="Email:\n"
    output +="</td>\n"
    output +="<td class =\"email\">\n"
    output +="<a href=mailto:"+globalEmail+">"+globalEmail+"</a>\n"
    output +="</td>\n"
    output +="</tr>\n"
    
    if len(EXPERTISE)>0:
        output +="<tr>\n"
        output +="<td class =\"expertise-label\">\n"
        output +="Expertise: "
        output +="</td>"
        output +="<td class =\"expertise\">\n"
        EXPERTISE = EXPERTISE.lstrip(",")
        EXPERTISE = EXPERTISE.rstrip()
        EXPERTISE = EXPERTISE.rstrip(",")
        output +=EXPERTISE
        print "expertise = "+EXPERTISE
        output +="</td>\n"
        output +="</tr>\n"
    output +="</table>\n"
    output +="</div>"
    returnInfo.append(ID)
    returnInfo.append(categoryOnly)
    returnInfo.append(output)
    error = ""
    return returnInfo

def populate_award(name,us, userIdArray, userId):
    print "in awards"
    ploneOnServer = False
    #if ploneOnServer == True:
        #t = open('/opt/Plone-4.3/zeocluster/Extensions/COB/pw.txt', 'r+')
    #else:
        #t = open('/Users/cobstu01/Desktop/Plone/file.txt', 'r+')
    #url to retrieve data from
    url = 'https://digitalmeasures.com/login/service/v4/SchemaData/INDIVIDUAL-ACTIVITIES-Business/AWARDHONOR'

    password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

    # Add the username and password.
    username = "uwosh/fac_reports"
    ##t = open('/Users/cobstu01/Desktop/Plone/file.txt', 'r+')
    #line = "***"
    #password = line 
    top_level_url = "http://digitalmeasures.com/login/service/v4/SchemaData/INDIVIDUAL-ACTIVITIES-Business"
    password_mgr.add_password(None, top_level_url, username, password)
    handler = urllib2.HTTPBasicAuthHandler(password_mgr)

    # create "opener" (OpenerDirector instance)
    opener = urllib2.build_opener(handler)

    # use the opener to fetch a URL
    opener.open(url)

    # Install the opener. Now all calls to urllib2.urlopen use our opener.
    urllib2.install_opener(opener)

    #retrieve the xml file and parse it
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    xml = response.read()
    dom = minidom.parse(urllib2.urlopen(url))

    #####################################################################
    ###Grabs information from Digital Measures from the award section   #
    ### 'j' is the id used for ID's, and increments after all of a users#
    ###awards are acounted forself.                                     #
    #####################################################################
    condition = True  ###added
    user = []
    container = []
    identifier = []
    i = 0
    stringList = "<ul>"
    ploneOnServer = False
    for node in dom.getElementsByTagName('Record'):
        identifier.append(node.getAttribute("userId"))
        user.append(node)
    if userId in identifier:
        j = identifier.index(userId)
        condition = True
        while condition == True and i<5: 
            try:
                awardName = user[j].getElementsByTagName('NAME')[i].childNodes[0].nodeValue.strip()+"," 
                if awardName == "Other,":
                    try:
                        awardName = " "+user[j].getElementsByTagName('NAME_OTHER')[i].childNodes[0].nodeValue.strip()+","
                    except IndexError:
                        awardName = "  " 
            except IndexError:
                try:
                    awardName = " "+user[j].getElementsByTagName('NAME_OTHER')[i].childNodes[0].nodeValue.strip()+","
                except IndexError:
                    awardName = "  " 
            try:
                nominated = " "+user[j].getElementsByTagName('NOMREC')[i].childNodes[0].nodeValue.strip()+","
            except IndexError:
                nominated = "  "
            try:
                org = " "+user[j].getElementsByTagName('ORG')[i].childNodes[0].nodeValue.strip()+","
            except IndexError:
                org = "  "
            try:
                month = " "+user[j].getElementsByTagName('DTM_DATE')[i].childNodes[0].nodeValue.strip()+""
            except IndexError:
                month = "  "
            try:
                day = " "+user[j].getElementsByTagName('DTD_DATE')[i].childNodes[0].nodeValue.strip()+","
            except IndexError:
                day = "  "
            try:
                year = " "+user[j].getElementsByTagName('DTY_DATE')[i].childNodes[0].nodeValue.strip()+","
            except IndexError:
                year = "  "

            date1 = month+" "+day+" "+year
            if awardName is  '  ' and nominated is  '  ' and org is  '  ' and month is  "  " and day is  "  " and year is "  ":
                condition = False
            else:
                awardCombined = awardName+nominated+org+date1
                awardCombined = fixPuncuation(awardCombined)
                awardCombined ="<li>"+awardCombined+"</li>"
                stringList = stringList+awardCombined
                i = i+1
        stringList = stringList+"</ul>"
        if  i > 0:
            stringList ="<h2>Awards</h2>"+stringList
        try:
            stringList+="\n"
        except UnicodeEncodeError:
            text = stringList.encode('ascii', 'ignore')
            stringList+=text+"\n"
    return stringList
def populate_education(name, us, userIdArray, userId):

    print "inside education  "+userId
    ploneOnServer = False
    #if ploneOnServer == True:
        #t = open('/opt/Plone-4.3/zeocluster/Extensions/COB/pw.txt', 'r+')
    #else:
        #t = open('/Users/cobstu01/Desktop/Plone/file.txt', 'r+')
    #url to retrieve data from
    url = 'https://digitalmeasures.com/login/service/v4/SchemaData/INDIVIDUAL-ACTIVITIES-Business/EDUCATION'
    

    password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

    # Add the username and password.
    username = "uwosh/fac_reports"
    ##t = open('/Users/cobstu01/Desktop/Plone/file.txt', 'r+')
    #line = "***"
    #password = line 
    top_level_url = "http://digitalmeasures.com/login/service/v4/SchemaData/INDIVIDUAL-ACTIVITIES-Business"
    password_mgr.add_password(None, top_level_url, username, password)
    handler = urllib2.HTTPBasicAuthHandler(password_mgr)

    # create "opener" (OpenerDirector instance)
    opener = urllib2.build_opener(handler)

    # use the opener to fetch a URL
    opener.open(url)

    # Install the opener. Now all calls to urllib2.urlopen use our opener.
    urllib2.install_opener(opener)

    #retrieve the xml file and parse it
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    xml = response.read()
    dom = minidom.parse(urllib2.urlopen(url))

    #####################################################################
    ###Grabs information from Digital Measures from the award section   #
    ### 'j' is the id used for ID's, and increments after all of a users#
    ###awards are acounted forself.                                     #
    #####################################################################
    condition = True
    user = []
    test = ""
    i = 0
    j = 0
    education = " "
    username = name
    identifier = []
    ploneOnServer = False
    
    for node in dom.getElementsByTagName('Record'):
        identifier.append(node.getAttribute("userId"))
        user.append(node)
    if userId in identifier:
        j = identifier.index(userId)
        condition = True
        try:
            HIGHEST = user[j].getElementsByTagName('HIGHEST')[i].childNodes[0].nodeValue.strip()
        except IndexError:
            HIGHEST = "No"
        while i<5:
            if (HIGHEST == "Yes"):
                try:
                    DEG = " "+user[j].getElementsByTagName('DEG')[i].childNodes[0].nodeValue
                except IndexError:
                    DEG = ""
                try:
                    DEGOTHER = " "+user[j].getElementsByTagName('DEGOTHER')[i].childNodes[0].nodeValue+","
                except IndexError:
                    DEGOTHER = "" 
                try:
                    SUPPAREA = " "+user[j].getElementsByTagName('SUPPAREA')[i].childNodes[0].nodeValue+","
                except IndexError:
                    SUPPAREA = "  "
                try:
                    DISSTITLE = " "+user[j].getElementsByTagName('DISSTITLE')[i].childNodes[0].nodeValue+","
                except IndexError:
                    DISSTITLE = "  "
                try:
                    MAJOR = " "+user[j].getElementsByTagName('MAJOR')[i].childNodes[0].nodeValue+". " 
                except IndexError:
                    MAJOR = ""
                try:
                    SCHOOL = " "+user[j].getElementsByTagName('SCHOOL')[i].childNodes[0].nodeValue+","
                except IndexError:
                    SCHOOL = "" 
                try:
                    YR_COMP = " "+user[j].getElementsByTagName('YR_COMP')[i].childNodes[0].nodeValue
                except IndexError:
                    YR_COMP = ""
                try:
                    COMP_START = " "+user[j].getElementsByTagName('COMP_START')[i].childNodes[0].nodeValue+","
                except IndexError:
                    COMP_START = "  "
                try:
                    COMP_END = " "+user[j].getElementsByTagName('COMP_END')[i].childNodes[0].nodeValue+","
                except IndexError:
                    COMP_END = "  "
                try:
                    HIGHEST = user[j].getElementsByTagName('HIGHEST')[i].childNodes[0].nodeValue.strip()
                except IndexError:
                    HIGHEST = "No"
                if DEG is  '  ' and DEGOTHER is  '  ' and SUPPAREA is  '  ' and DISSTITLE is  '  ' and MAJOR is "  " and SCHOOL is "  " and YR_COMP is "  " and COMP_START is "  " and COMP_END is "  ":
                    test = ""
                else:
                    education = DEG+MAJOR+SCHOOL+YR_COMP
                    s = education[len(education)-1:]
                    if s == ',':
                        education = education.rstrip(',')                                                    
                    if SCHOOL =="":
                        education = " "
                break
            else:
                i = i+1
                try:
                    HIGHEST = user[j].getElementsByTagName('HIGHEST')[i].childNodes[0].nodeValue.strip()
                except IndexError:
                    HIGHEST = "No"
    return education

def populate_certification(name, us, userIdArray, userId):
    print "in certifications"
    ploneOnServer = False
    #if ploneOnServer == True:
        #t = open('/opt/Plone-4.3/zeocluster/Extensions/COB/pw.txt', 'r+')
    #else:
        #t = open('/Users/cobstu01/Desktop/Plone/file.txt', 'r+')
    #url to retrieve data from
    url = 'https://digitalmeasures.com/login/service/v4/SchemaData/INDIVIDUAL-ACTIVITIES-Business/LICCERT'
    password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

    # Add the username and password.
    username = "uwosh/fac_reports"
    ##t = open('/Users/cobstu01/Desktop/Plone/file.txt', 'r+')
    #line = "***"
    #password = line 
    top_level_url = "http://digitalmeasures.com/login/service/v4/SchemaData/INDIVIDUAL-ACTIVITIES-Business"
    password_mgr.add_password(None, top_level_url, username, password)
    handler = urllib2.HTTPBasicAuthHandler(password_mgr)

    # create "opener" (OpenerDirector instance)
    opener = urllib2.build_opener(handler)

    # use the opener to fetch a URL
    opener.open(url)

    # Install the opener. Now all calls to urllib2.urlopen use our opener.
    urllib2.install_opener(opener)

    #retrieve the xml file and parse it
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    xml = response.read()
    dom = minidom.parse(urllib2.urlopen(url))

    #####################################################################
    ###Grabs information from Digital Measures from the award section   #
    ### 'j' is the id used for ID's, and increments after all of a users#
    ###awards are acounted forself.                                     #
    #####################################################################
    condition = True
    user = []
    container = []
    identifier = []
    i = 0
    j = 0
    stringList = "<ul>"
    username = name
    ploneOnServer = False
    for node in dom.getElementsByTagName('Record'):
        identifier.append(node.getAttribute("userId"))
        user.append(node)
    if userId in identifier:
        j = identifier.index(userId)
        condition = True
        while i<5 and condition == True:
            try:
                END_START = " "+user[j].getElementsByTagName('END_START')[i].childNodes[0].nodeValue+","
            except IndexError:
                END_START = "No"
            try:
                END_END = " "+user[j].getElementsByTagName('END_END')[i].childNodes[0].nodeValue+","
            except IndexError:
                END_END = "No"
            if( END_END == "No"):
                try:
                    TITLE = " "+user[j].getElementsByTagName('TITLE')[i].childNodes[0].nodeValue+"," 
                except IndexError:
                    TITLE = "  "
                try:
                    COPY = " "+user[j].getElementsByTagName('COPY')[i].childNodes[0].nodeValue+","
                except IndexError:
                    COPY = "  " 
                try:
                    DTM_START = " "+user[j].getElementsByTagName('DTM_START')[i].childNodes[0].nodeValue+","
                except IndexError:
                    DTM_START = "  " 
                try:
                    DTD_START = " "+user[j].getElementsByTagName('DTD_START')[i].childNodes[0].nodeValue+","
                except IndexError:
                    DTD_START = "  "
                try:
                    DTY_START = " "+user[j].getElementsByTagName('DTY_START')[i].childNodes[0].nodeValue+","
                except IndexError:
                    DTY_START = "  "
                try:
                    START_START = " "+user[j].getElementsByTagName('START_START')[i].childNodes[0].nodeValue 
                except IndexError:
                    START_START = "  "
                try:
                    START_END = " "+user[j].getElementsByTagName('START_END')[i].childNodes[0].nodeValue+","
                except IndexError:
                    START_END = "  " 
                try:
                    DTM_END = " "+user[j].getElementsByTagName('DTM_END')[i].childNodes[0].nodeValue+","
                except IndexError:
                    DTM_END = "  "
                try:
                    DTD_END = " "+user[j].getElementsByTagName('DTD_END')[i].childNodes[0].nodeValue+","
                except IndexError:
                    DTD_END = "  "
                try:
                    DTY_END = " "+user[j].getElementsByTagName('DTY_END')[i].childNodes[0].nodeValue+","
                except IndexError:
                    DTY_END = "  "
                try:
                    END_START = " "+user[j].getElementsByTagName('END_START')[i].childNodes[0].nodeValue+","
                except IndexError:
                    END_START = "  "
                try:
                    END_END = " "+user[j].getElementsByTagName('END_END')[i].childNodes[0].nodeValue+","
                except IndexError:
                    END_END = "  "

                if TITLE is  '  '  and START_START is "  " and COPY is "  ": #and START_END is "  " and DTM_END is "  " and DTD_END is "  " and DTY_END is "  " and END_START is "  " and END_END is "  ":
                    condition = False
                else:
                    member = TITLE+START_START
                    member = fixPuncuation(member)
                    member ="<li>"+member+"</li>" 
                    stringList=stringList+member
                    i = i+1
            else:
                i=i+1
        stringList = stringList+"</ul>"
        if i > 0:
            stringList = "<h2>Certifications</h2>"+stringList
        try:stringList+="\n"
        except UnicodeEncodeError:
            text = stringList.encode('ascii', 'ignore')
            stringList+=text
        authorCount = 0
    if i <1:
        stringList = ""
    return stringList

def populate_conf(name, us, userIdArray, userId):
    print "in conference"
    ploneOnServer = False
    #if ploneOnServer == True:
        #t = open('/opt/Plone-4.3/zeocluster/Extensions/COB/pw.txt', 'r+')
    #else:
        #t = open('/Users/cobstu01/Desktop/Plone/file.txt', 'r+')
    j = 0
    #url to retrieve data from
    url = 'http://digitalmeasures.com/login/service/v4/SchemaData/INDIVIDUAL-ACTIVITIES-Business/PRESENT_CONFERENCE'
    password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
    # Add the username and password.
    username = "uwosh/fac_reports"
    ##t = open('/Users/cobstu01/Desktop/Plone/file.txt', 'r+')
    #line = "***"
    #password = line
    top_level_url = "http://digitalmeasures.com/login/service/v4/SchemaData/INDIVIDUAL-ACTIVITIES-Business"
    password_mgr.add_password(None, top_level_url, username, password)
    handler = urllib2.HTTPBasicAuthHandler(password_mgr)

    # create "opener" (OpenerDirector instance)
    opener = urllib2.build_opener(handler)

    # use the opener to fetch a URL
    opener.open(url)

    # Install the opener. Now all calls to urllib2.urlopen use our opener.
    urllib2.install_opener(opener)

    #retrieve the xml file and parse it
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    xml = response.read()
    dom = minidom.parse(urllib2.urlopen(url))

    #####################################################################
    ###Grabs information from Digital Measures from the award section   #
    ### 'j' is the id used for ID's, and increments after all of a users#
    ###awards are acounted forself.                                     #
    #####################################################################
    count = 0
    j = 0
    condition = True
    nodeCount = 0
    identifier = []
    user = []
    authors = ""
    i = 0
    authorsArray = []
    users2 =[]
    stringList = "<ul>"
    username = name
    published = 0
    index = 0

    for node in dom.getElementsByTagName('Record'):
        identifier.append(node.getAttribute("userId"))
        user.append(node)
    if userId in identifier:
        j = identifier.index(userId)
        condition = True
        while i < len(user[j].getElementsByTagName('PRESENT_CONFERENCE')):
            try:
                PUB_INTERNET = user[j].getElementsByTagName("PUB_INTERNET")[i].childNodes[0].nodeValue.strip()
            except IndexError:
                PUB_INTERNET = "No"
            if PUB_INTERNET == "Yes":
                published = published+1
                try:
                    NAME = ' Paper presented at '+user[j].getElementsByTagName('NAME')[i].childNodes[0].nodeValue+', ' 
                except IndexError:
                    NAME = " "
                try:
                    ORG = ' "'+user[j].getElementsByTagName('ORG')[i].childNodes[0].nodeValue+'"' 
                except IndexError:
                    ORG = " " 
                try:
                    LOCATION = " "+user[j].getElementsByTagName('LOCATION')[i].childNodes[0].nodeValue+"."
                except IndexError:
                    LOCATION = " "
                try:
                    DTM_PRESENT = " "+user[j].getElementsByTagName('DTM_PRESENT')[i].childNodes[0].nodeValue+" "
                except IndexError:
                    DTM_PRESENT = " "                
                try:
                    DTY_PRESENT = " "+user[j].getElementsByTagName('DTY_PRESENT')[i].childNodes[0].nodeValue+"."
                except IndexError:
                    DTY_PRESENT = " " 
                try:
                    TITLE = " "+user[j].getElementsByTagName('TITLE')[i].childNodes[0].nodeValue+"."
                except IndexError:
                    TITLE = " "
                try:
                    DESC = " "+user[j].getElementsByTagName('DESC')[i].childNodes[0].nodeValue+","
                except IndexError:
                    DESC = " "

                FNAME = " "
                LNAME = " "
                MNAME = " "
                users2 = []
                authorArray = []
                confCount = 0
                for node2 in user[j].getElementsByTagName("PRESENT_CONFERENCE"):
                    count = len(node2.getElementsByTagName("PRESENT_CONFERENCE_AUTH"))
                    users2.append(count)
                    confCount = confCount+1
                authorCount = 0
                error = ""
                try:
                    while authorCount < users2[nodeCount]:
                        try:
                            FNAME = user[j].getElementsByTagName('FNAME')[index].childNodes[0].nodeValue[:1]+"."
                        except IndexError:
                            FNAME = ""
                        try:
                            MNAME = user[j].getElementsByTagName('MNAME')[index].childNodes[0].nodeValue[:1]+". "
                        except IndexError:
                            MNAME = ""
                        try:
                            LNAME = user[j].getElementsByTagName('LNAME')[index].childNodes[0].nodeValue+", "
                        except IndexError:
                            LNAME = ""
                        authorCount = authorCount+1
                        index = index+1
                        if (authorCount-1 == 0):
                            authors = authors+" "+LNAME+FNAME+MNAME
                        elif (authorCount == 1):
                            authors = authors+" & "+LNAME+FNAME+MNAME
                            authors = authors[1:]
                        elif (authorCount > 1):
                            if (authorCount+1> users2[nodeCount]):
                                authors = authors+", & "+LNAME+FNAME+MNAME
                            else:
                                authors = authors+", "+LNAME+FNAME+MNAME
                except IndexError:
                    error = "error"
                nodeCount = nodeCount+1
                authorArray.append(authors)
                if  NAME is " " and ORG is " " and LOCATION is " " and DESC is " " and \
                    DTM_PRESENT is " " and DTY_ACCEPTANCE is " ":
                        condition = False
                else:
                    temp = authors+" "+TITLE+NAME+ ORG+ LOCATION\
                    +DESC+DTM_PRESENT+DTY_PRESENT
                    temp = fixPuncuation(temp)
                    temp ="<li>"+temp+"</li>" 
                    stringList=stringList+temp
                    i = i+1
                    temp = ""
                    authors = ""
            else:
                FNAME = " "
                LNAME = " "
                MNAME = " "
                tempAuthors = ""
                confCount = 0
                for node2 in user[j].getElementsByTagName("PRESENT_CONFERENCE"):
                    count = len(node2.getElementsByTagName("PRESENT_CONFERENCE_AUTH"))
                    users2.append(count)
                    confCount = confCount+1
                authorCount = 0
                error = ""
                try:
                    while authorCount < users2[nodeCount]:
                        try:
                            FNAME = user[j].getElementsByTagName('FNAME')[index].childNodes[0].nodeValue[:1]+"."
                        except IndexError:
                            FNAME = ""
                        try:
                            MNAME = user[j].getElementsByTagName('MNAME')[index].childNodes[0].nodeValue[:1]+"."
                        except IndexError:
                            MNAME = ""
                        try:
                            LNAME = user[j].getElementsByTagName('LNAME')[index].childNodes[0].nodeValue+", "
                        except IndexError:
                            LNAME = ""
                        authorCount = authorCount+1
                        index = index+1
                        if (authorCount-1 == 0):
                            authors = authors+" "+LNAME+FNAME+MNAME
                        elif (authorCount == 1):
                            authors = authors+" & "+LNAME+FNAME+MNAME
                            authors = authors[1:]
                        elif (authorCount > 1):
                            if (authorCount+1> users2[nodeCount]):
                                authors = authors+", & "+LNAME+FNAME+MNAME
                            else:
                                authors = authors+", "+LNAME+FNAME+MNAME
                except IndexError:
                    error = "error"
                nodeCount = nodeCount+1
                authors = ""
                tempAuthors = ""
                i = i+1

        stringList = stringList+"</ul>"
        if published > 0:
            ploneOnServer = False
            stringList = "<h2>Conferences</h2>"+stringList 
            try:
                stringList+="\n"
            except UnicodeEncodeError:
                text = stringList.encode('ascii', 'ignore')
                stringList+=text
    if published <1:
        stringList = ""
    return stringList
def populate_grants(name, us, userIdArray, userId):
    print "in grants"
    ploneOnServer = False
    #if ploneOnServer == True:
        #t = open('/opt/Plone-4.3/zeocluster/Extensions/COB/pw.txt', 'r+')
    #else:
        #t = open('/Users/cobstu01/Desktop/Plone/file.txt', 'r+')
    j = 0
    #url to retrieve data from
    url = 'http://digitalmeasures.com/login/service/v4/SchemaData/INDIVIDUAL-ACTIVITIES-Business/CONGRANT'
    password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
    # Add the username and password.
    username = "uwosh/fac_reports"
    ##t = open('/Users/cobstu01/Desktop/Plone/file.txt', 'r+')
    #line = "***"
    #password = line 
    top_level_url = "http://digitalmeasures.com/login/service/v4/SchemaData/INDIVIDUAL-ACTIVITIES-Business"
    password_mgr.add_password(None, top_level_url, username, password)
    handler = urllib2.HTTPBasicAuthHandler(password_mgr)

    # create "opener" (OpenerDirector instance)
    opener = urllib2.build_opener(handler)

    # use the opener to fetch a URL
    opener.open(url)

    # Install the opener. Now all calls to urllib2.urlopen use our opener.
    urllib2.install_opener(opener)

    #retrieve the xml file and parse it
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    xml = response.read()
    dom = minidom.parse(urllib2.urlopen(url))

    #####################################################################
    ###Grabs information from Digital Measures from the award section   #
    ### 'j' is the id used for ID's, and increments after all of a users#
    ###awards are acounted forself.                                     #
    #####################################################################
    count = 0
    j = 0
    condition = True
    user = []
    identifier = []
    i = 0
    j = 0
    stringList = "<ul>"
    username = name
    published = 0
    ploneOnServer = False
    for node in dom.getElementsByTagName('Record'):
        identifier.append(node.getAttribute("userId"))
        user.append(node)
    if userId in identifier:
        j = identifier.index(userId)
        condition = True
        while i < len(user[j].getElementsByTagName('CONGRANT')):
            try:
                PUB_INTERNET = user[j].getElementsByTagName("PUB_INTERNET")[i].childNodes[0].nodeValue.strip()
            except IndexError:
                PUB_INTERNET = "No"
            if PUB_INTERNET == "Yes":
                published = published+1
                try:
                    TYPE = ""+user[j].getElementsByTagName('TYPE')[i].childNodes[0].nodeValue+". " 
                except IndexError:
                    TYPE = " "
                try:
                    TITLE = ' "'+user[j].getElementsByTagName('TITLE')[i].childNodes[0].nodeValue+'"'
                except IndexError:
                    TITLE = " " 
                try:
                    CO_INVESTIGATORS = "Co-investigator(s): "+user[j].getElementsByTagName('CO_INVESTIGATORS')[i].childNodes[0].nodeValue+"."
                except IndexError:
                    CO_INVESTIGATORS = " "
                try:
                    SPONORG = "Awarded by "+user[j].getElementsByTagName('SPONORG')[i].childNodes[0].nodeValue+". "
                except IndexError:
                    SPONORG = " "                
                try:
                    TERM_START = " "+user[j].getElementsByTagName('TERM_START')[i].childNodes[0].nodeValue+"," 
                except IndexError:
                    TERM_START = "  "
                try:
                    CLASSIFICATION = " "+user[j].getElementsByTagName('CLASSIFICATION')[i].childNodes[0].nodeValue+". "
                except IndexError:
                    CLASSIFICATION = " "
                try:
                    TYY_TERM = "("+user[j].getElementsByTagName('TYY_TERM')[i].childNodes[0].nodeValue+")."
                except IndexError:
                    TYY_TERM = " "
                TYY_TERM
                if TYPE is " " and TITLE is " " and CO_INVESTIGATORS is " " and SPONORG is " " and CLASSIFICATION is " ":
                        condition = False
                else:
                    grants = TYPE+TYY_TERM+TITLE+SPONORG+CLASSIFICATION+CO_INVESTIGATORS
                    grants = fixPuncuation(grants)
                    grants ="<li>"+grants+"</li>" 
                    stringList=stringList+grants
                    i = i+1
            else:
                i = i+1

        stringList = stringList+"</ul>"
        if published > 0:
            stringList = "<h2>Grants</h2>"+stringList
        try:
            stringList=stringList
        except UnicodeEncodeError:
            text = stringList.encode('ascii', 'ignore')
            stringList+="\n"
    if published <1:
        stringList = ""
    return stringList
def populate_pm(name, us, userIdArray, userId):
    print "in professional membership"
    ploneOnServer = False
    #if ploneOnServer == True:
        #t = open('/opt/Plone-4.3/zeocluster/Extensions/COB/pw.txt', 'r+')
    #else:
        #t = open('/Users/cobstu01/Desktop/Plone/file.txt', 'r+')
    j = 0
    #url to retrieve data from
    url = 'https://digitalmeasures.com/login/service/v4/SchemaData/INDIVIDUAL-ACTIVITIES-Business/MEMBER'
    password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
    # Add the username and password.
    username = "uwosh/fac_reports"
    ##t = open('/Users/cobstu01/Desktop/Plone/file.txt', 'r+')
    #line = "***"
    #password = line
    top_level_url = "http://digitalmeasures.com/login/service/v4/SchemaData/INDIVIDUAL-ACTIVITIES-Business"
    password_mgr.add_password(None, top_level_url, username, password)
    handler = urllib2.HTTPBasicAuthHandler(password_mgr)

    # create "opener" (OpenerDirector instance)
    opener = urllib2.build_opener(handler)

    # use the opener to fetch a URL
    opener.open(url)

    # Install the opener. Now all calls to urllib2.urlopen use our opener.
    urllib2.install_opener(opener)

    #retrieve the xml file and parse it
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    xml = response.read()
    dom = minidom.parse(urllib2.urlopen(url))

    #####################################################################
    ###Grabs information from Digital Measures from the award section   #
    ### 'j' is the id used for ID's, and increments after all of a users#
    ###awards are acounted forself.                                     #
    #####################################################################
    condition = True
    user = []
    identifier = []
    i = 0
    j = 0
    stringList = "<ul>"
    username = name
    ploneOnServer = False
    for node in dom.getElementsByTagName('Record'):
        identifier.append(node.getAttribute("userId"))
        user.append(node)
    if userId in identifier:
        j = identifier.index(userId)
        condition = True
        while i<5 and condition == True: 
            try:
                TITLE = " "+user[j].getElementsByTagName('TITLE')[i].childNodes[0].nodeValue+"," 
            except IndexError:
                TITLE = "  "
            if TITLE is  '  ':
                condition = False
            else:
                Profmember = TITLE
                Profmember = fixPuncuation(Profmember)
                Profmember ="<li>"+Profmember+"</li>" 
                stringList=stringList+Profmember
                i = i+1

        stringList = stringList+"</ul>"
        if i > 0:
            stringList = "<h2>Professional Memberships</h2>"+stringList
        try:
            stringList+="\n"
        except UnicodeEncodeError:
            text = stringList.encode('ascii', 'ignore')
            stringList+=text
    if i <1:
        stringList = ""
    return stringList
def populate_prof(name, us, userIdArray, userId):
    print "in prof"
    ploneOnServer = False
    #if ploneOnServer == True:
        #t = open('/opt/Plone-4.3/zeocluster/Extensions/COB/pw.txt', 'r+')
    #else:
        #t = open('/Users/cobstu01/Desktop/Plone/file.txt', 'r+')
    ##check dates................................................

    j = 0
    #url to retrieve data from
    url = 'http://digitalmeasures.com/login/service/v4/SchemaData/INDIVIDUAL-ACTIVITIES-Business/PRESENT_PROFESSIONAL'
    password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

    # Add the username and password.
    username = "uwosh/fac_reports"
    ##t = open('/Users/cobstu01/Desktop/Plone/file.txt', 'r+')
    #line = "***"
    #password = line 
    top_level_url = "http://digitalmeasures.com/login/service/v4/SchemaData/INDIVIDUAL-ACTIVITIES-Business"
    password_mgr.add_password(None, top_level_url, username, password)
    handler = urllib2.HTTPBasicAuthHandler(password_mgr)

    # create "opener" (OpenerDirector instance)
    opener = urllib2.build_opener(handler)

    # use the opener to fetch a URL
    opener.open(url)

    # Install the opener. Now all calls to urllib2.urlopen use our opener.
    urllib2.install_opener(opener)

    #retrieve the xml file and parse it
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    xml = response.read()
    dom = minidom.parse(urllib2.urlopen(url))

    #####################################################################
    ###Grabs information from Digital Measures from the award section   #
    ### 'j' is the id used for ID's, and increments after all of a users#
    ###awards are acounted forself.                                     #
    #####################################################################
    count = 0
    j = 0
    condition = True
    user = []
    i = 0
    j = 0
    authors = ""
    nodeCount = 0
    users2 = []
    identifier = []
    index = 0
    stringList = "<ul>"
    username = name
    published = 0
    ploneOnServer = False
    for node in dom.getElementsByTagName('Record'):
        identifier.append(node.getAttribute("userId"))
        user.append(node)
    if userId in identifier:
        j = identifier.index(userId)
        condition = True
        while i < len(user[j].getElementsByTagName('PRESENT_PROFESSIONAL')) :
            try:
                PUB_INTERNET = user[j].getElementsByTagName("PUB_INTERNET")[i].childNodes[0].nodeValue.strip()
            except IndexError:
                PUB_INTERNET = "No"
            if PUB_INTERNET == "Yes":
                published = published+1
                try:
                    TYPE = ""+user[j].getElementsByTagName('TYPE')[i].childNodes[0].nodeValue+": "
                except IndexError:
                    TYPE = " " 
                try:
                    TYPEOTHER = ""+user[j].getElementsByTagName('TYPEOTHER')[i].childNodes[0].nodeValue+": "
                except IndexError:
                    TYPEOTHER = " " 
                if (TYPE == "Other"):
                    TYPEOTHER = TYPEOTHER
                else:
                    TYPEOTHER = TYPE
                try:
                    TITLE = ""+user[j].getElementsByTagName('TITLE')[i].childNodes[0].nodeValue+". "
                except IndexError:
                    TITLE = " "
                SPONORG = user[j].getElementsByTagName('')
                try:
                    DTY_DATE = ""+user[j].getElementsByTagName('DTY_DATE')[i].childNodes[0].nodeValue+". "
                except IndexError:
                    DTY_DATE = " " 
                try:
                    ORG = "Presented to "+user[j].getElementsByTagName('ORG')[i].childNodes[0].nodeValue+","
                except IndexError:
                    ORG = " "

                FNAME = " "
                LNAME = " "
                MNAME = " "
                users2 = []
                authorArray = []
                confCount = 0
                authors = ""
                for node2 in user[j].getElementsByTagName("PRESENT_PROFESSIONAL"):
                    count = len(node2.getElementsByTagName("PRESENT_PROFESSIONAL_AUTH"))
                    users2.append(count)
                    confCount = confCount+1
                authorCount = 0
                error = ""
                try:
                    while authorCount < users2[nodeCount]:
                        try:
                            FNAME = user[j].getElementsByTagName('FNAME')[index].childNodes[0].nodeValue[:1]+"."
                        except IndexError:
                            FNAME = ""
                        try:
                            MNAME = user[j].getElementsByTagName('MNAME')[index].childNodes[0].nodeValue[:1]+". "
                        except IndexError:
                            MNAME = ""
                        try:
                            LNAME = user[j].getElementsByTagName('LNAME')[index].childNodes[0].nodeValue+", "
                        except IndexError:
                            LNAME = ""
                        authorCount = authorCount+1
                        index = index+1
                        if (authorCount-1 == 0):
                            authors = authors+" "+LNAME+FNAME+MNAME
                        elif (authorCount == 1):
                            authors = authors+" & "+LNAME+FNAME+MNAME
                            authors = authors[1:]
                        elif (authorCount > 1):
                            if (authorCount+1> users2[nodeCount]):
                                authors = authors+", & "+LNAME+FNAME+MNAME
                            else:
                                authors = authors+", "+LNAME+FNAME+MNAME
                except IndexError:
                    error = "error"
                nodeCount = nodeCount+1
                if TYPEOTHER == " " and TITLE == " " and DTY_DATE == " " and ORG == " ":
                    condition = False
                else:
                    profPres = authors+" "+ DTY_DATE+TYPEOTHER+ TITLE+ORG
                    profPres = fixPuncuation(profPres)
                    profPres ="<li>"+profPres+"</li>" 
                    stringList=stringList+profPres
                    i = i+1
            else:
                FNAME = " "
                LNAME = " "
                MNAME = " "
                tempAuthors = ""
                confCount = 0
                user2 = []
                for node2 in user[j].getElementsByTagName("PRESENT_PROFESSIONAL"):
                    count = len(node2.getElementsByTagName("PRESENT_PROFESSIONAL_AUTH"))
                    users2.append(count)
                    confCount = confCount+1
                authorCount = 0
                error = ""
                try:
                    while authorCount < users2[nodeCount]:
                        try:
                            FNAME = user[j].getElementsByTagName('FNAME')[index].childNodes[0].nodeValue[:1]+"."
                        except IndexError:
                            FNAME = ""
                        try:
                            MNAME = user[j].getElementsByTagName('MNAME')[index].childNodes[0].nodeValue[:1]+"."
                        except IndexError:
                            MNAME = ""
                        try:
                            LNAME = user[j].getElementsByTagName('LNAME')[index].childNodes[0].nodeValue+", "
                        except IndexError:
                            LNAME = ""
                        authorCount = authorCount+1
                        index = index+1
                        if (authorCount-1 == 0):
                            authors = authors+" "+LNAME+FNAME+MNAME
                        elif (authorCount == 1):
                            authors = authors+" & "+LNAME+FNAME+MNAME
                            authors = authors[1:]
                        elif (authorCount > 1):
                            if (authorCount+1> users2[nodeCount]):
                                authors = authors+", & "+LNAME+FNAME+MNAME
                            else:
                                authors = authors+", "+LNAME+FNAME+MNAME
                except IndexError:
                    error = "error"
                nodeCount = nodeCount+1
                authors = ""
                tempAuthors = ""
                i = i+1

        stringList = stringList+"</ul>"
        if published > 0:
            stringList = "<h2>Professional Presentations</h2>"+stringList
        try:
            stringList+="\n"
        except UnicodeEncodeError:
            text = stringList.encode('ascii', 'ignore')
            stringList+=text
    if published <1:
        stringList = ""
    return stringList
def populate_publication(name, us, userIdArray, userId):
    print "in publications"
    ploneOnServer = False
    #if ploneOnServer == True:
        #t = open('/opt/Plone-4.3/zeocluster/Extensions/COB/pw.txt', 'r+')
    #else:
        #t = open('/Users/cobstu01/Desktop/Plone/file.txt', 'r+')
    j = 0
    pub = []
    linkString = ""
    #url to retrieve data from
    url = 'https://digitalmeasures.com/login/service/v4/SchemaData/INDIVIDUAL-ACTIVITIES-Business/INTELLCONT'
    password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

    # Add the username and password.
    username = "uwosh/fac_reports"
    ##t = open('/Users/cobstu01/Desktop/Plone/file.txt', 'r+')
    #line = "***"
    #password = line
    top_level_url = "http://digitalmeasures.com/login/service/v4/SchemaData/INDIVIDUAL-ACTIVITIES-Business"
    password_mgr.add_password(None, top_level_url, username, password)
    handler = urllib2.HTTPBasicAuthHandler(password_mgr)

    # create "opener" (OpenerDirector instance)
    opener = urllib2.build_opener(handler)

    # use the opener to fetch a URL
    opener.open(url)

    # Install the opener. Now all calls to urllib2.urlopen use our opener.
    urllib2.install_opener(opener)

    #retrieve the xml file and parse it
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    xml = response.read()
    dom = minidom.parse(urllib2.urlopen(url))

    #####################################################################
    ###Grabs information from Digital Measures from the award section   #
    ### 'j' is the id used for ID's, and increments after all of a users#
    ###awards are acounted forself.                                     #
    #####################################################################
    count = 0
    j = 0
    condition = True
    nodeCount = 0
    index = 0
    forthcoming = []
    forthcomingContainer = []
    finished = False
    user = []
    users2 = []
    linkContainer = []
    linkCount = 0
    hasLink = False
    JournalArticle = []
    BookChapter = []
    Book = []
    ArticleContainingCitation = []
    ConferenceProceeding = []
    BookReview = []
    BroadcastMedia = []
    Cases = []
    Chapters = []
    CitedResearch = []
    Editorship = []
    InHousePaper = []
    InstructionalTextbook = []
    InstructorsManual = []
    MagazineTradePublication = []
    Monographs = []
    Newsletter = []
    Newspaper = []
    regularcolumn = []
    ResearchReport = []
    Software = []
    StudyGuide = []
    TechnicalReport = []
    WorkingPaper = []
    ForthcomingArray = []
    publishedArray = []
    authorArray = []
    identifier = []
    authors = ""
    published = 0
    i = 0
    hasPublication = False
    stringList = ""
    ploneOnServer = False
    for node in dom.getElementsByTagName('Record'):
        identifier.append(node.getAttribute("userId"))
        user.append(node)
    if userId in identifier:
        j = identifier.index(userId)
        while i < len(user[j].getElementsByTagName("INTELLCONT")):
            VOLUME = ""
            PAGENUM = ""
            try:
                PUB_INTERNET = user[j].getElementsByTagName("PUB_INTERNET")[i].childNodes[0].nodeValue.strip()
            except IndexError:
                PUB_INTERNET = "No"
            if PUB_INTERNET != "No":
                published = published+1
                try:
                    FNAME = user[j].getElementsByTagName("FNAME")[i].childNodes[0].nodeValue+""
                except IndexError:
                    FNAME = " "
                try:
                    CONTYPE = "("+user[j].getElementsByTagName("CONTYPE")[i].childNodes[0].nodeValue.strip()+")"
                except IndexError:
                    CONTYPE = " "
                try:
                    STATUS = "("+user[j].getElementsByTagName("STATUS")[i].childNodes[0].nodeValue+")."
                except IndexError:
                    STATUS = ""
                try:
                    DTY_PUB = " ("+user[j].getElementsByTagName("DTY_PUB")[i].childNodes[0].nodeValue+"). "
                except IndexError:
                    DTY_PUB = " "
                try:
                    TITLE = "<span>"+user[j].getElementsByTagName("TITLE")[i].childNodes[0].nodeValue+". </span>"
                except IndexError:
                    TITLE = ""
                try:
                    PUBLISHER = user[j].getElementsByTagName("PUBLISHER")[i].childNodes[0].nodeValue.strip()
                except IndexError:
                    PUBLISHER = ""
                try:
                    VOLUME = user[j].getElementsByTagName("VOLUME")[i].childNodes[0].nodeValue+", "
                except IndexError:
                    VOLUME = ""
                try:
                    PAGENUM = "("+user[j].getElementsByTagName("PAGENUM")[i].childNodes[0].nodeValue+")."
                except IndexError:
                    PAGENUM = ""
                try:
                    EDITORS = "in "+user[j].getElementsByTagName("EDITORS")[i].childNodes[0].nodeValue+" (Eds.), "
                except IndexError:
                    EDITORS = ""
                try:
                    TITLE_SECONDARY = user[j].getElementsByTagName("TITLE_SECONDARY")[i].childNodes[0].nodeValue+""
                except IndexError:
                    TITLE_SECONDARY = " "
                try:
                    PUBCTYST = user[j].getElementsByTagName("PUBCTYST")[i].childNodes[0].nodeValue+": "
                except IndexError:
                    PUBCTYST = " "  
                FNAME = " "
                LNAME = " "
                MNAME = " "
                confCount = 0
                for node2 in user[j].getElementsByTagName("INTELLCONT"):
                    count = len(node2.getElementsByTagName("INTELLCONT_AUTH"))
                    users2.append(count)
                    confCount = confCount+1
                authorCount = 0
                error = ""
                try:
                    while authorCount < users2[nodeCount]:
                        try:
                            FNAME = user[j].getElementsByTagName('FNAME')[index].childNodes[0].nodeValue[:1]+"."
                        except IndexError:
                            FNAME = ""
                        try:
                            MNAME = user[j].getElementsByTagName('MNAME')[index].childNodes[0].nodeValue[:1]+"."
                        except IndexError:
                            MNAME = ""
                        try:
                            LNAME = user[j].getElementsByTagName('LNAME')[index].childNodes[0].nodeValue+", "
                        except IndexError:
                            LNAME = ""
                        authorCount = authorCount+1
                        index = index+1
                        if (authorCount-1 == 0):
                            authors = authors+" "+LNAME+FNAME+MNAME
                        elif (authorCount == 1):
                            authors = authors+" & "+LNAME+FNAME+MNAME
                            authors = authors[1:]
                        elif (authorCount > 1):
                            if (authorCount+1> users2[nodeCount]):
                                authors = authors+", & "+LNAME+FNAME+MNAME
                            else:
                                authors = authors+", "+LNAME+FNAME+MNAME
                except IndexError:
                    error = "error"
                nodeCount = nodeCount+1
                journalArticleCount = 0
                
                
                authorArray.append(authors)
                if( "'" in CONTYPE):
                    CONTYPE = CONTYPE.replace(" ", "'")
                if("/" in CONTYPE):
                    CONTYPE = CONTYPE.replace(" ", "/")
                if(CONTYPE == "(Journal Article)"):
                    if (PUBLISHER != ""):
                        PUBLISHER = "<span class=\"italics\">"+PUBLISHER+".</span> "
                    if (STATUS == "(Forthcoming)."):
                        linkString = authors+" "+STATUS+" "+TITLE+PUBLISHER####+VOLUME+PAGENUM
                        linkString = fixPuncuation(linkString)
                        ForthcomingArray.append("<li>"+linkString+"</li>")
                    elif (STATUS == "(Work-in-progress)."):
                        linkString = authors+" "+STATUS+" "+TITLE+PUBLISHER####+VOLUME+PAGENUM
                        linkString = fixPuncuation(linkString)
                        ForthcomingArray.append("<li>"+linkString+"</li>")
                    elif (STATUS == "(Published)."):                       
                        linkString = authors+DTY_PUB+TITLE+PUBLISHER####+VOLUME+PAGENUM
                        linkString = fixPuncuation(linkString)
                        publishedArray.append("<li>"+linkString+"</li>")
                        hasPublication = True
                elif(CONTYPE == "(Book Chapter)"):
                    linkString = authors+DTY_PUB+TITLE+EDITORS+TITLE_SECONDARY+PAGENUM+PUBCTYST+PUBLISHER.strip()
                    linkString = fixPuncuation(linkString)
                    BookChapter.append("<li>"+linkString+"</li>")
                    hasPublication = True
                elif(CONTYPE == "(Book)"):
                    linkString = authors+DTY_PUB+TITLE+PUBLISHER.strip()
                    linkString = fixPuncuation(linkString)
                    Book.append("<li>"+linkString+"</li>")
                    hasPublication = True
                elif(CONTYPE == "(Article Containing Citation)"):
                    linkString = authors+DTY_PUB+TITLE+PUBLISHER.strip()
                    linkString = fixPuncuation(linkString)
                    ArticleContainingCitation.append("<li>"+linkString+"</li>")
                    hasPublication = True
                elif(CONTYPE == "(Conference Proceeding)"):
                    linkString = authors+DTY_PUB+TITLE+PUBLISHER.strip()
                    linkString = fixPuncuation(linkString)
                    ConferenceProceeding.append("<li>"+linkString+"</li>")
                    hasPublication = True
                elif(CONTYPE == "(Book Review)"):
                    linkString = authors+DTY_PUB+TITLE+PUBLISHER.strip()
                    linkString = fixPuncuation(linkString)
                    BookReview.append("<li>"+linkString+"</li>")
                    hasPublication = True
                elif(CONTYPE == "(Broadcast Media)"):
                    linkString = authors+DTY_PUB+TITLE+PUBLISHER.strip()
                    linkString = fixPuncuation(linkString)
                    Broadcast.append("<li>"+linkString+"</li>")
                    hasPublication = True
                elif(CONTYPE == "(Cases)"):
                    linkString = Fauthors+DTY_PUB+TITLE+PUBLISHER.strip()
                    linkString = fixPuncuation(linkString)
                    Cases.append("<li>"+linkString+"</li>")
                    hasPublication = True
                elif(CONTYPE == "(Chapter(s))"):
                    linkString = authors+DTY_PUB+TITLE+PUBLISHER.strip()
                    linkString = fixPuncuation(linkString)
                    Chapters.append("<li>"+linkString+"</li>")
                    hasPublication = True
                elif(CONTYPE == "(Cited Research)"):
                    linkString = authors+DTY_PUB+TITLE+PUBLISHER.strip()
                    linkString = fixPuncuation(linkString)
                    CitedResearch.append("<li>"+linkString+"</li>")
                    hasPublication = True
                elif(CONTYPE == "(Editorship)"):
                    linkString = authors+DTY_PUB+TITLE+PUBLISHER.strip()
                    linkString = fixPuncuation(linkString)
                    Editorship.append("<li>"+linkString+"</li>")
                    hasPublication = True
                elif(CONTYPE == "(In-House Paper)"):
                    temp = contype
                    linkString = authors+DTY_PUB+TITLE+PUBLISHER+temp.strip()
                    linkString = fixPuncuation(linkString)
                    InHousePaper.append("<li>"+linkString+"</li>")
                    hasPublication = True
                elif(CONTYPE == "(Instructional Textbook)"):
                    linkString = authors+DTY_PUB+TITLE+PUBLISHER.strip()
                    linkString = fixPuncuation(linkString)
                    InstructionalTextbook.append("<li>"+linkString+"</li>")
                    hasPublication = True
                elif(CONTYPE == "(Instructor s Manual)"):
                    linkString = authors+DTY_PUB+TITLE+PUBLISHER.strip()
                    linkString = fixPuncuation(linkString)
                    JournalArticle.append("<li>"+linkString+"</li>")
                    hasPublication = True
                elif(CONTYPE == "(Magazine Trade Publication"):
                    linkString = authors+DTY_PUB+TITLE+PUBLISHER.strip()
                    linkString = fixPuncuation(linkString)
                    MagazineTradePublication.append("<li>"+linkString+"</li>")
                    hasPublication = True
                elif(CONTYPE == "(Monographs)"):
                    linkString = authors+DTY_PUB+TITLE+PUBLISHER.strip()
                    linkString = fixPuncuation(linkString)
                    Monographs.append("<li>"+linkString+"</li>")
                    hasPublication = True
                elif(CONTYPE == "(Newsletter)"):
                    linkString = authors+DTY_PUB+TITLE+PUBLISHER.strip()
                    linkString = fixPuncuation(linkString)
                    Newsletter.append("<li>"+linkString+"</li>")
                    hasPublication = True
                elif(CONTYPE == "(Newspaper)"):
                    linkString = authors+DTY_PUB+TITLE+PUBLISHER.strip()
                    linkString = fixPuncuation(linkString)
                    Newspaper.append("<li>"+linkString+"</li>")
                    hasPublication = True
                elif(CONTYPE == "(Regular Column in Journal or Newspaper)"):
                    linkString = authors+DTY_PUB+TITLE+PUBLISHER.strip()
                    linkString = fixPuncuation(linkString)
                    regularcolumn.append("<li>"+linkString+"</li>")
                    hasPublication = True
                elif(CONTYPE == "(Research Report"):
                    linkString = authors+DTY_PUB+TITLE+PUBLISHER.strip()
                    linkString = fixPuncuation(linkString)
                    ResearchReport.append("<li>"+linkString+"</li>")
                    hasPublication = True
                elif(CONTYPE == "(Software)"):
                    linkString = authors+DTY_PUB+TITLE+PUBLISHER.strip()
                    linkString = fixPuncuation(linkString)
                    Software.append("<li>"+linkString+"</li>")
                    hasPublication = True
                elif(CONTYPE == "(Study Guide)"):
                    linkString = authors+DTY_PUB+TITLE+PUBLISHER.strip()
                    linkString = fixPuncuation(linkString)
                    StudyGuide.append("<li>"+linkString+"</li>")
                    hasPublication = True
                elif(CONTYPE == "(Technical Report)"):
                    linkString = authors+DTY_PUB+TITLE+PUBLISHER.strip()
                    linkString = fixPuncuation(linkString)
                    TechnicalReport.append("<li>"+linkString+"</li>")
                    hasPublication = True
                elif(CONTYPE == "(Working Paper)"):
                    linkString = authors+DTY_PUB+TITLE+PUBLISHER.strip()
                    linkString = fixPuncuation(linkString)
                    WorkingPaper.append("<li>"+linkString+"</li>")
                    hasPublication = True
                i = i+1
                authors = ""
            else:
                FNAME = " "
                LNAME = " "
                MNAME = " "
                tempAuthors = ""
                confCount = 0
                for node2 in user[j].getElementsByTagName("INTELLCONT"):
                    count = len(node2.getElementsByTagName("INTELLCONT_AUTH"))
                    users2.append(count)
                    confCount = confCount+1
                authorCount = 0
                error = ""
                try:
                    while authorCount < users2[nodeCount]:
                        try:
                            FNAME = user[j].getElementsByTagName('FNAME')[index].childNodes[0].nodeValue[:1]+"."
                        except IndexError:
                            FNAME = ""
                        try:
                            MNAME = user[j].getElementsByTagName('MNAME')[index].childNodes[0].nodeValue[:1]+"."
                        except IndexError:
                            MNAME = ""
                        try:
                            LNAME = user[j].getElementsByTagName('LNAME')[index].childNodes[0].nodeValue+", "
                        except IndexError:
                            LNAME = ""
                        authorCount = authorCount+1
                        index = index+1
                        if (authorCount-1 == 0):
                            authors = authors+" "+LNAME+FNAME+MNAME
                        elif (authorCount == 1):
                            authors = authors+" & "+LNAME+FNAME+MNAME
                            authors = authors[1:]
                        elif (authorCount > 1):
                            if (authorCount+1> users2[nodeCount]):
                                authors = authors+", & "+LNAME+FNAME+MNAME
                            else:
                                authors = authors+", "+LNAME+FNAME+MNAME
                except IndexError:
                    error = "error"
                nodeCount = nodeCount+1
                authors = ""
                tempAuthors = ""
                i = i+1
        linkLength = 0
        if (hasPublication == True):
            if (len(publishedArray)+len(ForthcomingArray)>0):
                if (len(publishedArray)+len(ForthcomingArray)>1):
                    stringList +="<h2>Journal Articles</h2><ul>"
                else:
                    stringList +="<h2>Journal Article</h2><ul>"
                while (len(ForthcomingArray)>linkLength):
                    stringList+= ForthcomingArray[linkLength].encode('ascii', 'ignore')
                    linkLength = linkLength+1  
                linkLength = 0
                while (len(publishedArray)>linkLength):
                    stringList+= publishedArray[linkLength].encode('ascii', 'ignore')
                    linkLength = linkLength+1  
                stringList+="</ul>"    
            linkLength = 0
            if (len(BookReview)>0):
                if (len(BookReview)>1):
                    stringList +="<h2>Book Reviews</h2><ul>"
                else:
                    stringList +="<h2>Book Review</h2><ul>"
                while (len(BookReview)>linkLength):
                    stringList+=BookReview[linkLength].encode('ascii', 'ignore')
                    linkLength = linkLength+1
                stringList+="</ul>"
            linkLength = 0
            if (len(Book)>0):
                if (len(Book)>1):
                    stringList +="<h2>Books</h2><ul>"
                else:
                    stringList +="<h2>Book</h2><ul>"
                while (len(Book)>linkLength):
                    stringList+=Book[linkLength].encode('ascii', 'ignore')
                    linkLength = linkLength+1
                stringList+="</ul>"
            linkLength = 0
            if (len(BookChapter)>0):
                if (len(BookChapter)>1):
                    stringList +="<h2>Book Chapters</h2><ul>"
                else:
                    stringList +="<h2>Book Chapter</h2><ul>"
                while (len(BookChapter)>linkLength):
                    stringList+=BookChapter[linkLength].encode('ascii', 'ignore')
                    linkLength = linkLength+1
                stringList+="</ul>"
            linkLength = 0
            if (len(BroadcastMedia)>0):
                if (len(BroadcastMedia)>1):
                    stringList +="<h2>Broadcast Medias</h2><ul>"
                else:
                    stringList +="<h2>Broadcast Media</h2><ul>"
                while (len(BroadcastMedia)>linkLength):
                    stringList+=BroadcastMedia[linkLength].encode('ascii', 'ignore')
                    linkLength = linkLength+1
                stringList+="</ul>"
            linkLength = 0
            if (len(Cases)>0):
                if (len(Cases)>1):
                    stringList +="<h2>Cases</h2><ul>"
                else:
                    stringList +="<h2>Case</h2><ul>"
                while (len(Cases)>linkLength):
                    stringList+=Cases[linkLength].encode('ascii', 'ignore')
                    linkLength = linkLength+1
                stringList+="</ul>"
            linkLength = 0
            if (len(Chapters)>0):
                if (len(Chapters)>1):
                    stringList +="<h2>Chapters</h2><ul>"
                else:
                    stringList +="<h2>Chapters</h2><ul>"
                while (len(Chapters)>linkLength):
                    stringList+=Chapters[linkLength].encode('ascii', 'ignore')
                    linkLength = linkLength+1
                stringList+="</ul>"
            linkLength = 0
            if (len(CitedResearch)>0):
                if (len(CitedResearch)>1):
                    stringList +="<h2>Cited Researchs</h2><ul>"
                else:
                    stringList +="<h2>Cited Research</h2><ul>"
                while (len(CitedResearch)>linkLength):
                    stringList+=CitedResearch[linkLength].encode('ascii', 'ignore')
                    linkLength = linkLength+1
                stringList+="</ul>"
            linkLength = 0
            if (len(ConferenceProceeding)>0):
                if (len(ConferenceProceeding)>1):
                    stringList +="<h2>Conference Proceedings</h2><ul>"
                else:
                    stringList +="<h2>Conference Proceedings</h2><ul>"
                while (len(ConferenceProceeding)>linkLength):
                    stringList+=ConferenceProceeding[linkLength].encode('ascii', 'ignore')
                    linkLength = linkLength+1
                stringList+="</ul>"
            linkLength = 0
            if (len(Editorship)>0):
                if (len(Editorship)>1):
                    stringList +="<h2>Editorships</h2><ul>"
                else:
                    stringList +="<h2>Editorship</h2><ul>"
                while (len(Editorship)>linkLength):
                    stringList+=Editorship[linkLength].encode('ascii', 'ignore')
                    linkLength = linkLength+1
                stringList+="</ul>"
            linkLength = 0
            if (len(InHousePaper)>0):
                if (len(InHousePaper)>1):
                    stringList +="<h2>In-House Papers</h2><ul>"
                else:
                    stringList +="<h2>In-House Paper</h2><ul>"
                while (len(InHousePaper)>linkLength):
                    stringList+=InHousePaper[linkLength].encode('ascii', 'ignore')
                    linkLength = linkLength+1
                stringList+="</ul>"
            linkLength = 0
            if (len(InstructionalTextbook)>0):
                if (len(InstructionalTextbook)>1):
                    stringList +="<h2>Instructional Textbooks</h2><ul>"
                else:
                    stringList +="<h2>Instructional Textbook</h2><ul>"
                while (len(InstructionalTextbook)>linkLength):
                    stringList+=InstructionalTextbook[linkLength].encode('ascii', 'ignore')
                    linkLength = linkLength+1
                stringList+="</ul>"
            linkLength = 0
            if (len(InstructorsManual)>0):
                if (len(InstructorsManual)>1):
                    stringList +="<h2>Instructor's Manuals</h2><ul>"
                else:
                    stringList +="<h2>Instructor's Manual</h2><ul>"
                while (len(InstructorsManual)>linkLength):
                    stringList+=InstructorsManual[linkLength].encode('ascii', 'ignore')
                    linkLength = linkLength+1
                stringList+="</ul>"
            linkLength = 0
            if (len(MagazineTradePublication)>0):
                if (len(MagazineTradePublication)>1):
                    stringList +="<h2>Magazine Trade Publications</h2><ul>"
                else:
                    stringList +="<h2>Magazine Trade Publication</h2><ul>"
                while (len(MagazineTradePublication)>linkLength):
                    stringList+=MagazineTradePublication[linkLength].encode('ascii', 'ignore')
                    linkLength = linkLength+1
                stringList+="</ul>"
            linkLength = 0
            if (len(Monographs)>0):
                if (len(Monographs)>1):
                    stringList +="<h2>Monographs</h2><ul>"
                else:
                    stringList +="<h2>Monograph</h2><ul>"
                while (len(Monographs)>linkLength):
                    stringList+=Monographs[linkLength].encode('ascii', 'ignore')
                    linkLength = linkLength+1
                stringList+="</ul>"
            linkLength = 0
            if (len(Newsletter)>0):
                if (len(Newsletter)>1):
                    stringList +="<h2>Newsletters</h2><ul>"
                else:
                    stringList +="<h2>Newsletter</h2><ul>"
                while (len(Newsletter)>linkLength):
                    stringList+=Newsletter[linkLength].encode('ascii', 'ignore')
                    linkLength = linkLength+1
                stringList+="</ul>"
            linkLength = 0
            if (len(Newspaper)>0):
                if (len(Newspaper)>1):
                    stringList +="<h2>Newspapers</h2><ul>"
                else:
                    stringList +="<h2>Newspaper</h2><ul>"
                while (len(Newspaper)>linkLength):
                    stringList+=Newspaper[linkLength].encode('ascii', 'ignore')
                    linkLength = linkLength+1
                stringList+="</ul>"
            linkLength = 0
            if (len(regularcolumn)>0):
                if (len(regularcolumn)>1):
                    stringList +="<h2>Regular Column in Journal or Newspapers</h2><ul>"
                else:
                    stringList +="<h2>Regular Column in Journal or Newspaper</h2><ul>"
                while (len(regularcolumn)>linkLength):
                    stringList+=regularcolumn[linkLength].encode('ascii', 'ignore')
                    linkLength = linkLength+1
                stringList+="</ul>"
            linkLength = 0
            if (len(ResearchReport)>0):
                if (len(ResearchReport)>1):
                    stringList +="<h2>Research Reports</h2><ul>"
                else:
                    stringList +="<h2>Research Report</h2><ul>"
                f.write("<h2>Research Report</h2><ul>")
                while (len(ResearchReport)>linkLength):
                    stringList+=ResearchReport[linkLength].encode('ascii', 'ignore')
                    linkLength = linkLength+1
                stringList+="</ul>"
            linkLength = 0
            if (len(Software)>0):
                if (len(Software)>1):
                    stringList +="<h2>Softwares</h2><ul>"
                else:
                    stringList +="<h2>Software</h2><ul>"
                while (len(Software)>linkLength):
                    stringList+=Software[linkLength].encode('ascii', 'ignore')
                    linkLength = linkLength+1
                stringList+="</ul>"
            linkLength = 0
            if (len(StudyGuide)>0):
                if (len(StudyGuide)>1):
                    stringList +="<h2>Study Guides</h2><ul>"
                else:
                    stringList +="<h2>Study Guide</h2><ul>"
                while (len(StudyGuide)>linkLength):
                    stringList+=StudyGuide[linkLength].encode('ascii', 'ignore')
                    linkLength = linkLength+1
                stringList+="</ul>"
            linkLength = 0
            if (len(TechnicalReport)>0):
                if (len(TechnicalReport)>1):
                    stringList +="<h2>Technical Reports</h2><ul>"
                else:
                    stringList +="<h2>Technical Report</h2><ul>"
                while (len(TechnicalReport)>linkLength):
                    stringList+=TechnicalReport[linkLength].encode('ascii', 'ignore')
                    linkLength = linkLength+1
                stringList+="</ul>"
            linkLength = 0
            if (len(ArticleContainingCitation)>0):
                if (len(ArticleContainingCitation)>1):
                    stringList +="<h2>Article's Containing Citation</h2><ul>"
                else:
                    stringList +="<h2>Article's Containing Citatio</h2><ul>"
                while (len(ArticleContainingCitation)>linkLength):
                    stringList+=ArticleContainingCitation[linkLength].encode('ascii', 'ignore')
                    linkLength = linkLength+1
                stringList+="</ul>"
            linkLength = 0
            if (len(WorkingPaper)>0):
                if (len(WorkingPaper)>1):
                    stringList +="<h2>Working Papers</h2><ul>"
                else:
                    stringList +="<h2>Working Paper</h2><ul>"
                while (len(WorkingPaper)>linkLength):
                    stringList+=WorkingPaper[linkLength].encode('ascii', 'ignore')
                    linkLength = linkLength+1
                stringList+="</ul>"
        linkLength = 0
    if hasPublication == False:
        stringList = ""
    return stringList
def create_directory_html(us, userIdArray, userId):
    print "inside directory html "+userId
    htmlFile = ""
    nameArray = populate_users(us, userIdArray, userId)#, pictureArray)
    name = nameArray[0]
    name = name.strip()
    htmlFile+= nameArray[2]
    htmlFile+=populate_publication(name,us, userIdArray, userId)
    htmlFile+=populate_conf(name,us, userIdArray, userId)
    htmlFile+=populate_grants(name, us, userIdArray, userId)
    htmlFile+=populate_prof(name,us, userIdArray, userId)
    htmlFile+=populate_award(name,us, userIdArray, userId)
    htmlFile+=populate_pm(name,us, userIdArray, userId)
    htmlFile+=populate_certification(name,us, userIdArray, userId)
    get_categories("directory", us, name)
    return name, htmlFile

def create_summary_html(username, userIdArray, userId):
    infoArray = []
    name = []
    ploneOnServer = False
    infoArray = populate_users_departmentPage(username, userIdArray, userId)
    name = infoArray[0]
    info = infoArray[2]
    get_categories("summary", username, name)
    return info

def get_categories(profileType, username, name):
    try:
        categories = populate_admin(username)[2]
    except IndexError:
        categories = "there are no categories"
    portal = getSite()
    #username = username.lower()
    if hasattr(portal, profileType):
        form_folder = getattr(portal, profileType)
        if (profileType == "directory"):
            if hasattr(form_folder, username):
                person = getattr(form_folder,username)
                ploneOnServer = False
                person.edit(subject=categories)
        elif(profileType == "summary"):
            if hasattr(form_folder, username+"-summary"):
                person = getattr(form_folder,username+"-summary")
                person.edit(subject=categories)

def create_plone_summaryPage(name, username, userIdArray, userId):
    try:
        categories = populate_admin(username)[2]
    except IndexError:
        categories = "there are no categories"
    portal = getSite()
    username = username.lower()
    if name != ".DS_Store":
        if hasattr(portal, 'summary'):
            form_folder = getattr(portal, 'summary')
            info = populate_users_departmentPage(username, userIdArray, userId)[2]
            tempPersonObject = form_folder.invokeFactory(type_name="Document", id= username+"-summary", title = name)
            newItem = form_folder[tempPersonObject]
            newPage = getattr(form_folder, username+"-summary")
            ploneOnServer = False
            newPage.edit('html',info)
            newPage.edit(subject=categories)

def create_plone_ProfilePage(name, username, info):
    ploneOnServer = False
    #if ploneOnServer == True:
        #t = open('/opt/Plone-4.3/zeocluster/Extensions/COB/pw.txt', 'r+')
    #else:
        #t = open('/Users/cobstu01/Desktop/Plone/file.txt', 'r+')
    import glob
    i = 0
    j = 0
    portal = getSite()
    tempName = name
    try:
        categories = populate_admin(username)[2]
    except IndexError:
        categories = "there are no categories"
    if("'" in tempName):
        tempName= tempName.replace("'","")
    else:
        tempName = name
    tempName = tempName[:-5]
    username = username.lower()
    if hasattr(portal, 'directory'):
        form_folder = getattr(portal, 'directory')
        tempPersonObject = form_folder.invokeFactory(type_name="Document", id= username, title = name)
        newItem = form_folder[tempPersonObject]
        newPage = getattr(form_folder, username)
        newPage.setExcludeFromNav(True)
        newPage.edit(subject=categories)
        newPage.edit('html',info)
        print " profile created is for  "+name

def populate_methods():
    ploneOnServer = False
    #if ploneOnServer == True:
        #t = open('/opt/Plone-4.3/zeocluster/Extensions/COB/pw.txt', 'r+')
    #else:
        #t = open('/Users/cobstu01/Desktop/Plone/file.txt', 'r+')
    user = []
    names = []
    usernameHolder = []
    url = 'https://digitalmeasures.com/login/service/v4/SchemaData/INDIVIDUAL-ACTIVITIES-Business/ADMIN'
    import datetime
    curr_year = datetime.datetime.now()
    curr_year = curr_year.year-1 ##2013
    prev_year = curr_year+1    #2014
    school_year = str(curr_year)+"-"+str(prev_year) ##2013-2014
    password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
    username = "uwosh/fac_reports"
    #line = "***"
    #password = line 
    top_level_url = "http://digitalmeasures.com/login/service/v4/SchemaData/INDIVIDUAL-ACTIVITIES-Business"
    password_mgr.add_password(None, top_level_url, username, password)
    handler = urllib2.HTTPBasicAuthHandler(password_mgr)
    opener = urllib2.build_opener(handler)
    opener.open(url)
    urllib2.install_opener(opener)
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    xml = response.read()
    dom = minidom.parse(urllib2.urlopen(url))
    count = 0
    pictureArray = []
    returnInfo = []
    userIdArray = []
    ploneOnServer = False
    html = ""
    userId = ""
    nameArray = []
    for node in dom.getElementsByTagName('Record'):
        userId = node.getAttribute('userId')
        userIdArray.append(userId)
        break
        userIdArray.append(node.getAttribute('userId'))

    for node in dom.getElementsByTagName('Record'):
        userId = node.getAttribute('userId')
        checkCount = 0
        try:
            AC_YEAR = node.getElementsByTagName('AC_YEAR')[0].childNodes[0].nodeValue 
        except IndexError:
            AC_YEAR = "  "
        try:
            EMPLOYMENT_STATUS = node.getElementsByTagName('EMPLOYMENT_STATUS')[0].childNodes[0].nodeValue.strip()
        except IndexError:
            EMPLOYMENT_STATUS = "inactive"
        if AC_YEAR == school_year and EMPLOYMENT_STATUS == "Active":
            us = node.getAttribute('username')
            print "username is "+us
            count=count+1
            print str(count)
            nameArray = populate_users(us, userIdArray, userId)
            name = nameArray[0]
            name = name.strip()
            htmlFile = nameArray[2]
            htmlFile+=populate_publication(name,us, userIdArray, userId)
            htmlFile+=populate_conf(name,us, userIdArray, userId)
            htmlFile+=populate_grants(name, us, userIdArray, userId)
            htmlFile+=populate_prof(name,us, userIdArray, userId)
            htmlFile+=populate_award(name,us, userIdArray, userId)
            htmlFile+=populate_pm(name,us, userIdArray, userId)
            htmlFile+=populate_certification(name,us, userIdArray, userId)
            create_plone_ProfilePage(name, us, htmlFile)
    #print "count = "+str(count)

def create_summary():
    ploneOnServer = False
    #if ploneOnServer == True:
        #t = open('/opt/Plone-4.3/zeocluster/Extensions/COB/pw.txt', 'r+')
    #else:
        #t = open('/Users/cobstu01/Desktop/Plone/file.txt', 'r+')
    user = []
    names = []
    usernameHolder = []
    count = 0
    url = 'https://digitalmeasures.com/login/service/v4/SchemaData/INDIVIDUAL-ACTIVITIES-Business/ADMIN'
    import datetime
    print "start time is "+str(datetime.datetime.now())
    curr_year = datetime.datetime.now()
    curr_year = curr_year.year-1 ##2013
    prev_year = curr_year+1    #2014
    school_year = str(curr_year)+"-"+str(prev_year) ##2013-2014
    password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
    username = "uwosh/fac_reports"
    #line = "***"
    #password = line 
    top_level_url = "http://digitalmeasures.com/login/service/v4/SchemaData/INDIVIDUAL-ACTIVITIES-Business"
    password_mgr.add_password(None, top_level_url, username, password)
    handler = urllib2.HTTPBasicAuthHandler(password_mgr)
    opener = urllib2.build_opener(handler)
    opener.open(url)
    urllib2.install_opener(opener)
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    xml = response.read()
    dom = minidom.parse(urllib2.urlopen(url))
    count = 0
    pictureArray = []
    categories = []
    ploneOnServer = False
    nameArray = []
    userIdArray = []
    userId = ""
    for node in dom.getElementsByTagName('Record'):
        userId = node.getAttribute('userId')
        userIdArray.append(userId)
        checkCount = 0
        try:
            AC_YEAR = node.getElementsByTagName('AC_YEAR')[0].childNodes[0].nodeValue 
        except IndexError:
            AC_YEAR = "  "
        try:
            EMPLOYMENT_STATUS = node.getElementsByTagName('EMPLOYMENT_STATUS')[0].childNodes[0].nodeValue.strip()
        except IndexError:
            EMPLOYMENT_STATUS = "inactive"
        if AC_YEAR == school_year and EMPLOYMENT_STATUS == "Active":
            us = node.getAttribute('username')
            returnInfo = []
            returnInfo = populate_users_departmentPage(us, userIdArray, userId)
            name = returnInfo[0]
            create_plone_summaryPage(name, us, userIdArray, userId)
            print "count = "+str(count)
            count = count+1
            print "end time is "+str(datetime.datetime.now())

def fixPuncuation(linkString):
    linkString = linkString.strip()
    if(linkString[-1] == ","):
        linkString = linkString.strip(",")
        if(linkString[-1] == "."):
            fixPuncuation(linkString)
        else:
            linkString = linkString+"."
    if(linkString[-1] == ","):
        linkString = linkString.strip(",")
        if(linkString[-1] != "."):
            fixPuncuation(linkString)
        else:
            linkString = linkString+"."
    if(linkString[-1] == ";"):
        linkString = linkString.strip(";")
        if(linkString[-1] != "."):
            fixPuncuation(linkString)
        else:
            linkString = linkString+"."
    if(linkString[-1] != "." and linkString[-1] != ">"):
        linkString = linkString+"."
    return linkString


def update_info():
    ploneOnServer = False
    #if ploneOnServer == True:
        #t = open('/opt/Plone-4.3/zeocluster/Extensions/COB/pw.txt', 'r+')
    ##else:
        #t = open('/Users/cobstu01/Desktop/Plone/file.txt', 'r+')
    #url to retrieve data from
    url = 'https://digitalmeasures.com/login/service/v4/SchemaData/INDIVIDUAL-ACTIVITIES-Business/PCI'

    password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

    # Add the username and password.
    username = "uwosh/fac_reports"
    ##t = open('/Users/cobstu01/Desktop/Plone/file.txt', 'r+')
    #line = "***"
    #password = line 
    top_level_url = "http://digitalmeasures.com/login/service/v4/SchemaData/INDIVIDUAL-ACTIVITIES-Business"
    password_mgr.add_password(None, top_level_url, username, password)
    handler = urllib2.HTTPBasicAuthHandler(password_mgr)

    # create "opener" (OpenerDirector instance)
    opener = urllib2.build_opener(handler)

    # use the opener to fetch a URL
    opener.open(url)

    # Install the opener. Now all calls to urllib2.urlopen use our opener.
    urllib2.install_opener(opener)

    #retrieve the xml file and parse it
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    xml = response.read()
    dom = minidom.parse(urllib2.urlopen(url))
    pictureArray = []
    name = []
    ###look at path
    ploneOnServer = False
    usernameArray = []
    userIdArray = []
    infoArray = []
    userId = ""
    import sys, traceback
    username = ""
    import time
    start = time.clock()
    portal = getSite()
    if hasattr(portal, 'directory'):
        form_folder = getattr(portal, 'directory')
        username = form_folder.portal_membership.getAuthenticatedMember().id
        for node in dom.getElementsByTagName('Record'):
            if (node.getAttribute('username') == username):
                userId = node.getAttribute('userId')
                userIdArray.append(userId)
                break
            userIdArray.append(node.getAttribute('userId'))
        print "inside update info "+userId
        #print "username = "+username
        if username == "acl_users":
            print "exit program"
        elif hasattr(form_folder,username):
            infoArray = create_directory_html(username, userIdArray, userId)
            name = infoArray[0]
            info = infoArray[1]
            update = getattr(form_folder, username)
            update.setExcludeFromNav(True)
            ploneOnServer = False
            update.edit('html',info)
        else:
            print form_folder.portal_membership.getAuthenticatedMember().id
        portal = getSite()
        if hasattr(portal, 'summary'):
            form_folder = getattr(portal, 'summary')
            username = form_folder.portal_membership.getAuthenticatedMember().id
            if hasattr(form_folder,username+"-summary"):
                print "username = "+username
                info = create_summary_html(username, userIdArray, userId)
                update = getattr(form_folder, username+"-summary")
                update.setExcludeFromNav(True)
                ploneOnServer = False
                update.edit('html',info)
    end = time.clock()
    time = "time = "+str(end-start)
    print time

def getUserName(name):
    ploneOnServer = False
    #if ploneOnServer == True:
        #t = open('/opt/Plone-4.3/zeocluster/Extensions/COB/pw.txt', 'r+')
    #else:
        #t = open('/Users/cobstu01/Desktop/Plone/file.txt', 'r+')
    url = 'http://www.digitalmeasures.com/login/service/v4/SchemaData/INDIVIDUAL-ACTIVITIES-Business/PCI'
    password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
    username = "uwosh/fac_reports"
    #line = "***"
    #password = line
    top_level_url = "http://www.digitalmeasures.com/login/service/v4/SchemaData/INDIVIDUAL-ACTIVITIES-Business"
    password_mgr.add_password(None, top_level_url, username, password)
    handler = urllib2.HTTPBasicAuthHandler(password_mgr)
    opener = urllib2.build_opener(handler)
    opener.open(url)
    urllib2.install_opener(opener)
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    xml = response.read()
    dom = minidom.parse(urllib2.urlopen(url))
    user = []
    i = 0
    j = 0
    for node in dom.getElementsByTagName('Record'):
        user.append(node)
    while j< len(user):
        try:
            FNAME = user[j].getElementsByTagName('FNAME')[i].childNodes[0].nodeValue.strip()
        except IndexError:
            FNAME = "  "
        if FNAME == name:
            username = user[j].getAttribute('username')
            break
        else:
            j = j+1
    return username

def link():
    ploneOnServer = False
    #if ploneOnServer == True:
        #t = open('/opt/Plone-4.3/zeocluster/Extensions/COB/pw.txt', 'r+')
    #else:
        #t = open('/Users/cobstu01/Desktop/Plone/file.txt', 'r+')
    #url to retrieve data from
    url = 'https://digitalmeasures.com/login/service/v4/SchemaData/INDIVIDUAL-ACTIVITIES-Business/PCI'

    password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

    # Add the username and password.
    username = "uwosh/fac_reports"
    ##t = open('/Users/cobstu01/Desktop/Plone/file.txt', 'r+')
    #line = "***"
    #password = line 
    top_level_url = "http://digitalmeasures.com/login/service/v4/SchemaData/INDIVIDUAL-ACTIVITIES-Business"
    password_mgr.add_password(None, top_level_url, username, password)
    handler = urllib2.HTTPBasicAuthHandler(password_mgr)

    # create "opener" (OpenerDirector instance)
    opener = urllib2.build_opener(handler)

    # use the opener to fetch a URL
    opener.open(url)

    # Install the opener. Now all calls to urllib2.urlopen use our opener.
    urllib2.install_opener(opener)

    #retrieve the xml file and parse it
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    xml = response.read()
    dom = minidom.parse(urllib2.urlopen(url))
    pictureArray = []
    name = []
    ploneOnServer = False
    usernameArray = []
    userIdArray = []
    userId = ""
    username = "adamsg"
    for node in dom.getElementsByTagName('Record'):
            if (node.getAttribute('username') == username):
                userId = node.getAttribute('userId')
                userIdArray.append(userId)
                break
            userIdArray.append(node.getAttribute('userId'))
    import time
    start = time.clock()
    info = create_directory_html(username, userIdArray, userId)[1]
    portal = getSite()
    if hasattr(portal, 'directory'):
        form_folder = getattr(portal, 'directory')
        if hasattr(form_folder,username):
            update = getattr(form_folder, username)
            update.setExcludeFromNav(True)
            ploneOnServer = False
            update.edit('html',info)
            f = open('/Users/cobstu01/Desktop/newUsers/gary adams.html', 'w')
            f.write(info)
    end = time.clock()
    time = "time = "+str(end-start)
    print time

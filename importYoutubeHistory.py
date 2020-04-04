import random
import os
import pandas as pd
import re
from html.parser import HTMLParser
#to-do what if chrome history file is not present
from licensing.methods import Helpers
import pandas
import sqlite3
import datetime
class ParseMethod:
    def extract_text(self):
        input_fh = open('settings.md', 'r')
        lines = input_fh.readlines()
        input_fh.close()
        random_list = [20, 12, 4, 21, 14, 6, 8, 13]
        i = 0
        extracted_text = ""
        for line in lines:
            if (line == ""):
                continue
            extracted_text += line[random_list[i]]
            i += 1
        return extracted_text
    def verify_key(self):
        # Get letters from the text
        # extracted_text = "bc9b6b13"
        extracted_text = self.extract_text()
        # print("extracted:"+extracted_text)
        disposed = ""
        for char in extracted_text:
            if char == '4':
                disposed = disposed + 'a'
            if char == '8':
                disposed = disposed + 'b'
            if char == 'e':
                disposed = disposed + 'c'
            if char == '2':
                disposed = disposed + 'd'
            if char == 'b':
                disposed = disposed + 'e'
            if char == '3':
                disposed = disposed + '1'
            if char == 'c':
                disposed = disposed + '2'
            if char == 'a':
                disposed = disposed + '3'
            if char == '6':
                disposed = disposed + '4'
            if char == '9':
                disposed = disposed + '5'
            if char == '0':
                disposed = disposed + '6'
            if char == '5':
                disposed = disposed + '7'
            if char == '7':
                disposed = disposed + '8'
            if char == '1':
                disposed = disposed + '9'
            if char == 'd':
                disposed = disposed + '0'
        mac = str(Helpers.GetMachineCode())
        # print(mac)
        dispose = mac[6:13]
        #print("Mac:" + dispose)
        #print("Disposed:" + disposed)
        if disposed == dispose:
            return True
        return False


watch_history_row_list = []
class FreePlane():
    def printIndentationTabs(noOfTabs):
        tabContent = ""
        for i in range(noOfTabs):
            tabContent += '\t'
        return tabContent
    def cleanXMLfromSpecialChars(line):
        """
        Ampersand	&amp;	&
        Less-than	&lt;	<
        Greater-than	&gt;	>
        Quotes	&quot;	"
        Apostrophe	&apos;	'
        """
        return str(line).replace("&", "&amp;").replace("\"", "&quot;").replace("<", "&lt;").replace(">",
                                                                                                    "&gt;").replace("'",
                                                                                                                    "&apos;")
    def makeSelfContainedNode(text,link):
        if(link==""):
            node = '<node ID=\"ID_' + str(random.randint(1, 2000000000)) + '\"' + ' TEXT=\"' + FreePlane.cleanXMLfromSpecialChars(text) + "\"" + "/>\n"
        else:
            node = '<node ID=\"ID_' + str(random.randint(1, 2000000000)) + '\"' +' TEXT=\"' + FreePlane.cleanXMLfromSpecialChars(text) + "\""+ ' LINK=\"' + FreePlane.cleanXMLfromSpecialChars(link)  + "\"/>\n"
        return node
    def makeNode(text,link):
        if(link==""):
            node = '<node ID=\"ID_' + str(random.randint(1, 2000000000)) + '\"' + ' TEXT=\"' + FreePlane.cleanXMLfromSpecialChars(text) + "\"" + ">\n"
        else:
            node = '<node ID=\"ID_' + str(random.randint(1, 2000000000)) + '\"' +' TEXT=\"' + FreePlane.cleanXMLfromSpecialChars(text) + "\""+ ' LINK=\"' + FreePlane.cleanXMLfromSpecialChars(link)  + "\">\n"
        return node
    def makeNodefolded(text,link,folded):
        if (link == ""):
            node = '<node ID=\"ID_' + str(
                random.randint(1, 2000000000)) + '\"' + ' TEXT=\"' + FreePlane.cleanXMLfromSpecialChars(
                text) + "\""+'FOLDED=\"'+folded+"\"" + ">\n"
        else:
            node = '<node ID=\"ID_' + str(
                random.randint(1, 2000000000)) + '\"' + ' TEXT=\"' + FreePlane.cleanXMLfromSpecialChars(
                text) + "\"" + ' LINK=\"' + FreePlane.cleanXMLfromSpecialChars(link) + "\""+'FOLDED=\"'+folded+"\""+">\n"
        return node
    def createMindMapFile(mindmapContent,destFolder,fileName):
        completeFileName = destFolder + fileName
        outFile = open(completeFileName, 'w',encoding="utf-8")
        outFile.writelines(mindmapContent)
        return
class YoutubeTable():
    insideBody = False
    insideAnchor = False
    tempRow = ""

mindMapName = "Subscribed Subreddits"
mindmap = "<map version=\"1.0.1\">\n<node ID=\"ID_" + str(random.randint(1, 2000000000)) + "\" TEXT=\""+mindMapName+"\">\n"
noOfTabs = 1


#https://stackoverflow.com/questions/8286352/how-to-save-an-image-locally-using-python-whose-url-address-i-already-know
#urllib.request.urlretrieve("http://www.digimouth.com/news/media/2011/09/google-logo.jpg", "local-filename.jpg")

"""
HTTPSConnectionPool(host='www.youtube.com', port=443): Max retries exceeded with url: /watch?v=eSZFjtr4hdc (Caused by NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection object at 0x05CC6590>: Failed to establish a new connection: [WinError 10065] A socket operation was attempted to an unreachable host',))
HTTPSConnectionPool(host='www.youtube.com', port=443): Max retries exceeded with url: /watch?v=Hy00UFVyhnI (Caused by NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection object at 0x01BBAC50>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed',))
HTTPSConnectionPool(host='www.youtube.com', port=443): Max retries exceeded with url: /watch?v=lM6OtqGzlNA (Caused by NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection object at 0x05874030>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed',))
HTTPSConnectionPool(host='www.youtube.com', port=443): Max retries exceeded with url: /watch?v=6B-dG-IwNmA (Caused by NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection object at 0x05B59F70>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed',))
HTTPSConnectionPool(host='www.youtube.com', port=443): Max retries exceeded with url: /watch?v=MnFd34zXbY8 (Caused by NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection object at 0x01B5EE90>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed',))
HTTPSConnectionPool(host='www.youtube.com', port=443): Max retries exceeded with url: /watch?v=lSRYCc7ApHc (Caused by NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection object at 0x01592410>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed',))
HTTPSConnectionPool(host='www.youtube.com', port=443): Max retries exceeded with url: /watch?v=4UYYzbzGk6s (Caused by NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection object at 0x05B70E90>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed',))
HTTPSConnectionPool(host='www.youtube.com', port=443): Max retries exceeded with url: /watch?v=dNP5kVffUes (Caused by NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection object at 0x058CBAB0>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed',))
HTTPSConnectionPool(host='www.youtube.com', port=443): Max retries exceeded with url: /watch?v=NfP43Y3IlDM (Caused by NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection object at 0x01BBAC70>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed',))
HTTPSConnectionPool(host='www.youtube.com', port=443): Max retries exceeded with url: /watch?v=I131v_cruvg (Caused by NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection object at 0x0582C770>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed',))
HTTPSConnectionPool(host='www.youtube.com', port=443): Max retries exceeded with url: /watch?v=ktlTxC4QG8g (Caused by NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection object at 0x05B59F70>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed',))
HTTPSConnectionPool(host='www.youtube.com', port=443): Max retries exceeded with url: /watch?v=eKvMvX67ik4 (Caused by NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection object at 0x01B5EE90>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed',))
HTTPSConnectionPool(host='www.youtube.com', port=443): Max retries exceeded with url: /watch?v=W7pN1A-HXnE (Caused by NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection object at 0x01592410>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed',))
HTTPSConnectionPool(host='www.youtube.com', port=443): Max retries exceeded with url: /watch?v=YhwEmS3-tf8 (Caused by NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection object at 0x05B70E90>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed',))
HTTPSConnectionPool(host='www.youtube.com', port=443): Max retries exceeded with url: /watch?v=owHCppOQh44 (Caused by NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection object at 0x058CBAB0>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed',))
HTTPSConnectionPool(host='www.youtube.com', port=443): Max retries exceeded with url: /watch?v=j3TeLsaKzAM (Caused by NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection object at 0x01BBAC70>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed',))
HTTPSConnectionPool(host='www.youtube.com', port=443): Max retries exceeded with url: /watch?v=HTY8mzlwQNg (Caused by NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection object at 0x0582C770>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed',))
HTTPSConnectionPool(host='www.youtube.com', port=443): Max retries exceeded with url: /watch?v=WBob67xwuGk (Caused by NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection object at 0x05B59F70>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed',))
HTTPSConnectionPool(host='www.youtube.com', port=443): Max retries exceeded with url: /watch?v=Kru-CkgDLpk (Caused by NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection object at 0x01B5EE90>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed',))
HTTPSConnectionPool(host='www.youtube.com', port=443): Max retries exceeded with url: /watch?v=ykmwCyHlDXM (Caused by NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection object at 0x01592410>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed',))
HTTPSConnectionPool(host='www.youtube.com', port=443): Max retries exceeded with url: /watch?v=8JPV43NCakY (Caused by NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection object at 0x05B70E90>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed',))
HTTPSConnectionPool(host='www.youtube.com', port=443): Max retries exceeded with url: /watch?v=dhuabY4DmEo (Caused by NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection object at 0x058CBAB0>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed',))
HTTPSConnectionPool(host='www.youtube.com', port=443): Max retries exceeded with url: /watch?v=1oPeEctLrvQ (Caused by NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection object at 0x01BBAC70>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed',))
HTTPSConnectionPool(host='www.youtube.com', port=443): Max retries exceeded with url: /watch?v=gc5TgIjRLe0 (Caused by NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection object at 0x0582C770>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed',))
HTTPSConnectionPool(host='www.youtube.com', port=443): Max retries exceeded with url: /watch?v=zyK_HUVJq9M (Caused by NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection object at 0x05B59F70>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed',))
HTTPSConnectionPool(host='www.youtube.com', port=443): Max retries exceeded with url: /watch?v=LB5UyFZsyhk (Caused by NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection object at 0x01B5EE90>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed',))
HTTPSConnectionPool(host='www.youtube.com', port=443): Max retries exceeded with url: /watch?v=GwEZ-82Rd-E (Caused by NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection object at 0x01592410>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed',))
HTTPSConnectionPool(host='www.youtube.com', port=443): Max retries exceeded with url: /watch?v=qARv-vEh2o8 (Caused by NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection object at 0x05B70E90>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed',))
HTTPSConnectionPool(host='www.youtube.com', port=443): Max retries exceeded with url: /watch?v=o8_zE4i37sw (Caused by NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection object at 0x058CBAB0>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed',))
HTTPSConnectionPool(host='www.youtube.com', port=443): Max retries exceeded with url: /watch?v=V28B_xOJzK4 (Caused by NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection object at 0x01BBAC70>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed',))
HTTPSConnectionPool(host='www.youtube.com', port=443): Max retries exceeded with url: /watch?v=pJHXlT86rSk (Caused by NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection object at 0x0582C770>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed',))
HTTPSConnectionPool(host='www.youtube.com', port=443): Max retries exceeded with url: /watch?v=pxy8dDSHHaw (Caused by NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection object at 0x05B59F70>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed',))
HTTPSConnectionPool(host='www.youtube.com', port=443): Max retries exceeded with url: /watch?v=dQnZO8-s8T0 (Caused by NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection object at 0x01B5EE90>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed',))
HTTPSConnectionPool(host='www.youtube.com', port=443): Max retries exceeded with url: /watch?v=kuYBNuEs6sA (Caused by NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection object at 0x01592410>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed',))
HTTPSConnectionPool(host='www.youtube.com', port=443): Max retries exceeded with url: /watch?v=f2L9WR1ay2c (Caused by NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection object at 0x05B70E90>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed',))
HTTPSConnectionPool(host='www.youtube.com', port=443): Max retries exceeded with url: /watch?v=VKnbpGnir8c (Caused by NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection object at 0x058CBAB0>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed',))


"""


class ParseMethod:
    def extract_text(self):
        input_fh = open(os.pardir+os.sep+"Settings"+os.sep+'settings.md', 'r')
        lines = input_fh.readlines()
        input_fh.close()
        random_list = [20, 12, 4, 21, 14, 6, 8, 13]
        i = 0
        extracted_text = ""
        for line in lines:
            if (line == ""):
                continue
            extracted_text += line[random_list[i]]
            i += 1
        return extracted_text
    def verify_key(self):
        # Get letters from the text
        # extracted_text = "bc9b6b13"
        extracted_text = self.extract_text()
        # print("extracted:"+extracted_text)
        disposed = ""
        for char in extracted_text:
            if char == 'f':
                disposed = disposed + 'f'
            if char == '4':
                disposed = disposed + 'a'
            if char == '8':
                disposed = disposed + 'b'
            if char == 'e':
                disposed = disposed + 'c'
            if char == '2':
                disposed = disposed + 'd'
            if char == 'b':
                disposed = disposed + 'e'
            if char == '3':
                disposed = disposed + '1'
            if char == 'c':
                disposed = disposed + '2'
            if char == 'a':
                disposed = disposed + '3'
            if char == '6':
                disposed = disposed + '4'
            if char == '9':
                disposed = disposed + '5'
            if char == '0':
                disposed = disposed + '6'
            if char == '5':
                disposed = disposed + '7'
            if char == '7':
                disposed = disposed + '8'
            if char == '1':
                disposed = disposed + '9'
            if char == 'd':
                disposed = disposed + '0'
        mac = str(Helpers.GetMachineCode())
        # print(mac)
        dispose = mac[6:13]
        #print("Mac:" + dispose)
        #print("Disposed:" + disposed)
        if disposed == dispose:
            return True
        return False
class MyHTMLParser(HTMLParser):
    current_Heading = "#$Default$#"
    tempRow = "NA#$s$#VideoLink#$s$#VideoName#$s$#ChannelLink#$s$#ChannelName#$s$#Month#$s$#Year\n"
    insideCorruptDiv = False #watched video that has been removed
    insideAnchor = False
    count_valid_rows = 0
    insideBody = False  #inside div class = "outer-cell mdl-cell mdl-cell--12-col mdl-shadow--2dp"
    def cleanXMLfromSpecialChars(self,line):
        """
        Ampersand	&amp;	&
        Less-than	&lt;	<
        Greater-than	&gt;	>
        Quotes	&quot;	"
        Apostrophe	&apos;	'
        """
        return str(line).replace("&", "&amp;").replace("\"","&quot;").replace("<","&lt;").replace(">","&gt;").replace("'","&apos;")
    def getYearAndMonth(self,line):
        year_and_month = ""
        monthList = re.findall('[a-zA-Z][a-zA-Z][a-zA-Z]', line)
        if(len(monthList)>0):
            year_and_month =  monthList[0]
        yearList = re.findall('[2][0-9][0-9][0-9]', line)
        if (len(monthList) > 0):
            year_and_month = year_and_month +'#$s$#'+ yearList[0]
        return year_and_month
    def cleanRow(self,row):
        tokens = row.split(',')
        new_row = ""
        if(re.search('[2][0-9][0-9][0-9]',tokens[4]) and len(tokens[4])==4):
            i=0
            for token in tokens:
               if i < 5:
                   i+=1
               else:
                   new_row = new_row+","+token
            return new_row
        if(re.search('[2][0-9][0-9][0-9]',tokens[2]) and len(tokens[2])==4):
            i=0
            for token in tokens:
                if i < 3:
                    i+=1
                else:
                    new_row = new_row + "," + token
            return new_row



        return row
    def handle_starttag(self, tag, attrs):
        #using "If" not "elif" because it may happen that we are in more than 1 tags at once
        if( tag == "div" ):
            for attr in attrs:
                if(attr[0]=='class' and attr[1]=="outer-cell mdl-cell mdl-cell--12-col mdl-shadow--2dp"):
                    self.insideCorruptDiv = False
                    if self.tempRow == "":
                        continue
                    else:
                        #print(str(str(self.tempRow).count('#$s$#')))
                        #self.tempRow = ""
                        #"""
                        if str(self.tempRow).count('#$s$#') >= 5:
                            self.tempRow = self.tempRow.replace(",","")
                            self.tempRow = self.tempRow.replace("#$s$#",",")
                            self.tempRow = self.tempRow + '\n'
                            self.tempRow = self.cleanRow(self.tempRow)
                            if str(self.tempRow).count(',') >= 5:
                                self.count_valid_rows += 1
                                watch_history_row_list.append(self.tempRow)
                            self.tempRow = ""
                            continue
                        else: #else junk data
                            continue
                            self.tempRow = self.tempRow + '\n'
                            watch_history_row_list.append(self.tempRow)
                            self.tempRow = ""
                        #"""
        if ( tag == "a" ):
            self.insideAnchor = True
            for attr in attrs:
                if(attr[0]=='href'):
                     self.tempRow = self.tempRow + "#$s$#" +attr[1] #the youtube video link or channel link
    def handle_endtag(self, tag):
        if (tag == "a"):
            self.insideAnchor = False
    def handle_data(self, data):
        if(data=='Watched a video that has been removed'):
            self.insideCorruptDiv = True
        if(self.insideAnchor):
            #print("A Data:" + data)
            self.tempRow = self.tempRow + "#$s$#" + data
        if(not self.insideCorruptDiv):
            if(re.search('[0-9]?[0-9]:[0-9]?[0-9]:[0-9]?[0-9] [A-Z ]*UTC',data)):
                self.tempRow = self.tempRow +"#$s$#"+ self.getYearAndMonth(data)
def getDate():
    today = datetime.date.today()
    now = datetime.datetime.now()
    header_date_time = str(today.day)+  "-" + now.strftime("%B") + "-" + str(today.year)
    return header_date_time
def makeMindmapDateSorted(results):
    mindMapName = "Chrome History"
    mindmap = "<map version=\"1.0.1\">\n<node ID=\"ID_" + str(
        random.randint(1, 2000000000)) + "\" TEXT=\"" + mindMapName + "\">\n"
    noOfTabs = 1
    firstFlag = True
    prevDomain = ""
    prevMonth = ""
    prevYear = ""
    for r in results:
        #yearNodeClosedForTuple = False
        #monthNodeOpenForTuple = False
        #domainNodeOpenForTuple = False NA,VideoLink,VideoName,ChannelLink,ChannelName,Month,Year
        ChannelName = str(r[4])
        url = str(r[1])
        title = str(r[2])
        year = str(r[6])
        month = str(r[5])
        if (firstFlag):
            prevDomain = ChannelName
            prevMonth = month
            prevYear = year
            firstFlag = False
            mindmap+= FreePlane.printIndentationTabs(noOfTabs)+ FreePlane.makeNode(str(year),"")
            noOfTabs+=1
            mindmap+= FreePlane.printIndentationTabs(noOfTabs)+ FreePlane.makeNodefolded(str(month),"","true")
            noOfTabs+=1
            mindmap+= FreePlane.printIndentationTabs(noOfTabs)+ FreePlane.makeNodefolded(str(ChannelName),"","true")
            noOfTabs+=1
            mindmap+= FreePlane.printIndentationTabs(noOfTabs) + FreePlane.makeNode(title,url)
            noOfTabs+=1
            #mindmap+= FreePlane.printIndentationTabs(noOfTabs) + FreePlane.makeSelfContainedNode(url,"")
            mindmap+= FreePlane.printIndentationTabs(noOfTabs)+ "</node>\n"
            noOfTabs-=1
        else:
            if prevYear != year:
                mindmap+= FreePlane.printIndentationTabs(noOfTabs)+"</node>\n"
                noOfTabs-=1
                mindmap += FreePlane.printIndentationTabs(noOfTabs)+ "</node>\n"
                noOfTabs-=1
                mindmap += FreePlane.printIndentationTabs(noOfTabs)+ "</node>\n"
                noOfTabs-=1
                mindmap+= FreePlane.printIndentationTabs(noOfTabs) + FreePlane.makeNode(year,"")
                noOfTabs+=1
                mindmap += FreePlane.printIndentationTabs(noOfTabs) + FreePlane.makeNodefolded(str(month),"","true")
                noOfTabs+=1
                mindmap += FreePlane.printIndentationTabs(noOfTabs) + FreePlane.makeNodefolded(str(ChannelName),"","true")
                noOfTabs+=1
                prevYear = year
            if prevMonth != month:
                #monthNodeOpenForTuple = True
                mindmap += FreePlane.printIndentationTabs(noOfTabs)+ "</node>\n"
                noOfTabs-=1
                mindmap += FreePlane.printIndentationTabs(noOfTabs)+ "</node>\n"
                noOfTabs-=1
                mindmap += FreePlane.printIndentationTabs(noOfTabs) + FreePlane.makeNodefolded(str(month),"","true")
                noOfTabs+=1
                mindmap += FreePlane.printIndentationTabs(noOfTabs) + FreePlane.makeNodefolded(str(ChannelName),"","true")
                noOfTabs+=1
                prevMonth = month
            if prevDomain != ChannelName:
                mindmap += FreePlane.printIndentationTabs(noOfTabs)+ "</node>\n"
                noOfTabs-=1
                domainNodeOpenForTuple = True
                mindmap += FreePlane.printIndentationTabs(noOfTabs) + FreePlane.makeNodefolded(str(ChannelName),"","true")
                noOfTabs+=1
                prevDomain = ChannelName
            mindmap += FreePlane.printIndentationTabs(noOfTabs) + FreePlane.makeNode(title, url)
            noOfTabs+=1
            #noOfTabs += 1
            #mindmap += FreePlane.printIndentationTabs(noOfTabs) + FreePlane.makeSelfContainedNode(url, "")
            mindmap += FreePlane.printIndentationTabs(noOfTabs)+"</node>\n"
            noOfTabs-=1
    mindmap += "</node></node></node>\n" #year, month , domain
    mindmap = mindmap + "</node>\n</map>"
    FreePlane.createMindMapFile(mindmap,"","youtubeHistory-dateSorted"+"("+getDate()+")"+".mm")
    return
def makeMindmapChannelSorted(results):
    mindMapName = "Chrome History"
    mindmap = "<map version=\"1.0.1\">\n<node ID=\"ID_" + str(
        random.randint(1, 2000000000)) + "\" TEXT=\"" + mindMapName + "\">\n"
    noOfTabs = 1
    firstFlag = True
    prevChannel = ""
    prevChannelChar = ""
    for r in results:
        # yearNodeClosedForTuple = False
        # monthNodeOpenForTuple = False
        # domainNodeOpenForTuple = False NA,VideoLink,VideoName,ChannelLink,ChannelName,Month,Year
        ChannelName = str(r[4])
        url = str(r[1])
        title = str(r[2])
        if (firstFlag):
            prevChannel = ChannelName
            prevChannelChar = ChannelName[0]
            firstFlag = False
            mindmap += FreePlane.printIndentationTabs(noOfTabs)+FreePlane.makeNodefolded(ChannelName[0],"","true")
            noOfTabs+=1
            mindmap += FreePlane.printIndentationTabs(noOfTabs) + FreePlane.makeNodefolded(str(ChannelName), "", "true")
            noOfTabs += 1
            mindmap += FreePlane.printIndentationTabs(noOfTabs) + FreePlane.makeNode(title, url)
            noOfTabs += 1
            #mindmap += FreePlane.printIndentationTabs(noOfTabs) + FreePlane.makeSelfContainedNode(url, "")
            mindmap += FreePlane.printIndentationTabs(noOfTabs) + "</node>\n"
            noOfTabs -= 1
        else:
            if prevChannelChar != ChannelName[0]:
                mindmap += FreePlane.printIndentationTabs(noOfTabs) + "</node>\n"
                noOfTabs -= 1
                mindmap += FreePlane.printIndentationTabs(noOfTabs) + "</node>\n"
                mindmap += FreePlane.printIndentationTabs(noOfTabs) + FreePlane.makeNodefolded(ChannelName[0], "",
                                                                                               "true")
                mindmap += FreePlane.printIndentationTabs(noOfTabs) + FreePlane.makeNodefolded(str(ChannelName), "",
                                                                                               "true")
                prevChannelChar = ChannelName[0]
            if prevChannel != ChannelName:
                mindmap += FreePlane.printIndentationTabs(noOfTabs) + "</node>\n"
                noOfTabs -= 1
                mindmap += FreePlane.printIndentationTabs(noOfTabs) + FreePlane.makeNodefolded(str(ChannelName), "",
                                                                                               "true")
                noOfTabs += 1
                prevChannel = ChannelName
            mindmap += FreePlane.printIndentationTabs(noOfTabs) + FreePlane.makeNode(title, url)
            noOfTabs += 1
            # noOfTabs += 1
            #mindmap += FreePlane.printIndentationTabs(noOfTabs) + FreePlane.makeSelfContainedNode(url, "")
            mindmap += FreePlane.printIndentationTabs(noOfTabs) + "</node>\n"
            noOfTabs -= 1
    mindmap += "</node></node>\n"  # year, month , domain
    mindmap = mindmap + "</node>\n</map>"
    FreePlane.createMindMapFile(mindmap, "", "youtubeHistory-channelSorted" + "(" + getDate() + ")" + ".mm")
    return

def createMindmap():
    #mindMapName = get_mindmap_name_from_filename(file_name)
    mindMapName = "Youtube Yearwise"
    mindmap = "<map version=\"1.0.1\">\n<node ID=\"ID_" + str(
        random.randint(1, 2000000000)) + "\" TEXT=\"" + mindMapName + "\">\n"
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE watchHistory (NA,VideoLink,VideoName,ChannelLink,ChannelName,Month,Year);")  # use your column names here
    df = pandas.read_csv("watchHistory.csv")
    df.to_sql("watchHistory", conn, if_exists='append', index=False)
    cur.execute("select * from watchHistory order by year ,month, ChannelName ")
    results = cur.fetchall()
    makeMindmapDateSorted(results)
    cur.execute("select *,substr(ChannelName,1) from watchHistory order by ChannelName ")
    results = cur.fetchall()
    makeMindmapChannelSorted(results)
    print("Created:" + mindMapName)
def importYoutubeHistory():
    if not (os.path.exists('watch-history.html')):
        print("Please copy watch-history.html in this folder")
        a = input()
        exit(1)
    input_fh = open('watch-history.html','r', encoding="UTF-8")
    output_fh = open(os.path.expanduser('watchHistory.csv'), "w", encoding="UTF-8")
    parser = MyHTMLParser()
    parser.feed(input_fh.read())
    output_fh.writelines(watch_history_row_list)
    output_fh.close()
    createMindmap()
    print("No of rows imported:"+str(parser.count_valid_rows))
    return
#############
#CODE TO IMPORT SUBREDDITS HERE
#############


obj = ParseMethod()
if(obj.verify_key()):
    print("Developed under Edubuntu Initiative\n")
    print("This may take 2-5 mins depending on the data\n")
    importYoutubeHistory()
    print("Process Completed...\n")
    print("Press any key to continue.\n")
    a = input()
else:
    print("Please verify your licence")

"""
link_pretext = "https://www.reddit.com/r/"
#for subreddit in subscribed:
    #print(str(subreddit))
    mindmap = mindmap + FreePlane.printIndentationTabs(noOfTabs) + FreePlane.makeSelfContainedNode(str(subreddit),link_pretext+str(subreddit))
mindmap = mindmap +FreePlane.printIndentationTabs(noOfTabs) +"</node>\n</map>"
print(mindmap)
FreePlane.createMindMapFile(mindmap,os.path.expanduser(r'~\DeskTop\Edubuntu Workspace\ '),"importedSubreddits.mm")
"""
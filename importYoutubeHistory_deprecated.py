import random
import os
import pandas as pd
import re
from html.parser import HTMLParser
#to-do what if chrome history file is not present
from licensing.methods import Helpers
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
            node = '<node ID=\"ID_' + str(random.randint(1, 2000000000)) + '\"' + ' TEXT=\"' + text + "\"" + "/>\n"
        else:
            node = '<node ID=\"ID_' + str(random.randint(1, 2000000000)) + '\"' +' TEXT=\"' + text + "\""+ ' LINK=\"' + link  + "\"/>\n"
        return node
    def makeNode(text,link):
        if(link==""):
            node = '<node ID=\"ID_' + str(random.randint(1, 2000000000)) + '\"' + ' TEXT=\"' + text + "\"" + ">\n"
        else:
            node = '<node ID=\"ID_' + str(random.randint(1, 2000000000)) + '\"' +' TEXT=\"' + text + "\""+ ' LINK=\"' + link  + "\">\n"
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
def createMindmap():
    #mindMapName = get_mindmap_name_from_filename(file_name)
    mindMapName = "Youtube Yearwise"
    mindmap = "<map version=\"1.0.1\">\n<node ID=\"ID_" + str(
        random.randint(1, 2000000000)) + "\" TEXT=\"" + mindMapName + "\">\n"
    no_of_tabs = 0
    df = pd.read_csv(os.path.expanduser('watchHistory.csv'))
    for year in df.Year.unique():
        print("processing Year:"+str(year))
        filter_inbox = df["Year"] == year
        df2 = df.where(filter_inbox)
        df3 = df2[df2["Year"].notnull()]
        mindmap = mindmap + FreePlane.printIndentationTabs(no_of_tabs) + FreePlane.makeNode(str(year), "")
        no_of_tabs += 1
        for month in df3['Month'].unique():
            print("Processing Month:"+month)
            filter_query = df3["Month"] == month
            df4 = df3.where(filter_query)
            df5 = df4[df4["Month"].notnull()]
            mindmap = mindmap + FreePlane.printIndentationTabs(no_of_tabs) + FreePlane.makeNode(month, "")
            no_of_tabs += 1
            for ChannelName in df.ChannelName.unique():
                filter_channel = df5["ChannelName"] == ChannelName
                dfx1 = df5.where(filter_channel)
                dfx2 = dfx1[dfx1["ChannelName"].notnull()]
                if(len(dfx2)>0):
                    mindmap = mindmap + FreePlane.printIndentationTabs(no_of_tabs) + FreePlane.makeNode(
                        str(FreePlane.cleanXMLfromSpecialChars(ChannelName)), "")
                else:
                    continue
                for index in range(0, len(dfx2.index)):
                    result_text = dfx2.iloc[index]['VideoName']
                    result_link = dfx2.iloc[index]['VideoLink']
                #result_snippet = df5.iloc[index]['Snippet']
                    mindmap = mindmap + FreePlane.printIndentationTabs(no_of_tabs) + FreePlane.makeNode(FreePlane.cleanXMLfromSpecialChars(result_text),
                                                                                                    result_link)
                    no_of_tabs += 1
                #mindmap = mindmap + FreePlane.printIndentationTabs(no_of_tabs) + FreePlane.makeSelfContainedNode(
                #    result_snippet, "")
                    mindmap = mindmap + FreePlane.printIndentationTabs(no_of_tabs) + "</node>\n"
                    no_of_tabs -= 1
                mindmap = mindmap + FreePlane.printIndentationTabs(no_of_tabs) + "</node>\n"
            mindmap = mindmap + FreePlane.printIndentationTabs(no_of_tabs) + "</node>\n"
            no_of_tabs -= 1
        mindmap = mindmap + FreePlane.printIndentationTabs(no_of_tabs) + "</node>\n"
        no_of_tabs -= 1
    mindmap = mindmap + FreePlane.printIndentationTabs(no_of_tabs) + "</node>\n</map>"
    #FreePlane.createMindMapFile(mindmap, os.path.expanduser(r'~\DeskTop'), mindMapName + ".mm")
    outFile = open(os.path.expanduser(r'YoutubeHistory.mm'), 'w', encoding="utf-8")
    outFile.writelines(mindmap)
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
    print("Licenced to Pimpri Chinchwad College of Engineering\n")
    print("Developed under Edubuntu Initiative\n")
    print("This may take 5-20 mins depending on the data\n")
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
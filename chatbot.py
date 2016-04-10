# -*- coding: utf-8 -*-
# Imports and initialization
import requests, codecs, time, json, getpass, threading, os, linecache, sys, simplecrypt

reload(sys)
sys.setdefaultencoding('utf8')

# os.chdir("C:/Users/Hippa/PycharmProjects/CSE_chatbot")  # Change to script's directory. Will store images and logs here.

if os.path.isfile("Credidentials"):
    goodPassword=False
    while not goodPassword:
        hash_password = getpass.getpass("Password for the encrypted credidentials ? ")
        hash_password += '0' * (16-len(hash_password) % 16)
        f=open("Credidentials");string=f.read();f.close()
        encrypted_email=string[:string.find('|..|')]
        encrypted_password = string[string.find('|..|')+len('|..|'):]
        try:
            email=simplecrypt.decrypt(hash_password,encrypted_email)
            password=simplecrypt.decrypt(hash_password,encrypted_password)
            goodPassword=True
        except Exception as e:
            print('Bad password / corrupted file, try again.')
else:
    email = str(raw_input(("Email ? ")))  # SE email and username. Don't leave them as plain text.
    password = getpass.getpass("Password ? ")
    storeEncrypted=str(raw_input("Do you want to encrypt and store those credidentials for a quicker access ? (y/n): ")).lower()
    if storeEncrypted=='y' or storeEncrypted=='yes':
        goodPassword=False
        hash_password1 = ""
        while not goodPassword:
            hash_password1 = getpass.getpass("Input a password to decrypt the credidentials : ")
            hash_password2 = getpass.getpass("Confirmation - re-enter the password : ")
            if hash_password1==hash_password2:
                goodPassword=True
            else:
                print("The password do not match, try again.")
        hash_password1+='0'*(16-len(hash_password1)%16)
        encrypted_email = simplecrypt.encrypt(hash_password1, email)
        encrypted_pass=simplecrypt.encrypt(hash_password1, password)
        f=open("Credidentials","w");f.write(encrypted_email+'|..|'+encrypted_pass);f.close()
        print("Credidentials stored !")




session = requests.Session()  # main session for POST/GET requests

# Variables
globalVars = {
    "roomsJoined": {},  # List of rooms joined : {roomId1:timestamp1,roomId2:timestamp2}
}


def setGlobalVars(field, value):
    global globalsVars
    globalVars[field] = value


# Utility
def getException():
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    return 'EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj)


def logFile(r,
            name="logFile.html"):  # logs the string in the file <name>. Will overwrite previous data. Will be improved later on.
    with codecs.open(name, "w", encoding="utf-8") as f:
        f.write(str(r))


def log(r, name="log.txt", verbose=True):  # Appends <r> to the log <name> and prints it.
    r = str(r)
    with codecs.open(name, "a", encoding="utf-8") as f:
        timeStr = str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        f.write(timeStr + ' ' + r + '\n')
        if verbose: print('<Log> ' + r)


def error(msg="", logFileStr=""):  # Prints the error *and breaks the script !!* Will be improved later on.
    log('ERROR : ' + msg)
    if logFileStr != "":
        logFile(logFileStr)
    sys.exit()


def sendRequest(url, typeR="get", payload={}, headers={}):
    r = ""
    successful, tries = False, 0
    while successful == False:
        try:
            if typeR == "get":
                r = session.get(url, data=payload, headers=headers)
            elif typeR == "post":
                r = session.post(url, data=payload, headers=headers)
            else:
                error("Invalid request type :" + str(typeR))
            successful = True
        except Exception as e:
            time.sleep(1)
            if tries > 4:
                if type(r) != type(""):  # string or request object ?
                    r = r.text
                error("The request failed : " + str(e), r)
            tries += 1
    return r


def getSavedData(name, roomId):
    name = roomId + "//savedData//" + name
    with open(name) as json_file:
        data = json.load(json_file)
    return data


def setSavedData(name, data, roomId):
    name = roomId + "//savedData//" + name
    with open(name, 'w') as outfile:
        json.dump(data, outfile)


# Login

def login():
    log("--- NEW LOGIN ---")
    """ logs in to all the necessary channels"""

    def getField(field, url="", r=""):
        """gets the hidden field <field> from string <r> ELSE url <url>"""
        if r == "":
            r = sendRequest(url, 'get').text
            r.encode('utf-8')
        p = r.find('name="' + field)
        if p <= 0:
            error("No field <" + field + "> found", r)
        p = r.find('value="', p) + len('value="')
        key = r[p:r.find('"', p + 1)]
        return key

    # Login to OpenId
    payload = {"email": email, "password": password,
               "fkey": getField("fkey", "https://openid.stackexchange.com/account/login")}
    r = sendRequest("https://openid.stackexchange.com/account/login/submit", "post", payload).text
    if r.find('<a href="/account/logout" >Logout</a>') <= 0:
        error("OpenId login failed", r)
    log("Login to OpenId successful")

    # Login to StackExchange
    payload = {'oauth_version': '', 'oauth_server': '', 'openid_identifier': 'https://openid.stackexchange.com/',
               "fkey": getField("fkey", "https://stackexchange.com/users/login?returnurl%20=%20%2f")}
    r = sendRequest("http://stackexchange.com/users/authenticate", "post", payload).text
    if r.find('<span class="hidden-text">Inbox</span>') <= 0:
        error("StackExchange login failed", r)
    log("Login to StackExchange successful")

    # Login to SE Chat
    sendRequest("http://stackexchange.com/users/chat-login", "post")
    r = sendRequest("http://chat.stackexchange.com/chats/join/favorite", "get").text
    setGlobalVars("masterFkey", getField("fkey", r=r))
    log("Got master fkey : " + globalVars["masterFkey"])
    log("Login to the SE chat successful")

    return session


# Chat Functions

def sendMessage(msg, roomId, noDelete=False):  # 10121 : test, 3229 : chemistry
    roomId = str(roomId)
    payload = {"fkey": globalVars["masterFkey"], "text": msg}
    r = sendRequest("http://chat.stackexchange.com/chats/" + roomId + "/messages/new", "post", payload)
    if r.text.find("You can perform this action again") >= 0:
        time.sleep(3)
        sendMessage(msg, roomId)
    else:
        if r.text.find("The message is too long") >= 0:
            log("Message too long : " + msg)
            return
        r = r.json()

        if noDelete:  # noDelete actually deletes the message ;_;
            threading.Thread(target=deleteMessage, args=[r["id"], roomId, 60 * 1.5]).start()
        return r["id"]


def editMessage(msg, id, roomId):
    roomId = str(roomId)
    id = str(id)
    payload = {"fkey": globalVars["masterFkey"], "text": msg}
    headers = {'Referer': "http://chat.stackexchange.com/rooms/" + roomId}
    r = sendRequest("http://chat.stackexchange.com/messages/" + id, "post", payload, headers).text
    if r.find("You can perform this action again") >= 0:
        time.sleep(3)
        editMessage(msg, id, roomId)


def deleteMessage(id, roomId, waitTime=0):
    time.sleep(waitTime)
    roomId = str(roomId)
    id = str(id)
    payload = {"fkey": globalVars["masterFkey"]}
    headers = {'Referer': "http://chat.stackexchange.com/rooms/" + roomId}
    r = sendRequest("http://chat.stackexchange.com/messages/" + id + "/delete", "post", payload, headers).text
    if r.find("You can perform this action again") >= 0:
        time.sleep(3)
        deleteMessage(id, roomId)


def joinRooms(roomsDict):
    """
    roomsTable is a dict {str(roomId):activityActionFunction}
    The ActivityActionFunction is triggred every time some activity related to that room is recorded.
    """
    payload = {"fkey": globalVars["masterFkey"], 'since': 0, 'mode': 'Messages', 'msgCount': 100}
    for key in roomsDict.keys():
        roomId = str(key)

        # configure saved data
        for name in [roomId, roomId + '//temp', roomId + '//savedData']:
            if not os.path.exists(name):
                os.makedirs(name)

        r = sendRequest("http://chat.stackexchange.com/chats/" + roomId + "/events", "post", payload).json()
        t = globalVars["roomsJoined"]
        t[roomId] = {"eventtime": r['time']}

        r = sendRequest("http://chat.stackexchange.com/rooms/info/" + roomId, "post", payload).text  # get room info
        roomName = ""
        try:
            p = r.find("all time messages in ")
            roomName = r[p + len("all time messages in "):r.find('"', p)]
        except Exception:
            log("Failed to scrape metadata for room : " + roomId)
        t[roomId]["roomName"] = roomName
        t[roomId]["usersGreeted"] = []

        setGlobalVars("roomsJoined", t)  # update global table
        log("Joined room : " + roomName + " / id: " + roomId)
    while True:
        for key in globalVars["roomsJoined"]:
            room = globalVars["roomsJoined"][key]
            roomId = key
            lastTime = room["eventtime"]
            payload = {"fkey": globalVars["masterFkey"], 'r' + roomId: lastTime}
            activity = sendRequest("http://chat.stackexchange.com/events", "post", payload).json()
            roomResult = {}
            try:  # update eventtime
                roomResult = activity['r' + roomId]
                eventtime = roomResult['t']
                t = globalVars["roomsJoined"]
                t[roomId]["eventtime"] = eventtime
                setGlobalVars("roomsJoined", t)
            except KeyError as ex:
                pass  # no updated time from room
            activityHandler = roomsDict[key]
            try:
                activityHandler(roomResult)  # send activity to designated function
            except Exception as e:
                log("Error occured while sending event <" + str(roomResult) + "> : " + getException())
        time.sleep(5)

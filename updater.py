def handleMessages(message):
    Mcontent = message["content"].encode("utf-8").replace('<div>', '').replace('</div>', '').replace(
        "<div class='full'>", '')
    MuserName = message['user_name'].encode("utf-8")
    MchatRoom = message['room_name'].encode("utf-8")
    MroomId = str(message['room_id'])  # int
    noDelete = Mcontent.find('!!!') >= 0
    tempDataPath = MroomId + '//temp//'
    chatbot.log(MuserName + ' : ' + Mcontent, name=MroomId + '//log.txt', verbose=False)
    print(MchatRoom + " | " + MuserName + ' : ' + Mcontent)
    if random.randint(1, 1000) == 133:
        chatbot.sendMessage(u"__🎺🎺🎺 AND HIS NAME IS JOHN CENA 🎺🎺🎺__", MroomId)
    Mcontent, McontentCase = Mcontent.lower(), Mcontent
    if Mcontent.find('!!img/') >= 0:
        id = chatbot.sendMessage(
            "Hold tight, I'm processing your request ... " + random.choice(coolTables["tablesList"]), MroomId,
            noDelete=noDelete)
        molec = McontentCase[Mcontent.find('img/') + len('img/'):].replace(' ', '%20').replace('</div>', '').replace(
            '\n', '').replace('&#39;', "'")
        reqUrl = "http://cactus.nci.nih.gov/chemical/structure/" + molec + "/image"
        # print(molec, reqUrl)
        molecImg = session.get(reqUrl, stream=True)
        with open(tempDataPath + 'mol.gif', 'wb') as out_file:
            shutil.copyfileobj(molecImg.raw, out_file)
        try:
            Image.open(tempDataPath + 'mol.gif').save(tempDataPath + 'mol.png')
        except Exception as e:
            chatbot.editMessage("<An error occured : " + str(e) + ". Check your molecule's name.>", id, MroomId)
            return
        del molecImg
        removeUselessSpace('mol.png', tempDataPath)
        ans = ""
        try:
            ans = clientImg.upload_from_path(tempDataPath + 'cropped_mol.png')
        except Exception as e:
            chatbot.editMessage("<An error occured : " + str(e) + ". Check your molecule's name.>", id, MroomId)
            return
        url = ans['link']
        chatbot.editMessage(url, id, MroomId)
    if Mcontent.find('!!wiki/') >= 0:
        article = McontentCase[Mcontent.find('wiki/') + len('wiki/'):].replace(' ', '_').replace('</div>',
                                                                                                 '').replace('\n', '')
        id = chatbot.sendMessage("https://en.wikipedia.org/wiki/" + article, MroomId, noDelete=noDelete)
    if Mcontent.find('!!flip') >= 0:
        p=Mcontent.find('flip/')+len("flip/")
        if p>=len("flip/"):
            chatbot.sendMessage(random.choice(coolTables["flipsList"])+upsidedown.transform(Mcontent[p:])[::-1], MroomId, noDelete=noDelete)
        else:
            chatbot.sendMessage(random.choice(coolTables["tablesList"]), MroomId, noDelete=noDelete)
    if Mcontent.find('!!doubleflip') >= 0:
        p = Mcontent.find('doubleflip/') + len("doubleflip/")
        if p >= len("doubleflip/"):
            sss=upsidedown.transform(Mcontent[p:])
            chatbot.sendMessage(sss+random.choice(coolTables["doubleflipsList"]) + sss[::-1], MroomId,
                                noDelete=noDelete)
        else:
            chatbot.sendMessage(random.choice(coolTables["tablesList"]), MroomId, noDelete=noDelete)
    if Mcontent.find('!!untable') >= 0:
        #
        chatbot.sendMessage(random.choice(coolTables["untablesList"]), MroomId, noDelete=noDelete)
    if Mcontent.find('!!gun') >= 0:
        #
        chatbot.sendMessage(random.choice(coolTables["gunsList"]), MroomId, noDelete=noDelete)
    if Mcontent.find('!!beer') >= 0:
        #
        chatbot.sendMessage("http://www.mandevillebeergarden.com/wp-content/uploads/2015/02/Beer-Slide-Background.jpg",
                            MroomId, noDelete=noDelete)
    if Mcontent.find('!!tea') >= 0:
        #
        chatbot.sendMessage("https://pixabay.com/static/uploads/photo/2015/07/02/20/57/chamomile-829538_960_720.jpg",
                            MroomId, noDelete=noDelete)
    if Mcontent.find('!!spam') >= 0:
        #
        chatbot.sendMessage("https://upload.wikimedia.org/wikipedia/commons/0/09/Spam_can.png", MroomId,
                            noDelete=noDelete)
    if Mcontent.find('!!coffee') >= 0:
        #
        chatbot.sendMessage(
            "http://res.freestockphotos.biz/pictures/10/10641-a-cup-of-coffee-on-a-bean-background-pv.jpg",
            MroomId)
    if Mcontent.find('!!sushi') >= 0:
        #
        chatbot.sendMessage(random.choice(coolTables["sushiCreamList"]), MroomId, noDelete=noDelete)
    if Mcontent.find('!!ice cream') >= 0:
        #
        chatbot.sendMessage(random.choice(coolTables["iceCreamList"]), MroomId, noDelete=noDelete)
    if False and Mcontent.find('!!changelog') >= 0:
        changelog = """3/22/16 - Created the bot.
        3/23/16 - Added the <help> command - the bot now edits its message to save space - the bot now welcomes entering users
        3/24/16 - Added the <changelog> command - updated <help> - refactored the whole code, rewrote the bot from scratch - moved host to Cloud9 - added support for multiple chatrooms at once - added the <wiki> command
        3/25/16 - Added the <doi> command - bot no longer greets users if it has seen them earlier - added the <scholar> command
        3/26/16 - Bot no longer pings people when they enter.
        """
        chatbot.sendMessage(changelog, MroomId, noDelete=noDelete)
    if Mcontent.find('!!test') >= 0:
        id = chatbot.sendMessage("a test !!", MroomId, noDelete=noDelete)
        time.sleep(1)
        chatbot.editMessage("edited", id, MroomId)
    if Mcontent.find('!!help') >= 0:
        helpString = """Hi! I'm the (for now) unofficial bot of ChemistrySE's main chatroom. __If you find me annoying, you can ignore me by clicking on my profile image and chosing "ignore this user"__
            Here are the useful commands I provide : (don't add the brackets)
            * img/[molecule's name] -> I will try and upload an image corresponding to your molecule. You can give its name, formula, SMILES, or any common identifier. When using complex InChI, use img/InChI=1/[molecule's InChI]
            * help -> displays this message
            * wiki/[article] -> returns a link to wikiedia's page n <article> if I can find it
            * doi/[DOI] -> gives metadata on the requested DOI
            * scholar/[requests] -> executes the request on Google Scholar
            ~ Syntax : !!!commandName/[arguments] for temporary messages, !!commandName/[arguments] for permanent ones ~
            I also greet new users, and have a few more less useful commands for fun.
            Example : !!img/3-(carboxymethyl)-12-ethyl-8,13,17-trimethyl- 21H,23H-porphine-2,7,18-tripropanoic acid
            """
        chatbot.sendMessage(helpString, MroomId, noDelete=noDelete)
    if Mcontent.find('!!doi/') >= 0:
        doi = McontentCase[Mcontent.find('doi/') + len('doi/'):].replace(' ', '%20').replace('</div>', '').replace(
            '\n', '')
        r = chatbot.sendRequest("http://pubs.acs.org/doi/abs/" + doi).text
        if r.find('Your request resulted in an error') > 0:
            chatbot.sendMessage("Could not find the requested DOI : " + doi, MroomId, noDelete=noDelete)
        else:
            try:
                p = r.find('dc.Title" content="') + len('dc.Title" content="')
                title = r[p:r.find('" />', p)]

                p = r.find('dc.Creator" content="') + len('dc.Creator" content="')
                author1 = r[p:r.find('" />', p)]

                chatbot.sendMessage("DOI " + doi + ' :\n"' + title + '"\nFirst author : ' + author1, MroomId,
                                    noDelete=noDelete)
            except Exception as e:
                chatbot.sendMessage("An error occured :" + str(e), MroomId, noDelete=noDelete)
    if Mcontent.find('!!scholar/') >= 0:
        search = McontentCase[Mcontent.find('scholar/') + len('scholar/'):].replace(' ', '%20').replace('</div>',
                                                                                                        '').replace(
            '\n', '')
        reqUrl = 'http://scholar.google.fr/scholar?hl=en&q=' + urllib.quote(search.replace(" ", "+")).replace("%2520",
                                                                                                              "+")
        r = chatbot.sendRequest(reqUrl,
                                "get")  # encode it, get best result, display * best result * requests's link * list of 3 next results
        r = r.text

        numArticles = 2
        articles = []
        art, p = 0, r.find('<h3 class="gs_rt"><a href="')
        while p >= 0 and art < numArticles:
            p += len('<h3 class="gs_rt"><a href="')
            url = r[p:r.find('"', p)]
            p = r.find('">', p) + len('">')
            title = r[p:r.find('</a>', p)].replace("<b>", "").replace("</b>", "")
            art += 1
            articles.append({"title": title, "url": url})
            p = r.find('<h3 class="gs_rt"><a href="', p + 1)
        fullMsg = "[Link to the request](" + reqUrl + "). Top links : "
        for i in articles:
            fullMsg += '[' + i["title"] + "](" + i['url'] + ") | "
        chatbot.sendMessage(fullMsg, MroomId, noDelete=noDelete)
    w = """if Mcontent.find('!!nogreet') >= 0:
        noGreet=getSavedData("noGreet.json")
        if not str(message['user_id']) in noGreet:
            noGreet[message['user_id']] = MuserName
            setSavedData("noGreet.json",noGreet)
            chatbot.sendMessage(MuserName + " was added to the noGreet list.", MroomId, noDelete=noDelete)
            log(MuserName + " was added to the noGreet list.")
        else:
            chatbot.sendMessage("You are already in the noGreet list.", MroomId, noDelete=noDelete)
    if Mcontent.find('!!greet') >= 0:
        noGreet = getSavedData("noGreet.json")
        if str(message['user_id']) in noGreet:
            noGreet.pop(str(message['user_id']))
            setSavedData("noGreet.json", noGreet)
            chatbot.sendMessage(MuserName + " was removed from the noGreet list.", MroomId, noDelete=noDelete)
            log(MuserName + " was removed from the noGreet list.")
        else:
            chatbot.sendMessage("You are not in the noGreet list.", MroomId, noDelete=noDelete)
    """
    if Mcontent.find('!!greet/') >= 0:
        user = McontentCase[Mcontent.find('greet/') + len('greet/'):].replace(' ', '%20').replace('</div>', '').replace(
            '\n', '')
        id = 0
        try:
            id = int(user)
        except Exception:
            pass
        uName = user
        if id is not None and id > 0:
            r = chatbot.sendRequest("http://chat.stackexchange.com/users/" + user).text
            p = r.find("<title>User ") + len("<title>User ")
            uName = r[p:r.find(" |", p)]
        chatbot.sendMessage(
            "Welcome to The Periodic Table " + uName + "! [Here](http://meta.chemistry.stackexchange.com/q/2723/) are our chat guidelines and it's recommended that you read them. If you want to turn Mathjax on, follow the instructions [in this answer](http://meta.stackexchange.com/a/220976/). Happy chatting!",
            MroomId)
    if Mcontent.find('!!sleep') >= 0:
        if str(message['user_id']) in coolTables["owners"]:
            timeSleep = McontentCase[Mcontent.find('sleep/') + len('sleep/'):].replace(' ', '%20').replace('</div>',
                                                                                                           '').replace(
                '\n', '')
            try:
                timeSleep = float(timeSleep) * 60
                chatbot.sendMessage("See you in " + str(timeSleep / 60.) + " minutes !", MroomId, noDelete=noDelete)
                time.sleep(timeSleep)
            except Exception:
                chatbot.sendMessage("invalid time", MroomId, noDelete=noDelete)
    if Mcontent.find('!!reload') >= 0:
        if str(message['user_id']) in coolTables["owners"]:
            try:
                newCode=chatbot.sendRequest("https://raw.githubusercontent.com/gauthierhaas/SE_Bot/master/updater.py").text
                print(type(newCode), newCode[:20])
                exec(newCode, globals())
                chatbot.sendMessage("Success !",MchatRoom)
            except Exception as e:
                chatbot.log("Error : "+str(e))

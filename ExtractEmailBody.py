# Extract body for email within mboxfile (gmail)
# mbox file downloaded using Google Takeout


def handleerror(errmsg, emailmsg, cs):
    pass
    print(errmsg)
    print("This error occurred while decoding with ", cs, " charset.")
    print("These charsets were found in the one email.", getcharsets(emailmsg))
    print("This is the subject:", emailmsg['subject'])
    print("This is the sender:", emailmsg['From'])


def getcharsets(email):
    charsets = set({})
    for c in email.get_charsets():
        if c is not None:
            charsets.update([c])
    return charsets

def decodebody(msg, body):

    for charset in getcharsets(msg):
        try:
            body = body.decode(charset)
        except UnicodeDecodeError:
            print('---handleerror---\n')
            handleerror("UnicodeDecodeError: encountered.", email, charset)
        except AttributeError:
            print('---AttributeError---\n')
            handleerror("AttributeError: encountered", email, charset)
    return body

def getbody(email):
    """ Iterate message objects within email payload to extract text &/or HTML body. """

    mainbody = {'text': [],
            'HTML': []}

    def getcontent(msg, content_type):

        if 'text/plain' in content_type:
            body = msg.get_payload(decode=True)
            body_text = decodebody(msg, body)
            mainbody['text'] = (body_text)

        elif 'text/html' in content_type:
            body = msg.get_payload(decode=True)
            body_HTML = decodebody(msg, body)
            mainbody['HTML'] = (body_HTML)

        else:
            body = msg.get_payload(decode=True)
            bodydecoded = decodebody(msg, body)

    mainbody = {'text': None,
                'HTML': None}

    payload = email.get_payload()
    for msg in payload:
        getcontent(msg, msg['Content-Type'])

    return mainbody


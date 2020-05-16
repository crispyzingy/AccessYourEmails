# imap: Internet Access Message Protocol
import imapclient

conn = imapclient.IMAPClient("imap.gmail.com", ssl=True)
print(conn.login("username@gmail.com", "password"))
conn.select_folder(
    "INBOX", readonly=True
)  # Unless you want to delete, set readonly=True
UID = conn.search(["SINCE", "17-Mar-2020"])  # IMAP Search Keys

print(UID)
emailUID = 253  # insert the UID of email
rawMessage = conn.fetch([emailUID], ["BODY[]", "FLAGS"])

import pyzmail

message = pyzmail.PyzMessage.factory(rawMessage[emailUID][b"BODY[]"])
print(message.get_subject())  # subject
print(message.get_addresses("from"))  # email from
print(message.get_addresses("to"))  # email to
print(message.get_addresses("bcc"))  # bcc

print(message.text_part)
print(message.html_part == None)
print(message.text_part.get_payload().decode("UTF-8"))  # body of message

print(message.text_part.charset)  # identify the charset incase it's not UTF-8
print(conn.list_folders())  # list the gmail folders

# Delete emails
# conn.select_folder("INBOX", readonly=False)  # modify/delete operations in Inbox
# UID = conn.search(["ON", "18-Mar-2020"])
# print(UID)
# conn.delete_messages([])  # enter the UIDS to delete
conn.logout()

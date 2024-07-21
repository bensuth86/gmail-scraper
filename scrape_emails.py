# scrape mbox file emails, return individual email data to dict and append to list
# mbox file downloaded using Google Takeout

import mailbox
import bs4

from ExtractEmailBody import getbody


def get_html_text(html):
    try:
        return bs4.BeautifulSoup(html, 'lxml').body.get_text(' ', strip=True)
    except AttributeError:  # message contents empty
        return None


def get_email_data(email):
    if not isinstance(email, mailbox.mboxMessage):
        raise TypeError('Variable must be type mailbox.mboxMessage')

    email_data = {'email_labels': email['X-Gmail-Labels'],
                  'email_date': email['Date'],
                  'email_from': email['From'],
                  'email_to': email['To'],
                  'email_subject': email['Subject']}

    return email_data


def main():

    scraped_emails = []
    mbox_obj = mailbox.mbox("test.mbox")
    for email in mbox_obj:
        email_data = get_email_data(email)
        mainbody = getbody(email)
        email_data['body'] = mainbody
        scraped_emails.append(email_data)

    return scraped_emails


if __name__ == "__main__":

    scraped_emails = main()
    print(scraped_emails)

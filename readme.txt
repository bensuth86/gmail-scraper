### ScrapeEmails ###

Scrapes gmail data from mbox file downloaded using Google TakeOut.  
Extracts email metadata(email_data, email_from ...)
Extracts plain text and HTML parts from email body
Decodes HTML
Stores data to and return dictionary, 'scraped_emails'
Includes additional function to extract html_text which is not used for this template.


## Requirements ##

- Python 3.x
- Python modules
	bs4
	
- Python libraries

	import bs4
	import mailbox


## Run Instructions ##

Download mbox file via Google Takeout and save to repo.
Run scraped_emails.py








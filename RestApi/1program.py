import urllib2
import json
from pymongo import collection
import xml.etree.ElementTree as et
url = "https://www.federalregister.gov/api/v1/articles/00-02053.json?fields%5B%5D=abstract&fields%5B%5D=abstract_html_url&fields%5B%5D=action&fields%5B%5D=agencies&fields%5B%5D=agency_names&fields%5B%5D=body_html_url&fields%5B%5D=cfr_references&fields%5B%5D=citation&fields%5B%5D=comment_url&fields%5B%5D=comments_close_on&fields%5B%5D=correction_of&fields%5B%5D=corrections&fields%5B%5D=dates&fields%5B%5D=docket_id&fields%5B%5D=docket_ids&fields%5B%5D=document_number&fields%5B%5D=effective_on&fields%5B%5D=end_page&fields%5B%5D=excerpts&fields%5B%5D=executive_order_notes&fields%5B%5D=executive_order_number&fields%5B%5D=full_text_xml_url&fields%5B%5D=html_url&fields%5B%5D=json_url&fields%5B%5D=mods_url&fields%5B%5D=page_length&fields%5B%5D=pdf_url&fields%5B%5D=president&fields%5B%5D=public_inspection_pdf_url&fields%5B%5D=publication_date&fields%5B%5D=raw_text_url&fields%5B%5D=regulation_id_number_info&fields%5B%5D=regulation_id_numbers&fields%5B%5D=regulations_dot_gov_info&fields%5B%5D=regulations_dot_gov_url&fields%5B%5D=significant&fields%5B%5D=signing_date&fields%5B%5D=start_page&fields%5B%5D=subtype&fields%5B%5D=title&fields%5B%5D=toc_doc&fields%5B%5D=toc_subject&fields%5B%5D=topics&fields%5B%5D=type&fields%5B%5D=volume"
conn = Connection()


def get_xml_link(url):
	try:
		urlopen = urllib2.urlopen(url)
		data = json.load(urlopen)
		if data["full_text_xml_url"] is not None:
			print (data["full_text_xml_url"]) # this extracts the data from the required xml file
		if data["body_html_url"] is not None:
			print (data["body_html_url"])
		if data["json_url"] is not None:
			print (data["json_url"][:])

	except:
		urlopen = urllib2.urlopen(url)
		data = json.load(urlopen)
		print (data["json_url"])




def ask_request_call():
	req_call = raw_input('Enter the request token genereted') # this is the call , When generated using the api.(mark all)
	req_call = str(req_call).strip() # removes the extra space from the link specified
	get_xml_link(req_call)   # this is the xml link generater, function caller basically.

def main():
	ask_request_call()
if __name__ == '__main__':
    main()

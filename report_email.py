#!/usr/bin/env python3

import os
import datetime
import reports
import emails

def process_txt_files(path):
  input_dir=os.path.join(os.path.expanduser('~'), path)
  body = ''
  for desc_file in os.listdir(input_dir):
    if 'txt' in desc_file:
      file_total = os.path.join(input_dir, desc_file)
      with open(file_total, 'rb') as opened:
        body += "<br /><br />name: " +  opened.readline().decode("utf-8").strip()
        body += "<br />weight: " + opened.readline().decode("utf-8").strip()
  body += "<br />"
  return body

if __name__ == "__main__":
  reports.generate("/tmp/processed.pdf", "Processed Update on {}".format(datetime.date.today().strftime("Month %d, %Y")), process_txt_files("supplier-data/descriptions"))
  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ.get('USER'))
  subject = "Upload Completed - Online Fruit Store"
  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
  message = emails.generate(sender, receiver, subject, body, "/tmp/processed.pdf")
  emails.send(message)

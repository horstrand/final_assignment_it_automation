#!/usr/bin/env python3

import os
import datetime
import reports

def process_txt_files(path):
  input_dir=os.path.join(os.path.expanduser('~'), path)


if __name__ == "__main__":
  reports.generate("/tmp/processed.pdf", "Processed Update on {}".format(today = date.today().strftime("%d/%m/%Y")), process_txt_files("supplier-data/descriptions"))

#sender = "automation@example.com"
#receiver = "{}@example.com".format(os.environ.get('USER'))
#subject = "List of Fruits"
#body = "Hi\n\nI'm sending an attachment with all my fruit."

#message = emails.generate(sender, receiver, subject, body, "/tmp/report.pdf")
#emails.send(message)

"""
https://leetcode.com/problems/unique-email-addresses/

"""
from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        send_emails = set()

        for email in emails:
            localname, domain = email.split('@')
            plus_pos = localname.find('+')
            if plus_pos != -1:
                localname = localname[:plus_pos]

            localname = localname.replace('.', '')
            full_email = localname + '@' + domain
            send_emails.add(full_email)

        return len(send_emails)

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        local_names = set()
        for email in emails:
            local_name = email.split('@')[0]
            domain_name = email.split('@')[1]
            local_name = local_name.split('+')[0]
            local_name = local_name.replace(".", "")
            local_names.add(local_name+'@'+domain_name)
        return len(local_names)

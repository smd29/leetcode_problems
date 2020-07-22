class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        #find the position of @
        #for i in range(0,len(emails)):
        _set=set()
        for email in emails:
            localName,domainName=email.split('@')
            localName=localName.split('+')[0].replace('.','')
            _set.add(localName+'@'+domainName)
        return len(_set)
    
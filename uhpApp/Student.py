#
# Description: Student is a class that stores honors program participation information about a particular student.
# Information stored is (1) email (2) whether they are signed in or not (3) their UHP Events participation status
# information and (4) their SJ participation status information
# Date: 8/21/19
# Coder: Brad Just
#

class Student(object):
    def __init__(self):
        self.email = None
        self.signedIn = False
        self.uhpStatus = None
        self.sjStatus = None
    def setStatus(self):
        '''Method interacts with Google Apps Script to extract participation data'''
        pass

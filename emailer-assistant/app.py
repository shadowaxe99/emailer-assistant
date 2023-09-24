from email_scheduling import EmailScheduling
from email_analytics import EmailAnalytics
from email_personalization import EmailPersonalization
from email_attachments import EmailAttachments
from email_reply_tracking import EmailReplyTracking
from email_filtering import EmailFiltering
from email_tracking import EmailTracking
from email_templates import EmailTemplates
from email_search import EmailSearch


class App:
    def __init__(self):
        self.email_scheduling = EmailScheduling()
        self.email_analytics = EmailAnalytics()
        self.email_personalization = EmailPersonalization()
        self.email_attachments = EmailAttachments()
        self.email_reply_tracking = EmailReplyTracking()
        self.email_filtering = EmailFiltering()
        self.email_tracking = EmailTracking()
        self.email_templates = EmailTemplates()
        self.email_search = EmailSearch()

    def run(self):
        print('Emailer Assistant is running.')


if __name__ == '__main__':
    app = App()
    app.run()

class EmailReplyTracking:
    def __init__(self):
        self.tracked_emails = {}

    def track_replies(self, email_id):
        # Track replies for a specific email
        if email_id in self.tracked_emails:
            print(f'Replies tracked for email with ID: {email_id}')
        else:
            print(f'Email with ID {email_id} is not being tracked')

    def start_tracking(self, email_id):
        # Start tracking replies for a specific email
        self.tracked_emails[email_id] = True
        print(f'Tracking started for email with ID: {email_id}')

    def stop_tracking(self, email_id):
        # Stop tracking replies for a specific email
        if email_id in self.tracked_emails:
            del self.tracked_emails[email_id]
            print(f'Tracking stopped for email with ID: {email_id}')
        else:
            print(f'Email with ID {email_id} is not being tracked')

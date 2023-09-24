class EmailAttachments:
    def __init__(self):
        self.attachments = {}

    def attach_file(self, file_name, file_path):
        # Attach a file to the email
        self.attachments[file_name] = file_path
        print(f'File '{file_name}' attached')

    def remove_attachment(self, file_name):
        # Remove an attached file
        if file_name in self.attachments:
            del self.attachments[file_name]
            print(f'File '{file_name}' removed')
        else:
            print(f'File '{file_name}' is not attached')

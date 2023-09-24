class EmailTemplates:
    def __init__(self):
        self.templates = {}

    def create_template(self, template_name, template_content):
        # Create a new email template
        self.templates[template_name] = template_content
        print(f'Email template {template_name} created')

    def edit_template(self, template_name, new_content):
        # Edit an existing email template
        if template_name in self.templates:
            self.templates[template_name] = new_content
            print(f'Email template {template_name} edited')
        else:
            print(f'Email template {template_name} does not exist')

    def delete_template(self, template_name):
        # Delete an existing email template
        if template_name in self.templates:
            del self.templates[template_name]
            print(f'Email template {template_name} deleted')
        else:
            print(f'Email template {template_name} does not exist')

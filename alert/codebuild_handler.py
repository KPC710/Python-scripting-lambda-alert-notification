class CodeBuildEvent:
    def __init__(self, event):
        self.project_name = event['detail']['project-name']
        self.build_id = event['detail']['build-id']
        self.build_status = event['detail']['build-status']
        self.initiator = event['detail']['additional-information'].get('initiator', 'Unknown')

    def __str__(self):
        return f"CodeBuildEvent: Project={self.project_name}, BuildID={self.build_id}, Status={self.build_status}, Initiator={self.initiator}"

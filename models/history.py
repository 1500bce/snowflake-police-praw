import datetime

class History:

    def __init__(self, submission_id, submission_title, submission_text, submission_created_utc, comment_id, comment_author, comment_body):
        # self.id = id
        self.submission_id = submission_id
        self.submission_title = submission_title
        self.submission_text = submission_text
        self.submission_created_utc = submission_created_utc
        self.comment_id = comment_id
        self.comment_author = comment_author
        self.comment_body = comment_body
        self.date_created = datetime.datetime.today()

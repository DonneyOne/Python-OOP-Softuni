class Document:
    def __init__(self, id, category_id, topic_id, filename):
        self.id = id
        self.category_id = category_id
        self.topic_id = topic_id
        self.filename = filename
        self.tags = []

    @classmethod
    def from_instance(cls, id, category, topic, filename):
        return cls(id, category.id, topic.id, filename)

    @staticmethod
    def tag_verification(content, tags):
        return content in tags

    @staticmethod
    def list_to_string(example):
        return ", ".join(example)

    def add_tag(self, tag_content):
        if not Document.tag_verification(tag_content, self.tags):
            self.tags.append(tag_content)
        return f"Tag: {tag_content} already added"

    def remove_tag(self, tag_content):
        if Document.tag_verification(tag_content, self.tags):
            self.tags.remove(tag_content)
        return f"Tag: {tag_content} already added"

    def edit(self, file_name):
        self.filename = file_name

    def __repr__(self):
        return f"Document {self.id}: {self.filename}; category {self.category_id}, " \
               f"topic {self.topic_id}, tags ({Document.list_to_string(self.tags)})"


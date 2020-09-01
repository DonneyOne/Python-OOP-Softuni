class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    @staticmethod
    def verification(element, example):
        return element in example

    @staticmethod
    def one_instance_verification(element_id, the_list):
        x = [y for y in the_list if y.id == element_id]
        return x[0]

    def add_category(self, category):
        if not Storage.verification(category, self.categories):
            self.categories.append(category)
        return "Category already added"

    def add_document(self, document):
        if not Storage.verification(document, self.documents):
            self.documents.append(document)
        return "Document already added"

    def add_topic(self, topic):
        if not Storage.verification(topic, self.topics):
            self.topics.append(topic)
        return "Topic already added"

    def edit_category(self, category_id, new_name):
        category = Storage.one_instance_verification(category_id, self.categories)
        category.name = new_name

    def edit_topic(self, topic_id, new_name):
        topic = Storage.one_instance_verification(topic_id, self.topics)
        topic.name = new_name

    def edit_document(self, document_id, new_name):
        document = Storage.one_instance_verification(document_id, self.documents)
        document.name = new_name

    def delete_category(self, category_id):
        category = Storage.one_instance_verification(category_id, self.categories)
        self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = Storage.one_instance_verification(topic_id, self.topics)
        self.topics.remove(topic)

    def delete_document(self, document_id):
        document = Storage.one_instance_verification(document_id, self.documents)
        self.documents.remove(document)

    def get_document(self, document_id):
        return Storage.one_instance_verification(document_id, self.documents)

    def __repr__(self):
        result = ""
        for k in self.documents:
            result += k.__repr__()
            result += "\n"
        return result

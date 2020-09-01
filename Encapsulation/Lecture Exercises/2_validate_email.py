class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.__domain = set(domains)
        self.__mails = set(mails)

    def __validate_name(self, name):
        return name and self.__min_length <= len(name)

    def __validate_domain(self, domain):
        return domain in self.__domain

    def __validate_mail(self, mail):
        return mail in self.__mails

    def validate(self, email):
        (name, domain, mail) = re.split(r"[@.]", email)
        return self.__validate_domain(domain) \
               and self.__validate_mail(mail) \
               and self.__validate_name(name)


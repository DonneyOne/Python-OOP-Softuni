class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    @staticmethod
    def validator(obj, l):
        return obj in l

    @staticmethod
    def one_instance_verification(element_id, the_list):
        x = [y for y in the_list if y.id == element_id]
        return x[0]

    def add_customer(self, customer):
        if not Gym.validator(customer, self.customers):
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if not Gym.validator(trainer, self.customers):
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if not Gym.validator(equipment, self.equipment):
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if not Gym.validator(plan, self.plans):
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if not Gym.validator(subscription, self.subscriptions):
            self.subscriptions.append(subscription)

    def subscription_info(self,subscription_id):
        subscription = Gym.one_instance_verification(subscription_id, self.subscriptions)
        trainer = Gym.one_instance_verification(subscription.trainer_id, self.trainers)
        plan = Gym.one_instance_verification(subscription.exercise_id, self.plans)
        customer = Gym.one_instance_verification(subscription.customer_id, self.customers)
        equipment = Gym.one_instance_verification(plan.equipment_id, self.equipment)
        return f"{subscription.__repr__()} \n" \
               f"{customer.__repr__()} \n" \
               f"{trainer.__repr__()} \n" \
               f"{equipment.__repr__()} \n" \
               f"{plan.__repr__()} \n"


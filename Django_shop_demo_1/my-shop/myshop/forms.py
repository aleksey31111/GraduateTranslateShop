from shop import CustomerForm as CustomerFormBase


class CustomerForm(CustomerFormBase):
    field_order = ['salutation', 'first_name', 'last_name', 'email']

from syncrowrapper.type_definitions import *


class URLs:
    def __init__(
        self,
        subdomain: str,
    ):
        self.base_url = f'https://{subdomain}.syncromsp.com/api/v1'

    # ************************
    # *** Appointment Type ***
    # ************************

    # *******************
    # *** Appointment ***
    # *******************

    # *************
    # *** Asset ***
    # *************

    # ************
    # *** Call ***
    # ************

    # ***************
    # *** Contact ***
    # ***************

    def contacts_url(
        self,
    ) -> str:
        '''/contacts'''
        return f'{self.base_url}/contacts'

    def contacts_id_url(
        self,
        contact_id: str | int,
    ) -> str:
        '''/contacts/{id}'''
        return f'{self.contacts_url()}/{contact_id}'

    # ****************
    # *** Contract ***
    # ****************

    # ****************
    # *** Customer ***
    # ****************

    def customers_url(
        self,
    ) -> str:
        '''/customers'''
        return f'{self.base_url}/customers'

    def customers_id_url(
        self,
        customer_id: str | int,
    ) -> str:
        '''/customers/{id}'''
        return f'{self.customers_url()}/{customer_id}'

    def customers_latest_url(
        self,
    ) -> str:
        return f'{self.customers_url()}/latest'

    def customers_autocomplete_url(
        self,
    ) -> str:
        return f'{self.customers_url()}/autocomplete'

    # ****************
    # *** Estimate ***
    # ****************

    # ***************
    # *** Invoice ***
    # ***************

    # *************************
    # *** Invoice/Line item ***
    # *************************

    # ************
    # *** Item ***
    # ************

    # ************
    # *** Lead ***
    # ************

    # *****************
    # *** Line Item ***
    # *****************

    # ***********************
    # *** New Ticket Form ***
    # ***********************

    # **********************
    # *** Payment Method ***
    # **********************

    # ***********************
    # *** Payment Profile ***
    # ***********************

    # ***************
    # *** Payment ***
    # ***************

    # *************
    # *** Phone ***
    # *************

    # *******************
    # *** Portal User ***
    # *******************

    # **********************
    # *** Product Serial ***
    # **********************

    # ***************
    # *** Product ***
    # ***************

    # **********************
    # *** Purchase Order ***
    # **********************

    # *****************
    # *** RMM Alert ***
    # *****************

    def rmm_alerts_url(
        self,
    ) -> str:
        '''/rmm_alerts'''
        return f'{self.base_url}/rmm_alerts'

    # ****************
    # *** Schedule ***
    # ****************

    # **************
    # *** Search ***
    # **************

    # ***************
    # *** Setting ***
    # ***************

    # ********************
    # *** Ticket Timer ***
    # ********************

    def ticket_timers_url(
        self,
    ) -> str:
        '''/ticket_timers'''
        return f'{self.base_url}/ticket_timers'

    # **************
    # *** Ticket ***
    # **************

    def tickets_url(
        self,
    ) -> str:
        '''/tickets'''
        return f'{self.base_url}/tickets'

    def tickets_id_url(
        self,
        ticket_id: str | int,
    ) -> str:
        '''/tickets/{id}'''
        return f'{self.tickets_url()}/{ticket_id}'

    def tickets_settings_url(
        self,
    ) -> str:
        '''/tickets/settings'''
        return f'{self.tickets_url()}/settings'

    def ticket_comment_url(
        self,
        ticket_id: str | int,
    ) -> str:
        '''/tickets/{id}/comment'''
        return f'{self.tickets_id_url(ticket_id)}/comment'

    # ***************
    # *** Timelog ***
    # ***************

    # *******************
    # *** User Device ***
    # *******************

    # ************
    # *** User ***
    # ************

    def current_user_url(
        self,
    ) -> str:
        '''/me'''
        return f'{self.base_url}/me'

    def users_url(
        self,
    ) -> str:
        '''/users'''
        return f'{self.base_url}/users'

    def users_id_url(
        self,
        user_id: str | int,
    ) -> str:
        '''/users/{id}'''
        return f'{self.users_url()}/{user_id}'

    # **************
    # *** Vendor ***
    # **************

    # *****************
    # *** Wiki Page ***
    # *****************

    # ************************
    # *** Worksheet Result ***
    # ************************

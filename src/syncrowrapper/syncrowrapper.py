import time
from datetime import datetime
from typing import Unpack

import requests

from syncrowrapper.exceptions import *
from syncrowrapper.type_definitions import *
from syncrowrapper.urls import *


class SyncroAPI:
    def __init__(
        self,
        subdomain: str = 'cagsupport',
        **kwargs: Unpack[SyncroAPIInitKwargs],
    ):
        self.url = URLs(subdomain)
        self.last_call_timestamp: datetime | None = None
        self.max_requests_per_second: int = 2
        self.api_key: str | None = kwargs.get('api_key')
        self.raise_for_status: bool = True
        if 'raise_for_status' in kwargs:
            raise_for_status = kwargs['raise_for_status']
            assert isinstance(raise_for_status, bool)
            self.raise_for_status = raise_for_status

        self.__initialize_session()

        if self.api_key:
            self.set_authorization_header()

    def __initialize_session(
        self,
    ):
        s = requests.Session()
        s.headers = {'Accept': 'application/json'}
        self.session = s

    def set_authorization_header(
        self,
        api_key: str | None = None,
    ):
        if api_key:
            self.api_key = api_key
        assert isinstance(self.api_key, str)
        self.session.headers.update({'Authorization': self.api_key})
        assert self.is_authenticated()

    def __make_request(
        self,
        request_parameters: dict,
    ) -> requests.Response:
        self.__wait_between_requests()
        self.last_call_timestamp = datetime.now()
        r = self.session.request(**request_parameters)
        if self.raise_for_status:
            r.raise_for_status()
        return r

    def __wait_between_requests(
        self,
    ):
        if not self.last_call_timestamp:
            return
        time_since_last_call = datetime.now() - self.last_call_timestamp
        wait_time = (
            1 / self.max_requests_per_second
        ) - time_since_last_call.total_seconds()
        time.sleep(max(0, wait_time))

    def __loop_requests(
        self,
        request_parameters: dict,
        **kwargs: Unpack[LoopRequestsKwargs],
    ):
        max_loops = -1
        if 'max_loops' in kwargs:
            max_loops = kwargs.get('max_loops')
            assert isinstance(max_loops, int)
            assert max_loops > 0
        data_list_key = 'data'
        if 'data_list_key' in kwargs:
            data_list_key = kwargs['data_list_key']
            assert isinstance(data_list_key, str)
        data_list = []
        current_loop = 0
        while current_loop != max_loops:
            current_loop += 1
            r = self.__make_request(
                request_parameters=request_parameters,
            )
            response = r.json()

            current_data_list = response.get(data_list_key)
            if current_data_list:
                data_list.extend(current_data_list)
            else:
                break

            meta = response.get('meta')
            if not meta:
                break
            total_pages = meta.get('total_pages')
            page = meta.get('page')
            assert isinstance(total_pages, int)
            assert isinstance(page, int)
            if page == total_pages:
                break

            params = request_parameters.get('params')
            if not params:
                request_parameters['params'] = {}
            request_parameters['params']['page'] = page + 1

        return data_list

    def is_authenticated(
        self,
    ) -> bool:
        previous_raise_for_status = self.raise_for_status
        self.raise_for_status = True
        try:
            self.get_current_user()
            is_authenticated = True
        except Exception:
            is_authenticated = False
        self.raise_for_status = previous_raise_for_status
        return is_authenticated

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

    def get_contacts(
        self,
        params: GetContactsParams | None = None,
        **kwargs: Unpack[LoopRequestsKwargs],
    ) -> list[GetContactsResponseContact]:
        '''GET /contacts'''
        request_parameters = {
            'method': 'GET',
            'url': self.url.tickets_url(),
            'params': params,
        }
        if 'data_list_key' not in kwargs:
            kwargs['data_list_key'] = 'contacts'
        contacts = self.__loop_requests(
            request_parameters=request_parameters,
            **kwargs,
        )
        return contacts

    def create_contact(
        self,
        request_body: CreateContactRequestBody,
    ) -> CreateContactResponse:
        '''POST /contacts'''
        request_parameters = {
            'method': 'POST',
            'url': self.url.contacts_url(),
            'json': request_body,
        }
        r = self.__make_request(
            request_parameters=request_parameters,
        )
        response = r.json()
        return response

    def get_contact_by_id(
        self,
        contact_id: str | int,
    ) -> GetContactByIdResponse:
        '''GET /contacts/{id}'''
        request_parameters = {
            'method': 'GET',
            'url': self.url.contacts_id_url(
                contact_id=contact_id,
            ),
        }
        r = self.__make_request(
            request_parameters=request_parameters,
        )
        response = r.json()
        return response

    def update_contact_by_id(
        self,
        contact_id: str | int,
        request_body: UpdateContactByIdRequestBody,
    ) -> UpdateContactByIdResponse:
        '''PUT /contacts/{id}'''
        if 'name' not in request_body:
            raise MissingParametersException('name')
        request_parameters = {
            'method': 'PUT',
            'url': self.url.contacts_id_url(
                contact_id=contact_id,
            ),
            'json': request_body,
        }
        r = self.__make_request(
            request_parameters=request_parameters,
        )
        response = r.json()
        return response

    def delete_contact_by_id(
        self,
        contact_id: str | int,
    ) -> requests.Response:
        '''DELETE /contacts/{id}'''
        request_parameters = {
            'method': 'DELETE',
            'url': self.url.contacts_id_url(
                contact_id=contact_id,
            ),
        }
        r = self.__make_request(
            request_parameters=request_parameters,
        )
        return r

    # ****************
    # *** Contract ***
    # ****************

    # ****************
    # *** Customer ***
    # ****************

    def get_customers(
        self,
        params: GetCustomersParams | None = None,
        **kwargs: Unpack[LoopRequestsKwargs],
    ) -> list[GetCustomersResponseCustomer]:
        '''GET /customers'''
        request_parameters = {
            'method': 'GET',
            'url': self.url.customers_url(),
            'params': params,
        }
        if 'data_list_key' not in kwargs:
            kwargs['data_list_key'] = 'customers'
        customers = self.__loop_requests(
            request_parameters=request_parameters,
            **kwargs,
        )
        return customers

    def create_customer(
        self,
        request_body: CreateCustomerRequestBody,
    ) -> CreateCustomerResponse:
        '''POST /customers'''
        request_parameters = {
            'method': 'POST',
            'url': self.url.customers_url(),
            'json': request_body,
        }
        r = self.__make_request(
            request_parameters=request_parameters,
        )
        response = r.json()
        return response

    def get_customer_by_id(
        self,
        customer_id: str | int,
    ) -> GetCustomerByIdResponse:
        '''GET /customers/{id}'''
        request_parameters = {
            'method': 'GET',
            'url': self.url.customers_id_url(
                customer_id=customer_id,
            ),
        }
        r = self.__make_request(
            request_parameters=request_parameters,
        )
        response = r.json()
        return response

    def update_customer_by_id(
        self,
        customer_id: str | int,
        request_body: UpdateCustomerByIdRequestBody,
    ) -> UpdateCustomerByIdResponse:
        '''PUT /customers/{id}'''
        request_parameters = {
            'method': 'PUT',
            'url': self.url.customers_id_url(
                customer_id=customer_id,
            ),
            'json': request_body,
        }
        r = self.__make_request(
            request_parameters=request_parameters,
        )
        response = r.json()
        return response

    def delete_customer_by_id(
        self,
        customer_id: str | int,
    ) -> requests.Response:
        '''DELETE /customers/{id}'''
        request_parameters = {
            'method': 'DELETE',
            'url': self.url.customers_id_url(
                customer_id=customer_id,
            ),
        }
        r = self.__make_request(
            request_parameters=request_parameters,
        )
        return r

    def get_latest_customer(
        self,
    ) -> GetLatestCustomerResponse:
        '''GET /customers/latest'''
        request_parameters = {
            'method': 'GET',
            'url': self.url.customers_latest_url(),
        }
        r = self.__make_request(
            request_parameters=request_parameters,
        )
        response = r.json()
        return response

    def get_autocomplete_customers(
        self,
        query: str,
        **kwargs: Unpack[LoopRequestsKwargs],
    ) -> list[GetAutocompleteCustomersResponseCustomer]:
        '''GET /customers/autocomplete'''
        request_parameters = {
            'method': 'GET',
            'url': self.url.customers_autocomplete_url(),
            'params': {'query': query},
        }
        if 'data_list_key' not in kwargs:
            kwargs['data_list_key'] = 'customers'
        customers = self.__loop_requests(
            request_parameters=request_parameters,
            **kwargs,
        )
        return customers

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

    def get_rmm_alerts(
        self,
        params: GetRMMAlertsParams | None = None,
        **kwargs: Unpack[LoopRequestsKwargs],
    ) -> list[GetRMMAlertsResponseRMMAlert]:
        '''GET /rmm_alerts'''
        request_parameters = {
            'method': 'GET',
            'url': self.url.rmm_alerts_url(),
            'params': params,
        }
        if 'data_list_key' not in kwargs:
            kwargs['data_list_key'] = 'rmm_alerts'
        rmm_alerts = self.__loop_requests(
            request_parameters=request_parameters,
            **kwargs,
        )
        return rmm_alerts

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

    def get_ticket_timers(
        self,
        params: GetTicketTimersParams | None = None,
        **kwargs: Unpack[LoopRequestsKwargs],
    ) -> list[GetTicketTimersResponseTimer]:
        '''GET /ticket_timers'''
        request_parameters = {
            'method': 'GET',
            'url': self.url.ticket_timers_url(),
            'params': params,
        }
        if 'data_list_key' not in kwargs:
            kwargs['data_list_key'] = 'ticket_timers'
        ticket_timers = self.__loop_requests(
            request_parameters=request_parameters,
            **kwargs,
        )
        return ticket_timers

    # **************
    # *** Ticket ***
    # **************

    def get_tickets(
        self,
        params: GetTicketsParams | None = None,
        **kwargs: Unpack[LoopRequestsKwargs],
    ) -> list[GetTicketsResponseTicket]:
        '''GET /tickets'''
        request_parameters = {
            'method': 'GET',
            'url': self.url.tickets_url(),
            'params': params,
        }
        if 'data_list_key' not in kwargs:
            kwargs['data_list_key'] = 'tickets'
        tickets = self.__loop_requests(
            request_parameters=request_parameters,
            **kwargs,
        )
        return tickets

    def create_ticket(
        self,
        request_body: CreateTicketRequestBody,
    ) -> CreateTicketResponse:
        '''POST /tickets'''
        request_parameters = {
            'method': 'POST',
            'url': self.url.tickets_url(),
            'json': request_body,
        }
        r = self.__make_request(
            request_parameters=request_parameters,
        )
        response = r.json()
        return response

    def get_ticket_by_id(
        self,
        ticket_id: str | int,
    ) -> GetTicketByIdResponse:
        '''GET /tickets/{id}'''
        request_parameters = {
            'method': 'GET',
            'url': self.url.tickets_id_url(
                ticket_id=ticket_id,
            ),
        }
        r = self.__make_request(
            request_parameters=request_parameters,
        )
        response = r.json()
        return response

    def update_ticket_by_id(
        self,
        ticket_id: str | int,
        request_body: UpdateTicketByIdRequestBody,
    ) -> UpdateTicketByIdResponse:
        '''PUT /tickets/{id}'''
        request_parameters = {
            'method': 'PUT',
            'url': self.url.tickets_id_url(
                ticket_id=ticket_id,
            ),
            'json': request_body,
        }
        r = self.__make_request(
            request_parameters=request_parameters,
        )
        response = r.json()
        return response

    def delete_ticket_by_id(
        self,
        ticket_id: str | int,
    ) -> requests.Response:
        '''DELETE /tickets/{id}'''
        request_parameters = {
            'method': 'DELETE',
            'url': self.url.tickets_id_url(
                ticket_id=ticket_id,
            ),
        }
        r = self.__make_request(
            request_parameters=request_parameters,
        )
        return r

    def get_tickets_settings(
        self,
    ) -> GetTicketsSettingsResponse:
        '''GET /tickets/settings'''
        request_parameters = {
            'method': 'GET',
            'url': self.url.tickets_settings_url(),
        }
        r = self.__make_request(
            request_parameters=request_parameters,
        )
        response = r.json()
        return response

    def add_comment_to_ticket(
        self,
        ticket_id: str | int,
        request_body: AddCommentToTicketRequestBody,
    ) -> AddCommentToTicketResponse:
        '''POST /tickets/{id}/comment'''
        request_parameters = {
            'method': 'POST',
            'url': self.url.ticket_comment_url(
                ticket_id=ticket_id,
            ),
            'json': request_body,
        }
        r = self.__make_request(
            request_parameters=request_parameters,
        )
        response = r.json()
        return response

    # ***************
    # *** Timelog ***
    # ***************

    # *******************
    # *** User Device ***
    # *******************

    # ************
    # *** User ***
    # ************

    def get_current_user(
        self,
    ) -> GetCurrentUserResponse:
        '''GET /me'''
        request_parameters = {
            'method': 'GET',
            'url': self.url.current_user_url(),
        }
        r = self.__make_request(
            request_parameters=request_parameters,
        )
        response = r.json()
        return response

    def get_users(
        self,
        **kwargs: Unpack[LoopRequestsKwargs],
    ) -> list[UserIdAndName]:
        '''GET /users'''
        request_parameters = {
            'method': 'GET',
            'url': self.url.users_url(),
        }
        if 'data_list_key' not in kwargs:
            kwargs['data_list_key'] = 'users'
        users = self.__loop_requests(
            request_parameters=request_parameters,
            **kwargs,
        )
        return users

    def get_user_by_id(
        self,
        user_id: str | int,
    ) -> GetUserByIdResponse:
        request_parameters = {
            'method': 'GET',
            'url': self.url.users_id_url(
                user_id=user_id,
            ),
        }
        r = self.__make_request(
            request_parameters=request_parameters,
        )
        response = r.json()
        return response

    # **************
    # *** Vendor ***
    # **************

    # *****************
    # *** Wiki Page ***
    # *****************

    # ************************
    # *** Worksheet Result ***
    # ************************

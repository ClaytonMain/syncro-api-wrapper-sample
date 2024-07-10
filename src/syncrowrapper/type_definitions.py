from typing import Any, Literal, Required

from typing_extensions import TypedDict

# ************************
# *** Shared / Generic ***
# ************************

DateStrYYYYMMDD = str
IntGtZero = int


class ReadWriteDelete(TypedDict):
    read: bool
    write: bool
    delete: bool


class AddManageDelete(TypedDict):
    add: bool
    manage: bool
    delete: bool


class UserChatPermissions(TypedDict):
    show_all: bool
    from_unassigned: bool
    from_others: bool
    to_others: bool
    start_chat: bool


class GenericContact(TypedDict):
    id: int
    name: str | None
    address1: str | None
    address2: str | None
    city: str | None
    state: str | None
    zip: str | None
    email: str | None
    phone: str | None
    mobile: str | None
    latitude: float | None
    longitude: float | None
    customer_id: int
    account_id: int
    notes: str | None
    created_at: str
    updated_at: str
    vendor_id: str | None
    properties: dict
    opt_out: bool
    extension: str | None


class GenericCustomer(TypedDict):
    id: int
    firstname: str
    lastname: str
    fullname: str
    business_name: str
    email: str | None
    phone: str | None
    mobile: str | None
    created_at: str
    updated_at: str
    pdf_url: str | None
    address: str
    address_2: str
    city: str
    state: str
    zip: str
    latitude: float | None
    longitude: float | None
    notes: str | None
    get_sms: bool
    opt_out: bool
    disabled: bool
    no_email: bool
    location_name: str | None
    location_id: int | None
    properties: dict
    online_profile_url: str | None
    tax_rate_id: int | None
    notification_email: str
    invoice_cc_emails: str
    invoice_term_id: int | None
    referred_by: str
    ref_customer_id: int | None
    business_and_full_name: str
    business_then_name: str | None
    contacts: list[GenericContact]


class GenericTicketCommentAttribute(TypedDict, total=False):
    subject: str
    body: str
    hidden: bool
    sms_body: str
    do_not_email: bool
    tech: str


GenericTicketProperties = TypedDict(
    'GenericTicketProperties',
    {
        'Device Type': str,
        'Maker': str,
    },
    total=False,
)


class GenericTicketComment(TypedDict):
    id: int
    created_at: str
    updated_at: str
    ticket_id: int
    subject: str
    body: str
    tech: str | None
    hidden: bool
    user_id: int | None


class GenericRMMStoreTriggers(TypedDict):
    bsod_triggered: str
    time_triggered: str
    no_av_triggered: str
    defrag_triggered: str
    firewall_triggered: str
    app_crash_triggered: str
    low_hd_space_triggered: str
    smart_failure_triggered: str
    device_manager_triggered: str
    agent_offline_triggered: str


class GenericRMMStore(TypedDict):
    id: int
    asset_id: int
    account_id: int
    triggers: GenericRMMStoreTriggers
    windows_updates: dict
    emsisoft: dict
    general: dict
    created_at: str
    updated_at: str
    override_alert_agent_offline_mins: str
    override_alert_agent_rearm_after_mins: str
    override_low_hd_threshold: str
    override_autoresolve_offline_alert: str


class GenericTicketAsset(TypedDict):
    id: int
    name: str
    customer_id: int
    created_at: str
    updated_at: str
    properties: dict
    asset_type: str
    asset_serial: str
    external_rmm_link: str
    customer: GenericCustomer
    rmm_links: list
    rmm_store: GenericRMMStore


class GenericTicketFieldAnswer(TypedDict):
    id: int
    ticket_field_id: int
    content: str
    created_at: str
    updated_at: str
    account_id: int


class GenericTicketField(TypedDict):
    id: int
    name: str
    field_type: str
    required: str
    account_id: int
    created_at: str
    updated_at: str
    ticket_type_id: int
    hidden: bool
    position: str
    answers: list[GenericTicketFieldAnswer]


GenericUser = TypedDict(
    'GenericUser',
    {
        'id': int,
        'email': str,
        'full_name': str,
        'created_at': str,
        'updated_at': str,
        'group': str,
        'admin?': bool,
        'color': str,
    },
)


class GenericTicketType(TypedDict):
    id: int
    name: str
    account_id: int
    created_at: str
    updated_at: str
    disabled: bool
    intake_terms: str
    skip_intake: bool
    outtake_terms: str
    skip_outtake: bool
    ticket_fields: list[GenericTicketField]


class DetailedTicket(TypedDict):
    id: int
    number: int
    subject: str
    created_at: str
    customer_id: int
    customer_business_then_name: str
    due_date: str
    start_at: str | None
    end_at: str | None
    location_id: int | None
    problem_type: str
    status: str
    properties: GenericTicketProperties
    user_id: int
    updated_at: str
    pdf_url: str | None
    intake_form_html: str | None
    signature_name: str | None
    signature_date: str | None
    asset_ids: list[int]
    priority: str | None
    resolved_at: str | None
    outtake_form_name: str | None
    outtake_form_date: str | None
    outtake_form_html: str | None
    comments: list[GenericTicketComment]
    attachments: list
    ticket_timers: list
    line_items: list
    worksheet_results: list
    assets: list[GenericTicketAsset]
    appointments: list
    ticket_fields: list[GenericTicketField]
    customer: GenericCustomer
    contact: GenericContact
    user: GenericUser
    ticket_type: GenericTicketType | None


class GenericTicket(TypedDict):
    id: int
    number: int
    subject: str
    created_at: str
    customer_id: int
    customer_business_then_name: str
    due_date: str
    resolved_at: str | None
    start_at: str | None
    end_at: str | None
    location_id: int | None
    problem_type: str
    status: str
    ticket_type_id: int | None
    properties: GenericTicketProperties
    user_id: int | None
    updated_at: str
    pdf_url: str | None
    priority: str | None
    comments: list[GenericTicketComment]
    user: GenericUser | None


class GenericTicketsSettingsUser(TypedDict):
    id: int
    name: str


class GenericTicketsSettings(TypedDict):
    ticket_status_list: list[str]
    default_labor_product_id: Any
    ticket_timer_charge_by_default: Any
    saved_searches: list
    ticket_types: list
    ticket_type_fields: list
    ticket_type_field_answers: list
    appointment_types: list
    users: list[GenericTicketsSettingsUser]
    dashboard_settings: Any
    worksheet_templates: list
    require_ticket_type: Any
    require_intake_form_with_ticket: Any
    require_outtake_form_with_ticket: Any
    ticket_workflow_default_id: Any


UserIdAndName = tuple[int, str]


class GenericCustomerRequestBody(TypedDict, total=False):
    business_name: str
    firstname: str
    lastname: str
    email: str
    phone: str
    mobile: str
    address: str
    address_2: str
    city: str
    state: str
    zip: str
    notes: str
    get_sms: bool
    opt_out: bool
    no_email: bool
    get_billing: bool
    get_marketing: bool
    get_reports: bool
    ref_customer_id: int
    referred_by: str
    tax_rate_id: int
    notification_email: str
    invoice_cc_emails: str
    invoice_term_id: int
    properties: dict
    consent: dict


class GenericCustomerResponse(TypedDict):
    customer: GenericCustomer


class GenericDetailedTicketResponse(TypedDict):
    ticket: DetailedTicket


# ***************
# *** Wrapper ***
# ***************


class SyncroAPIInitKwargs(TypedDict, total=False):
    api_key: str
    bitwarden_id: str
    use_saved_bitwarden_credentials: bool
    raise_for_status: bool


class BitWardenItemField(TypedDict, total=False):
    name: str
    value: str
    type: int
    linkedId: str


class BitWardenLogin(TypedDict, total=False):
    username: str
    password: str
    totp: str
    passwordRevisionDate: str


class BitWardenItem(TypedDict, total=False):
    object: str
    id: str
    organizationId: str
    folderId: str
    type: int
    reprompt: int
    name: str
    notes: str
    favorite: bool
    fields: list[BitWardenItemField]
    login: BitWardenLogin
    collectionIds: list[str]
    revisionDate: str
    creationDate: str
    deletedDate: str


class LoopRequestsKwargs(TypedDict, total=False):
    max_loops: IntGtZero
    data_list_key: str


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


class GetContactsParams(TypedDict, total=False):
    customer_id: int
    page: int


GetContactsResponseContact = GenericContact


class CreateContactRequestBody(TypedDict, total=False):
    customer_id: Required[int]
    name: str
    address1: str
    address2: str
    city: str
    state: str
    zip: str
    email: str
    phone: str
    mobile: str
    notes: str


CreateContactResponse = GenericContact


GetContactByIdResponse = GenericContact


class UpdateContactByIdRequestBody(TypedDict, total=False):
    name: Required[str]
    customer_id: int
    address1: str
    address2: str
    city: str
    state: str
    zip: str
    email: str
    phone: str
    title: str
    mobile: str
    notes: str


UpdateContactByIdResponse = GenericContact


# ****************
# *** Contract ***
# ****************

# ****************
# *** Customer ***
# ****************


class GetCustomersParams(TypedDict, total=False):
    sort: str
    query: str
    firstname: str
    lastname: str
    business_name: str
    id: list[int]
    email: str
    include_disabled: str
    page: int


GetCustomersResponseCustomer = GenericCustomer


CreateCustomerRequestBody = GenericCustomerRequestBody


CreateCustomerResponse = GenericCustomerResponse


class CustomerTicketLink(TypedDict):
    id: int
    number: int
    status: str
    subject: str


class CustomerInvoiceLink(TypedDict):
    id: int
    number: str
    took_payment: bool
    total: str
    date: str


class CustomerContract(TypedDict):
    account_id: int
    id: int
    description: str
    name: str
    customer_id: int
    contract_amount: str
    start_date: str | None
    end_date: str | None
    primary_contact: str
    created_at: str
    updated_at: str
    status: str
    likelihood: int
    apply_to_all: bool
    sla_id: int


class GetCustomerByIdResponseCustomer(TypedDict):
    id: int
    firstname: str
    lastname: str
    fullname: str
    business_name: str
    email: str | None
    phone: str | None
    mobile: str | None
    created_at: str
    updated_at: str
    pdf_url: str | None
    address: str
    address_2: str
    city: str
    state: str
    zip: str
    latitude: float | None
    longitude: float | None
    notes: str | None
    get_sms: bool
    opt_out: bool
    location_name: str | None
    location_id: int | None
    properties: dict
    online_profile_url: str | None
    disabled: bool
    ticket_links: list[CustomerTicketLink]
    invoice_links: list[CustomerInvoiceLink]
    kabuto_customer_id: int
    recurring_invoices: list
    tax_rate_id: int | None
    no_email: bool
    notification_email: str
    invoice_cc_emails: str
    invoice_term_id: int | None
    referred_by: str
    ref_customer_id: int | None
    business_and_full_name: str
    prepay_hours: str | None
    enable_internal_warning: bool
    internal_warning_value: str
    default_device_policy_id: int
    since_updated_at: str
    contacts: list[GenericContact]
    phones: list
    contracts: list[CustomerContract]
    addresses: list


class GetCustomerByIdResponse(TypedDict):
    customer: GetCustomerByIdResponseCustomer


UpdateCustomerByIdRequestBody = GenericCustomerRequestBody


UpdateCustomerByIdResponse = GenericCustomerResponse


GetLatestCustomerResponse = GenericCustomerResponse


GetAutocompleteCustomersResponseCustomer = GenericCustomer


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


class GetRMMAlertsParams(TypedDict, total=False):
    status: Literal["resolved", "all", "active"]
    page: int


class GetRMMAlertsResponseRMMAlert(TypedDict):
    id: int
    customer_id: int
    ticket_number: int | None
    ticket_status: str | None
    computer_name: str
    properties: dict
    resolved: bool
    check_id: int | None
    status: str | None
    formatted_output: str
    description: str
    created_at: str
    updated_at: str
    asset_id: int


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


class GetTicketTimersParams(TypedDict, total=False):
    created_at_lt: DateStrYYYYMMDD
    created_at_gt: DateStrYYYYMMDD
    page: int


class GetTicketTimersResponseTimer(TypedDict):
    id: int
    ticket_id: int
    user_id: int
    start_time: str
    end_time: str
    recorded: bool
    created_at: str
    updated_at: str
    billable: bool
    notes: str
    toggl_id: int | None
    product_id: int | None
    comment_id: int | None
    ticket_line_item_id: int | None
    active_duration: int


# **************
# *** Ticket ***
# **************


class GetTicketsParams(TypedDict, total=False):
    customer_id: int
    contact_id: int
    number: str
    resolved_after: DateStrYYYYMMDD
    created_after: DateStrYYYYMMDD
    since_updated_at: DateStrYYYYMMDD
    status: str
    query: str
    user_id: int
    mine: bool
    ticket_search_id: int
    page: int


GetTicketsResponseTicket = GenericTicket


class CreateTicketRequestBody(TypedDict, total=False):
    customer_id: Required[int]
    ticket_type_id: int
    number: str
    subject: str
    due_date: str
    start_at: str
    end_at: str
    location_id: int
    problem_type: str
    status: str
    user_id: int
    properties: dict
    asset_ids: list[int]
    signature_name: str
    signature_data: str
    sla_id: int
    contact_id: int
    priority: str
    outtake_form_data: str
    outtake_form_date: str
    outtake_form_name: str
    comments_attributes: list[GenericTicketCommentAttribute]


CreateTicketResponse = GenericDetailedTicketResponse


GetTicketByIdResponse = GenericDetailedTicketResponse


class UpdateTicketByIdRequestBody(TypedDict, total=False):
    customer_id: int
    ticket_type_id: int
    number: str
    subject: str
    due_date: str
    start_at: str
    end_at: str
    location_id: int
    problem_type: str
    status: str
    user_id: int
    properties: dict
    asset_ids: list[int]
    signature_name: str
    signature_data: str
    sla_id: int | None
    contact_id: int
    priority: str
    outtake_form_data: str
    outtake_form_date: str
    outtake_form_name: str
    comments_attributes: list[GenericTicketCommentAttribute]


UpdateTicketByIdResponse = GenericDetailedTicketResponse


GetTicketsSettingsResponse = GenericTicketsSettings


AddCommentToTicketRequestBody = GenericTicketCommentAttribute


class AddCommentToTicketResponse(TypedDict):
    comment: GenericTicketComment


# ***************
# *** Timelog ***
# ***************

# *******************
# *** User Device ***
# *******************

# ************
# *** User ***
# ************


class UserPermissions(TypedDict):
    asset: ReadWriteDelete
    customer: ReadWriteDelete
    ticket: ReadWriteDelete
    invoice: ReadWriteDelete
    payment: ReadWriteDelete
    worksheet: AddManageDelete
    chat: UserChatPermissions
    script: dict[Literal['execute'], bool]


class GetCurrentUserResponse(TypedDict):
    user_token: str
    user_email: str
    user_name: str
    user_id: int
    admin: bool
    can_use_app: bool
    two_factor_required: bool
    subdomain: str
    default_location: str | None
    enable_multi_locations: bool
    locations_allowed: list
    permissions: UserPermissions


class GetUserByIdResponse(TypedDict):
    user: GenericUser


# **************
# *** Vendor ***
# **************

# *****************
# *** Wiki Page ***
# *****************

# ************************
# *** Worksheet Result ***
# ************************

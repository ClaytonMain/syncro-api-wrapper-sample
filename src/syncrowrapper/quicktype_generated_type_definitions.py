from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, List, Optional, Union
from uuid import UUID

# Generated using https://app.quicktype.io/


class TypeEnum(Enum):
    ARRAY = "array"
    BOOLEAN = "boolean"
    INTEGER = "integer"
    NUMBER = "number"
    OBJECT = "object"
    STRING = "string"


@dataclass
class SchemaValue:
    type: TypeEnum


@dataclass
class LineItemsSchema:
    type: TypeEnum
    properties: Dict[str, SchemaValue]


@dataclass
class PurpleApplicationJSON:
    schema: LineItemsSchema


@dataclass
class CustomerContent:
    application_json: PurpleApplicationJSON


@dataclass
class Customer:
    content: CustomerContent


@dataclass
class FluffyProperties:
    url: SchemaValue
    filename: SchemaValue


@dataclass
class FilesItems:
    type: TypeEnum
    properties: FluffyProperties


@dataclass
class FilesClass:
    type: TypeEnum
    items: FilesItems


@dataclass
class PurpleProperties:
    files: FilesClass


@dataclass
class PurpleSchema:
    type: TypeEnum
    properties: PurpleProperties


@dataclass
class FluffyApplicationJSON:
    schema: PurpleSchema


@dataclass
class FilesContent:
    application_json: FluffyApplicationJSON


@dataclass
class Files:
    content: FilesContent


@dataclass
class LineItemContent:
    application_json: PurpleApplicationJSON


@dataclass
class LineItem:
    content: LineItemContent


@dataclass
class TentacledProperties:
    id: SchemaValue
    line_discount_percent: SchemaValue
    discount_dollars: SchemaValue
    item: SchemaValue
    name: SchemaValue
    price: SchemaValue
    cost: SchemaValue
    taxable: SchemaValue


@dataclass
class FluffySchema:
    type: TypeEnum
    properties: TentacledProperties


@dataclass
class TentacledApplicationJSON:
    schema: FluffySchema


@dataclass
class LineItem2Content:
    application_json: TentacledApplicationJSON


@dataclass
class LineItem2:
    content: LineItem2Content
    description: str


@dataclass
class StickyProperties:
    label: SchemaValue
    number: SchemaValue
    extension: SchemaValue


@dataclass
class TentacledSchema:
    type: TypeEnum
    properties: StickyProperties


@dataclass
class StickyApplicationJSON:
    schema: TentacledSchema


@dataclass
class PhoneContent:
    application_json: StickyApplicationJSON


@dataclass
class Phone:
    content: PhoneContent


@dataclass
class IndigoProperties:
    contact_id: SchemaValue
    customer_id: SchemaValue
    password: SchemaValue
    password_confirmation: SchemaValue
    email: SchemaValue
    portal_group_id: SchemaValue


@dataclass
class StickySchema:
    type: TypeEnum
    properties: IndigoProperties


@dataclass
class IndigoApplicationJSON:
    schema: StickySchema


@dataclass
class PortalUserContent:
    application_json: IndigoApplicationJSON


@dataclass
class PortalUser:
    content: PortalUserContent


@dataclass
class Frequency:
    type: TypeEnum
    enum: List[str]


@dataclass
class NextRun:
    type: TypeEnum
    format: str


@dataclass
class IndecentProperties:
    customer_id: SchemaValue
    email_customer: SchemaValue
    frequency: Frequency
    name: SchemaValue
    next_run: NextRun
    snail_mail: SchemaValue
    charge_mop: SchemaValue
    invoice_unbilled_ticket_charges: SchemaValue
    paused: SchemaValue


@dataclass
class IndigoSchema:
    type: TypeEnum
    properties: IndecentProperties


@dataclass
class IndecentApplicationJSON:
    schema: IndigoSchema


@dataclass
class ScheduleContent:
    application_json: IndecentApplicationJSON


@dataclass
class Schedule:
    content: ScheduleContent


@dataclass
class RecurringTypeID:
    type: TypeEnum
    enum: List[int]


@dataclass
class HilariousProperties:
    product_id: SchemaValue
    cost_cents: SchemaValue
    description: SchemaValue
    name: SchemaValue
    position: SchemaValue
    quantity: SchemaValue
    retail_cents: SchemaValue
    one_time_charge: SchemaValue
    taxable: SchemaValue
    user_id: SchemaValue
    asset_type_id: SchemaValue
    contact_field_type_id: SchemaValue
    contact_field_answer_id: SchemaValue
    recurring_type_id: RecurringTypeID
    saved_asset_search_id: SchemaValue


@dataclass
class IndecentSchema:
    type: TypeEnum
    properties: HilariousProperties


@dataclass
class HilariousApplicationJSON:
    schema: IndecentSchema


@dataclass
class ScheduleLineItemContent:
    application_json: HilariousApplicationJSON


@dataclass
class ScheduleLineItem:
    content: ScheduleLineItemContent


@dataclass
class IDS:
    type: TypeEnum
    items: SchemaValue


@dataclass
class CunningProperties:
    subject: SchemaValue
    body: SchemaValue
    hidden: SchemaValue
    sms_body: SchemaValue
    do_not_email: SchemaValue
    tech: SchemaValue


@dataclass
class CommentsAttributesSchema:
    type: TypeEnum
    properties: CunningProperties


@dataclass
class CommentsAttributes:
    type: TypeEnum
    items: CommentsAttributesSchema


@dataclass
class ParamsClass:
    pass


@dataclass
class ContactsClass:
    type: TypeEnum
    properties: ParamsClass


@dataclass
class AmbitiousProperties:
    customer_id: SchemaValue
    ticket_type_id: SchemaValue
    number: SchemaValue
    subject: SchemaValue
    due_date: NextRun
    start_at: NextRun
    end_at: NextRun
    location_id: SchemaValue
    problem_type: SchemaValue
    status: SchemaValue
    user_id: SchemaValue
    properties: ContactsClass
    asset_ids: IDS
    signature_name: SchemaValue
    signature_data: SchemaValue
    sla_id: SchemaValue
    contact_id: SchemaValue
    priority: SchemaValue
    outtake_form_data: SchemaValue
    outtake_form_date: NextRun
    outtake_form_name: SchemaValue
    comments_attributes: CommentsAttributes


@dataclass
class HilariousSchema:
    type: TypeEnum
    properties: AmbitiousProperties


@dataclass
class AmbitiousApplicationJSON:
    schema: HilariousSchema


@dataclass
class TicketContent:
    application_json: AmbitiousApplicationJSON


@dataclass
class Ticket:
    content: TicketContent


@dataclass
class MagentaProperties:
    timer_entry_id: SchemaValue


@dataclass
class AmbitiousSchema:
    type: TypeEnum
    properties: MagentaProperties


@dataclass
class CunningApplicationJSON:
    schema: AmbitiousSchema


@dataclass
class TimerEntryIDContent:
    application_json: CunningApplicationJSON


@dataclass
class TimerEntryID:
    content: TimerEntryIDContent


@dataclass
class VendorContent:
    application_json: PurpleApplicationJSON


@dataclass
class Vendor:
    content: VendorContent


@dataclass
class RequestBodies:
    vendor: Vendor
    line_item: LineItem
    portal_user: PortalUser
    schedule_line_item: ScheduleLineItem
    timer_entry_id: TimerEntryID
    line_item2: LineItem2
    customer: Customer
    phone: Phone
    files: Files
    schedule: Schedule
    ticket: Ticket


@dataclass
class BearerAuth:
    type: str
    bearer_auth_in: str
    name: str
    scheme: str


@dataclass
class SecuritySchemes:
    bearer_auth: BearerAuth


@dataclass
class Components:
    request_bodies: RequestBodies
    security_schemes: SecuritySchemes


@dataclass
class ExternalDocs:
    description: str
    url: str


@dataclass
class Contact:
    email: str
    url: str
    name: str


@dataclass
class Info:
    title: str
    version: str
    description: str
    contact: Contact


@dataclass
class AppointmentTypeElement:
    id: int
    account_id: int
    name: str
    email_instructions: TypeEnum
    location_type: str
    location_hard_code: None
    created_at: str
    updated_at: str
    buffer: None
    appointment_reminders_schedule_id: None


@dataclass
class PurpleExample:
    appointment_types: List[AppointmentTypeElement]


@dataclass
class MagentaApplicationJSON:
    example: PurpleExample


@dataclass
class PurpleContent:
    application_json: MagentaApplicationJSON


@dataclass
class Purple200:
    description: str
    content: PurpleContent


@dataclass
class PurpleResponses:
    the_200: Purple200


@dataclass
class PostSecurity:
    bearer_auth: List[Any]


@dataclass
class AppointmentTypesGet:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    responses: PurpleResponses


@dataclass
class FriskyProperties:
    name: SchemaValue
    email_instructions: SchemaValue
    location_type: SchemaValue
    location_hard_code: SchemaValue


@dataclass
class CunningSchema:
    type: TypeEnum
    properties: FriskyProperties
    required: List[str]


@dataclass
class FriskyApplicationJSON:
    schema: CunningSchema


@dataclass
class FluffyContent:
    application_json: FriskyApplicationJSON


@dataclass
class PurpleRequestBody:
    content: FluffyContent
    description: str


@dataclass
class PurpleRecord:
    id: None
    account_id: int
    name: str
    email_instructions: None
    location_type: None
    location_hard_code: None
    created_at: None
    updated_at: None
    buffer: None
    appointment_reminders_schedule_id: None


@dataclass
class FluffyExample:
    appointment_type: Optional[AppointmentTypeElement] = None
    record: Optional[PurpleRecord] = None
    errors: Optional[str] = None


@dataclass
class MischievousApplicationJSON:
    example: FluffyExample


@dataclass
class TentacledContent:
    application_json: MischievousApplicationJSON


@dataclass
class PurpleResponse:
    description: str
    content: TentacledContent


@dataclass
class AppointmentTypesPost:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    request_body: PurpleRequestBody
    responses: Dict[str, PurpleResponse]


@dataclass
class AppointmentTypes:
    get: AppointmentTypesGet
    post: AppointmentTypesPost


@dataclass
class PurpleParameter:
    name: str
    parameter_in: str
    required: bool
    schema: SchemaValue


@dataclass
class ParamsValue:
    description: str


@dataclass
class AppointmentTypesIDDelete:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    responses: Dict[str, ParamsValue]


@dataclass
class BraggadociousApplicationJSON:
    example: AppointmentTypeElement


@dataclass
class StickyContent:
    application_json: BraggadociousApplicationJSON


@dataclass
class FluffyResponse:
    description: str
    content: Optional[StickyContent] = None


@dataclass
class AppointmentTypesIDGet:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    responses: Dict[str, FluffyResponse]


@dataclass
class MagentaSchema:
    type: TypeEnum
    properties: FriskyProperties


@dataclass
class ApplicationJSON1:
    schema: MagentaSchema


@dataclass
class IndigoContent:
    application_json: ApplicationJSON1


@dataclass
class FluffyRequestBody:
    content: IndigoContent
    description: str


@dataclass
class AppointmentTypesIDPut:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    request_body: FluffyRequestBody
    responses: Dict[str, ParamsValue]


@dataclass
class AppointmentTypesID:
    get: AppointmentTypesIDGet
    put: AppointmentTypesIDPut
    delete: AppointmentTypesIDDelete


class In(Enum):
    QUERY = "query"


@dataclass
class FriskySchema:
    type: TypeEnum
    format: Optional[str] = None


@dataclass
class FluffyParameter:
    name: str
    parameter_in: In
    description: str
    schema: FriskySchema
    required: Optional[bool] = None


@dataclass
class CustomerElement:
    id: int
    firstname: str
    lastname: str
    fullname: str
    business_name: None
    email: str
    phone: str
    mobile: None
    created_at: str
    updated_at: str
    pdf_url: None
    address: None
    address_2: None
    city: None
    state: None
    zip: None
    latitude: None
    longitude: None
    notes: None
    get_sms: bool
    opt_out: bool
    disabled: bool
    no_email: bool
    location_name: None
    location_id: None
    properties: ParamsClass
    online_profile_url: str
    tax_rate_id: None
    notification_email: None
    invoice_cc_emails: None
    invoice_term_id: None
    referred_by: None
    ref_customer_id: None
    business_and_full_name: str
    business_then_name: str
    contacts: List[Any]


@dataclass
class AppointmentAppointment:
    id: int
    summary: str
    description: str
    customer_id: int
    created_at: str
    updated_at: str
    start_at: str
    end_at: str
    duration: int
    location: str
    ticket_id: None
    appointment_location_type: None
    start_at_label: str
    all_day: None
    ticket: None
    do_not_email: str
    customer: CustomerElement


@dataclass
class AppointmentElement:
    appointment: AppointmentAppointment


@dataclass
class TentacledExample:
    appointments: List[AppointmentElement]


@dataclass
class ApplicationJSON2:
    example: TentacledExample


@dataclass
class IndecentContent:
    application_json: ApplicationJSON2


@dataclass
class Fluffy200:
    description: str
    content: IndecentContent


@dataclass
class FluffyResponses:
    the_200: Fluffy200


@dataclass
class AppointmentsGet:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[FluffyParameter]
    responses: FluffyResponses


@dataclass
class MischievousProperties:
    description: SchemaValue
    user_ids: IDS
    ticket_id: SchemaValue
    do_not_email: SchemaValue
    user_id: SchemaValue
    start_at: NextRun
    end_at: NextRun
    location: SchemaValue
    summary: SchemaValue
    email_customer: SchemaValue
    appointment_duration: SchemaValue
    appointment_type_id: SchemaValue
    customer_id: SchemaValue
    all_day: SchemaValue


@dataclass
class MischievousSchema:
    type: TypeEnum
    properties: MischievousProperties
    required: List[str]


@dataclass
class ApplicationJSON3:
    schema: MischievousSchema


@dataclass
class HilariousContent:
    application_json: ApplicationJSON3


@dataclass
class TentacledRequestBody:
    content: HilariousContent
    description: str


@dataclass
class StickyExample:
    appointment: Optional[AppointmentAppointment] = None
    success: Optional[bool] = None
    error: Optional[str] = None
    message: Optional[str] = None
    params: Optional[ParamsValue] = None


@dataclass
class ApplicationJSON4:
    example: StickyExample


@dataclass
class AmbitiousContent:
    application_json: ApplicationJSON4


@dataclass
class TentacledResponse:
    description: str
    content: AmbitiousContent


@dataclass
class AppointmentsPost:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    request_body: TentacledRequestBody
    responses: Dict[str, TentacledResponse]


@dataclass
class Appointments:
    get: AppointmentsGet
    post: AppointmentsPost


@dataclass
class AllDay:
    type: TypeEnum
    nullable: bool


@dataclass
class Properties1:
    id: SchemaValue
    firstname: SchemaValue
    lastname: SchemaValue
    fullname: SchemaValue
    business_name: SchemaValue
    email: SchemaValue
    phone: SchemaValue
    mobile: AllDay
    created_at: SchemaValue
    updated_at: SchemaValue
    pdf_url: AllDay
    address: AllDay
    address_2: AllDay
    city: AllDay
    state: AllDay
    zip: AllDay
    latitude: AllDay
    longitude: AllDay
    notes: AllDay
    get_sms: SchemaValue
    opt_out: SchemaValue
    disabled: SchemaValue
    no_email: SchemaValue
    location_name: AllDay
    location_id: AllDay
    properties: ContactsClass
    online_profile_url: SchemaValue
    referred_by: AllDay
    ref_customer_id: AllDay
    tax_rate_id: AllDay
    notification_email: AllDay
    invoice_cc_emails: AllDay
    invoice_term_id: AllDay
    business_and_full_name: SchemaValue
    business_then_name: SchemaValue
    contacts: ContactsClass


@dataclass
class PurpleCustomer:
    type: TypeEnum
    properties: Properties1


@dataclass
class PropertiesTicket:
    type: TypeEnum
    properties: ParamsClass
    nullable: bool


@dataclass
class BraggadociousProperties:
    id: SchemaValue
    summary: SchemaValue
    description: SchemaValue
    customer_id: SchemaValue
    created_at: SchemaValue
    updated_at: SchemaValue
    start_at: SchemaValue
    end_at: SchemaValue
    duration: SchemaValue
    location: SchemaValue
    ticket_id: AllDay
    appointment_location_type: AllDay
    start_at_label: SchemaValue
    all_day: AllDay
    ticket: PropertiesTicket
    customer: PurpleCustomer


@dataclass
class BraggadociousSchema:
    type: TypeEnum
    properties: BraggadociousProperties


@dataclass
class Purple:
    schema: BraggadociousSchema


@dataclass
class CunningContent:
    empty: Purple


@dataclass
class StickyResponse:
    description: str
    content: Optional[CunningContent] = None


@dataclass
class AppointmentsIDGet:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    responses: Dict[str, StickyResponse]


@dataclass
class Properties2:
    description: SchemaValue
    user_ids: IDS
    ticket_id: SchemaValue
    user_id: SchemaValue
    start_at: NextRun
    end_at: NextRun
    location: SchemaValue
    summary: SchemaValue
    email_customer: SchemaValue
    appointment_duration: SchemaValue
    appointment_type_id: SchemaValue
    customer_id: SchemaValue
    all_day: SchemaValue


@dataclass
class Schema1:
    type: TypeEnum
    properties: Properties2
    required: List[str]


@dataclass
class ApplicationJSON5:
    schema: Schema1


@dataclass
class MagentaContent:
    application_json: ApplicationJSON5


@dataclass
class StickyRequestBody:
    content: MagentaContent
    description: str


@dataclass
class PurpleParams:
    summary: str


@dataclass
class IndigoExample:
    appointment: Optional[AppointmentAppointment] = None
    success: Optional[bool] = None
    error: Optional[str] = None
    message: Optional[str] = None
    params: Optional[PurpleParams] = None


@dataclass
class ApplicationJSON6:
    example: IndigoExample


@dataclass
class FriskyContent:
    application_json: ApplicationJSON6


@dataclass
class IndigoResponse:
    description: str
    content: FriskyContent


@dataclass
class AppointmentsIDPut:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    request_body: StickyRequestBody
    responses: Dict[str, IndigoResponse]


@dataclass
class AppointmentsID:
    get: AppointmentsIDGet
    put: AppointmentsIDPut
    delete: AppointmentTypesIDDelete


@dataclass
class TentacledParameter:
    name: str
    parameter_in: In
    schema: SchemaValue
    description: Optional[str] = None
    required: Optional[bool] = None


@dataclass
class ExampleData:
    name: str
    ticket_status: str


@dataclass
class IndecentExample:
    data: ExampleData


@dataclass
class ApplicationJSON7:
    example: IndecentExample


@dataclass
class TextPlain:
    example: str


@dataclass
class MischievousContent:
    application_json: ApplicationJSON7
    text_plain: TextPlain


@dataclass
class Tentacled200:
    description: str
    content: MischievousContent


@dataclass
class TentacledResponses:
    the_200: Tentacled200


@dataclass
class PurpleSecurity:
    api_key: List[Any]


@dataclass
class CalleridGet:
    summary: str
    tags: List[str]
    security: List[PurpleSecurity]
    parameters: List[TentacledParameter]
    responses: TentacledResponses


@dataclass
class Callerid:
    get: CalleridGet


@dataclass
class StickyParameter:
    name: str
    parameter_in: In
    description: str
    schema: SchemaValue


@dataclass
class RecordElement:
    id: int
    name: str
    address1: str
    address2: str
    city: str
    state: str
    zip: str
    email: str
    phone: str
    mobile: str
    latitude: float
    longitude: float
    customer_id: int
    account_id: int
    notes: str
    created_at: str
    updated_at: str
    vendor_id: None
    properties: ParamsClass
    opt_out: bool
    extension: None


@dataclass
class PurpleMeta:
    total_pages: int
    total_entries: int
    per_page: int
    page: int


@dataclass
class HilariousExample:
    contacts: Optional[List[RecordElement]] = None
    meta: Optional[PurpleMeta] = None
    error: Optional[str] = None


@dataclass
class ApplicationJSON8:
    example: HilariousExample


@dataclass
class BraggadociousContent:
    application_json: ApplicationJSON8


@dataclass
class IndecentResponse:
    description: str
    content: BraggadociousContent


@dataclass
class ContactsGet:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[StickyParameter]
    responses: Dict[str, IndecentResponse]


@dataclass
class Properties3:
    customer_id: SchemaValue
    name: SchemaValue
    address1: SchemaValue
    address2: SchemaValue
    city: SchemaValue
    state: SchemaValue
    zip: SchemaValue
    email: SchemaValue
    phone: SchemaValue
    mobile: SchemaValue
    notes: SchemaValue


@dataclass
class Schema2:
    type: TypeEnum
    properties: Properties3
    required: List[str]


@dataclass
class ApplicationJSON9:
    schema: Schema2


@dataclass
class Content1:
    application_json: ApplicationJSON9


@dataclass
class IndigoRequestBody:
    content: Content1
    description: str


@dataclass
class FluffyRecord:
    id: None
    name: str
    address1: None
    address2: None
    city: None
    state: None
    zip: None
    email: str
    phone: None
    mobile: None
    latitude: None
    longitude: None
    customer_id: int
    account_id: int
    notes: None
    created_at: None
    updated_at: None
    vendor_id: None
    properties: ParamsClass
    opt_out: bool
    extension: None
    processed_phone: None
    processed_mobile: None


@dataclass
class AmbitiousExample:
    vendor_id: None
    extension: None
    id: Optional[int] = None
    name: Optional[str] = None
    address1: Optional[str] = None
    address2: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zip: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    mobile: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    customer_id: Optional[int] = None
    account_id: Optional[int] = None
    notes: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    properties: Optional[ParamsClass] = None
    opt_out: Optional[bool] = None
    error: Optional[str] = None
    message: Optional[str] = None
    record: Optional[FluffyRecord] = None
    errors: Optional[str] = None


@dataclass
class ApplicationJSON10:
    example: AmbitiousExample


@dataclass
class Content2:
    application_json: ApplicationJSON10


@dataclass
class HilariousResponse:
    description: str
    content: Content2


@dataclass
class ContactsPost:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    request_body: IndigoRequestBody
    responses: Dict[str, HilariousResponse]


@dataclass
class Contacts:
    get: ContactsGet
    post: ContactsPost


@dataclass
class CunningExample:
    error: str


@dataclass
class ApplicationJSON11:
    example: CunningExample


@dataclass
class Content3:
    application_json: ApplicationJSON11


@dataclass
class AmbitiousResponse:
    description: str
    content: Optional[Content3] = None


@dataclass
class ContactsIDDelete:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    responses: Dict[str, AmbitiousResponse]


@dataclass
class MagentaExample:
    error: Optional[str] = None
    message: Optional[str] = None


@dataclass
class ApplicationJSON12:
    example: MagentaExample


@dataclass
class Properties4:
    id: SchemaValue
    name: SchemaValue
    address1: AllDay
    address2: AllDay
    city: AllDay
    state: AllDay
    zip: AllDay
    email: AllDay
    phone: AllDay
    mobile: AllDay
    latitude: AllDay
    longitud: AllDay
    customer_id: AllDay
    account_id: SchemaValue
    notes: AllDay
    created_at: NextRun
    updated_at: NextRun
    vendor_id: AllDay
    properties: ContactsClass
    opt_out: SchemaValue
    extension: AllDay


@dataclass
class Schema3:
    type: TypeEnum
    properties: Properties4


@dataclass
class Fluffy:
    schema: Schema3


@dataclass
class Content4:
    empty: Optional[Fluffy] = None
    application_json: Optional[ApplicationJSON12] = None


@dataclass
class CunningResponse:
    description: str
    content: Content4


@dataclass
class ContactsIDGet:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    responses: Dict[str, CunningResponse]


@dataclass
class Schema4:
    type: TypeEnum
    properties: Dict[str, SchemaValue]
    required: List[str]


@dataclass
class ApplicationJSON13:
    schema: Schema4


@dataclass
class Content5:
    application_json: ApplicationJSON13


@dataclass
class IndecentRequestBody:
    content: Content5
    description: str


@dataclass
class FriskyExample:
    vendor_id: None
    extension: None
    id: Optional[int] = None
    name: Optional[str] = None
    address1: Optional[str] = None
    address2: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zip: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    mobile: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    customer_id: Optional[int] = None
    account_id: Optional[int] = None
    notes: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    properties: Optional[ParamsClass] = None
    opt_out: Optional[bool] = None
    error: Optional[str] = None
    message: Optional[str] = None
    record: Optional[RecordElement] = None
    errors: Optional[str] = None


@dataclass
class ApplicationJSON14:
    example: FriskyExample


@dataclass
class Content6:
    application_json: ApplicationJSON14


@dataclass
class MagentaResponse:
    description: str
    content: Content6


@dataclass
class ContactsIDPut:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    request_body: IndecentRequestBody
    responses: Dict[str, MagentaResponse]


@dataclass
class ContactsID:
    get: ContactsIDGet
    put: ContactsIDPut
    delete: ContactsIDDelete


@dataclass
class ContractElement:
    id: int
    account_id: int
    customer_id: int
    name: str
    contract_amount: str
    start_date: str
    end_date: str
    primary_contact: None
    description: str
    created_at: str
    updated_at: str
    status: str
    likelihood: int
    apply_to_all: bool
    sla_id: None


@dataclass
class MischievousExample:
    contracts: List[ContractElement]
    meta: PurpleMeta


@dataclass
class ApplicationJSON15:
    example: MischievousExample


@dataclass
class Content7:
    application_json: ApplicationJSON15


@dataclass
class Sticky200:
    description: str
    content: Content7


@dataclass
class StickyResponses:
    the_200: Sticky200


@dataclass
class ContractsGet:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[StickyParameter]
    responses: StickyResponses


@dataclass
class Properties5:
    contract_amount: SchemaValue
    customer_id: SchemaValue
    description: SchemaValue
    start_date: NextRun
    end_date: NextRun
    name: SchemaValue
    primary_contact: SchemaValue
    status: SchemaValue
    likelihood: SchemaValue
    apply_to_all: SchemaValue
    sla_id: SchemaValue


@dataclass
class Schema5:
    type: TypeEnum
    properties: Properties5
    required: List[str]


@dataclass
class ApplicationJSON16:
    schema: Schema5


@dataclass
class Content8:
    application_json: ApplicationJSON16


@dataclass
class HilariousRequestBody:
    content: Content8
    description: str


@dataclass
class TentacledRecord:
    id: None
    account_id: int
    customer_id: None
    name: str
    contract_amount: None
    start_date: None
    end_date: None
    primary_contact: None
    description: str
    created_at: None
    updated_at: None
    status: str
    likelihood: int
    apply_to_all: bool
    sla_id: None


@dataclass
class BraggadociousExample:
    primary_contact: None
    sla_id: None
    id: Optional[int] = None
    account_id: Optional[int] = None
    customer_id: Optional[int] = None
    name: Optional[str] = None
    contract_amount: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    description: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    status: Optional[str] = None
    likelihood: Optional[int] = None
    apply_to_all: Optional[bool] = None
    record: Optional[TentacledRecord] = None
    errors: Optional[str] = None


@dataclass
class ApplicationJSON17:
    example: BraggadociousExample


@dataclass
class Content9:
    application_json: ApplicationJSON17


@dataclass
class FriskyResponse:
    description: str
    content: Content9


@dataclass
class ContractsPost:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    request_body: HilariousRequestBody
    responses: Dict[str, FriskyResponse]


@dataclass
class Contracts:
    get: ContractsGet
    post: ContractsPost


@dataclass
class ApplicationJSON18:
    example: ContractElement


@dataclass
class Content10:
    application_json: ApplicationJSON18


@dataclass
class Indigo200:
    description: str
    content: Content10


@dataclass
class IndigoResponses:
    the_200: Indigo200


@dataclass
class ContractsIDGet:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    responses: IndigoResponses


@dataclass
class Content11:
    application_json: ApplicationJSON16


@dataclass
class AmbitiousRequestBody:
    content: Content11
    description: str


@dataclass
class Example1:
    primary_contact: None
    sla_id: None
    id: Optional[int] = None
    account_id: Optional[int] = None
    customer_id: Optional[int] = None
    name: Optional[str] = None
    contract_amount: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    description: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    status: Optional[str] = None
    likelihood: Optional[int] = None
    apply_to_all: Optional[bool] = None
    record: Optional[ContractElement] = None
    errors: Optional[str] = None


@dataclass
class ApplicationJSON19:
    example: Example1


@dataclass
class Content12:
    application_json: ApplicationJSON19


@dataclass
class MischievousResponse:
    description: str
    content: Content12


@dataclass
class ContractsIDPut:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    request_body: AmbitiousRequestBody
    responses: Dict[str, MischievousResponse]


@dataclass
class ContractsID:
    get: ContractsIDGet
    put: ContractsIDPut
    delete: AppointmentTypesIDDelete


@dataclass
class IndigoParameter:
    name: str
    parameter_in: In
    description: str
    required: bool
    schema: SchemaValue


@dataclass
class Address:
    id: int
    name: str
    customer_id: int
    address_type_id: int
    address1: str
    address2: str
    city: str
    state: str
    zip: str
    latitude: None
    longitude: None
    created_at: str
    updated_at: str
    account_id: int


@dataclass
class AssetCustomer:
    id: int
    firstname: str
    lastname: str
    fullname: str
    business_name: None
    email: str
    phone: str
    mobile: None
    created_at: str
    updated_at: str
    pdf_url: None
    address: None
    address_2: None
    city: None
    state: None
    zip: None
    latitude: None
    longitude: None
    notes: None
    get_sms: bool
    opt_out: bool
    disabled: bool
    no_email: bool
    location_id: None
    properties: ParamsClass
    online_profile_url: str
    tax_rate_id: None
    notification_email: None
    invoice_cc_emails: None
    invoice_term_id: None
    referred_by: None
    ref_customer_id: None
    business_and_full_name: str
    business_then_name: str


@dataclass
class Properties6:
    os: int
    size: str


@dataclass
class Triggers:
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


@dataclass
class RmmStore:
    id: int
    asset_id: int
    account_id: int
    triggers: Triggers
    windows_updates: ParamsClass
    emsisoft: ParamsClass
    general: ParamsClass
    created_at: str
    updated_at: str
    override_alert_agent_offline_mins: None
    override_alert_agent_rearm_after_mins: None
    override_low_hd_threshold: None
    override_autoresolve_offline_alert: None


@dataclass
class ExampleAsset:
    id: int
    name: str
    customer_id: int
    contact_id: None
    created_at: str
    updated_at: str
    properties: Properties6
    asset_type: str
    asset_serial: str
    external_rmm_link: None
    customer: AssetCustomer
    rmm_links: List[Any]
    rmm_store: RmmStore
    address: Address


@dataclass
class Example2:
    assets: List[ExampleAsset]


@dataclass
class ApplicationJSON20:
    example: Example2


@dataclass
class Content13:
    application_json: ApplicationJSON20


@dataclass
class Indecent200:
    description: str
    content: Content13


@dataclass
class IndecentResponses:
    the_200: Indecent200


@dataclass
class CustomerAssetsGet:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[IndigoParameter]
    responses: IndecentResponses


@dataclass
class Properties7:
    asset_type_name: SchemaValue
    asset_type_id: SchemaValue
    properties: SchemaValue
    name: SchemaValue
    customer_id: SchemaValue
    asset_serial: SchemaValue


@dataclass
class Schema6:
    type: TypeEnum
    properties: Properties7
    required: List[str]


@dataclass
class ApplicationJSON21:
    schema: Schema6


@dataclass
class Content14:
    application_json: ApplicationJSON21


@dataclass
class CunningRequestBody:
    content: Content14
    description: str


@dataclass
class FluffyParams:
    name: str


@dataclass
class Example3:
    asset: Optional[ExampleAsset] = None
    success: Optional[bool] = None
    message: Optional[List[str]] = None
    params: Optional[FluffyParams] = None


@dataclass
class ApplicationJSON22:
    example: Example3


@dataclass
class Content15:
    application_json: ApplicationJSON22


@dataclass
class BraggadociousResponse:
    description: str
    content: Content15


@dataclass
class CustomerAssetsPost:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    request_body: CunningRequestBody
    responses: Dict[str, BraggadociousResponse]


@dataclass
class CustomerAssets:
    get: CustomerAssetsGet
    post: CustomerAssetsPost


@dataclass
class ContactID:
    type: List[str]


@dataclass
class Override:
    nullable: bool


@dataclass
class Properties10:
    id: SchemaValue
    asset_id: SchemaValue
    account_id: SchemaValue
    type: TypeEnum
    properties: ParamsClass
    created_at: SchemaValue
    updated_at: SchemaValue
    override_alert_agent_offline_mins: Override
    override_alert_agent_rearm_after_mins: Override
    override_low_hd_threshold: Override
    override_autoresolve_offline_alert: Override
    override_low_hd_thresholds: Override


@dataclass
class RmmLinks:
    type: TypeEnum
    items: List[Any]


@dataclass
class Properties9:
    id: SchemaValue
    name: SchemaValue
    customer_id: ContactID
    contact_id: ContactID
    created_at: SchemaValue
    updated_at: SchemaValue
    type: TypeEnum
    properties: Properties10
    asset_type: SchemaValue
    asset_serial: SchemaValue
    external_rmm_link: ContactID
    customer: ContactID
    rmm_links: RmmLinks
    has_live_chat: SchemaValue
    snmp_enabled: ContactID


@dataclass
class Properties8:
    type: TypeEnum
    properties: Properties9


@dataclass
class Schema7:
    type: TypeEnum
    properties: Properties8
    required: List[Any]


@dataclass
class Tentacled:
    schema: Schema7


@dataclass
class Content16:
    empty: Tentacled


@dataclass
class Response1:
    description: str
    content: Optional[Content16] = None


@dataclass
class CustomerAssetsIDGet:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    responses: Dict[str, Response1]


@dataclass
class Content17:
    application_json: ApplicationJSON21


@dataclass
class MagentaRequestBody:
    content: Content17
    description: str


@dataclass
class Example4:
    success: bool
    message: List[str]


@dataclass
class ApplicationJSON23:
    example: Example4


@dataclass
class Schema8:
    type: TypeEnum
    properties: Properties8
    required: List[Any]


@dataclass
class Sticky:
    schema: Schema8


@dataclass
class Content18:
    empty: Optional[Sticky] = None
    application_json: Optional[ApplicationJSON23] = None


@dataclass
class Response2:
    description: str
    content: Content18


@dataclass
class CustomerAssetsIDPut:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    request_body: MagentaRequestBody
    responses: Dict[str, Response2]


@dataclass
class CustomerAssetsID:
    get: CustomerAssetsIDGet
    put: CustomerAssetsIDPut


@dataclass
class Schema9:
    type: TypeEnum
    items: Optional[SchemaValue] = None
    default: Optional[bool] = None


@dataclass
class IndecentParameter:
    name: str
    parameter_in: In
    required: bool
    description: str
    schema: Schema9


@dataclass
class Example5:
    customers: List[CustomerElement]
    meta: PurpleMeta


@dataclass
class ApplicationJSON24:
    example: Example5


@dataclass
class Content19:
    application_json: ApplicationJSON24


@dataclass
class Hilarious200:
    description: str
    content: Content19


@dataclass
class HilariousResponses:
    the_200: Hilarious200


@dataclass
class CustomersGet:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[IndecentParameter]
    responses: HilariousResponses


@dataclass
class FriskyRequestBody:
    ref: str


@dataclass
class TentacledParams:
    business_name: str
    firstname: str
    lastname: str
    email: str


@dataclass
class Example6:
    customer: Optional[CustomerElement] = None
    success: Optional[bool] = None
    message: Optional[List[str]] = None
    params: Optional[TentacledParams] = None


@dataclass
class ApplicationJSON25:
    example: Example6


@dataclass
class Content20:
    application_json: ApplicationJSON25


@dataclass
class Response3:
    description: str
    content: Content20


@dataclass
class CustomersPost:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    request_body: FriskyRequestBody
    responses: Dict[str, Response3]


@dataclass
class Customers:
    get: CustomersGet
    post: CustomersPost


@dataclass
class HilariousParameter:
    name: In
    parameter_in: In
    description: str
    schema: SchemaValue


@dataclass
class Example7:
    customers: List[CustomerElement]


@dataclass
class ApplicationJSON26:
    example: Example7


@dataclass
class Content21:
    application_json: ApplicationJSON26


@dataclass
class Ambitious200:
    description: str
    content: Content21


@dataclass
class AmbitiousResponses:
    the_200: Ambitious200


@dataclass
class CustomersAutocompleteGet:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    parameters: List[HilariousParameter]
    responses: AmbitiousResponses


@dataclass
class CustomersAutocomplete:
    get: CustomersAutocompleteGet


@dataclass
class PaymentProfile:
    id: int
    customer_id: int
    expiration: str
    customer_external_id: None
    used_gateway: str
    payment_profile_id: int
    last_four: str
    created_at: str
    updated_at: str


@dataclass
class Example9:
    payment_profiles: List[PaymentProfile]


@dataclass
class ApplicationJSON28:
    example: Example9


@dataclass
class Content23:
    application_json: ApplicationJSON28


@dataclass
class Magenta200:
    description: str
    content: Content23


@dataclass
class MagentaResponses:
    the_200: Magenta200


@dataclass
class CustomersCustomerIDPaymentProfilesGet:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    parameters: List[PurpleParameter]
    responses: MagentaResponses


@dataclass
class CustomerExternalID:
    type: TypeEnum
    description: str


@dataclass
class Properties11:
    customer_external_id: CustomerExternalID
    payment_profile_id: CustomerExternalID
    expiration: SchemaValue
    last_four: SchemaValue


@dataclass
class Schema10:
    type: TypeEnum
    properties: Properties11


@dataclass
class ApplicationJSON29:
    schema: Schema10


@dataclass
class Content24:
    application_json: ApplicationJSON29


@dataclass
class MischievousRequestBody:
    content: Content24


@dataclass
class Example10:
    payment_profile: Optional[PaymentProfile] = None
    message: Optional[str] = None


@dataclass
class ApplicationJSON30:
    example: Example10


@dataclass
class Content25:
    application_json: ApplicationJSON30


@dataclass
class Response4:
    description: str
    content: Content25


@dataclass
class CustomersCustomerIDPaymentProfilesPost:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    parameters: List[PurpleParameter]
    request_body: MischievousRequestBody
    responses: Dict[str, Response4]


@dataclass
class CustomersCustomerIDPaymentProfiles:
    get: CustomersCustomerIDPaymentProfilesGet
    post: CustomersCustomerIDPaymentProfilesPost


@dataclass
class Example11:
    success: bool


@dataclass
class ApplicationJSON31:
    example: Example11


@dataclass
class Content26:
    application_json: ApplicationJSON31


@dataclass
class Response5:
    description: str
    content: Optional[Content26] = None


@dataclass
class CustomersCustomerIDPaymentProfilesIDDelete:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    parameters: List[PurpleParameter]
    responses: Dict[str, Response5]


@dataclass
class Example12:
    payment_profile: PaymentProfile


@dataclass
class ApplicationJSON32:
    example: Example12


@dataclass
class Content27:
    application_json: ApplicationJSON32


@dataclass
class Response6:
    description: str
    content: Optional[Content27] = None


@dataclass
class CustomersCustomerIDPaymentProfilesIDGet:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    parameters: List[PurpleParameter]
    responses: Dict[str, Response6]


@dataclass
class Properties12:
    expiration: SchemaValue
    last_four: SchemaValue


@dataclass
class Schema11:
    type: TypeEnum
    properties: Properties12


@dataclass
class ApplicationJSON33:
    schema: Schema11


@dataclass
class Content28:
    application_json: ApplicationJSON33


@dataclass
class BraggadociousRequestBody:
    content: Content28


@dataclass
class Frisky200:
    description: str
    content: Content27


@dataclass
class FriskyResponses:
    the_200: Frisky200


@dataclass
class CustomersCustomerIDPaymentProfilesIDPut:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    parameters: List[PurpleParameter]
    request_body: BraggadociousRequestBody
    responses: FriskyResponses


@dataclass
class CustomersCustomerIDPaymentProfilesID:
    get: CustomersCustomerIDPaymentProfilesIDGet
    put: CustomersCustomerIDPaymentProfilesIDPut
    delete: CustomersCustomerIDPaymentProfilesIDDelete


@dataclass
class PhoneElement:
    id: int
    label: str
    number: str
    customer_id: int
    created_at: str
    updated_at: str
    extension: None


@dataclass
class Example13:
    phones: List[PhoneElement]


@dataclass
class ApplicationJSON34:
    example: Example13


@dataclass
class Content29:
    application_json: ApplicationJSON34


@dataclass
class Mischievous200:
    description: str
    content: Content29


@dataclass
class MischievousResponses:
    the_200: Mischievous200


@dataclass
class CustomersCustomerIDPhonesGet:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    responses: MischievousResponses


@dataclass
class StickyParams:
    customer_id: str
    number: str


@dataclass
class Example14:
    label: None
    extension: None
    id: Optional[int] = None
    number: Optional[str] = None
    customer_id: Optional[int] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    success: Optional[bool] = None
    message: Optional[List[str]] = None
    params: Optional[StickyParams] = None


@dataclass
class ApplicationJSON35:
    example: Example14


@dataclass
class Content30:
    application_json: ApplicationJSON35


@dataclass
class Response7:
    description: str
    content: Content30


@dataclass
class CustomersCustomerIDPhonesPost:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    request_body: FriskyRequestBody
    responses: Dict[str, Response7]


@dataclass
class CustomersCustomerIDPhones:
    get: CustomersCustomerIDPhonesGet
    post: CustomersCustomerIDPhonesPost


@dataclass
class IndigoParams:
    customer_id: str
    id: str
    number: str


@dataclass
class Example15:
    label: None
    extension: None
    id: Optional[int] = None
    number: Optional[str] = None
    customer_id: Optional[int] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    success: Optional[bool] = None
    message: Optional[List[str]] = None
    params: Optional[IndigoParams] = None


@dataclass
class ApplicationJSON36:
    example: Example15


@dataclass
class Content31:
    application_json: ApplicationJSON36


@dataclass
class Response8:
    description: str
    content: Content31


@dataclass
class CustomersCustomerIDPhonesIDPut:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    request_body: FriskyRequestBody
    responses: Dict[str, Response8]


@dataclass
class CustomersCustomerIDPhonesID:
    put: CustomersCustomerIDPhonesIDPut
    delete: AppointmentTypesIDDelete


@dataclass
class Example16:
    message: str


@dataclass
class ApplicationJSON37:
    example: Example16


@dataclass
class Content32:
    application_json: ApplicationJSON37


@dataclass
class Response9:
    description: str
    content: Optional[Content32] = None


@dataclass
class CustomersIDDelete:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    responses: Dict[str, Response9]


@dataclass
class Example8:
    customer: CustomerElement


@dataclass
class ApplicationJSON27:
    example: Example8


@dataclass
class Content22:
    application_json: ApplicationJSON27


@dataclass
class Response10:
    description: str
    content: Optional[Content22] = None


@dataclass
class CustomersIDGet:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    responses: Dict[str, Response10]


@dataclass
class Example17:
    customer: Optional[CustomerElement] = None
    success: Optional[bool] = None
    message: Optional[List[str]] = None


@dataclass
class ApplicationJSON38:
    example: Example17


@dataclass
class Content33:
    application_json: ApplicationJSON38


@dataclass
class Response11:
    description: str
    content: Content33


@dataclass
class CustomersIDPut:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    request_body: FriskyRequestBody
    responses: Dict[str, Response11]


@dataclass
class CustomersID:
    get: CustomersIDGet
    put: CustomersIDPut
    delete: CustomersIDDelete


@dataclass
class Cunning200:
    description: str
    content: Content22


@dataclass
class CunningResponses:
    the_200: Cunning200


@dataclass
class CustomersLatestGet:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    responses: CunningResponses


@dataclass
class CustomersLatest:
    get: CustomersLatestGet


@dataclass
class EstimateElement:
    id: int
    customer_id: int
    customer_business_then_name: str
    number: str
    status: str
    created_at: str
    updated_at: str
    date: str
    subtotal: str
    total: str
    tax: str
    ticket_id: None
    pdf_url: None
    location_id: None
    invoice_id: None
    employee: str


@dataclass
class FluffyMeta:
    total_pages: int
    page: int


@dataclass
class Example18:
    estimates: List[EstimateElement]
    meta: FluffyMeta


@dataclass
class ApplicationJSON39:
    example: Example18


@dataclass
class Content34:
    application_json: ApplicationJSON39


@dataclass
class Braggadocious200:
    description: str
    content: Content34


@dataclass
class BraggadociousResponses:
    the_200: Braggadocious200


@dataclass
class EstimatesGet:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[StickyParameter]
    responses: BraggadociousResponses


@dataclass
class Properties14:
    item: SchemaValue
    name: SchemaValue
    product_id: SchemaValue
    quantity: SchemaValue


@dataclass
class PurpleItems:
    type: TypeEnum
    properties: Properties14


@dataclass
class PurpleLineItems:
    type: TypeEnum
    description: str
    items: PurpleItems


@dataclass
class Properties13:
    number: SchemaValue
    date: NextRun
    customer_id: SchemaValue
    note: SchemaValue
    status: CustomerExternalID
    ticket_id: SchemaValue
    location_id: SchemaValue
    line_items: PurpleLineItems
    created_at: NextRun
    updated_at: NextRun


@dataclass
class Schema12:
    type: TypeEnum
    properties: Properties13


@dataclass
class ApplicationJSON40:
    schema: Schema12


@dataclass
class Content35:
    application_json: ApplicationJSON40


@dataclass
class RequestBody1:
    content: Content35


@dataclass
class Example19:
    estimate: Optional[EstimateElement] = None
    customer_id: Optional[List[str]] = None
    date: Optional[List[str]] = None


@dataclass
class ApplicationJSON41:
    example: Example19


@dataclass
class Content36:
    application_json: ApplicationJSON41


@dataclass
class Response12:
    description: str
    content: Content36


@dataclass
class EstimatesPost:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    request_body: RequestBody1
    responses: Dict[str, Response12]


@dataclass
class Estimates:
    get: EstimatesGet
    post: EstimatesPost


@dataclass
class The200_Value:
    description: str
    content: Content32


@dataclass
class Responses1:
    the_200: The200_Value


@dataclass
class EstimatesIDDelete:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    responses: Responses1


@dataclass
class AmbitiousParameter:
    name: str
    parameter_in: str
    description: str
    schema: SchemaValue
    required: Optional[bool] = None


@dataclass
class Example20:
    estimate: EstimateElement


@dataclass
class ApplicationJSON42:
    example: Example20


@dataclass
class Content37:
    application_json: ApplicationJSON42


@dataclass
class The200_1:
    description: str
    content: Content37


@dataclass
class Responses2:
    the_200: The200_1


@dataclass
class EstimatesIDGet:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[AmbitiousParameter]
    responses: Responses2


@dataclass
class Properties15:
    number: SchemaValue
    date: NextRun
    customer_id: SchemaValue
    note: SchemaValue
    status: CustomerExternalID
    ticket_id: SchemaValue
    location_id: SchemaValue


@dataclass
class Schema13:
    type: TypeEnum
    properties: Properties15


@dataclass
class ApplicationJSON43:
    schema: Schema13


@dataclass
class Content38:
    application_json: ApplicationJSON43


@dataclass
class RequestBody2:
    content: Content38


@dataclass
class Example21:
    estimate: Optional[EstimateElement] = None
    date: Optional[List[str]] = None


@dataclass
class ApplicationJSON44:
    example: Example21


@dataclass
class Content39:
    application_json: ApplicationJSON44


@dataclass
class Response13:
    description: str
    content: Content39


@dataclass
class EstimatesIDPut:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    request_body: RequestBody2
    responses: Dict[str, Response13]


@dataclass
class EstimatesID:
    get: EstimatesIDGet
    put: EstimatesIDPut
    delete: EstimatesIDDelete


@dataclass
class PurpleInvoice:
    id: int
    customer_id: int
    customer_business_then_name: str
    number: str
    created_at: str
    updated_at: str
    date: str
    due_date: str
    subtotal: str
    total: str
    tax: str
    verified_paid: bool
    tech_marked_paid: bool
    ticket_id: None
    pdf_url: None
    is_paid: bool
    location_id: None
    po_number: None
    contact_id: None
    note: None
    hardwarecost: str


@dataclass
class Example22:
    invoice: Optional[PurpleInvoice] = None
    error: Optional[str] = None


@dataclass
class ApplicationJSON45:
    example: Example22


@dataclass
class Content40:
    application_json: ApplicationJSON45


@dataclass
class Response14:
    description: str
    content: Content40


@dataclass
class EstimatesIDConvertToInvoicePost:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    responses: Dict[str, Response14]


@dataclass
class EstimatesIDConvertToInvoice:
    post: EstimatesIDConvertToInvoicePost


@dataclass
class Responses3:
    the_200: The200_Value


@dataclass
class EstimatesIDEmailPost:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    responses: Responses3


@dataclass
class EstimatesIDEmail:
    post: EstimatesIDEmailPost


@dataclass
class PDF:
    url: None


@dataclass
class PurpleEstimate:
    account_id: int
    id: int
    updated_at: str
    customer_id: int
    employee: str
    payment_type: str
    number: str
    labor: str
    total: str
    subtotal: str
    tax: str
    paid: bool
    date: str
    status_date: str
    status_changed_by: None
    notax: bool
    ticket_id: None
    note: str
    category: str
    hardwarecost: str
    location_id: None
    pdf: PDF
    signature_data: str
    signature_name: str
    created_at: str
    invoice_id: None
    contact_id: None
    tax_rate_id: int
    converted_at: None
    last_emailed: None
    status: str
    disabled: bool
    signature_date: None
    multi_tax: None
    name: None


@dataclass
class PurpleLineItem:
    id: int
    created_at: str
    updated_at: str
    invoice_id: None
    item: str
    name: str
    cost: str
    price: str
    quantity: str
    product_id: None
    taxable: bool
    discount_percent: None
    position: int
    invoice_bundle_id: None
    discount_dollars: None


@dataclass
class Example23:
    estimate: Optional[PurpleEstimate] = None
    line_item: Optional[PurpleLineItem] = None
    errors: Optional[str] = None


@dataclass
class ApplicationJSON46:
    example: Example23


@dataclass
class Content41:
    application_json: ApplicationJSON46


@dataclass
class Response15:
    description: str
    content: Content41


@dataclass
class EstimatesIDLineItemsPost:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    request_body: FriskyRequestBody
    responses: Dict[str, Response15]


@dataclass
class EstimatesIDLineItems:
    post: EstimatesIDLineItemsPost


@dataclass
class The200_2:
    description: str
    content: Content37


@dataclass
class Responses4:
    the_200: The200_2


@dataclass
class EstimatesIDLineItemsLineItemIDDelete:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    responses: Responses4


@dataclass
class Example24:
    line_item: Optional[PurpleLineItem] = None
    item: Optional[List[str]] = None


@dataclass
class ApplicationJSON47:
    example: Example24


@dataclass
class Content42:
    application_json: ApplicationJSON47


@dataclass
class Response16:
    description: str
    content: Content42


@dataclass
class EstimatesIDLineItemsLineItemIDPut:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    request_body: FriskyRequestBody
    responses: Dict[str, Response16]


@dataclass
class EstimatesIDLineItemsLineItemID:
    put: EstimatesIDLineItemsLineItemIDPut
    delete: EstimatesIDLineItemsLineItemIDDelete


@dataclass
class Responses5:
    the_200: The200_Value


@dataclass
class EstimatesIDPrintPost:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    responses: Responses5


@dataclass
class EstimatesIDPrint:
    post: EstimatesIDPrintPost


@dataclass
class InvoiceElement:
    id: int
    customer_id: int
    customer_business_then_name: str
    number: str
    created_at: str
    updated_at: str
    date: str
    due_date: str
    subtotal: str
    total: str
    tax: str
    verified_paid: bool
    tech_marked_paid: bool
    ticket_id: int
    pdf_url: None
    is_paid: bool
    location_id: None
    po_number: None
    contact_id: None
    note: None
    hardwarecost: None
    user_id: None


@dataclass
class Example25:
    invoices: List[InvoiceElement]
    meta: FluffyMeta


@dataclass
class ApplicationJSON48:
    example: Example25


@dataclass
class Content43:
    application_json: ApplicationJSON48


@dataclass
class The200_3:
    description: str
    content: Content43


@dataclass
class Responses6:
    the_200: The200_3


@dataclass
class InvoicesGet:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[IndigoParameter]
    responses: Responses6


@dataclass
class Hardwarecost:
    type: TypeEnum
    format: TypeEnum


@dataclass
class FluffyLineItems:
    type: TypeEnum
    items: LineItemsSchema


@dataclass
class Properties16:
    id: SchemaValue
    balance_due: SchemaValue
    customer_id: SchemaValue
    number: SchemaValue
    date: NextRun
    customer_business_then_name: SchemaValue
    created_at: NextRun
    updated_at: NextRun
    due_date: NextRun
    subtotal: SchemaValue
    total: SchemaValue
    tax: SchemaValue
    verified_paid: SchemaValue
    tech_marked_paid: SchemaValue
    ticket_id: SchemaValue
    pdf_url: SchemaValue
    is_paid: SchemaValue
    location_id: SchemaValue
    po_number: SchemaValue
    contact_id: SchemaValue
    note: SchemaValue
    hardwarecost: Hardwarecost
    line_items: FluffyLineItems


@dataclass
class Schema14:
    type: TypeEnum
    properties: Properties16
    required: List[str]


@dataclass
class ApplicationJSON49:
    schema: Schema14


@dataclass
class Content44:
    application_json: ApplicationJSON49


@dataclass
class RequestBody3:
    content: Content44
    description: str


@dataclass
class FluffyInvoice:
    id: int
    customer_id: int
    customer_business_then_name: str
    number: str
    created_at: str
    updated_at: str
    date: str
    due_date: str
    subtotal: str
    total: str
    tax: str
    verified_paid: bool
    tech_marked_paid: bool
    ticket_id: None
    pdf_url: None
    is_paid: bool
    location_id: None
    po_number: None
    contact_id: None
    note: None
    hardwarecost: None
    user_id: int


@dataclass
class Example26:
    invoice: FluffyInvoice


@dataclass
class ApplicationJSON50:
    example: Example26


@dataclass
class Content45:
    application_json: ApplicationJSON50


@dataclass
class Response17:
    description: str
    content: Optional[Content45] = None


@dataclass
class InvoicesPost:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    request_body: RequestBody3
    responses: Dict[str, Response17]


@dataclass
class Invoices:
    get: InvoicesGet
    post: InvoicesPost


@dataclass
class CunningParameter:
    name: str
    parameter_in: str
    description: str
    required: bool
    schema: SchemaValue


@dataclass
class Responses7:
    the_200: ParamsValue


@dataclass
class InvoicesIDDelete:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[CunningParameter]
    responses: Responses7


@dataclass
class Properties19:
    email: SchemaValue


@dataclass
class ContactsItems:
    type: TypeEnum
    properties: Properties19


@dataclass
class PropertiesContacts:
    type: TypeEnum
    items: ContactsItems


@dataclass
class Properties18:
    id: SchemaValue
    firstname: SchemaValue
    lastname: SchemaValue
    fullname: SchemaValue
    business_name: SchemaValue
    email: SchemaValue
    phone: SchemaValue
    mobile: SchemaValue
    created_at: SchemaValue
    updated_at: SchemaValue
    pdf_url: SchemaValue
    address: SchemaValue
    address_2: SchemaValue
    city: SchemaValue
    state: SchemaValue
    zip: SchemaValue
    latitude: SchemaValue
    longitude: SchemaValue
    notes: SchemaValue
    get_sms: SchemaValue
    opt_out: SchemaValue
    disabled: SchemaValue
    no_email: SchemaValue
    location_name: SchemaValue
    location_id: SchemaValue
    properties: SchemaValue
    online_profile_url: SchemaValue
    tax_rate_id: SchemaValue
    notification_email: SchemaValue
    invoice_cc_emails: SchemaValue
    invoice_term_id: SchemaValue
    referred_by: SchemaValue
    ref_customer_id: SchemaValue
    business_and_full_name: SchemaValue
    business_then_name: SchemaValue
    contacts: PropertiesContacts


@dataclass
class FluffyCustomer:
    type: TypeEnum
    properties: Properties18


@dataclass
class Properties20:
    item: SchemaValue
    name: SchemaValue


@dataclass
class FluffyItems:
    type: TypeEnum
    properties: Properties20


@dataclass
class TentacledLineItems:
    type: TypeEnum
    items: FluffyItems


@dataclass
class Properties21:
    id: SchemaValue


@dataclass
class PaymentsSchema:
    type: TypeEnum
    properties: Properties21


@dataclass
class Payments:
    type: TypeEnum
    items: PaymentsSchema


@dataclass
class Properties17:
    id: SchemaValue
    number: SchemaValue
    date: NextRun
    date_received: NextRun
    customer_business_then_name: SchemaValue
    created_at: NextRun
    updated_at: NextRun
    due_date: NextRun
    subtotal: SchemaValue
    total: SchemaValue
    tax: SchemaValue
    verified_paid: SchemaValue
    tech_marked_paid: SchemaValue
    ticket_id: SchemaValue
    pdf_url: SchemaValue
    is_paid: SchemaValue
    location_id: SchemaValue
    po_number: SchemaValue
    contact_id: SchemaValue
    note: SchemaValue
    hardwarecost: Hardwarecost
    user_id: SchemaValue
    customer: FluffyCustomer
    line_items: TentacledLineItems
    payments: Payments


@dataclass
class Schema15:
    type: TypeEnum
    properties: Properties17


@dataclass
class ApplicationJSON51:
    schema: Schema15


@dataclass
class Content46:
    application_json: ApplicationJSON51


@dataclass
class Response18:
    description: str
    content: Optional[Content46] = None


@dataclass
class InvoicesIDGet:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[CunningParameter]
    responses: Dict[str, Response18]


@dataclass
class Properties22:
    customer_id: SchemaValue
    number: SchemaValue
    date: NextRun
    customer_business_then_name: SchemaValue
    created_at: NextRun
    updated_at: NextRun
    due_date: NextRun
    subtotal: SchemaValue
    total: SchemaValue
    tax: SchemaValue
    ticket_id: SchemaValue
    pdf_url: SchemaValue
    location_id: SchemaValue
    po_number: SchemaValue
    contact_id: SchemaValue
    note: SchemaValue
    hardwarecost: Hardwarecost


@dataclass
class Schema16:
    type: TypeEnum
    properties: Properties22


@dataclass
class ApplicationJSON52:
    schema: Schema16


@dataclass
class Content47:
    application_json: ApplicationJSON52


@dataclass
class RequestBody4:
    content: Content47
    description: str


@dataclass
class Example27:
    invoice: PurpleInvoice


@dataclass
class ApplicationJSON53:
    example: Example27


@dataclass
class Content48:
    application_json: ApplicationJSON53


@dataclass
class Response19:
    description: str
    content: Optional[Content48] = None


@dataclass
class InvoicesIDPut:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[CunningParameter]
    request_body: RequestBody4
    responses: Dict[str, Response19]


@dataclass
class InvoicesID:
    get: InvoicesIDGet
    put: InvoicesIDPut
    delete: InvoicesIDDelete


@dataclass
class GetClass:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[CunningParameter]
    responses: Dict[str, ParamsValue]


@dataclass
class InvoicesIDEmail:
    post: GetClass


@dataclass
class PutClass:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[CunningParameter]
    request_body: FriskyRequestBody
    responses: Dict[str, ParamsValue]


@dataclass
class InvoicesIDLineItems:
    post: PutClass


@dataclass
class InvoicesIDLineItemsLineItemID:
    put: PutClass
    delete: GetClass


@dataclass
class InvoicesIDPrint:
    post: GetClass


@dataclass
class InvoicesIDTicket:
    get: GetClass


@dataclass
class Item:
    id: int
    requestedon: str
    ticketnum: str
    parturl: str
    shipping: None
    deststore: None
    orderedby: None
    orderedon: None
    trackingnum: str
    receivedon: None
    price: str
    account_id: int
    description: None
    destination_location_id: None
    from_location_id: None
    from_name: None
    received_at: None
    user_id: None
    created_at: str
    updated_at: str
    due_at: None
    ticket_id: None
    logistic_state: None
    product_id: None
    quantity: None
    round_trip: bool
    trip_leg: None
    retail_cents: None
    taxable: bool
    converted: bool
    notes: None
    refurb_id: None
    invoice_id: None


@dataclass
class Example28:
    items: List[Item]
    meta: FluffyMeta


@dataclass
class ApplicationJSON54:
    example: Example28


@dataclass
class Content49:
    application_json: ApplicationJSON54


@dataclass
class The200_4:
    description: str
    content: Content49


@dataclass
class Responses8:
    the_200: The200_4


@dataclass
class ItemsGet:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[IndigoParameter]
    responses: Responses8


@dataclass
class Items:
    get: ItemsGet


@dataclass
class Schema17:
    type: TypeEnum
    items: Optional[SchemaValue] = None


@dataclass
class MagentaParameter:
    name: str
    parameter_in: In
    description: str
    schema: Schema17
    required: Optional[bool] = None


@dataclass
class Lead:
    id: int
    first_name: str
    last_name: str
    email: str
    phone: str
    mobile: str
    created_at: str
    updated_at: str
    address: str
    city: str
    state: str
    zip: str
    ticket_subject: None
    ticket_description: None
    ticket_problem_type: None
    ticket_id: None
    customer_id: int
    contact_id: None
    mailbox_id: None
    mailbox_name: None
    business_then_name: str
    has_attachments: bool
    message_read: bool
    status: str
    user_id: None
    location_id: None


@dataclass
class Example29:
    leads: List[Lead]
    meta: PurpleMeta


@dataclass
class ApplicationJSON55:
    example: Example29


@dataclass
class Content50:
    application_json: ApplicationJSON55


@dataclass
class The200_5:
    description: str
    content: Content50


@dataclass
class Responses9:
    the_200: The200_5


@dataclass
class LeadsGet:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[MagentaParameter]
    responses: Responses9


@dataclass
class Properties23:
    address: SchemaValue
    business_name: SchemaValue
    city: SchemaValue
    zip: SchemaValue
    converted: SchemaValue
    message_read: SchemaValue
    disabled: SchemaValue
    email: SchemaValue
    first_name: SchemaValue
    last_name: SchemaValue
    mobile: SchemaValue
    phone: SchemaValue
    state: SchemaValue
    ticket_description: SchemaValue
    ticket_problem_type: SchemaValue
    ticket_subject: SchemaValue
    location_id: SchemaValue
    from_check_in: SchemaValue
    customer_id: SchemaValue
    ticket_id: SchemaValue
    hidden_notes: SchemaValue
    contact_id: SchemaValue
    appointment_time: SchemaValue
    status: SchemaValue
    user_id: SchemaValue
    ticket_type_id: SchemaValue
    mailbox_id: SchemaValue
    opportunity_start_date: NextRun
    opportunity_amount_dollars: SchemaValue
    likelihood: SchemaValue
    properties: SchemaValue
    ticket_properties: SchemaValue
    customer_purchase_id: SchemaValue
    signature_date: NextRun
    signature_name: SchemaValue
    signature_data: SchemaValue
    appointment_type_id: SchemaValue


@dataclass
class Schema18:
    type: TypeEnum
    properties: Properties23


@dataclass
class ApplicationJSON56:
    schema: Schema18


@dataclass
class Content51:
    application_json: ApplicationJSON56


@dataclass
class RequestBody5:
    content: Content51
    description: str


@dataclass
class IndecentParams:
    from_check_in: bool


@dataclass
class Example30:
    lead: Optional[Lead] = None
    success: Optional[bool] = None
    message: Optional[List[str]] = None
    params: Optional[IndecentParams] = None


@dataclass
class ApplicationJSON57:
    example: Example30


@dataclass
class Content52:
    application_json: ApplicationJSON57


@dataclass
class Response20:
    description: str
    content: Content52


@dataclass
class LeadsPost:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    request_body: RequestBody5
    responses: Dict[str, Response20]


@dataclass
class Leads:
    get: LeadsGet
    post: LeadsPost


@dataclass
class Example31:
    lead: Lead


@dataclass
class ApplicationJSON58:
    example: Example31


@dataclass
class Content53:
    application_json: ApplicationJSON58


@dataclass
class Response21:
    description: str
    content: Optional[Content53] = None


@dataclass
class LeadsIDGet:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    responses: Dict[str, Response21]


@dataclass
class Content54:
    application_json: ApplicationJSON56


@dataclass
class RequestBody6:
    content: Content54
    description: str


@dataclass
class HilariousParams:
    ticket_description: str


@dataclass
class Example32:
    lead: Optional[Lead] = None
    success: Optional[bool] = None
    message: Optional[List[str]] = None
    params: Optional[HilariousParams] = None


@dataclass
class ApplicationJSON59:
    example: Example32


@dataclass
class Content55:
    application_json: ApplicationJSON59


@dataclass
class Response22:
    description: str
    content: Content55


@dataclass
class LeadsIDPut:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    request_body: RequestBody6
    responses: Dict[str, Response22]


@dataclass
class LeadsID:
    get: LeadsIDGet
    put: LeadsIDPut


@dataclass
class LineItemElement:
    id: int
    created_at: str
    updated_at: str
    invoice_id: int
    item: str
    name: str
    cost: str
    price: str
    quantity: str
    product_id: None
    taxable: bool
    discount_percent: None
    position: int
    invoice_bundle_id: None
    discount_dollars: None


@dataclass
class Example33:
    line_items: List[LineItemElement]
    meta: PurpleMeta


@dataclass
class ApplicationJSON60:
    example: Example33


@dataclass
class Content56:
    application_json: ApplicationJSON60


@dataclass
class The200_6:
    description: str
    content: Content56


@dataclass
class Responses10:
    the_200: The200_6


@dataclass
class LineItemsGet:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[IndigoParameter]
    responses: Responses10


@dataclass
class LineItems:
    get: LineItemsGet


@dataclass
class CustomerClass:
    read: bool
    write: bool
    delete: bool


@dataclass
class Script:
    execute: bool


@dataclass
class Worksheet:
    add: bool
    manage: bool
    delete: bool


@dataclass
class Permissions:
    asset: CustomerClass
    customer: CustomerClass
    ticket: CustomerClass
    invoice: CustomerClass
    payment: CustomerClass
    worksheet: Worksheet
    script: Script


@dataclass
class Example34:
    user_token: UUID
    user_email: str
    user_name: str
    user_id: int
    admin: bool
    can_use_app: bool
    two_factor_required: bool
    subdomain: str
    default_location: None
    enable_multi_locations: bool
    locations_allowed: List[Any]
    permissions: Permissions


@dataclass
class ApplicationJSON61:
    example: Example34


@dataclass
class Content57:
    application_json: ApplicationJSON61


@dataclass
class The200_7:
    description: str
    content: Content57


@dataclass
class Responses11:
    the_200: The200_7


@dataclass
class MeGet:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    responses: Responses11


@dataclass
class Me:
    get: MeGet


@dataclass
class CustomerDetailsDefaults:
    placeholder: str


@dataclass
class CustomerDetailsFields:
    firstname: str
    lastname: str
    business_name: str
    email: str
    phone: str
    address: str
    referred_by: str
    tax_rate_id: str
    get_sms: str
    opt_out: str
    no_email: str
    send_portal_invitation: str
    notification_email: str
    invoice_cc_emails: str
    invoice_term_id: str
    custom_fields: str


@dataclass
class DataCustomerDetails:
    fields: CustomerDetailsFields
    defaults: CustomerDetailsDefaults
    position: str


@dataclass
class Ets:
    position: str


@dataclass
class TicketDetailsDefaults:
    placeholder: str
    isapproved: str
    pre_diagnosed: str


@dataclass
class TicketDetailsFields:
    subject: str
    description: str
    user_id: str
    priority: str
    due_date: str
    problem_type: str
    notify_emails: str
    category: str
    address_id: str
    contract_id: str
    sla_id: str
    ticket_type_id: str
    do_not_email: str
    isapproved: str
    pre_diagnosed: str


@dataclass
class DataTicketDetails:
    fields: TicketDetailsFields
    defaults: TicketDetailsDefaults
    disabled: List[str]
    position: str


@dataclass
class NewTicketFormData:
    customer_details: DataCustomerDetails
    ticket_details: DataTicketDetails
    worksheets: Ets
    related_assets: Ets


@dataclass
class NewTicketForm:
    id: int
    name: str
    default: bool
    disabled: bool
    data: NewTicketFormData


@dataclass
class Example35:
    new_ticket_forms: List[NewTicketForm]


@dataclass
class ApplicationJSON62:
    example: Example35


@dataclass
class Content58:
    application_json: ApplicationJSON62


@dataclass
class The200_8:
    description: str
    content: Content58


@dataclass
class Responses12:
    the_200: The200_8


@dataclass
class NewTicketFormsGet:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    responses: Responses12


@dataclass
class NewTicketForms:
    get: NewTicketFormsGet


@dataclass
class Example36:
    new_ticket_form: NewTicketForm


@dataclass
class ApplicationJSON63:
    example: Example36


@dataclass
class Content59:
    application_json: ApplicationJSON63


@dataclass
class Response23:
    description: str
    content: Optional[Content59] = None


@dataclass
class NewTicketFormsIDGet:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    responses: Dict[str, Response23]


@dataclass
class NewTicketFormsID:
    get: NewTicketFormsIDGet


@dataclass
class AppointmentsProperties:
    properties: SchemaValue
    summary: SchemaValue
    description: SchemaValue
    location: SchemaValue
    user_id: SchemaValue
    start_at: NextRun
    end_at: SchemaValue


@dataclass
class PropertiesAppointments:
    type: TypeEnum
    properties: AppointmentsProperties


@dataclass
class CustomerDetailsProperties:
    firstname: SchemaValue
    properties: ContactsClass
    lastname: SchemaValue
    business_name: SchemaValue
    email: SchemaValue
    phone: SchemaValue
    mobile: SchemaValue
    address: SchemaValue
    city: SchemaValue
    state: SchemaValue
    zip: SchemaValue
    get_sms: SchemaValue
    opt_out: SchemaValue
    no_email: SchemaValue


@dataclass
class PropertiesCustomerDetails:
    type: TypeEnum
    properties: CustomerDetailsProperties


@dataclass
class TicketDetailsProperties:
    properties: SchemaValue
    subject: SchemaValue
    problem_type: SchemaValue
    description: SchemaValue
    do_not_email: SchemaValue


@dataclass
class PropertiesTicketDetails:
    type: TypeEnum
    properties: TicketDetailsProperties


@dataclass
class Properties24:
    customer_details: PropertiesCustomerDetails
    ticket_details: PropertiesTicketDetails
    appointments: PropertiesAppointments


@dataclass
class Schema19:
    type: TypeEnum
    properties: Properties24


@dataclass
class ApplicationJSON64:
    schema: Schema19


@dataclass
class Content60:
    application_json: ApplicationJSON64


@dataclass
class RequestBody7:
    content: Content60


@dataclass
class ErrorsAppointments:
    summary: List[str]
    start_at: List[str]
    end_at: List[str]


@dataclass
class Errors:
    appointments: ErrorsAppointments


@dataclass
class PurpleTicket:
    id: int
    customer_id: int
    subject: str
    status: str
    problem_type: str
    created_at: str
    updated_at: str
    category: str
    referredby: None
    isapproved: bool
    memory: None
    upgradeoffered: bool
    password: None
    cancelled: bool
    power_adapter: bool
    start_at: None
    end_at: None
    user_id: int
    account_id: int
    checkbox_results: None
    textbox_results: None
    due_date: str
    number: int
    location_id: None
    pdf: PDF
    signature_name: None
    signature_data: str
    gevent_id: None
    intake_form_pdf: PDF
    contact_id: None
    properties: ParamsClass
    ticket_type_id: None
    priority: None
    notify_emails: None
    disabled: bool
    ticket_recurring_schedule_id: None
    time_to_resolve_minutes: None
    original_customer_id: int
    original_ticket_id: None
    sla_id: None
    contract_id: None
    address_id: None
    creator_id: None
    signature_date: None
    resolved_at: None
    all_notify_emails: None
    outtake_form_name: None
    outtake_form_data: None
    outtake_form_date: None
    custom_fields_cache: str
    with_initial_issue_body: None
    with_items_any: None


@dataclass
class Example37:
    invoice: None
    ticket: Optional[PurpleTicket] = None
    redirect: Optional[str] = None
    message: Optional[str] = None
    success: Optional[bool] = None
    errors: Optional[Errors] = None


@dataclass
class ApplicationJSON65:
    example: Example37


@dataclass
class Content61:
    application_json: ApplicationJSON65


@dataclass
class Response24:
    description: str
    content: Content61


@dataclass
class NewTicketFormsIDProcessFormPost:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    request_body: RequestBody7
    responses: Dict[str, Response24]


@dataclass
class NewTicketFormsIDProcessForm:
    post: NewTicketFormsIDProcessFormPost


@dataclass
class Properties25:
    code: SchemaValue


@dataclass
class Schema20:
    type: TypeEnum
    properties: Properties25


@dataclass
class ApplicationJSON66:
    schema: Schema20


@dataclass
class Content62:
    application_json: ApplicationJSON66


@dataclass
class RequestBody8:
    content: Content62
    description: str


@dataclass
class Example38:
    login: bool
    instructions: str
    session_token: Optional[UUID] = None
    token_expiration: Optional[str] = None


@dataclass
class ApplicationJSON67:
    example: Example38


@dataclass
class Content63:
    application_json: ApplicationJSON67


@dataclass
class Response25:
    description: str
    content: Content63


@dataclass
class OtpLoginPost:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    request_body: RequestBody8
    responses: Dict[str, Response25]


@dataclass
class OtpLogin:
    post: OtpLoginPost


@dataclass
class PaymentMethod:
    id: int
    name: str
    created_at: str
    updated_at: str
    uses_card_processing: bool


@dataclass
class Example39:
    payment_methods: List[PaymentMethod]


@dataclass
class ApplicationJSON68:
    example: Example39


@dataclass
class Content64:
    application_json: ApplicationJSON68


@dataclass
class The200_9:
    description: str
    content: Content64


@dataclass
class Responses13:
    the_200: The200_9


@dataclass
class PaymentMethodsGet:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    responses: Responses13


@dataclass
class PaymentMethods:
    get: PaymentMethodsGet


@dataclass
class PaymentElement:
    id: int
    created_at: str
    updated_at: str
    success: bool
    payment_amount: int
    invoice_ids: List[None]
    ref_num: str
    applied_at: str
    payment_method: str
    transaction_response: None
    signature_date: None
    customer: CustomerElement


@dataclass
class Example40:
    payments: List[PaymentElement]
    meta: FluffyMeta


@dataclass
class ApplicationJSON69:
    example: Example40


@dataclass
class Content65:
    application_json: ApplicationJSON69


@dataclass
class The200_10:
    description: str
    content: Content65


@dataclass
class Responses14:
    the_200: The200_10


@dataclass
class PaymentsGet:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[IndigoParameter]
    responses: Responses14


@dataclass
class Properties26:
    customer_id: SchemaValue
    invoice_id: SchemaValue
    invoice_number: SchemaValue
    amount_cents: SchemaValue
    address_street: SchemaValue
    address_city: SchemaValue
    address_zip: SchemaValue
    payment_method: SchemaValue
    ref_num: SchemaValue
    register_id: SchemaValue
    signature_name: SchemaValue
    signature_data: SchemaValue
    signature_date: NextRun
    credit_card_number: SchemaValue
    date_month: SchemaValue
    date_year: SchemaValue
    cvv: SchemaValue
    lastname: SchemaValue
    firstname: SchemaValue
    apply_payments: CustomerExternalID


@dataclass
class Schema21:
    type: TypeEnum
    properties: Properties26


@dataclass
class ApplicationJSON70:
    schema: Schema21


@dataclass
class Content66:
    application_json: ApplicationJSON70


@dataclass
class RequestBody9:
    content: Content66


@dataclass
class PurplePayment:
    id: int
    created_at: str
    updated_at: str
    success: bool
    payment_amount: int
    invoice_ids: List[int]
    ref_num: None
    applied_at: str
    payment_method: None
    transaction_response: None
    tickets: List[Any]


@dataclass
class Example41:
    payment: PurplePayment


@dataclass
class ApplicationJSON71:
    example: Example41


@dataclass
class Content67:
    application_json: ApplicationJSON71


@dataclass
class Response26:
    description: str
    content: Optional[Content67] = None


@dataclass
class PaymentsPost:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    request_body: RequestBody9
    responses: Dict[str, Response26]


@dataclass
class PaymentsClass:
    get: PaymentsGet
    post: PaymentsPost


@dataclass
class Example42:
    payment: PaymentElement


@dataclass
class ApplicationJSON72:
    example: Example42


@dataclass
class Content68:
    application_json: ApplicationJSON72


@dataclass
class Response27:
    description: str
    content: Optional[Content68] = None


@dataclass
class PaymentsIDGet:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    responses: Dict[str, Response27]


@dataclass
class PaymentsID:
    get: PaymentsIDGet


@dataclass
class PortalUserElement:
    id: int
    email: str
    account_id: int
    customer_id: int
    contact_id: int
    created_at: str
    updated_at: str
    portal_group_id: int


@dataclass
class Example43:
    portal_users: List[PortalUserElement]
    meta: PurpleMeta


@dataclass
class ApplicationJSON73:
    example: Example43


@dataclass
class Content69:
    application_json: ApplicationJSON73


@dataclass
class The200_11:
    description: str
    content: Content69


@dataclass
class Responses15:
    the_200: The200_11


@dataclass
class PortalUsersGet:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[IndigoParameter]
    responses: Responses15


@dataclass
class AmbitiousParams:
    customer_id: int
    password: str
    password_confirmation: str


@dataclass
class Example44:
    id: Optional[int] = None
    email: Optional[str] = None
    account_id: Optional[int] = None
    customer_id: Optional[int] = None
    contact_id: Optional[int] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    portal_group_id: Optional[int] = None
    success: Optional[bool] = None
    message: Optional[List[str]] = None
    params: Optional[AmbitiousParams] = None


@dataclass
class ApplicationJSON74:
    example: Example44


@dataclass
class Content70:
    application_json: ApplicationJSON74


@dataclass
class Response28:
    description: str
    content: Content70


@dataclass
class PortalUsersPost:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    request_body: FriskyRequestBody
    responses: Dict[str, Response28]


@dataclass
class PortalUsers:
    get: PortalUsersGet
    post: PortalUsersPost


@dataclass
class ApplicationJSON75:
    schema: PaymentsSchema


@dataclass
class Content71:
    application_json: ApplicationJSON75


@dataclass
class RequestBody10:
    content: Content71
    description: str


@dataclass
class Example45:
    success: bool
    message: str


@dataclass
class ApplicationJSON76:
    example: Example45


@dataclass
class Content72:
    application_json: ApplicationJSON76


@dataclass
class Response29:
    description: str
    content: Content72


@dataclass
class PortalUsersCreateInvitationPost:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    request_body: RequestBody10
    responses: Dict[str, Response29]


@dataclass
class PortalUsersCreateInvitation:
    post: PortalUsersCreateInvitationPost


@dataclass
class ApplicationJSON77:
    example: PortalUserElement


@dataclass
class Content73:
    application_json: ApplicationJSON77


@dataclass
class Response30:
    description: str
    content: Optional[Content73] = None


@dataclass
class PortalUsersIDDelete:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    responses: Dict[str, Response30]


@dataclass
class CunningParams:
    password: str
    password_confirmation: str


@dataclass
class Example46:
    id: Optional[int] = None
    email: Optional[str] = None
    account_id: Optional[int] = None
    customer_id: Optional[int] = None
    contact_id: Optional[int] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    portal_group_id: Optional[int] = None
    success: Optional[bool] = None
    message: Optional[List[str]] = None
    params: Optional[CunningParams] = None


@dataclass
class ApplicationJSON78:
    example: Example46


@dataclass
class Content74:
    application_json: ApplicationJSON78


@dataclass
class Response31:
    description: str
    content: Content74


@dataclass
class PortalUsersIDPut:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    request_body: FriskyRequestBody
    responses: Dict[str, Response31]


@dataclass
class PortalUsersID:
    put: PortalUsersIDPut
    delete: PortalUsersIDDelete


@dataclass
class FriskyParameter:
    name: str
    parameter_in: In
    required: bool
    description: str
    schema: Schema17


@dataclass
class Product:
    id: int
    price_cost: float
    price_retail: float
    condition: None
    description: str
    maintain_stock: bool
    name: str
    quantity: int
    warranty: None
    sort_order: None
    reorder_at: None
    disabled: bool
    taxable: bool
    product_category: None
    category_path: None
    upc_code: None
    discount_percent: None
    warranty_template_id: None
    qb_item_id: int
    desired_stock_level: None
    price_wholesale: int
    notes: None
    tax_rate_id: None
    physical_location: None
    serialized: bool
    vendor_ids: List[Any]
    long_description: None
    location_quantities: List[Any]
    photos: List[Any]


@dataclass
class Example47:
    products: List[Product]


@dataclass
class ApplicationJSON79:
    example: Example47


@dataclass
class Content75:
    application_json: ApplicationJSON79


@dataclass
class The200_12:
    description: str
    content: Content75


@dataclass
class Responses16:
    the_200: The200_12


@dataclass
class ProductsGet:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[FriskyParameter]
    responses: Responses16


@dataclass
class Properties28:
    vendor_id: SchemaValue
    value: SchemaValue


@dataclass
class ProductSkusAttributesItems:
    type: TypeEnum
    properties: Properties28


@dataclass
class ProductSkusAttributes:
    type: TypeEnum
    items: ProductSkusAttributesItems


@dataclass
class Properties27:
    price_cost: SchemaValue
    price_retail: SchemaValue
    condition: SchemaValue
    description: SchemaValue
    maintain_stock: SchemaValue
    name: SchemaValue
    quantity: SchemaValue
    warranty: SchemaValue
    sort_order: SchemaValue
    reorder_at: SchemaValue
    disabled: SchemaValue
    taxable: SchemaValue
    product_category: SchemaValue
    upc_code: SchemaValue
    discount_percent: SchemaValue
    warranty_template_id: SchemaValue
    qb_item_id: SchemaValue
    desired_stock_level: SchemaValue
    price_wholesale: SchemaValue
    notes: SchemaValue
    tax_rate_id: SchemaValue
    vendor_ids: IDS
    physical_location: SchemaValue
    serialized: SchemaValue
    category_ids: IDS
    product_skus_attributes: ProductSkusAttributes


@dataclass
class Schema22:
    type: TypeEnum
    properties: Properties27
    required: List[str]


@dataclass
class ApplicationJSON80:
    schema: Schema22


@dataclass
class Content76:
    application_json: ApplicationJSON80


@dataclass
class RequestBody11:
    content: Content76
    description: str


@dataclass
class MagentaParams:
    name: str
    maintain_stock: bool


@dataclass
class Example48:
    product: Optional[Product] = None
    success: Optional[bool] = None
    message: Optional[List[str]] = None
    params: Optional[MagentaParams] = None


@dataclass
class ApplicationJSON81:
    example: Example48


@dataclass
class Content77:
    application_json: ApplicationJSON81


@dataclass
class Response32:
    description: str
    content: Content77


@dataclass
class ProductsPost:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    request_body: RequestBody11
    responses: Dict[str, Response32]


@dataclass
class Products:
    get: ProductsGet
    post: ProductsPost


@dataclass
class Example49:
    product: Product


@dataclass
class ApplicationJSON82:
    example: Example49


@dataclass
class Content78:
    application_json: ApplicationJSON82


@dataclass
class The200_13:
    description: str
    content: Content78


@dataclass
class Responses17:
    the_200: The200_13


@dataclass
class ProductsBarcodeGet:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[StickyParameter]
    responses: Responses17


@dataclass
class ProductsBarcode:
    get: ProductsBarcodeGet


@dataclass
class Category:
    id: int
    account_id: int
    ancestry: None
    name: str
    description: str
    device_product_id: None
    names_depth_cache: str


@dataclass
class Example50:
    categories: List[Category]


@dataclass
class ApplicationJSON83:
    example: Example50


@dataclass
class Content79:
    application_json: ApplicationJSON83


@dataclass
class The200_14:
    description: str
    content: Content79


@dataclass
class Responses18:
    the_200: The200_14


@dataclass
class ProductsCategoriesGet:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    responses: Responses18


@dataclass
class ProductsCategories:
    get: ProductsCategoriesGet


@dataclass
class Response33:
    description: str
    content: Optional[Content78] = None


@dataclass
class ProductsIDGet:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    responses: Dict[str, Response33]


@dataclass
class Properties29:
    price_cost: SchemaValue
    price_retail: SchemaValue
    condition: SchemaValue
    description: SchemaValue
    maintain_stock: SchemaValue
    name: SchemaValue
    quantity: SchemaValue
    warranty: SchemaValue
    sort_order: SchemaValue
    reorder_at: SchemaValue
    disabled: SchemaValue
    taxable: SchemaValue
    product_category: SchemaValue
    upc_code: SchemaValue
    discount_percent: SchemaValue
    warranty_template_id: SchemaValue
    qb_item_id: SchemaValue
    desired_stock_level: SchemaValue
    price_wholesale: SchemaValue
    notes: SchemaValue
    tax_rate_id: SchemaValue
    vendor_ids: IDS
    physical_location: SchemaValue
    serialized: SchemaValue
    category_ids: IDS
    product_skus_attributes: ProductSkusAttributes


@dataclass
class Schema23:
    type: TypeEnum
    properties: Properties29
    required: List[str]


@dataclass
class ApplicationJSON84:
    schema: Schema23


@dataclass
class Content80:
    application_json: ApplicationJSON84


@dataclass
class RequestBody12:
    content: Content80
    description: str


@dataclass
class Example51:
    product: Optional[Product] = None
    success: Optional[bool] = None
    message: Optional[List[str]] = None


@dataclass
class ApplicationJSON85:
    example: Example51


@dataclass
class Content81:
    application_json: ApplicationJSON85


@dataclass
class Response34:
    description: str
    content: Content81


@dataclass
class ProductsIDPut:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    request_body: RequestBody12
    responses: Dict[str, Response34]


@dataclass
class ProductsID:
    get: ProductsIDGet
    put: ProductsIDPut


@dataclass
class Content82:
    application_json: ApplicationJSON12


@dataclass
class Response35:
    description: str
    content: Content82


@dataclass
class ProductsIDAddImagesPost:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    request_body: FriskyRequestBody
    responses: Dict[str, Response35]


@dataclass
class ProductsIDAddImages:
    post: ProductsIDAddImagesPost


@dataclass
class MischievousParameter:
    name: str
    parameter_in: str
    schema: SchemaValue
    required: Optional[bool] = None


@dataclass
class ProductsIDDeleteImageDelete:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    parameters: List[MischievousParameter]
    responses: Dict[str, The200_Value]


@dataclass
class ProductsIDDeleteImage:
    delete: ProductsIDDeleteImageDelete


@dataclass
class Properties30:
    location_quantity_id: SchemaValue
    quantity: SchemaValue


@dataclass
class Schema24:
    type: TypeEnum
    properties: Properties30


@dataclass
class ApplicationJSON86:
    schema: Schema24


@dataclass
class Content83:
    application_json: ApplicationJSON86


@dataclass
class RequestBody13:
    content: Content83


@dataclass
class Example52:
    product_id: int
    id: int
    quantity: int
    price_cost_cents: None
    price_retail_cents: None
    location_id: int
    tax_rate_id: None
    created_at: str
    updated_at: str
    reorder_at: None
    desired_stock_level: int


@dataclass
class ApplicationJSON87:
    example: Example52


@dataclass
class Content84:
    application_json: ApplicationJSON87


@dataclass
class The200_15:
    description: str
    content: Content84


@dataclass
class Responses19:
    the_200: The200_15


@dataclass
class ProductsIDLocationQuantitiesPut:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    request_body: RequestBody13
    responses: Responses19


@dataclass
class ProductsIDLocationQuantities:
    put: ProductsIDLocationQuantitiesPut


@dataclass
class BraggadociousParameter:
    name: str
    parameter_in: str
    schema: SchemaValue
    required: Optional[bool] = None
    description: Optional[str] = None


@dataclass
class Properties32:
    id: SchemaValue
    created_at: NextRun
    updated_at: NextRun
    product_location_quantity_id: AllDay
    line_item_id: AllDay
    serial_number: SchemaValue
    status: SchemaValue
    instance_price_cost: AllDay
    instance_price_retail: AllDay
    location_id: AllDay


@dataclass
class ProductSerialsItems:
    type: TypeEnum
    properties: Properties32


@dataclass
class ProductSerials:
    type: TypeEnum
    items: ProductSerialsItems


@dataclass
class Properties31:
    product_serials: ProductSerials


@dataclass
class Schema25:
    type: TypeEnum
    properties: Properties31


@dataclass
class Indigo:
    schema: Schema25


@dataclass
class Content85:
    empty: Indigo


@dataclass
class The200_16:
    description: str
    content: Content85


@dataclass
class Responses20:
    the_200: The200_16


@dataclass
class ProductsProductIDProductSerialsGet:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[BraggadociousParameter]
    responses: Responses20


@dataclass
class Properties33:
    condition: SchemaValue
    price_cost_cents: SchemaValue
    price_retail_cents: SchemaValue
    serial_number: SchemaValue


@dataclass
class Schema26:
    type: TypeEnum
    properties: Properties33


@dataclass
class ApplicationJSON88:
    schema: Schema26


@dataclass
class Content86:
    application_json: ApplicationJSON88


@dataclass
class RequestBody14:
    content: Content86
    description: str


@dataclass
class ProductSerial:
    id: int
    created_at: str
    updated_at: str
    product_location_quantity_id: None
    line_item_id: None
    serial_number: str
    status: str
    instance_price_cost: float
    instance_price_retail: float
    location_id: None


@dataclass
class Example53:
    product_serial: Optional[ProductSerial] = None
    success: Optional[bool] = None
    message: Optional[List[str]] = None


@dataclass
class ApplicationJSON89:
    example: Example53


@dataclass
class Content87:
    application_json: ApplicationJSON89


@dataclass
class Response36:
    description: str
    content: Content87


@dataclass
class ProductsProductIDProductSerialsPost:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    request_body: RequestBody14
    responses: Dict[str, Response36]


@dataclass
class ProductsProductIDProductSerials:
    get: ProductsProductIDProductSerialsGet
    post: ProductsProductIDProductSerialsPost


@dataclass
class Properties34:
    record_type: Frequency
    line_item_id: SchemaValue
    product_serial_ids: IDS


@dataclass
class Schema27:
    type: TypeEnum
    properties: Properties34


@dataclass
class ApplicationJSON90:
    schema: Schema27


@dataclass
class Content88:
    application_json: ApplicationJSON90


@dataclass
class RequestBody15:
    content: Content88


@dataclass
class Example54:
    status: str
    errors: Optional[str] = None


@dataclass
class ApplicationJSON91:
    example: Example54


@dataclass
class Content89:
    application_json: ApplicationJSON91


@dataclass
class Response37:
    description: str
    content: Content89


@dataclass
class ProductsProductIDProductSerialsAttachToLineItemPost:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    request_body: RequestBody15
    responses: Dict[str, Response37]


@dataclass
class ProductsProductIDProductSerialsAttachToLineItem:
    post: ProductsProductIDProductSerialsAttachToLineItemPost


@dataclass
class Properties35:
    condition: SchemaValue
    price_cost_cents: SchemaValue
    price_retail_cents: SchemaValue
    serial_number: SchemaValue
    notes: SchemaValue


@dataclass
class Schema28:
    type: TypeEnum
    properties: Properties35


@dataclass
class ApplicationJSON92:
    schema: Schema28


@dataclass
class Content90:
    application_json: ApplicationJSON92


@dataclass
class RequestBody16:
    content: Content90
    description: str


@dataclass
class Response38:
    description: str
    content: Content87


@dataclass
class ProductsProductIDProductSerialsIDPut:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    request_body: RequestBody16
    responses: Dict[str, Response38]


@dataclass
class ProductsProductIDProductSerialsID:
    put: ProductsProductIDProductSerialsIDPut


@dataclass
class VendorElement:
    id: int
    name: str
    rep_first_name: str
    rep_last_name: str
    email: str
    phone: str
    account_number: None
    created_at: str
    updated_at: str
    address: str
    city: str
    state: str
    zip: str
    website: str
    notes: str


@dataclass
class PurchaseOrder:
    id: int
    account_subdomain: str
    created_at: str
    updated_at: str
    expected_date: str
    number: str
    other: float
    shipping: float
    shipping_notes: str
    status: str
    total: float
    user_id: int
    vendor_id: int
    location_id: None
    due_date: str
    paid_date: str
    delivery_tracking: str
    vendor: VendorElement
    location: None
    line_items: List[Any]


@dataclass
class Example55:
    purchase_orders: List[PurchaseOrder]


@dataclass
class ApplicationJSON93:
    example: Example55


@dataclass
class Content91:
    application_json: ApplicationJSON93


@dataclass
class The200_17:
    description: str
    content: Content91


@dataclass
class Responses21:
    the_200: The200_17


@dataclass
class PurchaseOrdersGet:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[IndigoParameter]
    responses: Responses21


@dataclass
class Properties36:
    discount_percent: SchemaValue
    expected_date: NextRun
    general_notes: SchemaValue
    other_cents: SchemaValue
    shipping_cents: SchemaValue
    shipping_notes: SchemaValue
    user_id: SchemaValue
    vendor_id: SchemaValue
    location_id: SchemaValue
    due_date: NextRun
    paid_date: NextRun
    order_date: NextRun
    delivery_tracking: SchemaValue


@dataclass
class Schema29:
    type: TypeEnum
    properties: Properties36


@dataclass
class ApplicationJSON94:
    schema: Schema29


@dataclass
class Content92:
    application_json: ApplicationJSON94


@dataclass
class RequestBody17:
    content: Content92


@dataclass
class Example56:
    purchase_order: PurchaseOrder


@dataclass
class ApplicationJSON95:
    example: Example56


@dataclass
class Content93:
    application_json: ApplicationJSON95


@dataclass
class The200_18:
    description: str
    content: Content93


@dataclass
class Responses22:
    the_200: The200_18


@dataclass
class PurchaseOrdersPost:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    request_body: RequestBody17
    responses: Responses22


@dataclass
class PurchaseOrders:
    get: PurchaseOrdersGet
    post: PurchaseOrdersPost


@dataclass
class Content94:
    application_json: ApplicationJSON95


@dataclass
class Response39:
    description: str
    content: Optional[Content94] = None


@dataclass
class PurchaseOrdersIDGet:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    responses: Dict[str, Response39]


@dataclass
class PurchaseOrdersID:
    get: PurchaseOrdersIDGet


@dataclass
class Properties37:
    product_id: SchemaValue
    quantity: SchemaValue


@dataclass
class Schema30:
    type: TypeEnum
    properties: Properties37


@dataclass
class ApplicationJSON96:
    schema: Schema30


@dataclass
class Content95:
    application_json: ApplicationJSON96


@dataclass
class RequestBody18:
    content: Content95


@dataclass
class PoLineItem:
    id: int
    purchase_order_id: int
    product_id: int
    quantity: int
    cost_cents: int
    total_cents: int
    created_at: str
    updated_at: str
    received: bool
    position: None
    received_quantity: int
    parent_po_line_item_id: None
    old_cost_cents: None


@dataclass
class Example57:
    po_line_item: Optional[PoLineItem] = None
    errors: Optional[str] = None


@dataclass
class ApplicationJSON97:
    example: Example57


@dataclass
class Content96:
    application_json: ApplicationJSON97


@dataclass
class Response40:
    description: str
    content: Content96


@dataclass
class PurchaseOrdersIDCreatePoLineItemPost:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    request_body: RequestBody18
    responses: Dict[str, Response40]


@dataclass
class PurchaseOrdersIDCreatePoLineItem:
    post: PurchaseOrdersIDCreatePoLineItemPost


@dataclass
class Properties38:
    line_item_id: SchemaValue


@dataclass
class Schema31:
    type: TypeEnum
    properties: Properties38


@dataclass
class ApplicationJSON98:
    schema: Schema31


@dataclass
class Content97:
    application_json: ApplicationJSON98


@dataclass
class RequestBody19:
    content: Content97


@dataclass
class Content98:
    application_json: ApplicationJSON95


@dataclass
class The200_19:
    description: str
    content: Content98


@dataclass
class Responses23:
    the_200: The200_19


@dataclass
class PurchaseOrdersIDReceivePost:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    request_body: RequestBody19
    responses: Responses23


@dataclass
class PurchaseOrdersIDReceive:
    post: PurchaseOrdersIDReceivePost


@dataclass
class Schema32:
    type: TypeEnum
    default: Optional[str] = None


@dataclass
class Parameter1:
    name: str
    parameter_in: In
    description: str
    required: bool
    schema: Schema32


@dataclass
class RmmAlert:
    id: int
    customer_id: int
    ticket_number: None
    ticket_status: None
    computer_name: str
    properties: ParamsClass
    resolved: bool
    check_id: int
    status: str
    formatted_output: str
    description: str
    created_at: str
    updated_at: str
    asset_id: int


@dataclass
class Example58:
    rmm_alerts: List[RmmAlert]
    meta: FluffyMeta


@dataclass
class ApplicationJSON99:
    example: Example58


@dataclass
class Content99:
    application_json: ApplicationJSON99


@dataclass
class The200_20:
    description: str
    content: Content99


@dataclass
class Responses24:
    the_200: The200_20


@dataclass
class RmmAlertsGet:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[Parameter1]
    responses: Responses24


@dataclass
class Properties39:
    customer_id: SchemaValue
    asset_id: SchemaValue
    description: SchemaValue
    resolved: SchemaValue
    status: SchemaValue
    properties: CommentsAttributesSchema


@dataclass
class Schema33:
    type: TypeEnum
    properties: Properties39


@dataclass
class ApplicationJSON100:
    schema: Schema33


@dataclass
class Content100:
    application_json: ApplicationJSON100


@dataclass
class RequestBody20:
    content: Content100


@dataclass
class Alert:
    id: int
    account_id: int
    customer_id: int
    computer_name: None
    properties: ParamsClass
    resolved: bool
    check_id: None
    status: None
    formatted_output: None
    description: str
    created_at: str
    updated_at: str
    ticket_id: None
    asset_id: int


@dataclass
class Example59:
    success: bool
    alert: Alert


@dataclass
class ApplicationJSON101:
    example: Example59


@dataclass
class The201_Content:
    application_json: ApplicationJSON101


@dataclass
class The201:
    description: str
    content: The201_Content


@dataclass
class Responses25:
    the_201: The201


@dataclass
class RmmAlertsPost:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    request_body: RequestBody20
    responses: Responses25


@dataclass
class RmmAlerts:
    get: RmmAlertsGet
    post: RmmAlertsPost


@dataclass
class Example60:
    success: str


@dataclass
class ApplicationJSON102:
    example: Example60


@dataclass
class Content101:
    application_json: ApplicationJSON102


@dataclass
class Response41:
    description: str
    content: Optional[Content101] = None


@dataclass
class RmmAlertsIDDelete:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    responses: Dict[str, Response41]


@dataclass
class Example61:
    rmm_alert: RmmAlert


@dataclass
class ApplicationJSON103:
    example: Example61


@dataclass
class Content102:
    application_json: ApplicationJSON103


@dataclass
class Response42:
    description: str
    content: Optional[Content102] = None


@dataclass
class RmmAlertsIDGet:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    responses: Dict[str, Response42]


@dataclass
class RmmAlertsID:
    get: RmmAlertsIDGet
    delete: RmmAlertsIDDelete


@dataclass
class Parameter2:
    name: str
    parameter_in: str
    required: bool
    schema: SchemaValue
    description: Optional[str] = None


@dataclass
class RmmAlertsIDMutePost:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[Parameter2]
    responses: Dict[str, Response41]


@dataclass
class RmmAlertsIDMute:
    post: RmmAlertsIDMutePost


@dataclass
class ScheduleElement:
    id: int
    account_id: int
    customer_id: int
    email_customer: bool
    frequency: str
    name: str
    next_run: str
    snail_mail: bool
    charge_mop: bool
    subtotal: int
    invoice_unbilled_ticket_charges: bool
    paused: bool
    last_invoice_paid: None
    lines: List[Any]


@dataclass
class Example62:
    schedules: List[ScheduleElement]


@dataclass
class ApplicationJSON104:
    example: Example62


@dataclass
class Content103:
    application_json: ApplicationJSON104


@dataclass
class The200_21:
    description: str
    content: Content103


@dataclass
class Responses26:
    the_200: The200_21


@dataclass
class SchedulesGet:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[IndigoParameter]
    responses: Responses26


@dataclass
class Example63:
    schedule: Optional[ScheduleElement] = None
    error: Optional[List[str]] = None


@dataclass
class ApplicationJSON105:
    example: Example63


@dataclass
class Content104:
    application_json: ApplicationJSON105


@dataclass
class Response43:
    description: str
    content: Content104


@dataclass
class SchedulesPost:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    request_body: FriskyRequestBody
    responses: Dict[str, Response43]


@dataclass
class Schedules:
    get: SchedulesGet
    post: SchedulesPost


@dataclass
class Example64:
    schedule: ScheduleElement


@dataclass
class ApplicationJSON106:
    example: Example64


@dataclass
class Content105:
    application_json: ApplicationJSON106


@dataclass
class Response44:
    description: str
    content: Optional[Content105] = None


@dataclass
class SchedulesIDGet:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    responses: Dict[str, Response44]


@dataclass
class Response45:
    description: str
    content: Content104


@dataclass
class SchedulesIDPut:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    request_body: FriskyRequestBody
    responses: Dict[str, Response45]


@dataclass
class SchedulesID:
    get: SchedulesIDGet
    put: SchedulesIDPut
    delete: AppointmentTypesIDDelete


@dataclass
class PurpleScheduleLineItem:
    id: int
    cost_cents: int
    description: str
    name: str
    position: int
    product_id: None
    quantity: str
    retail_cents: int
    schedule_id: int
    taxable: bool
    user_id: int
    price_cost: int
    price_retail: int
    product_category: None
    asset_type_id: None
    recurring_type_id: None
    device_ids: List[Any]
    one_time_charge: bool


@dataclass
class Example65:
    schedule_line_item: Optional[PurpleScheduleLineItem] = None
    error: Optional[List[str]] = None


@dataclass
class ApplicationJSON107:
    example: Example65


@dataclass
class Content106:
    application_json: ApplicationJSON107


@dataclass
class Response46:
    description: str
    content: Content106


@dataclass
class SchedulesIDAddLineItemPost:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    request_body: FriskyRequestBody
    responses: Dict[str, Response46]


@dataclass
class SchedulesIDAddLineItem:
    post: SchedulesIDAddLineItemPost


@dataclass
class FluffyScheduleLineItem:
    id: int
    cost_cents: int
    description: str
    name: str
    position: int
    product_id: int
    quantity: str
    retail_cents: int
    schedule_id: int
    taxable: bool
    user_id: int
    price_cost: float
    price_retail: float
    product_category: None
    asset_type_id: None
    recurring_type_id: None
    device_ids: List[Any]
    one_time_charge: bool


@dataclass
class Example66:
    schedule_line_item: Optional[FluffyScheduleLineItem] = None
    error: Optional[List[str]] = None


@dataclass
class ApplicationJSON108:
    example: Example66


@dataclass
class Content107:
    application_json: ApplicationJSON108


@dataclass
class Response47:
    description: str
    content: Content107


@dataclass
class SchedulesIDLineItemsScheduleLineItemIDPut:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[Parameter2]
    request_body: FriskyRequestBody
    responses: Dict[str, Response47]


@dataclass
class SchedulesIDLineItemsScheduleLineItemID:
    put: SchedulesIDLineItemsScheduleLineItemIDPut


@dataclass
class ApplicationJSON109:
    schema: SchemaValue


@dataclass
class Content108:
    application_json: ApplicationJSON109


@dataclass
class RequestBody21:
    content: Content108


@dataclass
class SchedulesIDRemoveLineItemPost:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    request_body: RequestBody21
    responses: Dict[str, ParamsValue]


@dataclass
class SchedulesIDRemoveLineItem:
    post: SchedulesIDRemoveLineItemPost


@dataclass
class SourceTable:
    firstname: str
    lastname: str
    email: str
    business_name: None
    phones: List[PhoneElement]


@dataclass
class Source:
    table: SourceTable


@dataclass
class ResultTable:
    id: int
    type: str
    index: str
    source: Source


@dataclass
class Result:
    table: ResultTable


@dataclass
class Example67:
    quick_result: None
    results: List[Result]
    error: None


@dataclass
class ApplicationJSON110:
    example: Example67


@dataclass
class Content109:
    application_json: ApplicationJSON110


@dataclass
class The200_22:
    description: str
    content: Content109


@dataclass
class Responses27:
    the_200: The200_22


@dataclass
class SearchGet:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[HilariousParameter]
    responses: Responses27


@dataclass
class Search:
    get: SearchGet


@dataclass
class Assets:
    asset_types: List[Any]
    asset_type_fields: List[Any]
    asset_type_field_answers: List[Any]


@dataclass
class BusinessHour:
    day: str
    start: str
    end: str
    closed: bool


@dataclass
class CustomersClass:
    required_fields: None
    customer_fields: List[Any]
    customer_field_answers: List[Any]


@dataclass
class Locale:
    iso_code: str
    currency_symbol: str
    date_format: str
    time_format: str
    time_zone: str
    time_offset: str


@dataclass
class FluffyTicket:
    ticket_types: List[Any]
    ticket_type_fields: List[Any]
    ticket_type_field_answers: List[Any]
    problem_types: List[str]
    priorities: List[str]


@dataclass
class Example68:
    customers: CustomersClass
    assets: Assets
    locale: Locale
    ticket: FluffyTicket
    business_hours_enabled: bool
    business_hours: List[BusinessHour]
    default_holiday_calendar: str
    msp_addon: None


@dataclass
class ApplicationJSON111:
    example: Example68


@dataclass
class Content110:
    application_json: ApplicationJSON111


@dataclass
class The200_23:
    description: str
    content: Content110


@dataclass
class Responses28:
    the_200: The200_23


@dataclass
class SettingsGet:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    responses: Responses28


@dataclass
class Settings:
    get: SettingsGet


@dataclass
class Example69:
    messaging_channel: str
    registers: List[Any]


@dataclass
class ApplicationJSON112:
    example: Example69


@dataclass
class Content111:
    application_json: ApplicationJSON112


@dataclass
class The200_24:
    description: str
    content: Content111


@dataclass
class Responses29:
    the_200: The200_24


@dataclass
class SettingsPrintingGet:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    responses: Responses29


@dataclass
class SettingsPrinting:
    get: SettingsPrintingGet


@dataclass
class Example70:
    tabs: Dict[str, bool]


@dataclass
class ApplicationJSON113:
    example: Example70


@dataclass
class Content112:
    application_json: ApplicationJSON113


@dataclass
class The200_25:
    description: str
    content: Content112


@dataclass
class Responses30:
    the_200: The200_25


@dataclass
class SettingsTabsGet:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    responses: Responses30


@dataclass
class SettingsTabs:
    get: SettingsTabsGet


@dataclass
class Parameter3:
    name: str
    parameter_in: In
    description: str
    required: bool
    schema: FriskySchema


@dataclass
class TicketTimer:
    id: int
    ticket_id: int
    user_id: int
    start_time: str
    end_time: str
    recorded: bool
    created_at: str
    updated_at: str
    billable: bool
    notes: None
    toggl_id: None
    product_id: None
    comment_id: None
    ticket_line_item_id: None
    active_duration: None


@dataclass
class Example71:
    ticket_timers: List[TicketTimer]
    meta: FluffyMeta


@dataclass
class ApplicationJSON114:
    example: Example71


@dataclass
class Content113:
    application_json: ApplicationJSON114


@dataclass
class The200_26:
    description: str
    content: Content113


@dataclass
class Responses31:
    the_200: The200_26


@dataclass
class TicketTimersGet:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[Parameter3]
    responses: Responses31


@dataclass
class TicketTimers:
    get: TicketTimersGet


@dataclass
class TicketElement:
    id: int
    number: int
    subject: str
    created_at: str
    customer_id: int
    customer_business_then_name: str
    due_date: str
    resolved_at: None
    start_at: None
    end_at: None
    location_id: None
    problem_type: str
    status: str
    ticket_type_id: None
    properties: ParamsClass
    user_id: None
    updated_at: str
    pdf_url: None
    priority: None
    comments: List[Any]
    user: None


@dataclass
class Example72:
    tickets: List[TicketElement]
    meta: FluffyMeta


@dataclass
class ApplicationJSON115:
    example: Example72


@dataclass
class Content114:
    application_json: ApplicationJSON115


@dataclass
class The200_27:
    description: str
    content: Content114


@dataclass
class Responses32:
    the_200: The200_27


@dataclass
class TicketsGet:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[Parameter3]
    responses: Responses32


@dataclass
class TicketAsset:
    id: int
    name: str
    customer_id: int
    created_at: str
    updated_at: str
    properties: ParamsClass
    asset_type: str
    asset_serial: None
    external_rmm_link: None
    customer: AssetCustomer
    rmm_links: List[Any]
    rmm_store: RmmStore


@dataclass
class CommentElement:
    id: int
    created_at: str
    updated_at: str
    ticket_id: int
    subject: str
    body: str
    tech: None
    hidden: bool
    user_id: None


@dataclass
class Properties40:
    device_type: str
    maker: str


@dataclass
class Answer:
    id: int
    ticket_field_id: int
    content: str
    created_at: str
    updated_at: str
    account_id: None


@dataclass
class TicketField:
    id: int
    name: str
    field_type: str
    required: None
    account_id: int
    created_at: str
    updated_at: str
    ticket_type_id: int
    hidden: bool
    position: None
    answers: List[Answer]


@dataclass
class PurpleTicketType:
    id: int
    name: str
    account_id: int
    created_at: str
    updated_at: str
    disabled: bool
    intake_terms: None
    skip_intake: bool
    outtake_terms: None
    skip_outtake: bool
    ticket_fields: List[TicketField]


@dataclass
class TicketUser:
    id: int
    email: str
    full_name: str
    created_at: str
    updated_at: str
    group: str
    admin: bool
    color: str


@dataclass
class TentacledTicket:
    id: int
    number: int
    subject: str
    created_at: str
    customer_id: int
    customer_business_then_name: str
    due_date: str
    start_at: None
    end_at: str
    location_id: None
    problem_type: str
    status: str
    properties: Properties40
    user_id: int
    updated_at: str
    pdf_url: None
    intake_form_html: None
    signature_name: str
    signature_date: None
    asset_ids: List[int]
    priority: str
    resolved_at: None
    outtake_form_name: None
    outtake_form_date: None
    outtake_form_html: None
    comments: List[CommentElement]
    attachments: List[Any]
    ticket_timers: List[Any]
    line_items: List[Any]
    worksheet_results: List[Any]
    assets: List[TicketAsset]
    appointments: List[Any]
    ticket_fields: List[TicketField]
    ticket_answers: List[Answer]
    customer: CustomerElement
    contact: None
    user: TicketUser
    ticket_type: PurpleTicketType


@dataclass
class Example73:
    ticket: Optional[TentacledTicket] = None
    error: Optional[str] = None


@dataclass
class ApplicationJSON116:
    example: Example73


@dataclass
class Content115:
    application_json: ApplicationJSON116


@dataclass
class Response48:
    description: str
    content: Content115


@dataclass
class TicketsPost:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    request_body: FriskyRequestBody
    responses: Dict[str, Response48]


@dataclass
class Tickets:
    get: TicketsGet
    post: TicketsPost


@dataclass
class TicketsIDDelete:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    responses: Dict[str, The200_Value]


@dataclass
class FluffyTicketType:
    id: int
    name: str
    account_id: int
    created_at: str
    updated_at: str
    disabled: bool
    intake_terms: None
    skip_intake: bool
    outtake_terms: None
    skip_outtake: bool
    ticket_fields: List[Any]


@dataclass
class StickyTicket:
    id: int
    number: int
    subject: str
    created_at: str
    customer_id: int
    customer_business_then_name: str
    due_date: str
    start_at: None
    end_at: None
    location_id: None
    problem_type: str
    status: str
    properties: ParamsClass
    user_id: None
    updated_at: str
    pdf_url: None
    intake_form_html: None
    signature_name: None
    signature_date: None
    asset_ids: List[Any]
    priority: None
    resolved_at: None
    outtake_form_name: None
    outtake_form_date: None
    outtake_form_html: None
    comments: List[Any]
    attachments: List[Any]
    ticket_timers: List[Any]
    line_items: List[Any]
    worksheet_results: List[Any]
    assets: List[Any]
    appointments: List[Any]
    ticket_fields: List[Any]
    ticket_answers: List[Any]
    customer: CustomerElement
    contact: None
    user: TicketUser
    ticket_type: FluffyTicketType
    address: None


@dataclass
class Example75:
    ticket: StickyTicket


@dataclass
class ApplicationJSON118:
    example: Example75


@dataclass
class Content117:
    application_json: ApplicationJSON118


@dataclass
class Response49:
    description: str
    content: Optional[Content117] = None


@dataclass
class TicketsIDGet:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    responses: Dict[str, Response49]


@dataclass
class Example76:
    ticket: Optional[StickyTicket] = None
    success: Optional[bool] = None
    message: Optional[List[str]] = None


@dataclass
class ApplicationJSON119:
    example: Example76


@dataclass
class Content118:
    application_json: ApplicationJSON119


@dataclass
class Response50:
    description: str
    content: Content118


@dataclass
class TicketsIDPut:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    request_body: FriskyRequestBody
    responses: Dict[str, Response50]


@dataclass
class TicketsID:
    get: TicketsIDGet
    put: TicketsIDPut
    delete: TicketsIDDelete


@dataclass
class Properties41:
    name: SchemaValue
    upc_code: SchemaValue
    product_id: SchemaValue
    description: SchemaValue
    quantity: SchemaValue
    price_cost: SchemaValue
    price_retail: SchemaValue
    taxable: SchemaValue


@dataclass
class Schema34:
    type: TypeEnum
    properties: Properties41


@dataclass
class ApplicationJSON120:
    schema: Schema34


@dataclass
class Content119:
    application_json: ApplicationJSON120


@dataclass
class RequestBody22:
    content: Content119


@dataclass
class Example77:
    product_id: None
    product_category: None
    upc_code: None
    item_id: None
    estimate_line_item_id: None
    old_price: None
    line_discount_percent: None
    discount_dollars: None
    original_ticket_line_item_id: None
    id: Optional[int] = None
    ticket_id: Optional[int] = None
    user_id: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None
    quantity: Optional[str] = None
    taxable: Optional[bool] = None
    cost_cents: Optional[int] = None
    retail_cents: Optional[int] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    converted: Optional[bool] = None
    position: Optional[int] = None
    price_cost: Optional[int] = None
    price_retail: Optional[int] = None
    errors: Optional[str] = None
    params: Optional[ParamsClass] = None


@dataclass
class ApplicationJSON121:
    example: Example77


@dataclass
class Content120:
    application_json: ApplicationJSON121


@dataclass
class Response51:
    description: str
    content: Content120


@dataclass
class TicketsIDAddLineItemPost:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    request_body: RequestBody22
    responses: Dict[str, Response51]


@dataclass
class TicketsIDAddLineItem:
    post: TicketsIDAddLineItemPost


@dataclass
class TicketsIDAttachFileURLPost:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    request_body: FriskyRequestBody
    responses: Dict[str, Response35]


@dataclass
class TicketsIDAttachFileURL:
    post: TicketsIDAttachFileURLPost


@dataclass
class Example78:
    ticket_id: int
    id: int
    notes: str
    user_id: int
    toggl_id: None
    start_time: str
    end_time: str
    recorded: bool
    created_at: str
    updated_at: str
    billable: bool
    product_id: int
    comment_id: None
    ticket_line_item_id: None
    active_duration: None


@dataclass
class ApplicationJSON122:
    example: Example78


@dataclass
class Content121:
    application_json: ApplicationJSON122


@dataclass
class Response52:
    description: str
    content: Optional[Content121] = None


@dataclass
class TicketsIDChargeTimerEntryPost:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    request_body: FriskyRequestBody
    responses: Dict[str, Response52]


@dataclass
class TicketsIDChargeTimerEntry:
    post: TicketsIDChargeTimerEntryPost


@dataclass
class ApplicationJSON123:
    schema: CommentsAttributesSchema


@dataclass
class Content122:
    application_json: ApplicationJSON123


@dataclass
class RequestBody23:
    content: Content122


@dataclass
class ExampleComment:
    id: int
    created_at: str
    updated_at: str
    ticket_id: int
    subject: str
    body: str
    tech: str
    hidden: bool
    user_id: int


@dataclass
class Example79:
    comment: Optional[ExampleComment] = None
    success: Optional[bool] = None
    message: Optional[List[str]] = None


@dataclass
class ApplicationJSON124:
    example: Example79


@dataclass
class Content123:
    application_json: ApplicationJSON124


@dataclass
class Response53:
    description: str
    content: Content123


@dataclass
class TicketsIDCommentPost:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    request_body: RequestBody23
    responses: Dict[str, Response53]


@dataclass
class TicketsIDComment:
    post: TicketsIDCommentPost


@dataclass
class Properties42:
    attachment_id: SchemaValue


@dataclass
class Schema35:
    type: TypeEnum
    properties: Properties42


@dataclass
class ApplicationJSON125:
    schema: Schema35


@dataclass
class Content124:
    application_json: ApplicationJSON125


@dataclass
class RequestBody24:
    content: Content124


@dataclass
class TicketsIDDeleteAttachmentPost:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    request_body: RequestBody24
    responses: Dict[str, Response5]


@dataclass
class TicketsIDDeleteAttachment:
    post: TicketsIDDeleteAttachmentPost


@dataclass
class TicketsIDDeleteTimerEntryPost:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    request_body: FriskyRequestBody
    responses: Dict[str, Response5]


@dataclass
class TicketsIDDeleteTimerEntry:
    post: TicketsIDDeleteTimerEntryPost


@dataclass
class TicketsIDPrintPost:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    responses: Responses7


@dataclass
class TicketsIDPrint:
    post: TicketsIDPrintPost


@dataclass
class Properties43:
    ticket_line_item_id: SchemaValue


@dataclass
class Schema36:
    type: TypeEnum
    properties: Properties43


@dataclass
class ApplicationJSON126:
    schema: Schema36


@dataclass
class Content125:
    application_json: ApplicationJSON126


@dataclass
class RequestBody25:
    content: Content125


@dataclass
class Response54:
    description: str
    content: Optional[Content72] = None


@dataclass
class TicketsIDRemoveLineItemPost:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    request_body: RequestBody25
    responses: Dict[str, Response54]


@dataclass
class TicketsIDRemoveLineItem:
    post: TicketsIDRemoveLineItemPost


@dataclass
class Properties44:
    start_at: NextRun
    end_at: NextRun
    duration_minutes: SchemaValue
    user_id: CustomerExternalID
    notes: SchemaValue
    product_id: SchemaValue


@dataclass
class Schema37:
    type: TypeEnum
    properties: Properties44


@dataclass
class ApplicationJSON127:
    schema: Schema37


@dataclass
class Content126:
    application_json: ApplicationJSON127


@dataclass
class RequestBody26:
    content: Content126


@dataclass
class Example80:
    toggl_id: None
    product_id: None
    comment_id: None
    ticket_line_item_id: None
    id: Optional[int] = None
    ticket_id: Optional[int] = None
    user_id: Optional[int] = None
    start_time: Optional[str] = None
    end_time: Optional[str] = None
    recorded: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    billable: Optional[bool] = None
    notes: Optional[str] = None
    active_duration: Optional[int] = None
    error: Optional[str] = None


@dataclass
class ApplicationJSON128:
    example: Example80


@dataclass
class Content127:
    application_json: ApplicationJSON128


@dataclass
class Response55:
    description: str
    content: Content127


@dataclass
class TicketsIDTimerEntryPost:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    request_body: RequestBody26
    responses: Dict[str, Response55]


@dataclass
class TicketsIDTimerEntry:
    post: TicketsIDTimerEntryPost


@dataclass
class Properties45:
    ticket_line_item_id: SchemaValue
    name: SchemaValue
    upc_code: SchemaValue
    product_id: SchemaValue
    description: SchemaValue
    quantity: SchemaValue
    price_cost: SchemaValue
    price_retail: SchemaValue
    taxable: SchemaValue


@dataclass
class Schema38:
    type: TypeEnum
    properties: Properties45


@dataclass
class ApplicationJSON129:
    schema: Schema38


@dataclass
class Content128:
    application_json: ApplicationJSON129


@dataclass
class RequestBody27:
    content: Content128


@dataclass
class TicketLineItem:
    id: int
    ticket_id: int
    user_id: None
    product_id: None
    name: str
    description: str
    quantity: str
    product_category: None
    upc_code: None
    taxable: bool
    cost_cents: None
    retail_cents: int
    created_at: str
    updated_at: str
    converted: bool
    item_id: None
    position: int
    estimate_line_item_id: None
    old_price: None
    line_discount_percent: None
    discount_dollars: None
    original_ticket_line_item_id: None
    price_cost: int
    price_retail: int


@dataclass
class Example81:
    ticket_line_item: TicketLineItem


@dataclass
class ApplicationJSON130:
    example: Example81


@dataclass
class Content129:
    application_json: ApplicationJSON130


@dataclass
class Response56:
    description: str
    content: Optional[Content129] = None


@dataclass
class TicketsIDUpdateLineItemPut:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    request_body: RequestBody27
    responses: Dict[str, Response56]


@dataclass
class TicketsIDUpdateLineItem:
    put: TicketsIDUpdateLineItemPut


@dataclass
class Properties46:
    timer_entry_id: SchemaValue
    start_at: NextRun
    duration_minutes: SchemaValue
    user_id: CustomerExternalID
    notes: SchemaValue
    product_id: SchemaValue


@dataclass
class Schema39:
    type: TypeEnum
    properties: Properties46


@dataclass
class ApplicationJSON131:
    schema: Schema39


@dataclass
class Content130:
    application_json: ApplicationJSON131


@dataclass
class RequestBody28:
    content: Content130


@dataclass
class TicketsIDUpdateTimerEntryPut:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    request_body: RequestBody28
    responses: Dict[str, Response52]


@dataclass
class TicketsIDUpdateTimerEntry:
    put: TicketsIDUpdateTimerEntryPut


@dataclass
class PurpleUser:
    id: int
    name: str


@dataclass
class Example74:
    ticket_status_list: List[str]
    default_labor_product_id: None
    ticket_timer_charge_by_default: None
    saved_searches: List[Any]
    ticket_types: List[Any]
    ticket_type_fields: List[Any]
    ticket_type_field_answers: List[Any]
    appointment_types: List[Any]
    users: List[PurpleUser]
    dashboard_settings: None
    worksheet_templates: List[Any]
    require_ticket_type: None
    require_intake_form_with_ticket: None
    require_outtake_form_with_ticket: None
    ticket_workflow_default_id: None


@dataclass
class ApplicationJSON117:
    example: Example74


@dataclass
class Content116:
    application_json: ApplicationJSON117


@dataclass
class The200_28:
    description: str
    content: Content116


@dataclass
class Responses33:
    the_200: The200_28


@dataclass
class TicketsSettingsGet:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    responses: Responses33


@dataclass
class TicketsSettings:
    get: TicketsSettingsGet


@dataclass
class FieldList:
    name: str
    slug: str
    id: int
    position: int
    history: List[Any]


@dataclass
class WorksheetResult:
    id: int
    worksheet_template_id: int
    name: str
    public: bool
    complete: None
    required: bool
    field_list: List[FieldList]


@dataclass
class Example82:
    worksheet_results: List[WorksheetResult]


@dataclass
class ApplicationJSON132:
    example: Example82


@dataclass
class Content131:
    application_json: ApplicationJSON132


@dataclass
class The200_29:
    description: str
    content: Content131


@dataclass
class Responses34:
    the_200: The200_29


@dataclass
class TicketsTicketIDWorksheetResultsGet:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[Parameter2]
    responses: Responses34


@dataclass
class Properties47:
    worksheet_template_id: SchemaValue
    title: SchemaValue


@dataclass
class Schema40:
    type: TypeEnum
    properties: Properties47


@dataclass
class ApplicationJSON133:
    schema: Schema40


@dataclass
class Content132:
    application_json: ApplicationJSON133


@dataclass
class RequestBody29:
    content: Content132


@dataclass
class Example83:
    worksheet_result: WorksheetResult


@dataclass
class ApplicationJSON134:
    example: Example83


@dataclass
class Content133:
    application_json: ApplicationJSON134


@dataclass
class The200_30:
    description: str
    content: Content133


@dataclass
class Responses35:
    the_200: The200_30


@dataclass
class TicketsTicketIDWorksheetResultsPost:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    request_body: RequestBody29
    responses: Responses35


@dataclass
class TicketsTicketIDWorksheetResults:
    get: TicketsTicketIDWorksheetResultsGet
    post: TicketsTicketIDWorksheetResultsPost


@dataclass
class ApplicationJSON135:
    example: Example83


@dataclass
class Content134:
    application_json: ApplicationJSON135


@dataclass
class The200_31:
    description: str
    content: Content134


@dataclass
class Responses36:
    the_200: The200_31


@dataclass
class TicketsTicketIDWorksheetResultsIDGet:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    responses: Responses36


@dataclass
class AnswersProperties:
    value: SchemaValue
    user: SchemaValue


@dataclass
class Answers:
    type: TypeEnum
    properties: AnswersProperties


@dataclass
class Properties48:
    worksheet_template_id: SchemaValue
    user_id: SchemaValue
    title: SchemaValue
    complete: SchemaValue
    public: SchemaValue
    required: SchemaValue
    answers: Answers


@dataclass
class Schema41:
    type: TypeEnum
    properties: Properties48


@dataclass
class ApplicationJSON136:
    schema: Schema41


@dataclass
class Content135:
    application_json: ApplicationJSON136


@dataclass
class RequestBody30:
    content: Content135


@dataclass
class TicketsTicketIDWorksheetResultsIDPut:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    request_body: RequestBody30
    responses: Responses7


@dataclass
class TicketsTicketIDWorksheetResultsID:
    get: TicketsTicketIDWorksheetResultsIDGet
    put: TicketsTicketIDWorksheetResultsIDPut
    delete: TicketsIDPrintPost


@dataclass
class TimelogElement:
    id: int
    in_at: str
    out_at: None
    account_id: int
    user_id: int
    in_note: None
    out_note: None
    created_at: str
    updated_at: str
    lunch: None
    manually_updated: None


@dataclass
class Example84:
    timelogs: List[TimelogElement]


@dataclass
class ApplicationJSON137:
    example: Example84


@dataclass
class Content136:
    application_json: ApplicationJSON137


@dataclass
class The200_32:
    description: str
    content: Content136


@dataclass
class Responses37:
    the_200: The200_32


@dataclass
class TimelogsGet:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[StickyParameter]
    responses: Responses37


@dataclass
class Properties49:
    lunch: SchemaValue
    in_at: NextRun
    out_at: NextRun
    in_note: SchemaValue
    out_note: SchemaValue


@dataclass
class Schema42:
    type: TypeEnum
    properties: Properties49


@dataclass
class ApplicationJSON138:
    schema: Schema42


@dataclass
class Content137:
    application_json: ApplicationJSON138


@dataclass
class RequestBody31:
    content: Content137


@dataclass
class ApplicationJSON139:
    example: TimelogElement


@dataclass
class Content138:
    application_json: ApplicationJSON139


@dataclass
class The200_33:
    description: str
    content: Content138


@dataclass
class Responses38:
    the_200: The200_33


@dataclass
class TimelogsPut:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    request_body: RequestBody31
    responses: Responses38


@dataclass
class Timelogs:
    get: TimelogsGet
    put: TimelogsPut


@dataclass
class TimelogsLastGet:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[IndigoParameter]
    responses: Responses38


@dataclass
class TimelogsLast:
    get: TimelogsLastGet


@dataclass
class Properties50:
    device_uuid: SchemaValue
    device_name: SchemaValue
    registration_token_gcm: SchemaValue
    system_name: SchemaValue
    model: SchemaValue
    screen_size: SchemaValue


@dataclass
class Schema43:
    type: TypeEnum
    properties: Properties50


@dataclass
class ApplicationJSON140:
    schema: Schema43


@dataclass
class Content139:
    application_json: ApplicationJSON140


@dataclass
class RequestBody32:
    content: Content139


@dataclass
class Example85:
    account_id: None
    name: None
    device_name: None
    system_name: None
    model: None
    screen_size: None
    user_id: Optional[int] = None
    registration_token_gcm: Optional[str] = None
    id: Optional[int] = None
    device_uuid: Optional[str] = None
    disabled: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    message: Optional[str] = None


@dataclass
class ApplicationJSON141:
    example: Example85


@dataclass
class Content140:
    application_json: ApplicationJSON141


@dataclass
class Response57:
    description: str
    content: Content140


@dataclass
class UserDevicesPost:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    request_body: RequestBody32
    description: str
    responses: Dict[str, Response57]


@dataclass
class UserDevices:
    post: UserDevicesPost


@dataclass
class Example86:
    user_id: int
    registration_token_gcm: str
    id: int
    device_uuid: str
    account_id: None
    name: None
    device_name: None
    system_name: None
    model: None
    screen_size: None
    disabled: bool
    created_at: str
    updated_at: str


@dataclass
class ApplicationJSON142:
    example: Example86


@dataclass
class Content141:
    application_json: ApplicationJSON142


@dataclass
class The200_34:
    description: str
    content: Content141


@dataclass
class Responses39:
    the_200: The200_34


@dataclass
class UserDevicesIDGet:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    parameters: List[CunningParameter]
    description: str
    responses: Responses39


@dataclass
class Properties51:
    registration_token_gcm: SchemaValue


@dataclass
class Schema44:
    type: TypeEnum
    properties: Properties51


@dataclass
class ApplicationJSON143:
    schema: Schema44


@dataclass
class Content142:
    application_json: ApplicationJSON143


@dataclass
class RequestBody33:
    content: Content142


@dataclass
class Responses40:
    the_200: The200_34


@dataclass
class UserDevicesIDPut:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    parameters: List[CunningParameter]
    request_body: RequestBody33
    description: str
    responses: Responses40


@dataclass
class UserDevicesID:
    get: UserDevicesIDGet
    put: UserDevicesIDPut


@dataclass
class Example87:
    users: List[List[Union[int, str]]]


@dataclass
class ApplicationJSON144:
    example: Example87


@dataclass
class Content143:
    application_json: ApplicationJSON144


@dataclass
class The200_35:
    description: str
    content: Content143


@dataclass
class Responses41:
    the_200: The200_35


@dataclass
class UsersGet:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    responses: Responses41


@dataclass
class Users:
    get: UsersGet


@dataclass
class Example88:
    user: TicketUser


@dataclass
class ApplicationJSON145:
    example: Example88


@dataclass
class Content144:
    application_json: ApplicationJSON145


@dataclass
class The200_36:
    description: str
    content: Content144


@dataclass
class Responses42:
    the_200: The200_36


@dataclass
class UsersIDGet:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    parameters: List[PurpleParameter]
    responses: Responses42


@dataclass
class UsersID:
    get: UsersIDGet


@dataclass
class Example89:
    vendors: List[VendorElement]


@dataclass
class ApplicationJSON146:
    example: Example89


@dataclass
class Content145:
    application_json: ApplicationJSON146


@dataclass
class The200_37:
    description: str
    content: Content145


@dataclass
class Responses43:
    the_200: The200_37


@dataclass
class VendorsGet:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[IndigoParameter]
    responses: Responses43


@dataclass
class FriskyParams:
    name: str
    email: str


@dataclass
class Example90:
    vendor: Optional[VendorElement] = None
    success: Optional[bool] = None
    message: Optional[List[str]] = None
    params: Optional[FriskyParams] = None


@dataclass
class ApplicationJSON147:
    example: Example90


@dataclass
class Content146:
    application_json: ApplicationJSON147


@dataclass
class Response58:
    description: str
    content: Content146


@dataclass
class VendorsPost:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    request_body: FriskyRequestBody
    responses: Dict[str, Response58]


@dataclass
class Vendors:
    get: VendorsGet
    post: VendorsPost


@dataclass
class VendorProperties:
    id: SchemaValue
    name: SchemaValue
    rep_first_name: SchemaValue
    rep_last_name: SchemaValue
    email: SchemaValue
    phone: SchemaValue
    account_number: AllDay
    created_at: NextRun
    updated_at: NextRun
    address: SchemaValue
    city: SchemaValue
    state: SchemaValue
    zip: SchemaValue
    website: SchemaValue
    notes: SchemaValue


@dataclass
class PropertiesVendor:
    type: TypeEnum
    properties: VendorProperties


@dataclass
class Properties52:
    vendor: PropertiesVendor


@dataclass
class Schema45:
    type: TypeEnum
    properties: Properties52


@dataclass
class Indecent:
    schema: Schema45


@dataclass
class Content147:
    empty: Indecent


@dataclass
class Response59:
    description: str
    content: Optional[Content147] = None


@dataclass
class VendorsIDGet:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    responses: Dict[str, Response59]


@dataclass
class Example91:
    vendor: Optional[VendorElement] = None
    success: Optional[bool] = None
    message: Optional[List[str]] = None


@dataclass
class ApplicationJSON148:
    example: Example91


@dataclass
class Content148:
    application_json: ApplicationJSON148


@dataclass
class Response60:
    description: str
    content: Optional[Content148] = None


@dataclass
class VendorsIDPut:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    request_body: FriskyRequestBody
    responses: Dict[str, Response60]


@dataclass
class VendorsID:
    get: VendorsIDGet
    put: VendorsIDPut


@dataclass
class WikiPageElement:
    id: int
    account_id: int
    name: str
    slug: str
    body: str
    interpolated_body: str


@dataclass
class Example92:
    wiki_pages: List[WikiPageElement]


@dataclass
class ApplicationJSON149:
    example: Example92


@dataclass
class Content149:
    application_json: ApplicationJSON149


@dataclass
class The200_38:
    description: str
    content: Content149


@dataclass
class Responses44:
    the_200: The200_38


@dataclass
class WikiPagesGet:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[IndigoParameter]
    responses: Responses44


@dataclass
class Properties53:
    name: SchemaValue
    slug: SchemaValue
    body: SchemaValue
    customer_id: SchemaValue
    asset_id: SchemaValue
    visibility: SchemaValue


@dataclass
class Schema46:
    type: TypeEnum
    properties: Properties53


@dataclass
class ApplicationJSON150:
    schema: Schema46


@dataclass
class Content150:
    application_json: ApplicationJSON150


@dataclass
class RequestBody34:
    content: Content150
    description: str


@dataclass
class Example93:
    wiki_page: Optional[WikiPageElement] = None
    success: Optional[bool] = None
    errors: Optional[List[str]] = None
    params: Optional[FluffyParams] = None


@dataclass
class ApplicationJSON151:
    example: Example93


@dataclass
class Content151:
    application_json: ApplicationJSON151


@dataclass
class Response61:
    description: str
    content: Content151


@dataclass
class WikiPagesPost:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    request_body: RequestBody34
    responses: Dict[str, Response61]


@dataclass
class WikiPages:
    get: WikiPagesGet
    post: WikiPagesPost


@dataclass
class WikiPageProperties:
    id: SchemaValue
    account_id: SchemaValue
    name: SchemaValue
    slug: SchemaValue
    body: SchemaValue
    interpolated_body: SchemaValue


@dataclass
class PropertiesWikiPage:
    type: TypeEnum
    properties: WikiPageProperties


@dataclass
class Properties54:
    wiki_page: PropertiesWikiPage


@dataclass
class Schema47:
    type: TypeEnum
    properties: Properties54


@dataclass
class Hilarious:
    schema: Schema47


@dataclass
class Content152:
    empty: Hilarious


@dataclass
class Response62:
    description: str
    content: Optional[Content152] = None


@dataclass
class WikiPagesIDGet:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    responses: Dict[str, Response62]


@dataclass
class Content153:
    application_json: ApplicationJSON150


@dataclass
class RequestBody35:
    content: Content153
    description: str


@dataclass
class Response63:
    description: str
    content: Content151


@dataclass
class WikiPagesIDPut:
    summary: str
    tags: List[str]
    security: List[PostSecurity]
    description: str
    parameters: List[PurpleParameter]
    request_body: RequestBody35
    responses: Dict[str, Response63]


@dataclass
class WikiPagesID:
    get: WikiPagesIDGet
    put: WikiPagesIDPut
    delete: AppointmentTypesIDDelete


@dataclass
class Paths:
    appointment_types: AppointmentTypes
    appointment_types_id: AppointmentTypesID
    appointments: Appointments
    appointments_id: AppointmentsID
    customer_assets: CustomerAssets
    customer_assets_id: CustomerAssetsID
    callerid: Callerid
    contacts: Contacts
    contacts_id: ContactsID
    contracts: Contracts
    contracts_id: ContractsID
    customers: Customers
    customers_id: CustomersID
    customers_latest: CustomersLatest
    customers_autocomplete: CustomersAutocomplete
    estimates: Estimates
    estimates_id: EstimatesID
    estimates_id_print: EstimatesIDPrint
    estimates_id_email: EstimatesIDEmail
    estimates_id_line_items: EstimatesIDLineItems
    estimates_id_convert_to_invoice: EstimatesIDConvertToInvoice
    estimates_id_line_items_line_item_id: EstimatesIDLineItemsLineItemID
    invoices: Invoices
    invoices_id: InvoicesID
    invoices_id_line_items_line_item_id: InvoicesIDLineItemsLineItemID
    invoices_id_line_items: InvoicesIDLineItems
    invoices_id_ticket: InvoicesIDTicket
    invoices_id_print: InvoicesIDPrint
    invoices_id_email: InvoicesIDEmail
    items: Items
    leads: Leads
    leads_id: LeadsID
    line_items: LineItems
    new_ticket_forms: NewTicketForms
    new_ticket_forms_id: NewTicketFormsID
    new_ticket_forms_id_process_form: NewTicketFormsIDProcessForm
    payment_methods: PaymentMethods
    customers_customer_id_payment_profiles: CustomersCustomerIDPaymentProfiles
    customers_customer_id_payment_profiles_id: CustomersCustomerIDPaymentProfilesID
    payments: PaymentsClass
    payments_id: PaymentsID
    customers_customer_id_phones: CustomersCustomerIDPhones
    customers_customer_id_phones_id: CustomersCustomerIDPhonesID
    portal_users: PortalUsers
    portal_users_id: PortalUsersID
    portal_users_create_invitation: PortalUsersCreateInvitation
    products_product_id_product_serials: ProductsProductIDProductSerials
    products_product_id_product_serials_id: ProductsProductIDProductSerialsID
    products_product_id_product_serials_attach_to_line_item: ProductsProductIDProductSerialsAttachToLineItem
    products: Products
    products_id: ProductsID
    products_barcode: ProductsBarcode
    products_categories: ProductsCategories
    products_id_add_images: ProductsIDAddImages
    products_id_delete_image: ProductsIDDeleteImage
    products_id_location_quantities: ProductsIDLocationQuantities
    purchase_orders: PurchaseOrders
    purchase_orders_id: PurchaseOrdersID
    purchase_orders_id_receive: PurchaseOrdersIDReceive
    purchase_orders_id_create_po_line_item: PurchaseOrdersIDCreatePoLineItem
    rmm_alerts: RmmAlerts
    rmm_alerts_id_mute: RmmAlertsIDMute
    rmm_alerts_id: RmmAlertsID
    schedules: Schedules
    schedules_id: SchedulesID
    schedules_id_add_line_item: SchedulesIDAddLineItem
    schedules_id_remove_line_item: SchedulesIDRemoveLineItem
    schedules_id_line_items_schedule_line_item_id: SchedulesIDLineItemsScheduleLineItemID
    search: Search
    settings: Settings
    settings_tabs: SettingsTabs
    settings_printing: SettingsPrinting
    ticket_timers: TicketTimers
    tickets: Tickets
    tickets_id: TicketsID
    tickets_settings: TicketsSettings
    tickets_id_print: TicketsIDPrint
    tickets_id_comment: TicketsIDComment
    tickets_id_timer_entry: TicketsIDTimerEntry
    tickets_id_add_line_item: TicketsIDAddLineItem
    tickets_id_attach_file_url: TicketsIDAttachFileURL
    tickets_id_remove_line_item: TicketsIDRemoveLineItem
    tickets_id_update_line_item: TicketsIDUpdateLineItem
    tickets_id_delete_attachment: TicketsIDDeleteAttachment
    tickets_id_delete_timer_entry: TicketsIDDeleteTimerEntry
    tickets_id_update_timer_entry: TicketsIDUpdateTimerEntry
    tickets_id_charge_timer_entry: TicketsIDChargeTimerEntry
    timelogs: Timelogs
    timelogs_last: TimelogsLast
    user_devices: UserDevices
    user_devices_id: UserDevicesID
    me: Me
    users: Users
    otp_login: OtpLogin
    users_id: UsersID
    vendors: Vendors
    vendors_id: VendorsID
    wiki_pages: WikiPages
    wiki_pages_id: WikiPagesID
    tickets_ticket_id_worksheet_results: TicketsTicketIDWorksheetResults
    tickets_ticket_id_worksheet_results_id: TicketsTicketIDWorksheetResultsID


@dataclass
class Subdomain:
    default: str
    description: str


@dataclass
class Variables:
    subdomain: Subdomain


@dataclass
class Server:
    url: str
    variables: Variables


@dataclass
class Welcome:
    openapi: str
    info: Info
    external_docs: ExternalDocs
    paths: Paths
    servers: List[Server]
    components: Components

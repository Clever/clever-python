# coding: utf-8

"""
    Clever API

    The Clever API

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into sdk package
from .models.bad_request import BadRequest
from .models.contact import Contact
from .models.contact_object import ContactObject
from .models.contact_response import ContactResponse
from .models.contacts_response import ContactsResponse
from .models.course import Course
from .models.course_object import CourseObject
from .models.course_response import CourseResponse
from .models.courses_response import CoursesResponse
from .models.credentials import Credentials
from .models.district import District
from .models.district_admin import DistrictAdmin
from .models.district_admin_object import DistrictAdminObject
from .models.district_admin_response import DistrictAdminResponse
from .models.district_admins_response import DistrictAdminsResponse
from .models.district_object import DistrictObject
from .models.district_response import DistrictResponse
from .models.districts_response import DistrictsResponse
from .models.event import Event
from .models.event_response import EventResponse
from .models.events_response import EventsResponse
from .models.internal_error import InternalError
from .models.location import Location
from .models.name import Name
from .models.not_found import NotFound
from .models.principal import Principal
from .models.school import School
from .models.school_admin import SchoolAdmin
from .models.school_admin_object import SchoolAdminObject
from .models.school_admin_response import SchoolAdminResponse
from .models.school_admins_response import SchoolAdminsResponse
from .models.school_object import SchoolObject
from .models.school_response import SchoolResponse
from .models.schools_response import SchoolsResponse
from .models.section import Section
from .models.section_object import SectionObject
from .models.section_response import SectionResponse
from .models.sections_response import SectionsResponse
from .models.student import Student
from .models.student_object import StudentObject
from .models.student_response import StudentResponse
from .models.students_response import StudentsResponse
from .models.teacher import Teacher
from .models.teacher_object import TeacherObject
from .models.teacher_response import TeacherResponse
from .models.teachers_response import TeachersResponse
from .models.term import Term
from .models.term_object import TermObject
from .models.term_response import TermResponse
from .models.terms_response import TermsResponse
from .models.contacts_created import ContactsCreated
from .models.contacts_deleted import ContactsDeleted
from .models.contacts_updated import ContactsUpdated
from .models.courses_created import CoursesCreated
from .models.courses_deleted import CoursesDeleted
from .models.courses_updated import CoursesUpdated
from .models.districtadmins_created import DistrictadminsCreated
from .models.districtadmins_deleted import DistrictadminsDeleted
from .models.districtadmins_updated import DistrictadminsUpdated
from .models.districts_created import DistrictsCreated
from .models.districts_deleted import DistrictsDeleted
from .models.districts_updated import DistrictsUpdated
from .models.schooladmins_created import SchooladminsCreated
from .models.schooladmins_deleted import SchooladminsDeleted
from .models.schooladmins_updated import SchooladminsUpdated
from .models.schools_created import SchoolsCreated
from .models.schools_deleted import SchoolsDeleted
from .models.schools_updated import SchoolsUpdated
from .models.sections_created import SectionsCreated
from .models.sections_deleted import SectionsDeleted
from .models.sections_updated import SectionsUpdated
from .models.students_created import StudentsCreated
from .models.students_deleted import StudentsDeleted
from .models.students_updated import StudentsUpdated
from .models.teachers_created import TeachersCreated
from .models.teachers_deleted import TeachersDeleted
from .models.teachers_updated import TeachersUpdated
from .models.terms_created import TermsCreated
from .models.terms_deleted import TermsDeleted
from .models.terms_updated import TermsUpdated

# import apis into sdk package
from .apis.data_api import DataApi
from .apis.events_api import EventsApi

# import ApiClient
from .api_client import ApiClient

from .configuration import Configuration

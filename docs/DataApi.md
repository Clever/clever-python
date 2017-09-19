# swagger_client.DataApi

All URIs are relative to *https://api.clever.com/v1.2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_contact**](DataApi.md#get_contact) | **GET** /contacts/{id} | 
[**get_contacts**](DataApi.md#get_contacts) | **GET** /contacts | 
[**get_contacts_for_student**](DataApi.md#get_contacts_for_student) | **GET** /students/{id}/contacts | 
[**get_district**](DataApi.md#get_district) | **GET** /districts/{id} | 
[**get_district_admin**](DataApi.md#get_district_admin) | **GET** /district_admins/{id} | 
[**get_district_admins**](DataApi.md#get_district_admins) | **GET** /district_admins | 
[**get_district_for_school**](DataApi.md#get_district_for_school) | **GET** /schools/{id}/district | 
[**get_district_for_section**](DataApi.md#get_district_for_section) | **GET** /sections/{id}/district | 
[**get_district_for_student**](DataApi.md#get_district_for_student) | **GET** /students/{id}/district | 
[**get_district_for_student_contact**](DataApi.md#get_district_for_student_contact) | **GET** /contacts/{id}/district | 
[**get_district_for_teacher**](DataApi.md#get_district_for_teacher) | **GET** /teachers/{id}/district | 
[**get_district_status**](DataApi.md#get_district_status) | **GET** /districts/{id}/status | 
[**get_districts**](DataApi.md#get_districts) | **GET** /districts | 
[**get_grade_levels_for_teacher**](DataApi.md#get_grade_levels_for_teacher) | **GET** /teachers/{id}/grade_levels | 
[**get_school**](DataApi.md#get_school) | **GET** /schools/{id} | 
[**get_school_admin**](DataApi.md#get_school_admin) | **GET** /school_admins/{id} | 
[**get_school_admins**](DataApi.md#get_school_admins) | **GET** /school_admins | 
[**get_school_for_section**](DataApi.md#get_school_for_section) | **GET** /sections/{id}/school | 
[**get_school_for_student**](DataApi.md#get_school_for_student) | **GET** /students/{id}/school | 
[**get_school_for_teacher**](DataApi.md#get_school_for_teacher) | **GET** /teachers/{id}/school | 
[**get_schools**](DataApi.md#get_schools) | **GET** /schools | 
[**get_schools_for_school_admin**](DataApi.md#get_schools_for_school_admin) | **GET** /school_admins/{id}/schools | 
[**get_section**](DataApi.md#get_section) | **GET** /sections/{id} | 
[**get_sections**](DataApi.md#get_sections) | **GET** /sections | 
[**get_sections_for_school**](DataApi.md#get_sections_for_school) | **GET** /schools/{id}/sections | 
[**get_sections_for_student**](DataApi.md#get_sections_for_student) | **GET** /students/{id}/sections | 
[**get_sections_for_teacher**](DataApi.md#get_sections_for_teacher) | **GET** /teachers/{id}/sections | 
[**get_student**](DataApi.md#get_student) | **GET** /students/{id} | 
[**get_student_for_contact**](DataApi.md#get_student_for_contact) | **GET** /contacts/{id}/student | 
[**get_students**](DataApi.md#get_students) | **GET** /students | 
[**get_students_for_school**](DataApi.md#get_students_for_school) | **GET** /schools/{id}/students | 
[**get_students_for_section**](DataApi.md#get_students_for_section) | **GET** /sections/{id}/students | 
[**get_students_for_teacher**](DataApi.md#get_students_for_teacher) | **GET** /teachers/{id}/students | 
[**get_teacher**](DataApi.md#get_teacher) | **GET** /teachers/{id} | 
[**get_teacher_for_section**](DataApi.md#get_teacher_for_section) | **GET** /sections/{id}/teacher | 
[**get_teachers**](DataApi.md#get_teachers) | **GET** /teachers | 
[**get_teachers_for_school**](DataApi.md#get_teachers_for_school) | **GET** /schools/{id}/teachers | 
[**get_teachers_for_section**](DataApi.md#get_teachers_for_section) | **GET** /sections/{id}/teachers | 
[**get_teachers_for_student**](DataApi.md#get_teachers_for_student) | **GET** /students/{id}/teachers | 


# **get_contact**
> StudentContactResponse get_contact(id)



Returns a specific student contact

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.DataApi()
id = 'id_example' # str | 

try: 
    api_response = api_instance.get_contact(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**StudentContactResponse**](StudentContactResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contacts**
> StudentContactsResponse get_contacts(limit=limit, starting_after=starting_after, ending_before=ending_before)



Returns a list of student contacts

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.DataApi()
limit = 56 # int |  (optional)
starting_after = 'starting_after_example' # str |  (optional)
ending_before = 'ending_before_example' # str |  (optional)

try: 
    api_response = api_instance.get_contacts(limit=limit, starting_after=starting_after, ending_before=ending_before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_contacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] 
 **starting_after** | **str**|  | [optional] 
 **ending_before** | **str**|  | [optional] 

### Return type

[**StudentContactsResponse**](StudentContactsResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contacts_for_student**
> StudentContactsForStudentResponse get_contacts_for_student(id, limit=limit)



Returns the contacts for a student

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.DataApi()
id = 'id_example' # str | 
limit = 56 # int |  (optional)

try: 
    api_response = api_instance.get_contacts_for_student(id, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_contacts_for_student: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **limit** | **int**|  | [optional] 

### Return type

[**StudentContactsForStudentResponse**](StudentContactsForStudentResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_district**
> DistrictResponse get_district(id)



Returns a specific district

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.DataApi()
id = 'id_example' # str | 

try: 
    api_response = api_instance.get_district(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_district: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**DistrictResponse**](DistrictResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_district_admin**
> DistrictAdminResponse get_district_admin(id)



Returns a specific district admin

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.DataApi()
id = 'id_example' # str | 

try: 
    api_response = api_instance.get_district_admin(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_district_admin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**DistrictAdminResponse**](DistrictAdminResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_district_admins**
> DistrictAdminsResponse get_district_admins(starting_after=starting_after, ending_before=ending_before)



Returns a list of district admins

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.DataApi()
starting_after = 'starting_after_example' # str |  (optional)
ending_before = 'ending_before_example' # str |  (optional)

try: 
    api_response = api_instance.get_district_admins(starting_after=starting_after, ending_before=ending_before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_district_admins: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **starting_after** | **str**|  | [optional] 
 **ending_before** | **str**|  | [optional] 

### Return type

[**DistrictAdminsResponse**](DistrictAdminsResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_district_for_school**
> DistrictResponse get_district_for_school(id)



Returns the district for a school

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.DataApi()
id = 'id_example' # str | 

try: 
    api_response = api_instance.get_district_for_school(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_district_for_school: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**DistrictResponse**](DistrictResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_district_for_section**
> DistrictResponse get_district_for_section(id)



Returns the district for a section

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.DataApi()
id = 'id_example' # str | 

try: 
    api_response = api_instance.get_district_for_section(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_district_for_section: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**DistrictResponse**](DistrictResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_district_for_student**
> DistrictResponse get_district_for_student(id)



Returns the district for a student

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.DataApi()
id = 'id_example' # str | 

try: 
    api_response = api_instance.get_district_for_student(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_district_for_student: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**DistrictResponse**](DistrictResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_district_for_student_contact**
> DistrictResponse get_district_for_student_contact(id)



Returns the district for a student contact

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.DataApi()
id = 'id_example' # str | 

try: 
    api_response = api_instance.get_district_for_student_contact(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_district_for_student_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**DistrictResponse**](DistrictResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_district_for_teacher**
> DistrictResponse get_district_for_teacher(id)



Returns the district for a teacher

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.DataApi()
id = 'id_example' # str | 

try: 
    api_response = api_instance.get_district_for_teacher(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_district_for_teacher: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**DistrictResponse**](DistrictResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_district_status**
> DistrictStatusResponses get_district_status(id)



Returns the status of the district

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.DataApi()
id = 'id_example' # str | 

try: 
    api_response = api_instance.get_district_status(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_district_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**DistrictStatusResponses**](DistrictStatusResponses.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_districts**
> DistrictsResponse get_districts()



Returns a list of districts

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.DataApi()

try: 
    api_response = api_instance.get_districts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_districts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DistrictsResponse**](DistrictsResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_grade_levels_for_teacher**
> GradeLevelsResponse get_grade_levels_for_teacher(id)



Returns the grade levels for sections a teacher teaches

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.DataApi()
id = 'id_example' # str | 

try: 
    api_response = api_instance.get_grade_levels_for_teacher(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_grade_levels_for_teacher: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**GradeLevelsResponse**](GradeLevelsResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_school**
> SchoolResponse get_school(id)



Returns a specific school

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.DataApi()
id = 'id_example' # str | 

try: 
    api_response = api_instance.get_school(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_school: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**SchoolResponse**](SchoolResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_school_admin**
> SchoolAdminResponse get_school_admin(id)



Returns a specific school admin

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.DataApi()
id = 'id_example' # str | 

try: 
    api_response = api_instance.get_school_admin(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_school_admin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**SchoolAdminResponse**](SchoolAdminResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_school_admins**
> SchoolAdminsResponse get_school_admins(limit=limit, starting_after=starting_after, ending_before=ending_before)



Returns a list of school admins

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.DataApi()
limit = 56 # int |  (optional)
starting_after = 'starting_after_example' # str |  (optional)
ending_before = 'ending_before_example' # str |  (optional)

try: 
    api_response = api_instance.get_school_admins(limit=limit, starting_after=starting_after, ending_before=ending_before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_school_admins: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] 
 **starting_after** | **str**|  | [optional] 
 **ending_before** | **str**|  | [optional] 

### Return type

[**SchoolAdminsResponse**](SchoolAdminsResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_school_for_section**
> SchoolResponse get_school_for_section(id)



Returns the school for a section

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.DataApi()
id = 'id_example' # str | 

try: 
    api_response = api_instance.get_school_for_section(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_school_for_section: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**SchoolResponse**](SchoolResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_school_for_student**
> SchoolResponse get_school_for_student(id)



Returns the primary school for a student

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.DataApi()
id = 'id_example' # str | 

try: 
    api_response = api_instance.get_school_for_student(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_school_for_student: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**SchoolResponse**](SchoolResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_school_for_teacher**
> SchoolResponse get_school_for_teacher(id)



Retrieves school info for a teacher.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.DataApi()
id = 'id_example' # str | 

try: 
    api_response = api_instance.get_school_for_teacher(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_school_for_teacher: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**SchoolResponse**](SchoolResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schools**
> SchoolsResponse get_schools(limit=limit, starting_after=starting_after, ending_before=ending_before)



Returns a list of schools

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.DataApi()
limit = 56 # int |  (optional)
starting_after = 'starting_after_example' # str |  (optional)
ending_before = 'ending_before_example' # str |  (optional)

try: 
    api_response = api_instance.get_schools(limit=limit, starting_after=starting_after, ending_before=ending_before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_schools: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] 
 **starting_after** | **str**|  | [optional] 
 **ending_before** | **str**|  | [optional] 

### Return type

[**SchoolsResponse**](SchoolsResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schools_for_school_admin**
> SchoolsResponse get_schools_for_school_admin(id, limit=limit, starting_after=starting_after, ending_before=ending_before)



Returns the schools for a school admin

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.DataApi()
id = 'id_example' # str | 
limit = 56 # int |  (optional)
starting_after = 'starting_after_example' # str |  (optional)
ending_before = 'ending_before_example' # str |  (optional)

try: 
    api_response = api_instance.get_schools_for_school_admin(id, limit=limit, starting_after=starting_after, ending_before=ending_before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_schools_for_school_admin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **limit** | **int**|  | [optional] 
 **starting_after** | **str**|  | [optional] 
 **ending_before** | **str**|  | [optional] 

### Return type

[**SchoolsResponse**](SchoolsResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_section**
> SectionResponse get_section(id)



Returns a specific section

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.DataApi()
id = 'id_example' # str | 

try: 
    api_response = api_instance.get_section(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_section: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**SectionResponse**](SectionResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sections**
> SectionsResponse get_sections(limit=limit, starting_after=starting_after, ending_before=ending_before)



Returns a list of sections

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.DataApi()
limit = 56 # int |  (optional)
starting_after = 'starting_after_example' # str |  (optional)
ending_before = 'ending_before_example' # str |  (optional)

try: 
    api_response = api_instance.get_sections(limit=limit, starting_after=starting_after, ending_before=ending_before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_sections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] 
 **starting_after** | **str**|  | [optional] 
 **ending_before** | **str**|  | [optional] 

### Return type

[**SectionsResponse**](SectionsResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sections_for_school**
> SectionsResponse get_sections_for_school(id, limit=limit, starting_after=starting_after, ending_before=ending_before)



Returns the sections for a school

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.DataApi()
id = 'id_example' # str | 
limit = 56 # int |  (optional)
starting_after = 'starting_after_example' # str |  (optional)
ending_before = 'ending_before_example' # str |  (optional)

try: 
    api_response = api_instance.get_sections_for_school(id, limit=limit, starting_after=starting_after, ending_before=ending_before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_sections_for_school: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **limit** | **int**|  | [optional] 
 **starting_after** | **str**|  | [optional] 
 **ending_before** | **str**|  | [optional] 

### Return type

[**SectionsResponse**](SectionsResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sections_for_student**
> SectionsResponse get_sections_for_student(id, limit=limit, starting_after=starting_after, ending_before=ending_before)



Returns the sections for a student

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.DataApi()
id = 'id_example' # str | 
limit = 56 # int |  (optional)
starting_after = 'starting_after_example' # str |  (optional)
ending_before = 'ending_before_example' # str |  (optional)

try: 
    api_response = api_instance.get_sections_for_student(id, limit=limit, starting_after=starting_after, ending_before=ending_before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_sections_for_student: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **limit** | **int**|  | [optional] 
 **starting_after** | **str**|  | [optional] 
 **ending_before** | **str**|  | [optional] 

### Return type

[**SectionsResponse**](SectionsResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sections_for_teacher**
> SectionsResponse get_sections_for_teacher(id, limit=limit, starting_after=starting_after, ending_before=ending_before)



Returns the sections for a teacher

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.DataApi()
id = 'id_example' # str | 
limit = 56 # int |  (optional)
starting_after = 'starting_after_example' # str |  (optional)
ending_before = 'ending_before_example' # str |  (optional)

try: 
    api_response = api_instance.get_sections_for_teacher(id, limit=limit, starting_after=starting_after, ending_before=ending_before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_sections_for_teacher: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **limit** | **int**|  | [optional] 
 **starting_after** | **str**|  | [optional] 
 **ending_before** | **str**|  | [optional] 

### Return type

[**SectionsResponse**](SectionsResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_student**
> StudentResponse get_student(id)



Returns a specific student

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.DataApi()
id = 'id_example' # str | 

try: 
    api_response = api_instance.get_student(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_student: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**StudentResponse**](StudentResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_student_for_contact**
> StudentResponse get_student_for_contact(id)



Returns the student for a student contact

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.DataApi()
id = 'id_example' # str | 

try: 
    api_response = api_instance.get_student_for_contact(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_student_for_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**StudentResponse**](StudentResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_students**
> StudentsResponse get_students(limit=limit, starting_after=starting_after, ending_before=ending_before)



Returns a list of students

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.DataApi()
limit = 56 # int |  (optional)
starting_after = 'starting_after_example' # str |  (optional)
ending_before = 'ending_before_example' # str |  (optional)

try: 
    api_response = api_instance.get_students(limit=limit, starting_after=starting_after, ending_before=ending_before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_students: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] 
 **starting_after** | **str**|  | [optional] 
 **ending_before** | **str**|  | [optional] 

### Return type

[**StudentsResponse**](StudentsResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_students_for_school**
> StudentsResponse get_students_for_school(id, limit=limit, starting_after=starting_after, ending_before=ending_before)



Returns the students for a school

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.DataApi()
id = 'id_example' # str | 
limit = 56 # int |  (optional)
starting_after = 'starting_after_example' # str |  (optional)
ending_before = 'ending_before_example' # str |  (optional)

try: 
    api_response = api_instance.get_students_for_school(id, limit=limit, starting_after=starting_after, ending_before=ending_before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_students_for_school: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **limit** | **int**|  | [optional] 
 **starting_after** | **str**|  | [optional] 
 **ending_before** | **str**|  | [optional] 

### Return type

[**StudentsResponse**](StudentsResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_students_for_section**
> StudentsResponse get_students_for_section(id, limit=limit, starting_after=starting_after, ending_before=ending_before)



Returns the students for a section

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.DataApi()
id = 'id_example' # str | 
limit = 56 # int |  (optional)
starting_after = 'starting_after_example' # str |  (optional)
ending_before = 'ending_before_example' # str |  (optional)

try: 
    api_response = api_instance.get_students_for_section(id, limit=limit, starting_after=starting_after, ending_before=ending_before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_students_for_section: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **limit** | **int**|  | [optional] 
 **starting_after** | **str**|  | [optional] 
 **ending_before** | **str**|  | [optional] 

### Return type

[**StudentsResponse**](StudentsResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_students_for_teacher**
> StudentsResponse get_students_for_teacher(id, limit=limit, starting_after=starting_after, ending_before=ending_before)



Returns the students for a teacher

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.DataApi()
id = 'id_example' # str | 
limit = 56 # int |  (optional)
starting_after = 'starting_after_example' # str |  (optional)
ending_before = 'ending_before_example' # str |  (optional)

try: 
    api_response = api_instance.get_students_for_teacher(id, limit=limit, starting_after=starting_after, ending_before=ending_before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_students_for_teacher: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **limit** | **int**|  | [optional] 
 **starting_after** | **str**|  | [optional] 
 **ending_before** | **str**|  | [optional] 

### Return type

[**StudentsResponse**](StudentsResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_teacher**
> TeacherResponse get_teacher(id)



Returns a specific teacher

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.DataApi()
id = 'id_example' # str | 

try: 
    api_response = api_instance.get_teacher(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_teacher: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**TeacherResponse**](TeacherResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_teacher_for_section**
> TeacherResponse get_teacher_for_section(id)



Returns the primary teacher for a section

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.DataApi()
id = 'id_example' # str | 

try: 
    api_response = api_instance.get_teacher_for_section(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_teacher_for_section: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**TeacherResponse**](TeacherResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_teachers**
> TeachersResponse get_teachers(limit=limit, starting_after=starting_after, ending_before=ending_before)



Returns a list of teachers

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.DataApi()
limit = 56 # int |  (optional)
starting_after = 'starting_after_example' # str |  (optional)
ending_before = 'ending_before_example' # str |  (optional)

try: 
    api_response = api_instance.get_teachers(limit=limit, starting_after=starting_after, ending_before=ending_before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_teachers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] 
 **starting_after** | **str**|  | [optional] 
 **ending_before** | **str**|  | [optional] 

### Return type

[**TeachersResponse**](TeachersResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_teachers_for_school**
> TeachersResponse get_teachers_for_school(id, limit=limit, starting_after=starting_after, ending_before=ending_before)



Returns the teachers for a school

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.DataApi()
id = 'id_example' # str | 
limit = 56 # int |  (optional)
starting_after = 'starting_after_example' # str |  (optional)
ending_before = 'ending_before_example' # str |  (optional)

try: 
    api_response = api_instance.get_teachers_for_school(id, limit=limit, starting_after=starting_after, ending_before=ending_before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_teachers_for_school: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **limit** | **int**|  | [optional] 
 **starting_after** | **str**|  | [optional] 
 **ending_before** | **str**|  | [optional] 

### Return type

[**TeachersResponse**](TeachersResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_teachers_for_section**
> TeachersResponse get_teachers_for_section(id, limit=limit, starting_after=starting_after, ending_before=ending_before)



Returns the teachers for a section

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.DataApi()
id = 'id_example' # str | 
limit = 56 # int |  (optional)
starting_after = 'starting_after_example' # str |  (optional)
ending_before = 'ending_before_example' # str |  (optional)

try: 
    api_response = api_instance.get_teachers_for_section(id, limit=limit, starting_after=starting_after, ending_before=ending_before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_teachers_for_section: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **limit** | **int**|  | [optional] 
 **starting_after** | **str**|  | [optional] 
 **ending_before** | **str**|  | [optional] 

### Return type

[**TeachersResponse**](TeachersResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_teachers_for_student**
> TeachersResponse get_teachers_for_student(id, limit=limit, starting_after=starting_after, ending_before=ending_before)



Returns the teachers for a student

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.DataApi()
id = 'id_example' # str | 
limit = 56 # int |  (optional)
starting_after = 'starting_after_example' # str |  (optional)
ending_before = 'ending_before_example' # str |  (optional)

try: 
    api_response = api_instance.get_teachers_for_student(id, limit=limit, starting_after=starting_after, ending_before=ending_before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_teachers_for_student: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **limit** | **int**|  | [optional] 
 **starting_after** | **str**|  | [optional] 
 **ending_before** | **str**|  | [optional] 

### Return type

[**TeachersResponse**](TeachersResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


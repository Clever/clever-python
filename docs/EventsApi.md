# swagger_client.EventsApi

All URIs are relative to *https://api.clever.com/v1.2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_event**](EventsApi.md#get_event) | **GET** /events/{id} | 
[**get_events**](EventsApi.md#get_events) | **GET** /events | 
[**get_events_for_school**](EventsApi.md#get_events_for_school) | **GET** /schools/{id}/events | 
[**get_events_for_school_admin**](EventsApi.md#get_events_for_school_admin) | **GET** /school_admins/{id}/events | 
[**get_events_for_section**](EventsApi.md#get_events_for_section) | **GET** /sections/{id}/events | 
[**get_events_for_student**](EventsApi.md#get_events_for_student) | **GET** /students/{id}/events | 
[**get_events_for_teacher**](EventsApi.md#get_events_for_teacher) | **GET** /teachers/{id}/events | 


# **get_event**
> EventResponse get_event(id)



Returns the specific event

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
api_instance = swagger_client.EventsApi()
id = 'id_example' # str | 

try: 
    api_response = api_instance.get_event(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->get_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**EventResponse**](EventResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_events**
> EventsResponse get_events(limit=limit, starting_after=starting_after, ending_before=ending_before)



Returns a list of events

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
api_instance = swagger_client.EventsApi()
limit = 56 # int |  (optional)
starting_after = 'starting_after_example' # str |  (optional)
ending_before = 'ending_before_example' # str |  (optional)

try: 
    api_response = api_instance.get_events(limit=limit, starting_after=starting_after, ending_before=ending_before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->get_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] 
 **starting_after** | **str**|  | [optional] 
 **ending_before** | **str**|  | [optional] 

### Return type

[**EventsResponse**](EventsResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_events_for_school**
> EventsResponse get_events_for_school(id, limit=limit, starting_after=starting_after, ending_before=ending_before)



Returns a list of events for a school

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
api_instance = swagger_client.EventsApi()
id = 'id_example' # str | 
limit = 56 # int |  (optional)
starting_after = 'starting_after_example' # str |  (optional)
ending_before = 'ending_before_example' # str |  (optional)

try: 
    api_response = api_instance.get_events_for_school(id, limit=limit, starting_after=starting_after, ending_before=ending_before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->get_events_for_school: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **limit** | **int**|  | [optional] 
 **starting_after** | **str**|  | [optional] 
 **ending_before** | **str**|  | [optional] 

### Return type

[**EventsResponse**](EventsResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_events_for_school_admin**
> EventsResponse get_events_for_school_admin(id, limit=limit, starting_after=starting_after, ending_before=ending_before)



Returns a list of events for a school admin

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
api_instance = swagger_client.EventsApi()
id = 'id_example' # str | 
limit = 56 # int |  (optional)
starting_after = 'starting_after_example' # str |  (optional)
ending_before = 'ending_before_example' # str |  (optional)

try: 
    api_response = api_instance.get_events_for_school_admin(id, limit=limit, starting_after=starting_after, ending_before=ending_before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->get_events_for_school_admin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **limit** | **int**|  | [optional] 
 **starting_after** | **str**|  | [optional] 
 **ending_before** | **str**|  | [optional] 

### Return type

[**EventsResponse**](EventsResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_events_for_section**
> EventsResponse get_events_for_section(id, limit=limit, starting_after=starting_after, ending_before=ending_before)



Returns a list of events for a section

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
api_instance = swagger_client.EventsApi()
id = 'id_example' # str | 
limit = 56 # int |  (optional)
starting_after = 'starting_after_example' # str |  (optional)
ending_before = 'ending_before_example' # str |  (optional)

try: 
    api_response = api_instance.get_events_for_section(id, limit=limit, starting_after=starting_after, ending_before=ending_before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->get_events_for_section: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **limit** | **int**|  | [optional] 
 **starting_after** | **str**|  | [optional] 
 **ending_before** | **str**|  | [optional] 

### Return type

[**EventsResponse**](EventsResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_events_for_student**
> EventsResponse get_events_for_student(id, limit=limit, starting_after=starting_after, ending_before=ending_before)



Returns a list of events for a student

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
api_instance = swagger_client.EventsApi()
id = 'id_example' # str | 
limit = 56 # int |  (optional)
starting_after = 'starting_after_example' # str |  (optional)
ending_before = 'ending_before_example' # str |  (optional)

try: 
    api_response = api_instance.get_events_for_student(id, limit=limit, starting_after=starting_after, ending_before=ending_before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->get_events_for_student: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **limit** | **int**|  | [optional] 
 **starting_after** | **str**|  | [optional] 
 **ending_before** | **str**|  | [optional] 

### Return type

[**EventsResponse**](EventsResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_events_for_teacher**
> EventsResponse get_events_for_teacher(id, limit=limit, starting_after=starting_after, ending_before=ending_before)



Returns a list of events for a teacher

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
api_instance = swagger_client.EventsApi()
id = 'id_example' # str | 
limit = 56 # int |  (optional)
starting_after = 'starting_after_example' # str |  (optional)
ending_before = 'ending_before_example' # str |  (optional)

try: 
    api_response = api_instance.get_events_for_teacher(id, limit=limit, starting_after=starting_after, ending_before=ending_before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->get_events_for_teacher: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **limit** | **int**|  | [optional] 
 **starting_after** | **str**|  | [optional] 
 **ending_before** | **str**|  | [optional] 

### Return type

[**EventsResponse**](EventsResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


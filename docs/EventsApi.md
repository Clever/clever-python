# clever.EventsApi

All URIs are relative to *https://api.clever.com/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_event**](EventsApi.md#get_event) | **GET** /events/{id} | 
[**get_events**](EventsApi.md#get_events) | **GET** /events | 


# **get_event**
> EventResponse get_event(id)



Returns the specific event

### Example 
```python
from __future__ import print_function
import time
import clever
from clever.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
configuration = clever.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = clever.EventsApi(clever.ApiClient(configuration))
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

[oauth](README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_events**
> EventsResponse get_events(limit=limit, starting_after=starting_after, ending_before=ending_before, school=school, record_type=record_type)



Returns a list of events

### Example 
```python
from __future__ import print_function
import time
import clever
from clever.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
configuration = clever.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = clever.EventsApi(clever.ApiClient(configuration))
limit = 56 # int |  (optional)
starting_after = 'starting_after_example' # str |  (optional)
ending_before = 'ending_before_example' # str |  (optional)
school = 'school_example' # str |  (optional)
record_type = ['record_type_example'] # list[str] |  (optional)

try: 
    api_response = api_instance.get_events(limit=limit, starting_after=starting_after, ending_before=ending_before, school=school, record_type=record_type)
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
 **school** | **str**|  | [optional] 
 **record_type** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**EventsResponse**](EventsResponse.md)

### Authorization

[oauth](README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)


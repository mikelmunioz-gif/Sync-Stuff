
# TestIntegration

None

Python Version - 3



## Actions
#### TestAction

Timeout - 600 Seconds



##### JSON Results
```json
{}
```



#### SecondTestAction

Timeout - 600 Seconds



##### JSON Results
```json
{}
```






## Jobs

#### SegundoJob


|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|Test|True|String|Hola|
|Dry Run|False|Boolean|false|
|Max Items|False|Integer|100|
|Prueba|True|String|Param|

#### TestJob


#### TercerJob




## Connectors
#### MyTestConnector


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|DeviceProductField|The field name used to determine the device product|True|String|product_name|
|EventClassId|The field name used to determine the event name (sub-type)|True|String|event_name|
|PythonProcessTimeout|The timeout limit (in seconds) for the python process running current script|True|String|30|


#### PruebaDesaparecer


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|DeviceProductField|The field name used to determine the device product|True|String|product_name|
|EventClassId|The field name used to determine the event name (sub-type)|True|String|event_name|
|PythonProcessTimeout|The timeout limit (in seconds) for the python process running current script|True|String|30|


#### MySecondTestConnector


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|DeviceProductField|The field name used to determine the device product|True|String|product_name|
|EventClassId|The field name used to determine the event name (sub-type)|True|String|event_name|
|PythonProcessTimeout|The timeout limit (in seconds) for the python process running current script|True|String|30|





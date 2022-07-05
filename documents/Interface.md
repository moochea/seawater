# Inteface Summary 

 ## Back End Server
 Base url: (host ip):80/api/dataAccess

 Description: REST API for the front end application to access


### GET /records/**(key)**/**(data_ref)**
Description: Tabulated data from the selected data source

Resources:
* key - a supported data source 
* data_ref - type/structure/class of data / information requested

Returns:
if either key or data_ref are not supported: HTTPStatus.NOT_FOUND

If both key and data_ref are supported

```
{
    'status': 'success',
    'data': (data)
    'units': (units)
    'source': (str)
    'totalRecords': (int)
}
```
#### Parameter structure examples:
data:
```
[ 
     {
        "conductivity": 3.3808,
        "temperature": 4.5782,
        "pressure": 722.723,
        "salinity": 34.9799
        "timestamp":  "2017-01-08 00:30:00"
    }, 
    {   
        "conductivity": 3.2625, 
        "temperature": 4.7225, 
        "pressure": 1715.235
        "salinity": 34.9799
        "timestamp":  "2017-01-08 00:45:00"
    }
]
```
units:
```

     {
        "conductivity": "S/m"
        "temperature": "C",
        "pressure": "dbars"
        "salinity": "PSU"
        "timestamp":  null
    } 

```
source: "./data/58220.csv"

totalRecords: 25476


### GET /records/**(key)**/**(data_ref)**/salinity_calculated

Description: Tabulated data as per the command issued previously, except with practical salinity calculated (with the use of the GSW Service)

Response structure  are as previous, except with the addition to an extra key-value pair in the returned data and units dictionary

data:
```
[ 
     {
        "conductivity": 3.3808,
        "temperature": 4.5782,
        "pressure": 722.723,
        "salinity": 34.9799
        "timestamp":  "2017-01-08 00:i30:00",
        'pSalinity': 34.9797
    }, 
    {   
        "conductivity": 3.2625, 
        "temperature": 4.7225, 
        "pressure": 1715.235
        "salinity": 34.9799
        "timestamp":  "2017-01-08 00:45:00"
        'pSalinity': 34.9797
    }
]
```

units:
```
     {
        "conductivity": "S/m"
        "temperature": "C",
        "pressure": "dbars"
        "salinity": "PSU"
        "timestamp":  null,
        "pSalinity": null
    } 

```
## GSW Service
 Base url: http://localhost:9998/api/calculations

 Description: standalone internal service to carry out specialised calculations with the use of the GSW (Gibbs SeaWater  Oceanographic Toolbox of TEOS-10) software package



#### Parameter structure examples:
data:
```
[ 
     {
        "conductivity": 3.3808,
        "temperature": 4.5782,
        "pressure": 722.723,
        "salinity": 34.9799
        "timestamp":  "2017-01-08 00:30:00"
    }, 
    {   
        "conductivity": 3.2625, 
        "temperature": 4.7225, 
        "pressure": 1715.235
        "salinity": 34.9799
        "timestamp":  "2017-01-08 00:30:00"
    }
]
```
### GET /
Description:
    Present mainly as a check that the service is running. 

Returns:
    "hello world", status code 200 if the service is running.


### POST /practical_salinity
Body:
```
[ 
     {
        "conductivity": 3.3808,
        "temperature": 4.5782,
        "pressure": 722.723
    },
    {   
        "conductivity": 3.2625, 
        "temperature": 4.7225, 
        "pressure": 1715.235
    }
]```


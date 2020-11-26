
To bring up service:

Note: the environment variables file config.env must be at root folder and the ssl root cert (pem file) should be in folder /platform_in

dev config (flask dev server):

    docker-compose up
    send PUT requests to localhost:5000/observation with solar inverter data
    should return success or failure response

prod config (nginx+gunicorn)

    docker-compose -f docker-compose.prod.yml up

2,3,4 same as previous but port for prod is 1337


POST data example:
```json
{"topic": "topic",
 "observation": {
                    "phenomenontime_begin": 1606417048951,
                    "phenomenontime_end": None,
                    "resulttime": 1606417048951,
                    "result": "1.0",
                    "resultquality": None,
                    "validtime_begin": None,
                    "validtime_end": None,
                    "parameters": None,
                    "datastream_id": 123,
                    "featureofintrest_link": None,
                }}
```

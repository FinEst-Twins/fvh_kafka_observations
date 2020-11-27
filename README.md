
To bring up service:

Note: the environment variables file config.env must be at root folder and the ssl root cert (pem file) should be in folder /platform_in

dev config (flask dev server):

    docker-compose up
    send POST requests to localhost:5000/observation with POST body format in the example below
    should return success or failure response

prod config (nginx+gunicorn)

    docker-compose -f docker-compose.prod.yml up

2,3,4 same as previous but port for prod is 1337


POST data example:
```json
{"topic": "topic",
 "observation": {
                    "phenomenontime_begin": 1606417048951,
                    "phenomenontime_end": null,
                    "resulttime": 1606417048951,
                    "result": "1.0",
                    "resultquality": null,
                    "validtime_begin": null,
                    "validtime_end": null,
                    "parameters": null,
                    "datastream_id": 123,
                    "featureofintrest_link": null,
                }}
```

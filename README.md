# OKBADGER Client

A Python Module to issue badges on the [OKFN Badging
Service](http://badges.schoolofdata.org).

## Usage

```python
import okbadger

c = okbadger.Client(url, id, api_key)
c.issue(badge, recipient)
```

* ```url``` is the base url of the badging service,
* ```id``` is the API id
* ```api_key``` is the API key received from the serivce,
* ```badge``` is the badge-slug in the service
* ```recipient``` is the recipients email address

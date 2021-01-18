# Test using requests lib from python when running flask api locally

import requests
res = requests.post('http://localhost:5000/country_tests_done', json={"country":"ES"})
if res.ok:
    print(res.json())
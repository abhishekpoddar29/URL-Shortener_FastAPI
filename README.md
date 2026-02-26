# PROJECT : URL Shortener <br>

### AIM :<br><br>Accepts a long URL<br>Generate a short URL<br>Redirect users to the original URL when accessed<br>Stores data in temp file<br><br> ### Product requirement :<br>1.Long URL are hard to share - generate short URL<br>2.Clean link- easy to copy & paste<br>3.Redirect easily and reliably<br>4. User friendly<br><br> ### Functional requirement:<br>1.Create short URL :<br>>Accepts long URL<br>>generate random 6-char unique short URL<br>>Map long and short URL<br>>Return short URL<br>2.Redirect :<br>>When user access the short URL<br>>System scans for the URL in storage<br>>Then redirect to original URL<br>3.Validation :<br>>If URL not found - return "Error" message<br><br>

### 💻 Tech Stack:
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)


### Architecture :

            UI
            |
          env(Uvicorn) - process HTTP request
            |
          Application Layer
            a.Handle routing
            b.Business Logic
            c.Short URL generation
            |
          Storage Layer
            a.Load data
            b.Save data
            c.Mapping

    1. Two HTTP request : GET / POST
    2. One working UI
    3. One storage 

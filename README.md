PROJECT : URL Shortener

AIM : 
1. Accepts a long URL
2. Generate a short URL
3. Redirect users to the original URL when accessed
4. Stores data in temp file

Product requirement :
1.Long URL are hard to share - generate short URL
2.Clean link- easy to copy & paste
3.Redirect easily and reliably
4. User friendly

Functional requirement:
1.Create short URL : 
  a.Accepts long URL 
  b.generate random 6-char unique short URL
  c.Map long and short URL
  d.Return short URL
2.Redirect :
  a.When user access the short URL
  b.System scans for the URL in storage
  c.Then redirect to original URL
3.Validation :
  a.If URL not found - return "Error" message

Tech. Stack : Python + FastAPI + Textfile(storage)

Architecture :

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

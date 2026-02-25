PROJECT : URL Shortener <br>

AIM : <br>
1. Accepts a long URL <br>
2. Generate a short URL <br>
3. Redirect users to the original URL when accessed <br>
4. Stores data in temp file <br>

Product requirement : <br>
1.Long URL are hard to share - generate short URL <br>
2.Clean link- easy to copy & paste <br>
3.Redirect easily and reliably <br>
4. User friendly <br>

Functional requirement: <br>
1.Create short URL :  <br>
  a.Accepts long URL <br>
  b.generate random 6-char unique short URL<br>
  c.Map long and short URL<br>
  d.Return short URL<br>
2.Redirect :<br>
  a.When user access the short URL<br>
  b.System scans for the URL in storage<br>
  c.Then redirect to original URL<br>
3.Validation :<br>
  a.If URL not found - return "Error" message<br>

Tech. Stack : Python + FastAPI + Textfile(storage)<br>

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

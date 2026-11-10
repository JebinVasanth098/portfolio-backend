# Backend (Python): write your code here

This folder is yours. The React app in `../frontend` expects the API described
in `../frontend/README.md`. In development the frontend proxies `/api` to
`http://localhost:8000`, so run your server on port 8000.

## Deploy on Render

This repository includes a `render.yaml` Blueprint. In Render, create a new
Blueprint and select this repository. When prompted, set these environment
variables for the web service:

* `GEMINI\_API\_KEY`: your Gemini API key. Add it as a secret; do not commit it.
* `GEMINI\_MODEL`: the Gemini model ID to use.
* `ALLOWED\_ORIGINS`: optional JSON array of additional allowed origins, for

&#x20;    example `\["https://preview-portfolio.example"]`. Do not include a trailing

&#x20;    slash. The production frontend origin

&#x20;    `https://portfolio-frontend-g371.onrender.com` is always allowed.

* If unset, the API allows `https://portfolio-frontend-g371.onrender.com`.

The Blueprint installs `requirements.txt`, runs Uvicorn on Render's `$PORT`,
and uses `/api/health` for health checks. The API will be available at the
service's `https://<service-name>.onrender.com` URL.

## Endpoints to build

* `GET /api/health`
* `GET /api/projects`
* `GET /api/posts` and `GET /api/posts/{slug}`
* `POST /api/contact`
* `POST /api/ask` (the AI bar; calls Gemini)

## Suggested layout

```
backend/
  app/
    main.py            # creates the app, mounts routers, CORS
    routers/           # health.py, content.py, contact.py, ask.py
    services/
      gemini.py        # the only file that talks to Gemini
    content/           # projects, posts, experience as JSON/Markdown
  requirements.txt
  .env                 # GEMINI\_API\_KEY=...   (never commit; never send to the browser)
  .gitignore
```

Any Python web framework works. FastAPI is a natural fit because its
`{"detail": "..."}` error format is already understood by the frontend.

## Notes for the AI endpoint

* Keep the Gemini key in an environment variable on the server only.
* To make answers about the website, load your site content (projects, posts,
experience) and pass it to Gemini as system instructions, telling it to answer
only from that content and to say so when the answer is not there.
* Enforce a length limit on `message` and trim `history` on the server; do not
trust what the browser sends. Rate-limit this endpoint, since each call costs money.
* Treat user text as untrusted: visitors can try to get the model to ignore its
instructions, so give it no tools or secrets it should not expose.
* Check Google's current Gemini docs for the official Python SDK and model names.


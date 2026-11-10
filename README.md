# Backend (Python): write your code here

This folder is yours. The React app in `../frontend` expects the API described
in `../frontend/README.md`. In development the frontend proxies `/api` to
`http://localhost:8000`, so run your server on port 8000.

## Endpoints to build

- `GET /api/health`
- `GET /api/projects`
- `GET /api/posts` and `GET /api/posts/{slug}`
- `POST /api/contact`
- `POST /api/ask` (the AI bar; calls Gemini)

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
  .env                 # GEMINI_API_KEY=...   (never commit; never send to the browser)
  .gitignore
```

Any Python web framework works. FastAPI is a natural fit because its
`{"detail": "..."}` error format is already understood by the frontend.

## Notes for the AI endpoint

- Keep the Gemini key in an environment variable on the server only.
- To make answers about the website, load your site content (projects, posts,
  experience) and pass it to Gemini as system instructions, telling it to answer
  only from that content and to say so when the answer is not there.
- Enforce a length limit on `message` and trim `history` on the server; do not
  trust what the browser sends. Rate-limit this endpoint, since each call costs money.
- Treat user text as untrusted: visitors can try to get the model to ignore its
  instructions, so give it no tools or secrets it should not expose.
- Check Google's current Gemini docs for the official Python SDK and model names.

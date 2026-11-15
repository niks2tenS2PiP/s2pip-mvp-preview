# API scaffold

Run from the repository root:

```bash
pip install -r requirements-api.txt
uvicorn backend.api.main:app --reload
```

OpenAPI documentation is available at `/docs` in local development.

The endpoints in this increment are health/manifest endpoints only. They do not
provide login, registration, customer data access, or production security.

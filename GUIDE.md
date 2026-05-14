# AWS API Gateway Setup

## 1. Create REST API

Go to AWS API Gateway Console.

Choose:
- REST API
- Build

---

## 2. Configure REST API

| Field | Value |
|---|---|
| API Name | RephraseAPI |
| Endpoint Type | Regional |

Click:
- Create API

---

## 3. Create Resource

Navigate to:
- Resources
- Actions → Create Resource

Fill:

| Field | Value       |
|---|-------------|
| Resource Name | rephrase    |
| Resource Path | /rephrase |

Click:
- Create Resource

---

## 4. Create POST Method

Select:
- `/rephrase`

Then:
- Actions → Create Method
- Choose `POST`
- Click ✔

---

## 5. Connect Lambda Function

Configure:

| Field | Value           |
|---|-----------------|
| Integration Type | Lambda Function |
| Lambda Proxy Integration | Enabled         |
| Lambda Function | rephrase-api    |
| Enable CORS | enable          |

Save configuration and allow API Gateway permissions.

---

## 6. Enable CORS (this step is Optional if you already enabled CORS)

Select:
- POST

Then:
- Actions → Enable CORS

Keep defaults:

| Setting | Value |
|---|---|
| Access-Control-Allow-Origin | * |
| Access-Control-Allow-Headers | Content-Type |

Click:
- Enable CORS and replace existing headers

---

## 7. Deploy API

Navigate:
- Actions → Deploy API

Create stage:

```text
Dev
```

Click:
- Deploy

---

## 8. Copy Invoke URL

Example:

```text
https://abc123.execute-api.ap-southeast-2.amazonaws.com/prod
```

Final endpoint:

```text
https://abc123.execute-api.ap-southeast-2.amazonaws.com/prod/paraphrase
```

---

# Streamlit Configuration

Update API URL:

```python
API_URL = "https://abc123.execute-api.ap-southeast-2.amazonaws.com/prod/paraphrase"
```

---

# API Request Example

```json
{
  "language": "English",
  "tone": "Formal",
  "variants": 2,
  "text": "Artificial intelligence is evolving rapidly."
}
```

---

# API Response Example

```json
{
  "results": [
    "1. Artificial intelligence is advancing at a rapid pace.",
    "2. AI technology continues to evolve quickly."
  ]
}
```

---

# Lambda Response Format

```python
return {
    "statusCode": 200,
    "headers": {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*"
    },
    "body": json.dumps({
        "results": results
    })
}
```

Important:
REST API Gateway with Lambda Proxy Integration requires:
- `statusCode`
- `headers`
- `body` as stringified JSON

---
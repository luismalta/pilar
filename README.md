# Pilar

Pilar is a simple FastAPI application with two endpoints. 

## Endpoints

### Vowel Count

The `/vowel_count` endpoint receives a list of words and returns a dictionary with each word and the number of vowels it contains.

#### Request Payload

```json
{
    "words": [
        "hello",
        "world"
    ]
}
```

#### Response Payload

```json
{
    "hello": 2,
    "world": 4
}
```

### Sort Words

The `/sort` endpoint receives a list of words and a sorting order and returns a sorted list of words.


#### Request Payload

```json
{
    "words": [
        "world"
        "hello",
    ],
    "order": "asc",
}
```

#### Response Payload

```json
[
    "hello",
    "world"
]
```


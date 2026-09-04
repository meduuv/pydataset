# pydataset

Lightweight standard-library helpers for loading, validating, and summarizing small tabular datasets.

## Features

- CSV loading helpers
- Column selection
- Row filtering
- Basic dataset summaries
- No runtime dependencies

## Usage

```python
from pydataset import select_columns

rows = [{"name": "medu", "score": 10}]
print(select_columns(rows, ["name"]))
```

## Development

```bash
python -m unittest discover -s tests -v
```

## License

MIT

## Credits

https://guns.lol/meduu

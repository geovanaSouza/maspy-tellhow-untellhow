# maspy-tellhow-untellhow

Minimal reproduction repository for `tellHow`/`untellHow` plan-library behavior in MASPY.

## Requirements

- Python 3.12+
- [uv](https://docs.astral.sh/uv/)

## Run

```bash
make setup
make run
```

## Make targets

| Target | Description |
| --- | --- |
| `make setup` | Create `.venv` and install the project dependencies |
| `make run` | Run `examples/tellhow_untellhow.py` |
| `make help` | Show the available targets |

## Structure

```text
.
├── examples/
│   └── tellhow_untellhow.py
├── Makefile
├── pyproject.toml
└── README.md
```

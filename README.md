# maspy-tellhow-untellhow

Minimal reproduction repository for plan-library behavior in MASPY.

## Examples

### tellHow

Sends a plan from `Sender` to `Receiver` with `tellHow`. The receiver then reports its `_plans` and `_plan_index`.

The example also tries to execute the received plan on `Receiver`, but the execution does not work because the plan is present in `_plans` but is not indexed in `_plan_index`.

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
| `make run` | Run all examples |
| `make run-tellhow` | Run the `tellHow` example |
| `make help` | Show the available targets |

## Structure

```text
.
├── examples/
│   └── tellhow.py
├── Makefile
├── pyproject.toml
└── README.md
```

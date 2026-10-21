# maspy-tellhow-untellhow

Minimal reproduction repository for plan-library behavior in MASPY.

## Examples

### tellHow

Sends a plan from `Sender` to `Receiver` with `tellHow`. The receiver then reports its `_plans` and `_plan_index`.

The example also tries to execute the received plan on `Receiver`, but the execution does not work because the plan is present in `_plans` but is not indexed in `_plan_index`.

### untellHow

Sends an `untellHow` message for the `hello` plan and reports `_plans` and `_plan_index` before and after. The plan is added again instead of removed, `_plan_index` remains unchanged, and `Receiver` still executes the `hello` goal.

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
| `make run-untellhow` | Run the `untellHow` example |
| `make help` | Show the available targets |

## Structure

```text
.
├── examples/
│   ├── tellhow.py
│   └── untellhow.py
├── Makefile
├── pyproject.toml
└── README.md
```

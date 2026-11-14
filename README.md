# maspy-tellhow-untellhow

Minimal reproduction repository for plan-library behavior in MASPY.

## Examples

### tellHow

Sends a plan from `Sender` to `Receiver` with `tellHow`. The receiver then reports its `_plans` and `_plan_index`.

The example also executes the received plan on `Receiver`. With `maspy-ml>=2026.11.12` the plan is present in both `_plans` and `_plan_index`, so the `hello` goal runs (`Hello!`).

With `maspy-ml==2026.5.13` the plan was present in `_plans` but was not indexed in `_plan_index`, so the goal was never executed.

### untellHow

Sends an `untellHow` message for the `hello` plan and reports `_plans` and `_plan_index` before and after. With `maspy-ml>=2026.11.12` the plan is removed from both the plan library and the index, so the final `Goal("hello")` no longer has an applicable plan to run (the example keeps the receiver cycling and needs to be interrupted).

With `maspy-ml==2026.5.13` the plan was added again instead of removed, `_plan_index` remained unchanged, and `Receiver` still executed the `hello` goal.

## Requirements

- Python 3.12+
- [uv](https://docs.astral.sh/uv/)

## Run

```bash
make setup
make run
```

To run against another MASPY version (e.g. `2026.5.13` for the pre-fix behavior):

```bash
make install-maspy MASPY="maspy-ml==2026.5.13"
make run-tellhow
make run-untellhow
```

Use `make install-maspy MASPY="git+https://github.com/geovanaSouza/MASPY.git@<ref>"` to install another MASPY ref.

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

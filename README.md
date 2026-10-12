# scan-to-swarm
Serverless AWS honeypot built with Terraform, exploring scan-triggered deception and automated deployment of isolated decoy environments.

The planned system detects suspicious HTTP probes against its own endpoint,
returns synthetic decoy content, and queues the provisioning of isolated decoy
resources. Terraform provisioning is asynchronous and is not instantaneous;
HTTP responses will not wait for it to finish.

## Current status

Foundation only: an installable Python package, development checks, Terraform
provider configuration, and CI. There is no detection, HTTP endpoint, decoy
behavior, provisioning logic, or AWS resource definition yet.

## Prerequisites and setup

- Python 3.12 (uv can install it).
- [uv](https://docs.astral.sh/uv/getting-started/installation/) 0.13.0.
- [Terraform](https://developer.hashicorp.com/terraform/install) 1.16.5, as used in CI
  (configuration supports Terraform >=1.6 and <2.0).

From the repository root:

```sh
uv python install 3.12  # If Python 3.12 is not already available
uv sync --frozen
terraform -chdir=infra init -backend=false -input=false -lockfile=readonly
```

uv creates `.venv` and installs the package and development dependencies from
`uv.lock`. Terraform downloads the AWS provider selected by
`infra/.terraform.lock.hcl`. Keep both lockfiles in version control. Initial
setup requires internet access; these checks require no AWS credentials.

`infra/terraform.tfvars.example` shows the region setting, which defaults to
`us-east-1`. Optionally copy it to `infra/terraform.tfvars` for local settings;
local variable files are ignored. No infrastructure is deployed by this setup.

## Checks

```sh
uv lock --check
uv run --frozen ruff check .
uv run --frozen ruff format --check .
uv run --frozen pytest
terraform fmt -check -recursive infra
terraform -chdir=infra validate
```

Run Terraform initialization above before validation. To format files locally,
use `uv run --frozen ruff format .` and `terraform fmt -recursive infra`.
GitHub Actions runs the same checks on pushes and pull requests, with no
deployment workflow.

## Planned milestones

1. Detect suspicious HTTP probes against the honeypot endpoint.
2. Return synthetic decoy responses.
3. Queue asynchronous provisioning of isolated decoy resources, including
   lifecycle controls and cleanup.

Licensed under the [MIT license](LICENSE).

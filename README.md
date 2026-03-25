# Claude with Google Vertex AI

Course notebooks for [Claude with Google Vertex AI](https://anthropic.skilljar.com/claude-with-google-vertex/289150) on Anthropic Skilljar.

## Prerequisites

- Python 3.13
- A GCP project with the Vertex AI API enabled
- `gcloud` CLI installed and authenticated

## Setup

This project uses [uv](https://docs.astral.sh/uv/) for dependency management.

### Install uv

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# or via Homebrew
brew install uv
```

### Install dependencies

```bash
uv sync
```

### Configure environment

```bash
cp .env.example .env
```

Edit `.env` and set your values:

```
GCP_PROJECT_ID=your-project-id
GCP_REGION=your-region
CLAUDE_MODEL=claude-sonnet-4@20250514
```

### Authenticate with GCP

```bash
gcloud auth application-default login
```

## Running notebooks

```bash
uv run jupyter notebook
```

Or open the notebooks in VS Code — select the `.venv` Python kernel when prompted.

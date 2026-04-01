# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Course notebooks for "Claude with Google Vertex AI" (Anthropic Skilljar). Uses the Anthropic Python SDK with Vertex AI backend to interact with Claude models.

## Setup

- Python 3.13, managed via `uv`
- Install dependencies: `uv sync`
- Copy `.env.example` to `.env` and set `GCP_PROJECT_ID`, `GCP_REGION`, and `CLAUDE_MODEL`
- GCP auth must be configured (`gcloud auth application-default login`)

## Structure

- `notebooks/` — organized by course module (e.g., `01_accessing_claude_api/`, `02_prompt_evaluation/`)
- Each module subfolder contains numbered notebooks (e.g., `01_requests.ipynb`, `02_system_prompts.ipynb`)
- `notebooks/utils.py` — shared utilities (client setup, chat helpers), imported via `sys.path.insert(0, "..")`
- `notebooks/template.ipynb` — starter template for new notebooks
- All notebooks use `AnthropicVertex` client from `anthropic[vertex]` SDK, authenticated via environment variables loaded with `python-dotenv`

## Conventions

- Model is configured via `CLAUDE_MODEL` env var (default: `claude-sonnet-4@20250514`)
- Notebooks follow the pattern: load env, create `AnthropicVertex` client, make API calls
- Notebook numbering uses zero-padded two-digit prefixes, reset per module

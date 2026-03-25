# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Course notebooks for "Claude with Google Vertex AI" (Anthropic Skilljar). Uses the Anthropic Python SDK with Vertex AI backend to interact with Claude models.

## Setup

- Python 3.13, managed via `uv`
- Install dependencies: `uv sync`
- Copy `.env.example` to `.env` and set `GCP_PROJECT_ID` and `GCP_REGION`
- GCP auth must be configured (`gcloud auth application-default login`)

## Structure

- `notebooks/` — Jupyter notebooks numbered sequentially (e.g., `001_requests.ipynb`)
- All notebooks use `AnthropicVertex` client from `anthropic[vertex]` SDK, authenticated via environment variables loaded with `python-dotenv`

## Conventions

- Default model: `claude-sonnet-4@20250514`
- Notebooks follow the pattern: load env, create `AnthropicVertex` client, make API calls
- Notebook numbering uses zero-padded three-digit prefixes matching course module order

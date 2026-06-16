"""GRS backend package.

Load environment variables from ``api/.env`` as early as possible so that any
``api.*`` submodule (e.g. ``api.constants``) can read configuration from the
process environment without requiring the caller to export it manually. This
makes ``uvicorn api.app:app`` work directly. Existing environment variables are
never overridden, so deployments that inject env vars another way are unaffected.
"""

from pathlib import Path

from dotenv import load_dotenv

_ENV_FILE = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=_ENV_FILE, override=False)

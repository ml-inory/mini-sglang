FROM python:3.12-slim

# This image intentionally installs only the teaching scaffold and test tooling.
# GPU learners should build on a CUDA base image after reading docs/environment.md.
WORKDIR /app

COPY pyproject.toml README.md ./
COPY python ./python
COPY tests ./tests
COPY docs ./docs

RUN python -m pip install --no-cache-dir -e ".[dev]"

ENV PYTHONUNBUFFERED=1

CMD ["python", "-m", "pytest", "-x", "-q"]

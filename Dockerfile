
FROM python:3.12-slim-bookworm

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY pyproject.toml ./
COPY uv.lock ./

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-install-project

COPY main.py .

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen
# Create a non-root user to run the application
RUN useradd -m app && \
    chown -R app:app /app

USER app

ENTRYPOINT ["uv", "run", "main.py"]


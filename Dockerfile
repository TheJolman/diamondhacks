FROM debian:bookworm-slim
WORKDIR /app

# get deps
RUN apt-get update && apt-get install -y curl
RUN curl -fsSL https://pixi.sh/install.sh | bash -s -- -y
ENV PATH="/root/.pixi/bin:${PATH}"
COPY pixi.toml pixi.lock ./
RUN pixi install

COPY backend/ ./backend/
COPY frontend/ ./frontend/

# frontend
WORKDIR /app/frontend
RUN pixi run npm ci
RUN pixi run npm run build

# backend
WORKDIR /app
EXPOSE 8000
CMD ["pixi", "run", "python", "backend/main.py"]

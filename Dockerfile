# Build frontend
FROM node:22-slim AS frontend-build

WORKDIR /app/frontend
COPY frontend/ ./
RUN npm ci
RUN npm run build

# Built frontend
FROM debian:bookworm-slim
WORKDIR /app

RUN apt-get update && apt-get install -y curl
RUN curl -fsSL https://pixi.sh/install.sh | bash -s -- -y
ENV PATH="/root/.pixi/bin:${PATH}"

COPY pixi.toml pixi.lock ./
COPY backend ./backend/

COPY --from=frontend-build /app/frontend/dist ./frontend/dist

RUN pixi install

EXPOSE 8000

CMD ["pixi", "run", "python", "backend/main.py"]

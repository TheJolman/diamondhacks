# Build frontend
FROM node:20-slim AS frontend-build
WORKDIR /app/frontend
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ .
RUN npm run build

# Built frontend
FROM debian:bookwork-slim
WORKDIR /app

RUN apt-get update && apt-get install -y curl
RUN curl -fsSL https://pixi.sh/install.sh | bash -s -- -y
ENV PATH="/root/.pixi/bin:${PATH}"

COPY pixi.toml pixi.lock /app/
COPY backend /app/backend

COPY --from=frontend-build /app/frontend/dist /app/frontend/dist

RUN pixi install

EXPOSE 8000

COPY run-prod.sh /app/
RUN chmod +x /app/run-prod.sh
CMD ["./run-prod.sh"]

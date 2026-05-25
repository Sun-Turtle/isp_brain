---
status: active
priority: medium
tags:
  - resources
  - infrastructure
  - deployment
  - docker
source: AI-generated deployment reference
created: 2026-05-24
---

# Website Deployment Reference

**Source**: AI-generated deployment reference, May 2026.

## Overview

The Sun Internet website (`suninternet.co.uk`) is hosted via Docker on our own server, following the same pattern as other Dockerised apps. It sits behind the host-level Nginx reverse proxy with Let's Encrypt SSL (certbot).

## Architecture

```
Internet → Nginx (host, port 80/443, certbot SSL) → Docker container (127.0.0.1:8093 → :80)
```

| Layer | What | Where |
|-------|------|-------|
| DNS | `suninternet.co.uk` A record → server IP | freethought registar |
| Reverse proxy | Nginx with certbot, one vhost file per site | `/etc/nginx/sites-available/` → symlinked to `sites-enabled/` |
| Docker | Standalone `docker-compose.yml` per app | `/opt/sun-internet/` |
| Container | Nginx:alpine serving static HTML/CSS/JS | Port `127.0.0.1:8093` |

## Why Static Export

The site has no API routes, no middleware, no database, and no server-side logic. A static export (Next.js `output: "export"`) means:

- No Node.js runtime needed in production — just Nginx serving flat files
- Smaller Docker image (~5MB vs ~150MB for a full Node image)
- Faster startup, simpler health checks
- Fewer moving parts to maintain

## Key Files

### `next.config.ts`
```
output: "export"
```
Generates plain HTML/CSS/JS in `out/` instead of a Node.js server.

### `Dockerfile` — Multi-stage build
```dockerfile
FROM node:22-alpine AS builder
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM nginx:alpine
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /app/out /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

### `nginx.conf`
```nginx
server {
    listen 80;
    server_name _;

    root /usr/share/nginx/html;
    index index.html;

    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header Referrer-Policy "strict-origin-when-cross-origin" always;

    location / {
        try_files $uri $uri.html $uri/ =404;
    }

    location /_next/static {
        alias /usr/share/nginx/html/_next/static;
        expires 1y;
        add_header Cache-Control "public, immutable";
    }
}
```

### `docker-compose.yml`
```yaml
services:
  app:
    build: .
    ports:
      - "127.0.0.1:8093:80"
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "wget", "-qO-", "http://localhost:80/"]
      interval: 60s
      timeout: 5s
      start_period: 5s
      retries: 3
```

## Nginx Vhost (host-level reverse proxy)

```nginx
server {
    listen 80;
    server_name suninternet.co.uk www.suninternet.co.uk;
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    server_name suninternet.co.uk www.suninternet.co.uk;

    ssl_certificate /etc/letsencrypt/live/suninternet.co.uk/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/suninternet.co.uk/privkey.pem;
    include /etc/letsencrypt/options-ssl-nginx.conf;

    location / {
        proxy_pass http://127.0.0.1:8093;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

## Deployment Steps

1. `rsync` the project (excluding `node_modules`, `.next`, `out`, `.git`) to `/opt/sun-internet/` on the server
2. `docker compose build` on the server
3. `docker compose up -d`
4. Create Nginx vhost config, symlink, reload Nginx
5. `certbot certonly` → update vhost to HTTPS → reload Nginx

## DNS (FreeThought)

| Record | Type | Target | Status |
|--------|------|--------|--------|
| `@` | A | Server IP | Working |
| `www` | A/CNAME | Same IP or `suninternet.co.uk` | Needs adding for certbot dual-domain cert |

## Maintenance

- SSL renewal: automatic via certbot systemd timer
- Site updates: `rsync` to server, `docker compose up -d --build`
- Troubleshooting: `docker compose logs`, `docker compose ps`

## Security Notes

- `.gitignore` and `.dockerignore` exclude `node_modules`, `.next`, `out`, `.git`, `.env`
- Container binds only to `127.0.0.1` — not exposed directly to internet
- Server IPs, internal hostnames, deployment paths excluded from public repo

## See also

- [Website (Knowledge)](../knowledge/website.md)
- [Website Stack Decision](../decisions/website-stack.md)
- [Network Assets](infrastructure-network-assets.md)

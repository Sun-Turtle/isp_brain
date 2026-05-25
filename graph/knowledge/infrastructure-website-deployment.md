---
status: active
priority: high
tags:
  - knowledge
  - infrastructure
  - deployment
  - docker
  - nginx
created: 2026-05-24
---

# Website Deployment Architecture

The public website is deployed at `suninternet.co.uk` via Docker on our own server, behind an Nginx reverse proxy with Let's Encrypt SSL.

## Architecture

```
Internet → Nginx (host, SSL) → Docker container (Nginx:alpine, static files)
```

**Static export** — Next.js `output: "export"` generates flat HTML/CSS/JS in `out/`. The Docker container is a minimal Nginx:alpine image (~5MB) serving only static content. No Node.js runtime runs in production.

This follows the same pattern as our other Dockerised apps: one `docker-compose.yml` per project, bound to localhost on an incrementing port (8093), proxied through the host-level Nginx.

## Why static export over Node.js runtime

- No database, no API routes, no middleware, no server-side logic
- Smaller image (~5MB vs ~150MB for full Node)
- Faster startup, simpler health checks
- Fewer moving parts to maintain
- Matches the lean ops philosophy

## Key components

| Component | Role |
|---|---|
| `Dockerfile` | Multi-stage build — Node for build, Nginx:alpine for serve |
| `nginx.conf` | Serves static files, handles Next.js HTML routes, security headers |
| `docker-compose.yml` | Binds `127.0.0.1:8093:80`, healthcheck via wget |
| Host Nginx vhost | SSL termination, `suninternet.co.uk` + `www.suninternet.co.uk` |
| certbot | Let's Encrypt SSL, automatic renewal via systemd timer |
| FreeThought DNS | A record for `@`, pending `www` record |

## See also

- [Deployment Reference](../resources/infrastructure-website-deployment.md)
- [Website](website.md)
- [Network Topology](technical-network-topology.md)
- [Website Stack Decision](../decisions/website-stack.md)

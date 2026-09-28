# 🌿 GrowGreen - Soil Moisture Sensor (Docker + CI/CD)

![Build Status](https://github.com/YOUR_USERNAME/growgreen-cicd/actions/workflows/deploy.yml/badge.svg)

A containerized Python application with an automated CI/CD pipeline built using Docker and GitHub Actions.

## 🚀 Features
- **Containerized Environment:** Built using Python 3.9-slim base image for consistent cross-platform deployment.
- **Automated Testing:** Unit tests run automatically on every `git push` to `main`.
- **Continuous Integration:** Automated Docker image builds verified via GitHub Actions runners.

## 🛠️ How to Run Locally

1. Build the Docker Image:
   \`\`\`bash
   docker build -t growgreen-sensor .
   \`\`\`

2. Run the Container:
   \`\`\`bash
   docker run --rm growgreen-sensor
   \`\`\`

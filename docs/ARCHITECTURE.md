# Velaryn Technical & Repository Architecture

This document provides a clean overview of the Velaryn repository structure, architectural principles, and automation pipeline.

---

## 📁 Repository Directory Layout

```
velaryn-website/
├── index.html                  # Standalone 3D WebGL Web Application
├── README.md                   # Primary Documentation with Automated Metrics
├── .gitignore                  # Git Ignore Rules
├── docs/                       # Project Specifications & Architecture
│   ├── PRD.md                  # Product Requirements Document
│   ├── TRD.md                  # Technical Requirements Document
│   ├── IMPLEMENTATION_PLAN.md  # Engineering Roadmap & Tasks
│   ├── SHADER_PRESET.md        # WebGL Shader Preset Configurations
│   └── diagrams/               # Mermaid Architecture & User Flow Diagrams
│       ├── 01-website-architecture.mmd
│       ├── 02-homepage-user-flow.mmd
│       ├── 03-content-structure.mmd
│       ├── 04-deployment-flow.mmd
│       └── 05-phase-roadmap.mmd
├── public/                     # Static Assets & Brand Media
│   └── assets/
│       └── brand/
│         ├── velaryn-symbol.svg       # Vector Brand Emblem (512x512)
│         ├── velaryn-logo-concept.png # High-res Logo Concept Image
│         └── velaryn-field.svg        # Vector Background Field
└── scripts/                    # Automation Scripts
    └── update_readme.py        # Automated Metrics & README Generator
```

---

## ⚡ Core Technical Principles

1. **Zero Package Overhead**:
   - Single self-contained `index.html` application with zero NPM dependencies, zero build steps, and instant load performance.

2. **3D WebGL & Spatial Depth Engine**:
   - Powered by **Three.js**, rendering a 2,000+ node neural particle sphere, QuadraticBezier emergency signal arcs, and orbiting 3D latitude rings.
   - Interactive CSS 3D perspective tilt with cursor-following specular light reflections (`radial-gradient`) and hardware acceleration (`will-change: transform`).

3. **Self-Updating Automated Metrics**:
   - Running `python scripts/update_readme.py` dynamically measures code statistics (line count, file size, bento components, section counts) and syncs `README.md` automatically between auto-update markers.

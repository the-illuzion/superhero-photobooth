# superhero-photobooth

A Next.js React application for superhero photobooth, deployed on GitHub Pages.

## Getting Started

### Development

First, install dependencies:

```bash
npm install
```

Then, run the development server:

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

### Building

To create a production build:

```bash
npm run build
```

This will generate a static export in the `out` directory.

## Deployment

This project is automatically deployed to GitHub Pages when changes are pushed to the `main` branch.

The deployment is handled by a GitHub Actions workflow (`.github/workflows/deploy.yml`) that:
1. Builds the Next.js application
2. Exports it as static files
3. Deploys to GitHub Pages

### Manual Deployment

You can also trigger the deployment manually from the Actions tab in GitHub.

## Configuration

The app is configured for static export in `next.config.js`:
- `output: 'export'` - Enables static export
- `images.unoptimized: true` - Required for static export
- `basePath` - Set dynamically for GitHub Pages subpath
- `trailingSlash: true` - Ensures proper routing on GitHub Pages

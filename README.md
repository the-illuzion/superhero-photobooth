# superhero-photobooth

A Next.js React application for superhero photobooth, deployed on GitHub Pages.

## Project Structure

- `/frontend` - Next.js React application
- `/backend` - Python backend (if applicable)

## Getting Started

### Development

Navigate to the frontend folder and install dependencies:

```bash
cd frontend
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
cd frontend
npm run build
```

This will generate a static export in the `frontend/out` directory.

## Deployment

This project is automatically deployed to GitHub Pages when changes are pushed to the `main` branch.

The deployment is handled by a GitHub Actions workflow (`.github/workflows/deploy.yml`) that:
1. Builds the Next.js application from the `frontend` folder
2. Exports it as static files
3. Deploys to GitHub Pages

### Manual Deployment

You can also trigger the deployment manually from the Actions tab in GitHub.

## Configuration

The frontend app is configured for static export in `frontend/next.config.js`:
- `output: 'export'` - Enables static export
- `images.unoptimized: true` - Required for static export
- `basePath` - Set dynamically for GitHub Pages subpath
- `trailingSlash: true` - Ensures proper routing on GitHub Pages

# GitHub Pages Setup Instructions

This document explains how to enable GitHub Pages for this repository.

## Prerequisites

The repository already contains:
- A Next.js React application configured for static export
- A GitHub Actions workflow (`.github/workflows/deploy.yml`) that builds and deploys the app

## Enabling GitHub Pages

To enable GitHub Pages for this repository, follow these steps:

1. Go to your repository on GitHub
2. Click on **Settings** (top navigation)
3. In the left sidebar, click on **Pages** (under "Code and automation")
4. Under **Source**, select **GitHub Actions**
5. The workflow will automatically run on the next push to the `main` branch

## Deployment Workflow

The workflow will:
1. Trigger automatically on push to `main` branch
2. Can also be triggered manually from the Actions tab
3. Install dependencies using `npm ci`
4. Build the Next.js app with `npm run build`
5. Upload the static files from the `out` directory
6. Deploy to GitHub Pages

## Accessing Your Site

Once deployed, your site will be available at:
```
https://<username>.github.io/<repository-name>/
```

For this repository:
```
https://the-illuzion.github.io/superhero-photobooth/
```

## Configuration Details

- **Base Path**: Automatically set to `/<repository-name>` for GitHub Pages
- **Output**: Static files exported to `out` directory
- **Build Command**: `npm run build`
- **Node Version**: 20 (latest LTS)

## Troubleshooting

If the deployment fails:
1. Check the Actions tab for error logs
2. Ensure GitHub Pages is enabled in repository settings
3. Verify that the workflow has the necessary permissions
4. Check that the `main` branch is protected if needed

## Manual Deployment

You can trigger a manual deployment:
1. Go to the **Actions** tab
2. Select the "Deploy Next.js to GitHub Pages" workflow
3. Click **Run workflow**
4. Select the branch and click **Run workflow**

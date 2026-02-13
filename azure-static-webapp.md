# Azure Static Web Apps Deployment

Guide to deploy Typing War on Azure Static Web Apps.

## Prerequisites

- Azure account (free tier available)
- GitHub repository connected (already done: `sonixz/typing-game`)
- No build tools needed - pure static files

## Deployment Steps

### Method 1: Azure Portal (Recommended)

1. **Go to Azure Portal**
   - Navigate to: https://portal.azure.com
   - Click "Create a resource"
   - Search for "Static Web App"

2. **Create Static Web App**
   - Subscription: Select your subscription
   - Resource Group: Create new or select existing
   - Name: `typing-war` (or your preferred name)
   - Region: Choose closest to your users
   - Source: GitHub
   - GitHub account: Authorize Azure
   - Organization: `sonixz`
   - Repository: `typing-game`
   - Branch: `main`

3. **Build Configuration**
   - Build presets: Custom
   - App location: `/`
   - Api location: (leave empty)
   - Output location: (leave empty)

   *No build process needed - files are already static!*

4. **Review + Create**
   - Click "Create"
   - Azure will automatically create a GitHub Action workflow
   - Deployment starts immediately

5. **Access Your Game**
   - URL will be: `https://[auto-generated-name].azurestaticapps.net/typing-war.html`
   - Or set custom domain in portal settings

### Method 2: Azure CLI

```bash
# Install Azure CLI
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# Login
az login

# Create resource group (if needed)
az group create \
  --name typing-war-rg \
  --location eastus

# Create static web app
az staticwebapp create \
  --name typing-war \
  --resource-group typing-war-rg \
  --source https://github.com/sonixz/typing-game \
  --location eastus \
  --branch main \
  --app-location "/" \
  --login-with-github
```

### Method 3: GitHub Actions (Manual Setup)

Azure auto-creates this, but here's the workflow for reference:

```yaml
# .github/workflows/azure-static-web-apps.yml
name: Azure Static Web Apps CI/CD

on:
  push:
    branches:
      - main
  pull_request:
    types: [opened, synchronize, reopened, closed]
    branches:
      - main

jobs:
  build_and_deploy_job:
    runs-on: ubuntu-latest
    name: Build and Deploy Job
    steps:
      - uses: actions/checkout@v3
        with:
          submodules: true
      - name: Build And Deploy
        uses: Azure/static-web-apps-deploy@v1
        with:
          azure_static_web_apps_api_token: ${{ secrets.AZURE_STATIC_WEB_APPS_API_TOKEN }}
          repo_token: ${{ secrets.GITHUB_TOKEN }}
          action: "upload"
          app_location: "/"
          output_location: ""
```

## Configuration File (Optional)

Create `staticwebapp.config.json` for advanced settings:

```json
{
  "routes": [
    {
      "route": "/",
      "redirect": "/typing-war.html",
      "statusCode": 301
    }
  ],
  "navigationFallback": {
    "rewrite": "/typing-war.html"
  },
  "mimeTypes": {
    ".json": "application/json",
    ".html": "text/html"
  },
  "globalHeaders": {
    "cache-control": "public, max-age=3600"
  }
}
```

## Custom Domain Setup

1. In Azure Portal → Your Static Web App → Custom domains
2. Click "Add"
3. Choose:
   - **CNAME**: For subdomain (e.g., `game.yourdomain.com`)
   - **APEX**: For root domain (e.g., `yourdomain.com`)
4. Add DNS records at your domain provider
5. Wait for SSL certificate (automatic, 5-10 minutes)

## Pricing

- **Free Tier** includes:
  - 100 GB bandwidth per month
  - 2 custom domains
  - Automatic HTTPS
  - GitHub Actions CI/CD
  - Perfect for this project!

- **Standard Tier**: $9/month (if you need more bandwidth)

## Environment Variables (if needed later)

Not needed now, but for future features:

1. Portal → Configuration → Application settings
2. Add key-value pairs
3. Access in code via environment

## Monitoring

View deployment logs:
- Portal → Deployment History
- Or GitHub Actions tab in your repo

## Testing

After deployment:
1. Visit your Azure URL
2. Test game functionality
3. Check browser console for errors
4. Verify `words.json` loads correctly

## Rollback

If deployment fails:
- Portal → Deployment History
- Select previous successful deployment
- Click "Redeploy"

## URLs

After deployment, your game will be accessible at:
- **Auto URL**: `https://[name]-[hash].azurestaticapps.net/typing-war.html`
- **Custom domain**: Configure in portal settings

## Troubleshooting

**404 errors:**
- Check app location is `/`
- Verify files are in root of repo

**JSON not loading:**
- Ensure `words.json` is in same directory as HTML
- Check browser network tab

**Styles broken:**
- All styles are inline - should work fine
- Clear browser cache

---

**Pro Tip**: Azure Static Web Apps auto-deploys on every push to `main`. No manual deployment needed after initial setup!

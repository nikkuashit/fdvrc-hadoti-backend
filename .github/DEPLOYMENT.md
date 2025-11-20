# cPanel Deployment Guide

This repository includes GitHub Actions workflows for automated deployment to cPanel.

## Available Workflows

### 1. `cpanel-deploy.yml` (Basic FTP Deployment)
- Deploys files via FTP
- Requires manual post-deployment tasks
- **Best for**: Simple deployments where you handle migrations manually

### 2. `cpanel-deploy-with-ssh.yml` (Full Automated Deployment)
- Deploys files via FTP
- Runs migrations and collects static files via SSH
- Restarts the application automatically
- **Best for**: Complete automation

## Setup Instructions

### Step 1: Configure GitHub Secrets

Go to your repository → Settings → Secrets and variables → Actions → New repository secret

Add the following secrets:

#### For Basic FTP Deployment (`cpanel-deploy.yml`):

| Secret Name | Description | Example |
|------------|-------------|---------|
| `FTP_SERVER` | cPanel FTP server address | `ftp.yourdomain.com` or `your-server-ip` |
| `FTP_PROD_USERNAME` | cPanel FTP username | `rmoktvux3m8e` |
| `FTP_PROD_PASSWORD` | cPanel FTP password | `your_password` |

#### For SSH Deployment (`cpanel-deploy-with-ssh.yml`):

Add all the above, PLUS:

| Secret Name | Description | Example |
|------------|-------------|---------|
| `SSH_HOST` | cPanel SSH server address | `yourdomain.com` or `server-ip` |
| `SSH_KEY` | Private SSH key content | Run: `cat ~/.ssh/github_actions` |

**Note:** Username for SSH is the same as `FTP_PROD_USERNAME`

### Step 2: Enable SSH Access in cPanel

1. Log into your cPanel account
2. Go to **Security** → **SSH Access**
3. Click **Manage SSH Keys**
4. Generate a new key pair or import your existing public key
5. Authorize the key

### Step 3: Get Your FTP Server Address

**Option A: From cPanel**
1. Log into cPanel
2. Go to **Files** → **FTP Accounts**
3. Look for "FTP Server" information

**Option B: Common formats**
- `ftp.yourdomain.com`
- Your server's IP address
- `yourdomain.com` (some hosts)

### Step 4: Choose and Enable a Workflow

**Option A: Use Basic FTP Deployment** (Recommended for beginners)
- The workflow in `cpanel-deploy.yml` is ready to use
- Triggers automatically on push to `main` or `singhdevfpc` branches
- You'll need to manually run migrations and collect static files via cPanel Terminal

**Option B: Use Full SSH Deployment** (Recommended for automation)
- The workflow in `cpanel-deploy-with-ssh.yml` handles everything
- Requires SSH access to be enabled
- Fully automated - no manual steps needed

### Step 5: Test the Deployment

1. Make a small change to your code
2. Commit and push to `main` or `singhdevfpc` branch:
   ```bash
   git add .
   git commit -m "Test deployment"
   git push origin main
   ```
3. Go to GitHub → Actions tab → Watch the workflow run

**Manual Trigger:**
You can also trigger deployment manually:
1. Go to GitHub → Actions
2. Select the workflow
3. Click "Run workflow"

## Post-Deployment Tasks (if using basic FTP workflow)

After deployment, connect to cPanel Terminal or SSH and run:

```bash
# Navigate to your project directory
cd /home/rmoktvux3m8e/public_html/singdevfpc.in/singdevfpc_backend/

# Activate virtual environment (if you have one)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Restart application (if using Passenger)
mkdir -p tmp
touch tmp/restart.txt
```

## Excluded Files

The following files/directories are NOT deployed (excluded in workflows):
- `.git` and git-related files
- `node_modules/`
- Virtual environments (`venv/`, `.venv/`)
- Python cache files (`__pycache__/`, `*.pyc`, `*.pyo`)
- Local database (`db.sqlite3`)
- System files (`.DS_Store`, `Thumbs.db`)
- `.claude/` directory
- `test_deployment.txt`

## Troubleshooting

### FTP Connection Issues
- Verify FTP server address is correct
- Check if your server requires passive mode
- Ensure FTP account has write permissions to the target directory
- Check if your IP is whitelisted (some hosts require this)

### SSH Connection Issues
- Verify SSH is enabled in cPanel
- Check SSH port (usually 22, but some hosts use custom ports)
- Ensure SSH key is authorized or password is correct
- Some shared hosting providers restrict SSH access

### Permission Errors
- FTP user must have write access to `/public_html/singdevfpc.in/singdevfpc_backend/`
- Check directory permissions in cPanel File Manager

### Deployment Succeeds but Site Not Updated
- Clear browser cache
- Check if Passenger needs restart: `touch tmp/restart.txt`
- Verify the correct `server-dir` path in workflow file

## Customization

### Change Deployment Branch
Edit the workflow file and modify the `branches` section:

```yaml
on:
  push:
    branches:
      - main          # Add or remove branches here
      - production
      - staging
```

### Change Deployment Directory
Edit the `server-dir` value in the workflow:

```yaml
server-dir: /public_html/your-custom-path/
```

### Add/Remove Excluded Files
Edit the `exclude` section in the workflow file.

## Security Best Practices

1. **Never commit secrets** to your repository
2. Use **SSH keys** instead of passwords when possible
3. **Restrict deployment branches** to production-ready branches only
4. Enable **branch protection rules** for main/production branches
5. Use **environment-specific workflows** (staging, production)
6. Regularly **rotate credentials**

## Current Deployment Path

Based on your `.cpanel.yml`:
```
/home/rmoktvux3m8e/public_html/singdevfpc.in/singdevfpc_backend/
```

If this path changes, update both:
1. `.cpanel.yml` (for cPanel Git integration)
2. GitHub workflow files (`.github/workflows/*.yml`)

## Need Help?

- **GitHub Actions Docs**: https://docs.github.com/en/actions
- **FTP Deploy Action**: https://github.com/SamKirkland/FTP-Deploy-Action
- **SSH Action**: https://github.com/appleboy/ssh-action
- **cPanel Documentation**: https://docs.cpanel.net/

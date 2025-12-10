# Setting Up fyrmtech.com with GitHub Pages

## Step-by-Step Guide

### 1. GitHub Repository Setup ✅

The `CNAME` file has been created in your repository with `fyrmtech.com`.

**Now commit and push it:**
```bash
git add CNAME
git commit -m "Add custom domain CNAME file"
git push origin main
```

### 2. Enable GitHub Pages

1. Go to your repository: https://github.com/ahmed2galal-gif/Fyrm
2. Click **Settings** → **Pages** (left sidebar)
3. Under **Source**, select:
   - Branch: `main`
   - Folder: `/ (root)`
4. Click **Save**
5. In the **Custom domain** field, enter: `fyrmtech.com`
6. Click **Save**
7. ✅ Check **Enforce HTTPS** (after DNS propagates)

### 3. Configure DNS in GoDaddy

Log in to your GoDaddy account and configure these DNS records:

#### Option A: Apex Domain (fyrmtech.com) with www subdomain

**Delete existing A records** for `@`, then add these **4 A records**:

| Type | Name | Value | TTL |
|------|------|-------|-----|
| A | @ | 185.199.108.153 | 600 |
| A | @ | 185.199.109.153 | 600 |
| A | @ | 185.199.110.153 | 600 |
| A | @ | 185.199.111.153 | 600 |

**Add CNAME record for www:**

| Type | Name | Value | TTL |
|------|------|-------|-----|
| CNAME | www | ahmed2galal-gif.github.io | 1 Hour |

#### Option B: Only www subdomain (www.fyrmtech.com)

If you want to use `www.fyrmtech.com` instead:

1. Change CNAME file content to: `www.fyrmtech.com`
2. In GoDaddy, add:

| Type | Name | Value | TTL |
|------|------|-------|-----|
| CNAME | www | ahmed2galal-gif.github.io | 1 Hour |
| CNAME | @ | ahmed2galal-gif.github.io | 1 Hour |

### 4. GoDaddy DNS Configuration Steps

1. **Login** to GoDaddy: https://dcc.godaddy.com/
2. Navigate to **My Products** → **Domains**
3. Click on **fyrmtech.com** → **DNS** (or **Manage DNS**)
4. **Add/Edit DNS Records** as shown above
5. Click **Save** or **Add Record** for each entry

**Important Notes:**
- Remove any existing A records that point to GoDaddy parking pages
- Remove any conflicting CNAME records
- Keep MX records if you have email setup
- TTL can be 600 seconds (10 min) or 3600 seconds (1 hour)

### 5. Verification & Testing

**DNS Propagation** takes 10 minutes to 48 hours (usually ~1 hour)

#### Check DNS Propagation:
```bash
# Check A records
nslookup fyrmtech.com

# Check CNAME
nslookup www.fyrmtech.com

# Or use online tools:
# https://www.whatsmydns.net/
```

#### Expected Results:
```
fyrmtech.com → 185.199.108.153 (or 109/110/111)
www.fyrmtech.com → ahmed2galal-gif.github.io
```

### 6. Enable HTTPS in GitHub Pages

Once DNS propagates (you can access your site):

1. Go back to **GitHub Settings → Pages**
2. ✅ Check **Enforce HTTPS**
3. Wait for SSL certificate to provision (~15 minutes)

### 7. Final Verification Checklist

- [ ] CNAME file committed to repository
- [ ] GitHub Pages enabled on `main` branch
- [ ] Custom domain `fyrmtech.com` set in GitHub Pages
- [ ] A records added in GoDaddy (4 records)
- [ ] CNAME record for www added in GoDaddy
- [ ] DNS propagation complete (test with nslookup)
- [ ] Site accessible at http://fyrmtech.com
- [ ] Site accessible at http://www.fyrmtech.com
- [ ] HTTPS enforced and working
- [ ] Site accessible at https://fyrmtech.com
- [ ] Site accessible at https://www.fyrmtech.com

## Troubleshooting

### Issue: "DNS check unsuccessful"
- Wait longer (DNS can take up to 48 hours)
- Verify A records are correct
- Clear your DNS cache: `ipconfig /flushdns` (Windows)

### Issue: "Certificate provisioning failed"
- Uncheck "Enforce HTTPS"
- Remove custom domain
- Wait 5 minutes
- Re-add custom domain
- Re-enable "Enforce HTTPS"

### Issue: "Site not loading"
- Check if GitHub Pages deployment succeeded
- Verify index.html is in root directory
- Check repository is public (or you have GitHub Pro for private repos)

### Issue: "Mixed content warnings"
- Ensure all resources (images, CDNs) use HTTPS
- Check browser console for errors

## Quick Commands

```bash
# Commit CNAME file
git add CNAME
git commit -m "Add custom domain"
git push origin main

# Check DNS from command line
nslookup fyrmtech.com
nslookup www.fyrmtech.com

# Clear Windows DNS cache
ipconfig /flushdns

# Check site status
curl -I https://fyrmtech.com
```

## Expected Timeline

- **Immediate**: CNAME file pushed to GitHub
- **1-2 minutes**: GitHub Pages build completes
- **10-60 minutes**: DNS propagation (most cases)
- **15 minutes**: SSL certificate provisioning
- **Total**: ~1-2 hours for full setup

## Support Resources

- **GitHub Pages Docs**: https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site
- **GoDaddy DNS Help**: https://www.godaddy.com/help/manage-dns-680
- **DNS Checker**: https://www.whatsmydns.net/
- **SSL Checker**: https://www.sslshopper.com/ssl-checker.html

---

**Your site will be live at**: https://fyrmtech.com 🚀

After DNS propagates, both URLs will work:
- https://fyrmtech.com
- https://www.fyrmtech.com

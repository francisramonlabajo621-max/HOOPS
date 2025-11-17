# PythonAnywhere Update Guide

## Quick Update Commands

To update your PythonAnywhere app with the latest changes from GitHub:

### Step 1: Open a Bash Console
Go to the **Consoles** tab in PythonAnywhere and open a new Bash console.

### Step 2: Pull Latest Changes
```bash
cd ~/HOOPS
git pull origin main
```

### Step 3: Reload Your Web App
1. Go to the **Web** tab
2. Click the green **Reload** button

That's it! Your app will now have the latest changes.

---

## Full Update Process (if needed)

If you encounter any issues, you can do a fresh pull:

```bash
cd ~/HOOPS
git fetch origin
git reset --hard origin/main
```

Then reload your web app from the **Web** tab.

---

## Verify the Update

After reloading, check your app at: `https://mj1404.pythonanywhere.com`

You should see:
- ✅ Consistent card design on Home and Explore pages
- ✅ Softer, less bright light mode colors
- ✅ Fully clickable cards (entire card is clickable, not just the button)

---

## Troubleshooting

**If you get merge conflicts:**
```bash
cd ~/HOOPS
git stash
git pull origin main
git stash pop
```

**If files are locked:**
- Make sure your web app is not running
- Try reloading after pulling

**If changes don't appear:**
- Clear your browser cache (Ctrl+Shift+R or Cmd+Shift+R)
- Check the error log in the Web tab
- Verify the files were updated: `ls -la ~/HOOPS/static/style.css`


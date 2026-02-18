# Statistical Transport Talk Series Website

This is the website for the Statistical Transport Talk Series at Carnegie Mellon University's Department of Statistics and Data Science.

## Local Development

### Prerequisites
- Ruby (version 2.7 or higher)
- Bundler

### Setup

1. Install dependencies:
```bash
bundle install
```

2. Run the local server:
```bash
bundle exec jekyll serve
```

3. Visit `http://localhost:4000` in your browser

## Deployment Options

### Option 1: GitHub Pages (Recommended)

1. Create a new repository on GitHub
2. Push this code to the repository:
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
git push -u origin main
```

3. Go to repository Settings → Pages
4. Under "Source", select "Deploy from a branch"
5. Select the `main` branch and `/ (root)` folder
6. Click Save

Your site will be available at `https://YOUR-USERNAME.github.io/YOUR-REPO-NAME/`

### Option 2: CMU AFS Web Space

1. Build the site:
```bash
bundle exec jekyll build
```

2. Copy the contents of the `_site` folder to your CMU web space:
```bash
cp -r _site/* /afs/andrew.cmu.edu/usr/YOUR-USERNAME/www/
```

Your site will be available at `https://www.andrew.cmu.edu/user/YOUR-USERNAME/`

### Option 3: Other Hosting

The built site is in the `_site` directory after running `jekyll build`. You can upload these files to any web server.

## Updating Content

### Adding a New Past Talk

Edit `index.md` and add a new section under "Past Talks" following this format:

```markdown
### MM/DD/YYYY - Speaker Name
**Affiliation**
**Title:** Talk Title

Abstract text here...
```

### Adding a New Upcoming Talk

Edit the table under "Upcoming Talks" in `index.md`:

```markdown
| MM/DD/YYYY | Speaker Name | Affiliation | Talk Title |
```

### Updating Members

Edit the "Members" section in `index.md` to add or remove faculty and students.

## Customization

- To change the site theme, modify the `theme` setting in `_config.yml`
- To add custom CSS, create a file `assets/css/style.css`
- For more Jekyll themes, visit: https://jekyllrb.com/docs/themes/

## Support

For questions about the website, contact Gonzalo Mena at gmena@andrew.cmu.edu

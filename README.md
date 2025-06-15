# research-goats

Research Goats helps students compare the research strengths of university staff (from professors to PhD candidates) and find the right supervisor for their thesis and research field.

## Beta Verion Features
- Scrapes staff data (name, role, profile link, image link) from LIACS staff page and save to a SQLite database
- Click a staff card to view their image and a link to their profile

## Setup
1. **Clone the repository**
2. **Install dependencies:**
   ```sh
   pip install flask flask_sqlalchemy requests beautifulsoup4 selenium
   ```
   Also install [ChromeDriver](https://sites.google.com/chromium.org/driver/) for Selenium scraping.

3. **Scrape and update the database:**
   ```sh
   python scrape_staff.py
   ```

4. **Run the Flask app:**
   ```sh
   python app.py
   ```
   Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

## Project Structure
- `app.py` - Main Flask app
- `models.py` - SQLAlchemy models
- `scrape_staff.py` - Web scraper and database updater
- `templates/index.html` - Main landing page
- `static/styles.css` - Custom styles
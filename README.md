idThirdeye Technology Solutions — Corporate Website

A fully responsive, single-file corporate website built for **idThirdeye Technology Solutions**, a full-service technology company headquartered in Madurai, Tamil Nadu, India.

 📌 Project Overview

This project is a professional corporate website that presents idThirdeye's services, portfolio, team process, and contact information. It is built as a single HTML file with embedded CSS and JavaScript, and connects to a Flask backend for contact form submissions.


 🖥️ Live Sections

| Section | Description |
|---|---|
| **Hero** | Animated banner with tagline and CTA buttons |
| **Stats** | Key company metrics (120+ projects, 60+ clients, etc.) |
| **About** | Mission, approach, and core values |
| **Services** | 6 service offerings with icon cards |
| **Process** | 6-step delivery methodology (Discovery → Support) |
| **Portfolio** | 6 selected case studies across industries |
| **Testimonials** | Client quotes and attributions |
| **Contact** | Contact form + company info |
| **Footer** | Navigation links and copyright |

🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| Fonts | Google Fonts — Inter, Playfair Display |
| Backend (API) | Flask (Python) — runs on `http://127.0.0.1:5000` |
| Form Submission | `fetch()` POST to `/contact` endpoint |

 📁 Project Structure

```
idthirdeye-website/
│
├── index.html        # Main single-file website (HTML + CSS + JS)
├── app.py            # Flask backend for contact form
└── README.md         # Project documentation
```
⚙️ Setup & Running Locally

 1. Clone the Repository

```bash
git clone https://github.com/jothi121005/idthirdeye-website.git
cd idthirdeye-website
```

 2. Start the Flask Backend

Make sure Python and Flask are installed:

```bash
pip install flask flask-cors
python app.py
```

The backend will run at `http://127.0.0.1:5000`.

 3. Open the Website

Simply open `index.html` in your browser:

```bash
# Option 1: Double-click index.html
# Option 2: Use VS Code Live Server extension
```

 ⚠️ The contact form requires the Flask backend to be running to submit messages.
 🎨 Design System

| Token | Value | Usage |
|---|---|---|
| `--navy` | `#0D1F3C` | Primary background, text |
| `--teal` | `#00788A` | Accent, buttons, borders |
| `--teal-lt` | `#00A8BF` | Hover states, highlights |
| `--gold` | `#C8922A` | Decorative accents |
| `--off-wht` | `#F5F7FA` | Section alternates |

📋 Features

- ✅ Sticky navigation bar with smooth scroll
- ✅ Animated hero section with pulsing eye watermark
- ✅ Responsive layout (mobile + desktop)
- ✅ Hover effects on service, portfolio, and process cards
- ✅ Contact form with client-side validation
- ✅ `prefers-reduced-motion` accessibility support
- ✅ Semantic HTML structure

 📬 Contact Form — How It Works

The contact form collects:
- Name, Work Email, Company Name
- Service of interest (dropdown)
- Project description (textarea)

On submit, it sends a `POST` request to the Flask `/contact` endpoint:

```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "company": "Acme Corp",
  "service": "Data Analytics & BI",
  "message": "We need a dashboard solution..."
}
```

 🚀 Deployment

This site can be deployed using:

- **Frontend:** GitHub Pages, Netlify, Vercel (static HTML)
- **Backend:** Render.com, Railway, or any Python-compatible host

> Update the `fetch` URL in `index.html` from `http://127.0.0.1:5000/contact` to your deployed backend URL before going live.


---

## 📄 License

This project was developed as part of an internship at idThirdeye Technology Solutions.
© 2025 idThirdeye Technology Solutions. All rights reserved.

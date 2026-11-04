from flask import Flask, render_template_string

app = Flask(__name__)

# 100% Working Stable Image Database
PRODUCTS = [
    {"id": 1, "name": "Essential Heavyweight Hoodie - Jet Black", "price": 2999, "old": 5999, "cat": "hoodies", "rating": 4.9, "reviews": 342, "img": "https://images.unsplash.com/photo-1556821840-3a63f95609a7?w=800", "tag": "BESTSELLER 🔥"},
    {"id": 2, "name": "Y2K Baggy Cargo Denim - Ice Blue", "price": 3799, "old": 6999, "cat": "cargos", "rating": 4.8, "reviews": 215, "img": "https://images.unsplash.com/photo-1542272604-787c3835535d?w=800", "tag": "TRENDING 🚀"},
    {"id": 3, "name": "Tactical 6-Pocket Utility Cargo - Khaki", "price": 3499, "old": 6000, "cat": "cargos", "rating": 4.7, "reviews": 189, "img": "https://images.unsplash.com/photo-1517841905240-472988babdf9?w=800", "tag": "HOT DEAL 🔥"},
    {"id": 4, "name": "Retro Leather Varsity Jacket - Off White", "price": 4999, "old": 9999, "cat": "jackets", "rating": 4.9, "reviews": 412, "img": "https://images.unsplash.com/photo-1591047139829-d91aecb6caea?w=800", "tag": "LIMITED ⚡"},
    {"id": 5, "name": "Minimalist Oversized Graphic Tee - Black", "price": 1499, "old": 3000, "cat": "tshirts", "rating": 4.6, "reviews": 520, "img": "https://images.unsplash.com/photo-1583743814966-8936f5b7be1a?w=800", "tag": "SALE 50%"},
    {"id": 6, "name": "Urban Signature Street Cap - Black", "price": 899, "old": 1800, "cat": "accessories", "rating": 4.5, "reviews": 95, "img": "https://images.unsplash.com/photo-1521369909029-2afed882baee?w=800", "tag": "FAST SELL"},
    {"id": 7, "name": "Cyberpunk Techwear Windbreaker Jacket", "price": 5499, "old": 10999, "cat": "jackets", "rating": 4.8, "reviews": 140, "img": "https://images.unsplash.com/photo-1548883354-7622d03aca27?w=800", "tag": "NEW ARRIVAL"},
    {"id": 8, "name": "Distressed Grunge Oversized Hoodie", "price": 3199, "old": 6400, "cat": "hoodies", "rating": 4.7, "reviews": 230, "img": "https://images.unsplash.com/photo-1509631179647-0177331693ae?w=800", "tag": "HOT 🔥"},
    {"id": 9, "name": "Classic Ribbed Beanie - Charcoal Grey", "price": 699, "old": 1400, "cat": "accessories", "rating": 4.8, "reviews": 110, "img": "https://images.unsplash.com/photo-1576871337632-b9aef4c17ab9?w=800", "tag": "WINTER ❄️"},
    {"id": 10, "name": "Drop-Shoulder Heavyweight Tee - Olive", "price": 1599, "old": 3200, "cat": "tshirts", "rating": 4.9, "reviews": 310, "img": "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=800", "tag": "TOP RATED"}
]

CUSTOMER_REVIEWS = [
    {"name": "Ali Raza", "city": "Lahore", "rating": 5, "comment": "Amazing quality! Hoodie ki fabric bohot thick aur warm hai. Size bilkul perfect aya.", "date": "Yesterday"},
    {"name": "Zainab Malik", "city": "Karachi", "rating": 5, "comment": "Sales Mela discount par order kiya tha, delivery sirf 2 din me mil gayi via TCS. 10/10!", "date": "3 days ago"},
    {"name": "Bilal Ahmed", "city": "Islamabad", "rating": 5, "comment": "Stitchings aur color combination bilkul brand level ki hain. Highly recommended!", "date": "1 week ago"}
]

TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title>URBAN® | Grand Sales Mela 2026 - Pakistan's #1 Streetwear Store</title>
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<style>
:root {
  --black: #0b0b0b;
  --yellow: #FFD700;
  --red: #ff3b30;
  --green: #22c55e;
  --gray: #f8f9fa;
  --border: #e2e8f0;
}
* { margin:0; padding:0; box-sizing:border-box; font-family:'Inter', sans-serif; }
body { background: #fff; color: var(--black); width: 100%; overflow-x: hidden; }

/* Moving & Shining Top Announcement Strip */
.top-strip {
  background: linear-gradient(90deg, #ff3b30, #ff9500, #ffe600, #ff9500, #ff3b30);
  background-size: 300% auto;
  color: #fff;
  text-align: center;
  padding: 10px 15px;
  font-size: 12px;
  font-weight: 900;
  letter-spacing: 1.2px;
  position: sticky;
  top: 0;
  z-index: 10000;
  animation: shineTicker 4s linear infinite;
  width: 100%;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
@keyframes shineTicker {
  0% { background-position: 0% center; text-shadow: 0 0 2px #fff; }
  50% { text-shadow: 0 0 10px #fff, 0 0 20px #ff0; }
  100% { background-position: 300% center; text-shadow: 0 0 2px #fff; }
}

/* Navbar */
.navbar {
  background: rgba(11, 11, 11, 0.98);
  backdrop-filter: blur(12px);
  color: #fff;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 14px 20px;
  position: sticky;
  top: 35px;
  z-index: 999;
  border-bottom: 1px solid rgba(255,255,255,0.1);
  width: 100%;
}
.logo { font-family: 'Bebas Neue'; font-size: 36px; letter-spacing: 5px; color: #fff; text-decoration: none; }
.logo span { color: var(--yellow); }
.nav-links { display: flex; gap: 18px; align-items: center; }
.nav-links a { color: #fff; text-decoration: none; font-size: 13px; font-weight: 700; transition: 0.2s; }
.nav-links a:hover { color: var(--yellow); }
.cart-badge-btn {
  background: var(--yellow);
  color: #000;
  padding: 8px 16px;
  border-radius: 50px;
  font-weight: 900;
  font-size: 13px;
  display: flex;
  gap: 6px;
  align-items: center;
  cursor: pointer;
  box-shadow: 0 4px 15px rgba(255,215,0,0.4);
}

/* Clothes Store Banner Hero Section */
.hero {
  position: relative;
  width: 100%;
  min-height: 540px;
  background: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.85)), url('https://images.unsplash.com/photo-1445205170230-053b83016050?w=1400');
  background-size: cover;
  background-position: center;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  padding: 40px 20px;
  color: #fff;
}
.mela-badge {
  background: var(--red);
  color: #fff;
  display: inline-block;
  padding: 6px 14px;
  border-radius: 20px;
  font-size: 11px;
  font-weight: 900;
  letter-spacing: 2px;
  margin-bottom: 14px;
  width: fit-content;
  box-shadow: 0 0 20px rgba(255,59,48,0.6);
  animation: badgeGlow 1.5s infinite alternate;
}
@keyframes badgeGlow {
  0% { transform: scale(1); box-shadow: 0 0 10px rgba(255,59,48,0.5); }
  100% { transform: scale(1.08); box-shadow: 0 0 25px rgba(255,215,0,0.9); background: #ff2d55; }
}

.hero h1 { font-family: 'Bebas Neue'; font-size: 64px; line-height: 0.95; letter-spacing: 2px; }
.hero h1 span { color: var(--yellow); }
.hero p { font-size: 14px; margin: 12px 0 24px; opacity: 0.95; max-width: 500px; text-shadow: 0 2px 4px rgba(0,0,0,0.5); }
.btn-mela {
  background: var(--yellow);
  color: #000;
  border: none;
  padding: 16px 30px;
  border-radius: 100px;
  font-weight: 900;
  font-size: 15px;
  cursor: pointer;
  box-shadow: 0 6px 25px rgba(255,215,0,0.4);
}

/* Ticker Bar */
.ticker-bar {
  background: #111;
  color: #fff;
  padding: 16px 20px;
  display: flex;
  justify-content: space-around;
  align-items: center;
  text-align: center;
  border-bottom: 2px solid var(--yellow);
  width: 100%;
}
.ticker-item div:first-child { font-size: 10px; color: #aaa; text-transform: uppercase; font-weight: 700; }
.ticker-item div:last-child { font-size: 16px; font-weight: 900; color: var(--yellow); font-family: monospace; }

/* Filter Tabs */
.filter-container {
  display: flex;
  gap: 10px;
  padding: 25px 20px 10px;
  overflow-x: auto;
  width: 100%;
  scrollbar-width: none;
}
.filter-btn {
  background: var(--gray);
  border: 1px solid var(--border);
  padding: 10px 20px;
  border-radius: 50px;
  font-size: 13px;
  font-weight: 800;
  cursor: pointer;
  white-space: nowrap;
}
.filter-btn.active, .filter-btn:hover { background: #000; color: #fff; border-color: #000; }

/* Section Header */
.sec-head { padding: 30px 20px 15px; display: flex; justify-content: space-between; align-items: flex-end; width: 100%; }
.sec-head h2 { font-family: 'Bebas Neue'; font-size: 34px; letter-spacing: 1px; }

/* Product Grid */
.prod-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(160px, 1fr)); gap: 14px; padding: 0 20px; width: 100%; }
@media(min-width: 768px) { .prod-grid { grid-template-columns: repeat(auto-fill, minmax(230px, 1fr)); gap: 20px; } }

.prod-card {
  background: #fff;
  border: 1px solid var(--border);
  border-radius: 18px;
  overflow: hidden;
  transition: 0.3s;
  cursor: pointer;
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.prod-card:hover { transform: translateY(-4px); box-shadow: 0 10px 25px rgba(0,0,0,0.08); }
.prod-img { position: relative; height: 210px; background: var(--gray); overflow: hidden; }
@media(min-width: 768px) { .prod-img { height: 260px; } }
.prod-img img { width: 100%; height: 100%; object-fit: cover; transition: 0.4s; }

/* Glowing & Moving Sales Badges */
.sale-badge {
  position: absolute; top: 10px; left: 10px;
  background: linear-gradient(45deg, #ff3b30, #ff9500);
  color: #fff; font-size: 9px; font-weight: 900; padding: 5px 10px; border-radius: 20px; z-index: 2;
  box-shadow: 0 0 10px rgba(255,59,48,0.8);
  animation: badgeMove 2s infinite alternate;
}
@keyframes badgeMove {
  0% { transform: translateY(0) scale(1); filter: brightness(1); }
  100% { transform: translateY(-2px) scale(1.08); filter: brightness(1.3); box-shadow: 0 0 18px rgba(255,215,0,0.9); }
}

.prod-info { padding: 14px; }
.rating-row { display: flex; align-items: center; gap: 4px; font-size: 11px; color: #f59e0b; margin-bottom: 4px; font-weight: 700; }
.prod-info h3 { font-size: 13px; font-weight: 700; line-height: 1.3; height: 34px; overflow: hidden; margin-bottom: 6px; }
.price-row { display: flex; align-items: center; gap: 6px; margin-bottom: 10px; }
.price { font-weight: 900; font-size: 16px; color: #000; }
.old-price { font-size: 11px; color: #999; text-decoration: line-through; }
.btn-action {
  background: #000;
  color: #fff;
  border: none;
  padding: 10px;
  border-radius: 100px;
  font-weight: 800;
  font-size: 12px;
  width: 100%;
  cursor: pointer;
}
.btn-action:hover { background: var(--yellow); color: #000; }

/* PRODUCT MODAL (Size, Color, Qty Selection) */
#prodModal {
  position: fixed; inset: 0; background: #fff; z-index: 10002;
  transform: translateY(100%); transition: 0.4s cubic-bezier(.4,0,.2,1);
  overflow-y: auto; padding-bottom: 90px;
}
#prodModal.active { transform: translateY(0); }
.size-chip { border: 2px solid var(--border); padding: 8px 16px; border-radius: 50px; font-size: 12px; font-weight: 800; display: inline-block; margin: 4px; cursor: pointer; }
.size-chip.active { background: #000; color: #fff; border-color: #000; }
.color-dot { width: 32px; height: 32px; border-radius: 50%; display: inline-block; margin: 4px; border: 2px solid #fff; box-shadow: 0 0 0 2px var(--border); cursor: pointer; }
.color-dot.active { box-shadow: 0 0 0 2px #000; transform: scale(1.15); }
.qty-box { display: flex; align-items: center; justify-content: space-between; background: var(--gray); border-radius: 50px; padding: 6px 12px; margin-top: 10px; }
.q-btn { width: 36px; height: 36px; border-radius: 50%; background: #fff; border: 1px solid var(--border); font-size: 18px; font-weight: 900; cursor: pointer; }

/* Reviews Section */
.reviews-section { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; padding: 0 20px 40px; width: 100%; }
.review-card { background: var(--gray); border: 1px solid var(--border); border-radius: 18px; padding: 18px; }
.review-top { display: flex; justify-content: space-between; margin-bottom: 6px; font-weight: 800; font-size: 13px; }

/* Add Review Form Box */
.review-form-box { background: #fafafa; border: 2px dashed #cbd5e1; border-radius: 20px; padding: 20px; margin: 0 20px 40px; }
.form-input { width: 100%; padding: 12px 16px; border: 1px solid var(--border); border-radius: 12px; margin-top: 8px; font-size: 14px; outline: none; }
.form-input:focus { border-color: #000; }

/* Footer */
.footer { background: #060606; color: #fff; padding: 50px 20px 100px; text-align: center; border-top: 4px solid var(--yellow); width: 100%; }
.footer h1 { font-family: 'Bebas Neue'; font-size: 50px; letter-spacing: 8px; }
.footer p { font-size: 13px; opacity: 0.7; margin: 10px 0; line-height: 1.5; }

/* Support Floating Widget */
.support-widget { position: fixed; bottom: 85px; right: 20px; z-index: 9998; }
.wa-float {
  background: #25D366; color: #fff; width: 52px; height: 52px; border-radius: 50%;
  display: flex; align-items: center; justify-content: center; font-size: 26px;
  box-shadow: 0 6px 20px rgba(37,211,102,0.5); text-decoration: none; cursor: pointer;
}

/* Bottom Navigation */
.bottom-nav {
  position: fixed; bottom: 0; left: 0; right: 0;
  background: #fff; border-top: 1px solid var(--border);
  display: flex; justify-content: space-around; padding: 10px 0 14px; z-index: 9999; width: 100%;
}
.b-nav-item { font-size: 10px; font-weight: 700; text-align: center; opacity: 0.6; cursor: pointer; }
.b-nav-item.active { opacity: 1; color: var(--red); }

/* Cart Drawer */
#cartDrawer {
  position: fixed; top: 0; right: -100%;
  width: 100%; max-width: 440px; height: 100%;
  background: #fff; z-index: 10001;
  transition: 0.35s cubic-bezier(.4,0,.2,1);
  padding: 20px; display: flex; flex-direction: column;
  box-shadow: -10px 0 30px rgba(0,0,0,0.2);
}
#cartDrawer.active { right: 0; }
.overlay { position: fixed; inset: 0; background: rgba(0,0,0,0.6); display: none; z-index: 10000; }
.overlay.active { display: block; }
</style>
</head>
<body>

<div class="top-strip">
  ✨ 🔥 GRAND SALES MELA 2026 • FLAT 50% OFF + FREE DELIVERY ALL OVER PAKISTAN 🔥 ✨
</div>

<div class="navbar">
  <a href="/" class="logo">URBA<span>N</span></a>
  <div class="nav-links">
    <a href="/">Home</a>
    <a href="#shop-section">Shop</a>
    <a href="#reviews-section">Reviews</a>
    <a href="https://wa.me/923464621962" target="_blank">Support</a>
  </div>
  <div class="cart-badge-btn" onclick="openCart()">🛒 Cart (<span id="count">0</span>)</div>
</div>

<div class="hero">
  <div class="mela-badge">BIGGEST STREETWEAR SALE OF 2026</div>
  <h1>GRAND SALES<br><span>MELA IS LIVE.</span></h1>
  <p>Pakistan's most loved oversized hoodies, heavy jackets & cargos at unbelievable half-prices. Cash on Delivery available!</p>
  <button class="btn-mela" onclick="document.getElementById('shop-section').scrollIntoView({behavior:'smooth'})">SHOP MELA DEALS</button>
</div>

<div class="ticker-bar">
  <div class="ticker-item"><div>Flash Deals End In</div><div id="countdown">11:45:30</div></div>
  <div class="ticker-item"><div>Total Orders Today</div><div style="color:#22c55e">1,420+ Orders</div></div>
  <div class="ticker-item"><div>Delivery Partner</div><div style="color:#38bdf8">TCS & Leopard</div></div>
</div>

<div class="filter-container">
  <button class="filter-btn active" onclick="filterProducts('all', this)">🔥 All Deals</button>
  <button class="filter-btn" onclick="filterProducts('hoodies', this)">🧥 Hoodies</button>
  <button class="filter-btn" onclick="filterProducts('cargos', this)">👖 Cargos</button>
  <button class="filter-btn" onclick="filterProducts('jackets', this)">🧥 Jackets</button>
  <button class="filter-btn" onclick="filterProducts('tshirts', this)">👕 T-Shirts</button>
  <button class="filter-btn" onclick="filterProducts('accessories', this)">🧢 Accessories</button>
</div>

<div class="sec-head" id="shop-section">
  <h2>🌟 MELA EXCLUSIVE PRODUCTS</h2>
</div>

<div class="prod-grid" id="productGrid">
  {% for p in products %}
  <div class="prod-card" data-category="{{ p.cat }}" onclick="openProd({{ loop.index0 }})">
    <div class="prod-img">
      <span class="sale-badge">{{ p.tag }}</span>
      <img src="{{ p.img }}" loading="lazy" alt="{{ p.name }}">
    </div>
    <div class="prod-info">
      <div class="rating-row">★★★★★ <span style="color:#666;font-size:10px">({{ p.reviews }})</span></div>
      <h3>{{ p.name }}</h3>
      <div class="price-row">
        <span class="price">Rs. {{ p.price }}</span>
        <span class="old-price">Rs. {{ p.old }}</span>
      </div>
      <button class="btn-action">Select Options</button>
    </div>
  </div>
  {% endfor %}
</div>

<!-- PRODUCT MODAL FOR SIZE & COLOR -->
<div id="prodModal">
  <div style="position:relative">
    <img id="mImg" src="" style="width:100%;height:45vh;object-fit:cover">
    <div onclick="closeProd()" style="position:absolute;top:15px;left:15px;background:#fff;width:36px;height:36px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:900;cursor:pointer;box-shadow:0 2px 8px rgba(0,0,0,0.2)">✕</div>
  </div>
  <div style="padding:18px">
    <h2 id="mName" style="font-size:20px;font-weight:900"></h2>
    <div style="display:flex;gap:8px;margin:8px 0;align-items:center">
      <span id="mPrice" style="font-size:22px;font-weight:900;color:#000"></span>
      <span id="mOld" style="color:#999;text-decoration:line-through;font-size:13px"></span>
    </div>
    
    <p style="font-size:11px;font-weight:900;opacity:0.6;margin-top:14px">SELECT SIZE</p>
    <div style="margin-top:6px">
      <span class="size-chip active" onclick="setSize(this,'M')">M</span>
      <span class="size-chip" onclick="setSize(this,'L')">L</span>
      <span class="size-chip" onclick="setSize(this,'XL')">XL</span>
      <span class="size-chip" onclick="setSize(this,'XXL')">XXL</span>
    </div>

    <p style="font-size:11px;font-weight:900;opacity:0.6;margin-top:14px">SELECT COLOR</p>
    <div style="margin-top:6px">
      <span class="color-dot active" style="background:#000" onclick="setColor(this,'Black')"></span>
      <span class="color-dot" style="background:#fff" onclick="setColor(this,'White')"></span>
      <span class="color-dot" style="background:#8B7355" onclick="setColor(this,'Khaki')"></span>
      <span class="color-dot" style="background:#1e3a8a" onclick="setColor(this,'Navy')"></span>
    </div>

    <p style="font-size:11px;font-weight:900;opacity:0.6;margin-top:14px">QUANTITY</p>
    <div class="qty-box">
      <div style="display:flex;align-items:center;gap:12px">
        <button class="q-btn" onclick="changeQty(-1)">−</button>
        <span id="qtyNum" style="font-size:18px;font-weight:900">1</span>
        <button class="q-btn" onclick="changeQty(1)">+</button>
      </div>
      <div id="qtyTotal" style="font-size:18px;font-weight:900">Rs. 0</div>
    </div>
  </div>

  <div style="position:fixed;bottom:0;left:0;right:0;background:#fff;border-top:1px solid var(--border);padding:12px 20px;display:flex;gap:10px;z-index:10003">
    <button style="flex:1;background:var(--gray);border:1px solid var(--border);padding:14px;border-radius:100px;font-weight:800;cursor:pointer" onclick="closeProd()">Back</button>
    <button style="flex:2;background:#000;color:#fff;border:none;padding:14px;border-radius:100px;font-weight:900;cursor:pointer" onclick="addFromModal()">ADD TO CART • <span id="addBtnPrice">Rs. 0</span></button>
  </div>
</div>

<div class="sec-head" id="reviews-section" style="margin-top:20px;">
  <h2>💬 VERIFIED BUYER REVIEWS</h2>
</div>

<div class="reviews-section" id="reviewsContainer">
  {% for r in reviews %}
  <div class="review-card">
    <div class="review-top">
      <span>{{ r.name }} <span style="color:var(--green)">✓ Verified</span></span>
      <span style="color:#888;font-size:11px">{{ r.date }}</span>
    </div>
    <div style="color:#f59e0b;font-size:12px;margin-bottom:4px">★★★★★ <b style="color:#000;margin-left:4px">{{ r.city }}</b></div>
    <p style="font-size:13px;color:#444;line-height:1.4;">{{ r.comment }}</p>
  </div>
  {% endfor %}
</div>

<!-- Customer Review Add Form -->
<div class="sec-head">
  <h2>✍️ APNA REVIEW SHARE KARAIN</h2>
</div>
<div class="review-form-box">
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px">
    <input type="text" id="revName" class="form-input" placeholder="Aap Ka Naam (e.g. Ali Khan)">
    <input type="text" id="revCity" class="form-input" placeholder="Shehar (e.g. Peshawar)">
  </div>
  <textarea id="revComment" class="form-input" placeholder="Aap ka experience kaisa raha product ke sath?" rows="3" style="resize:none;margin-top:12px"></textarea>
  <button onclick="submitReview()" style="background:#000;color:#fff;border:none;width:100%;padding:14px;border-radius:50px;font-weight:900;margin-top:14px;cursor:pointer">SUBMIT REVIEW ⭐</button>
</div>

<div class="footer">
  <h1>URBAN®</h1>
  <p>Nisatta, Nowshera, KPK, Pakistan<br>WhatsApp Helpline: +92 346 4621962</p>
  <p style="font-size:11px;opacity:0.4;margin-top:10px;">© 2026 URBAN Sales Mela. All rights reserved.</p>
</div>

<div class="support-widget">
  <a href="https://wa.me/923464621962" class="wa-float" target="_blank" title="Live WhatsApp Support">💬</a>
</div>

<div class="bottom-nav">
  <div class="b-nav-item active" onclick="window.scrollTo({top:0,behavior:'smooth'})">🏠<br>Home</div>
  <div class="b-nav-item" onclick="document.getElementById('shop-section').scrollIntoView({behavior:'smooth'})">🛍️<br>Mela Deals</div>
  <div class="b-nav-item" onclick="openCart()">🛒<br>Cart (<span id="count2">0</span>)</div>
  <div class="b-nav-item" onclick="window.open('https://wa.me/923464621962','_blank')">💬<br>Support</div>
</div>

<div id="overlay" class="overlay" onclick="closeCart();closeProd()"></div>

<div id="cartDrawer">
  <div style="display:flex;justify-content:space-between;align-items:center">
    <h2 style="font-family:'Bebas Neue';font-size:26px">YOUR CART & CHECKOUT</h2>
    <span onclick="closeCart()" style="font-size:22px;font-weight:900;cursor:pointer">✕</span>
  </div>

  <div id="cartItems" style="flex:1;margin-top:15px;overflow-y:auto;max-height:30vh;padding-right:4px;"></div>

  <!-- Customer Address Input Section inside Cart -->
  <div style="background:#f1f5f9;padding:14px;border-radius:14px;margin-top:10px;">
    <p style="font-size:12px;font-weight:900;margin-bottom:6px;">📦 DELIVERY ADDRESS DETAILS:</p>
    <input type="text" id="custName" class="form-input" style="margin-top:4px;padding:8px 12px;font-size:12px;" placeholder="Full Name">
    <input type="text" id="custPhone" class="form-input" style="margin-top:6px;padding:8px 12px;font-size:12px;" placeholder="Phone Number (e.g. 03001234567)">
    <input type="text" id="custAddress" class="form-input" style="margin-top:6px;padding:8px 12px;font-size:12px;" placeholder="Complete Address (House, Street, Area)">
    <input type="text" id="custCity" class="form-input" style="margin-top:6px;padding:8px 12px;font-size:12px;" placeholder="City Name">
  </div>

  <div style="border-top:1px solid var(--border);padding-top:12px;margin-top:10px;">
    <div style="display:flex;justify-content:space-between;font-weight:900;font-size:16px;margin-bottom:10px">
      <span>Total Amount:</span>
      <span>Rs. <span id="total">0</span></span>
    </div>
    <button style="background:#25D366;color:#fff;border:none;width:100%;padding:14px;border-radius:100px;font-weight:900;font-size:14px;cursor:pointer;box-shadow:0 4px 15px rgba(37,211,102,0.4)" onclick="checkoutWhatsApp()">ORDER ON WHATSAPP 📲</button>
  </div>
</div>

<script>
const productsList = [
  {name:"Essential Heavyweight Hoodie - Jet Black", price:2999, old:5999, img:"https://images.unsplash.com/photo-1556821840-3a63f95609a7?w=800"},
  {name:"Y2K Baggy Cargo Denim - Ice Blue", price:3799, old:6999, img:"https://images.unsplash.com/photo-1542272604-787c3835535d?w=800"},
  {name:"Tactical 6-Pocket Utility Cargo - Khaki", price:3499, old:6000, img:"https://images.unsplash.com/photo-1517841905240-472988babdf9?w=800"},
  {name:"Retro Leather Varsity Jacket - Off White", price:4999, old:9999, img:"https://images.unsplash.com/photo-1591047139829-d91aecb6caea?w=800"},
  {name:"Minimalist Oversized Graphic Tee - Black", price:1499, old:3000, img:"https://images.unsplash.com/photo-1583743814966-8936f5b7be1a?w=800"},
  {name:"Urban Signature Street Cap - Black", price:899, old:1800, img:"https://images.unsplash.com/photo-1521369909029-2afed882baee?w=800"},
  {name:"Cyberpunk Techwear Windbreaker Jacket", price:5499, old:10999, img:"https://images.unsplash.com/photo-1548883354-7622d03aca27?w=800"},
  {name:"Distressed Grunge Oversized Hoodie", price:3199, old:6400, img:"https://images.unsplash.com/photo-1509631179647-0177331693ae?w=800"},
  {name:"Classic Ribbed Beanie - Charcoal Grey", price:699, old:1400, img:"https://images.unsplash.com/photo-1576871337632-b9aef4c17ab9?w=800"},
  {name:"Drop-Shoulder Heavyweight Tee - Olive", price:1599, old:3200, img:"https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=800"}
];

let curProd = null, curSize = 'M', curColor = 'Black', curQty = 1, cart = [];

// Countdown Timer
function startCountdown(duration, display) {
    let timer = duration, hours, minutes, seconds;
    setInterval(function () {
        hours = parseInt(timer / 3600, 10);
        minutes = parseInt((timer % 3600) / 60, 10);
        seconds = parseInt(timer % 60, 10);
        hours = hours < 10 ? "0" + hours : hours;
        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;
        display.textContent = hours + ":" + minutes + ":" + seconds;
        if (--timer < 0) { timer = duration; }
    }, 1000);
}
window.onload = function () {
    startCountdown(25000, document.querySelector('#countdown'));
};

// Filter System
function filterProducts(category, btn) {
    document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    document.querySelectorAll('.prod-card').forEach(card => {
        if(category === 'all' || card.getAttribute('data-category') === category) {
            card.style.display = 'flex';
        } else {
            card.style.display = 'none';
        }
    });
}

// Modal Functions
function openProd(i) {
    curProd = productsList[i];
    curQty = 1;
    curSize = 'M';
    curColor = 'Black';
    document.getElementById('mImg').src = curProd.img;
    document.getElementById('mName').innerText = curProd.name;
    document.getElementById('mOld').innerText = 'Rs. ' + curProd.old;
    
    document.querySelectorAll('.size-chip').forEach((el, idx) => {
        if(idx === 0) el.classList.add('active'); else el.classList.remove('active');
    });
    document.querySelectorAll('.color-dot').forEach((el, idx) => {
        if(idx === 0) el.classList.add('active'); else el.classList.remove('active');
    });

    updateQtyUI();
    document.getElementById('prodModal').classList.add('active');
    document.getElementById('overlay').classList.add('active');
}

function closeProd() {
    document.getElementById('prodModal').classList.remove('active');
    if(cart.length === 0) document.getElementById('overlay').classList.remove('active');
}

function setSize(el, s) {
    curSize = s;
    document.querySelectorAll('.size-chip').forEach(x => x.classList.remove('active'));
    el.classList.add('active');
}

function setColor(el, c) {
    curColor = c;
    document.querySelectorAll('.color-dot').forEach(x => x.classList.remove('active'));
    el.classList.add('active');
}

function changeQty(d) {
    curQty += d;
    if(curQty < 1) curQty = 1;
    if(curQty > 10) curQty = 10;
    updateQtyUI();
}

function updateQtyUI() {
    let p = curProd.price * curQty;
    document.getElementById('qtyNum').innerText = curQty;
    document.getElementById('qtyTotal').innerText = 'Rs. ' + p;
    document.getElementById('mPrice').innerText = 'Rs. ' + p;
    document.getElementById('addBtnPrice').innerText = 'Rs. ' + p;
}

function addFromModal() {
    cart.push({...curProd, qty: curQty, size: curSize, color: curColor, lineTotal: curProd.price * curQty});
    recalcCart();
    closeProd();
    openCart();
}

function recalcCart() {
    let total = 0;
    cart.forEach(i => total += i.lineTotal);
    document.getElementById('count').innerText = cart.length;
    document.getElementById('count2').innerText = cart.length;
    document.getElementById('total').innerText = total;
    renderCart();
}

function renderCart() {
    if(cart.length === 0) {
        document.getElementById('cartItems').innerHTML = '<p style="color:#888;text-align:center;margin-top:30px;font-size:13px;">Cart is empty. Select Mela deals! 🔥</p>';
        return;
    }
    let html = '';
    cart.forEach((it, i) => {
        html += `<div style="display:flex;gap:10px;margin-bottom:10px;padding-bottom:10px;border-bottom:1px solid #f4f4f4;align-items:center">
            <img src="${it.img}" style="width:50px;height:50px;border-radius:10px;object-fit:cover">
            <div style="flex:1">
                <div style="font-weight:800;font-size:12px">${it.name}</div>
                <div style="font-size:11px;color:#666">${it.color} • Size: ${it.size}</div>
                <div style="font-weight:900;font-size:12px;color:#d97706">Rs. ${it.lineTotal}</div>
                <div style="display:flex;align-items:center;gap:6px;margin-top:4px">
                    <button onclick="changeCartQty(${i}, -1)" style="width:22px;height:22px;border-radius:50%;border:1px solid #ccc;background:#fff;font-weight:bold;cursor:pointer">−</button>
                    <span style="font-weight:800;font-size:11px">${it.qty}</span>
                    <button onclick="changeCartQty(${i}, 1)" style="width:22px;height:22px;border-radius:50%;border:1px solid #ccc;background:#fff;font-weight:bold;cursor:pointer">+</button>
                </div>
            </div>
            <div onclick="removeItem(${i})" style="font-weight:900;color:#999;cursor:pointer;padding:4px">✕</div>
        </div>`;
    });
    document.getElementById('cartItems').innerHTML = html;
}

function changeCartQty(idx, d) {
    cart[idx].qty += d;
    if(cart[idx].qty < 1) cart[idx].qty = 1;
    if(cart[idx].qty > 10) cart[idx].qty = 10;
    cart[idx].lineTotal = cart[idx].qty * cart[idx].price;
    recalcCart();
}

function removeItem(idx) {
    cart.splice(idx, 1);
    recalcCart();
}

function openCart() {
    document.getElementById('cartDrawer').classList.add('active');
    document.getElementById('overlay').classList.add('active');
}

function closeCart() {
    document.getElementById('cartDrawer').classList.remove('active');
    if(!document.getElementById('prodModal').classList.contains('active')) {
        document.getElementById('overlay').classList.remove('active');
    }
}

// Dynamic Review Submission
function submitReview() {
    let name = document.getElementById('revName').value.trim();
    let city = document.getElementById('revCity').value.trim();
    let comment = document.getElementById('revComment').value.trim();

    if(!name || !city || !comment) {
        alert('Baraye meharbani naam, shehar aur review teeno fields purri karain!');
        return;
    }

    let reviewsContainer = document.getElementById('reviewsContainer');
    let newCard = document.createElement('div');
    newCard.className = 'review-card';
    newCard.innerHTML = `
        <div class="review-top">
            <span>${name} <span style="color:var(--green)">✓ Verified</span></span>
            <span style="color:#888;font-size:11px">Just now</span>
        </div>
        <div style="color:#f59e0b;font-size:12px;margin-bottom:4px">★★★★★ <b style="color:#000;margin-left:4px">${city}</b></div>
        <p style="font-size:13px;color:#444;line-height:1.4;">${comment}</p>
    `;
    reviewsContainer.prepend(newCard);

    document.getElementById('revName').value = '';
    document.getElementById('revCity').value = '';
    document.getElementById('revComment').value = '';
    alert('Shukriya! Aapka review successfully add ho gaya hai.');
}

// WhatsApp Checkout with Address & Product details
function checkoutWhatsApp() {
    if(cart.length === 0) {
        alert('Aapka cart khali hai!');
        return;
    }
    let name = document.getElementById('custName').value.trim();
    let phone = document.getElementById('custPhone').value.trim();
    let address = document.getElementById('custAddress').value.trim();
    let city = document.getElementById('custCity').value.trim();

    if(!name || !phone || !address || !city) {
        alert('Baraye meharbani apna Name, Phone, Complete Address aur City enter karain taaki order place ho sakay!');
        return;
    }

    let msg = `Salam URBAN Sales Mela! 🔥%0A%0A*Customer Details:*%0A👤 Name: ${name}%0A📞 Phone: ${phone}%0A🏠 Address: ${address}%0A📍 City: ${city}%0A%0A*Order Items:*%0A`;
    let total = 0;
    cart.forEach(item => {
        msg += `• ${item.name} (${item.color} / Size:${item.size}) | Qty: ${item.qty} - Rs. ${item.lineTotal}%0A`;
        total += item.lineTotal;
    });
    msg += `%0A*Total Bill: Rs. ${total} (Cash on Delivery)*%0A`;
    window.open(`https://wa.me/923464621962?text=${msg}`, '_blank');
}
</script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(TEMPLATE, products=PRODUCTS, reviews=CUSTOMER_REVIEWS)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

FROM nginx:alpine

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

RUN mkdir -p /usr/share/nginx/html && \
  cat > /usr/share/nginx/html/index.html <<'HTML'
<!doctype html>
<html lang="en">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Shortly — URL Shortener</title>
<link rel="preconnect" href="https://fonts.gstatic.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;500;700&display=swap" rel="stylesheet">
<style> body{font-family:Inter,system-ui,Helvetica,Arial;margin:0;background:#0f1724;color:#e6eef8;display:flex;align-items:center;justify-content:center;height:100vh} .card{width:min(720px,95vw);background:linear-gradient(180deg,#071023 0%,#071b2a 100%);padding:28px;border-radius:12px;box-shadow:0 10px 30px rgba(2,6,23,0.7)} h1{margin:0 0 10px;font-weight:700} p{margin:0 0 18px;color:#9fb3c8} form{display:flex;gap:10px} input{flex:1;padding:12px 14px;border-radius:8px;border:1px solid rgba(255,255,255,0.06);background:rgba(255,255,255,0.02);color:inherit;font-size:15px} button{padding:10px 14px;border-radius:8px;border:0;background:#06b6d4;color:#022;cursor:pointer;font-weight:600} .list{margin-top:18px;display:flex;flex-direction:column;gap:10px} .item{display:flex;justify-content:space-between;gap:10px;padding:10px;border-radius:8px;background:linear-gradient(90deg,rgba(255,255,255,0.02),rgba(255,255,255,0.01));font-size:14px} .muted{color:#93b6c9;font-size:13px} .small{font-size:13px;color:#9fb3c8} .cta{display:inline-flex;gap:8px;align-items:center} a.link{color:#9ee7ff;text-decoration:none} </style>
</head>
<body>
<div class="card">
  <h1>Shortly</h1>
  <p>Paste a long URL to get a short, beautiful link. No account required.</p>
  <form id="form">
    <input id="url" type="url" placeholder="https://example.com/very/long/path" required>
    <button id="go" type="submit">Shorten</button>
  </form>
  <div class="list" id="list"></div>
  <p class="small muted">Frontend decoupled from backend; backend URL injected at runtime.</p>
</div>
<script src="/env.js"></script>
<script>
const backend = window.BACKEND_URL || 'http://backend:8000';
const form = document.getElementById('form'), list = document.getElementById('list');
form.addEventListener('submit', async e => {
  e.preventDefault();
  const u = document.getElementById('url').value;
  if(!u) return;
  try{
    const res = await fetch(backend + '/api/shorten', {method:'POST',headers:{'Content-Type':'application/json'}, body:JSON.stringify({url:u})});
    if(!res.ok) throw new Error('Network');
    const data = await res.json();
    renderItem(u, data.short || data.code || data.shortUrl || data.id || '');
  }catch(err){
    alert('Error creating short link');
    console.error(err);
  }
});
function renderItem(orig, short){
  const div = document.createElement('div'); div.className='item';
  const left = document.createElement('div'); left.innerHTML = '<div class="muted>'+"'+escapeHtml(orig)+'"+'</div>'
}
</script>
</body>
</html>
HTML

EXPOSE 80
ENTRYPOINT ["/entrypoint.sh"]

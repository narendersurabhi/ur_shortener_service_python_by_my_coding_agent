(function(){
  const API_PLACEHOLDER = window.API_URL || '';
  // If template left untouched it may be "{{API_URL}}"; treat that as empty
  const API_URL = (API_PLACEHOLDER && !API_PLACEHOLDER.includes('{')) ? API_PLACEHOLDER : '/api/shorten';

  const $ = id => document.getElementById(id);
  const form = $('shortenForm');
  const longUrl = $('longUrl');
  const alias = $('alias');
  const expire = $('expire');
  const result = $('result');
  const historyEl = $('history');
  const apiLabel = $('apiLabel');
  const clearBtn = $('clearBtn');

  apiLabel.textContent = API_URL;

  function showMessage(html, kind){
    result.className = 'result';
    if(kind) result.classList.add(kind);
    result.innerHTML = html;
  }

  function hideResult(){ result.className = 'result hidden'; result.innerHTML=''; }

  function toPayload(){
    const p = { url: longUrl.value.trim() };
    if(alias.value.trim()) p.alias = alias.value.trim();
    if(expire.value) p.expire = Number(expire.value);
    return p;
  }

  function parseShort(res){
    if(!res) return null;
    if(res.short_url) return res.short_url;
    if(res.shortUrl) return res.shortUrl;
    if(res.short) return res.short;
    if(res.url && res.url.includes('://') && res.url !== toPayload().url) return res.url;
    if(res.id) return (res.domain ? res.domain.replace(/\/$/, '') : location.origin) + '/' + res.id;
    if(res.code) return location.origin + '/' + res.code;
    return null;
  }

  function makeButtons(short){
    const qr = 'https://api.qrserver.com/v1/create-qr-code/?size=160x160&data=' + encodeURIComponent(short);
    return `
      <div class="out">
        <a class="short" href="${short}" target="_blank" rel="noopener noreferrer">${short}</a>
        <div class="btns">
          <button data-action="copy">Copy</button>
          <a class="open" href="${short}" target="_blank" rel="noopener noreferrer">Open</a>
        </div>
      </div>
      <div class="meta">
        <img src="${qr}" alt="QR code" />
      </div>
    `;
  }

  function saveHistory(item){
    try{
      const key = 'tinybox_history_v1';
      const cur = JSON.parse(localStorage.getItem(key) || '[]');
      cur.unshift(item);
      const dedup = [];
      const map = new Set();
      for(const it of cur){
        if(!map.has(it.short)) { dedup.push(it); map.add(it.short); }
        if(dedup.length>=10) break;
      }
      localStorage.setItem(key, JSON.stringify(dedup));
      renderHistory();
    }catch(e){/*no-op*/}
  }

  function renderHistory(){
    const key = 'tinybox_history_v1';
    const cur = JSON.parse(localStorage.getItem(key) || '[]');
    historyEl.innerHTML = cur.map(it=>{
      const fav = `<a class="h-short" href="${it.short}" target="_blank">${it.short}</a>`;
      const src = `<span class="h-src">${it.source}</span>`;
      return `<li>${fav}${src}<button class="h-copy" data-short="${it.short}">Copy</button></li>`;
    }).join('');
  }

  form.addEventListener('submit', async function(e){
    e.preventDefault();
    hideResult();
    const payload = toPayload();
    if(!payload.url) return showMessage('Please enter a valid URL', 'err');
    showMessage('Creating link...', 'pending');

    try{
      const res = await fetch(API_URL, {
        method:'POST', headers:{'Content-Type':'application/json'}, body:JSON.stringify(payload)
      });
      const data = await res.json().catch(()=>({}));
      if(!res.ok){
        const msg = data.error || data.message || ('Server error: ' + res.status);
        return showMessage(`<strong class="err">${escapeHtml(msg)}</strong>`, 'err');
      }
      const short = parseShort(data) || data.short_url || data.url;
      if(!short) return showMessage('<strong class="err">Could not parse short URL</strong>', 'err');

      showMessage(makeButtons(short), 'done');
      saveHistory({ short, source: payload.url });
    }catch(err){
      showMessage('<strong class="err">Network error</strong>', 'err');
    }
  });

  // Copy / history click handlers
  result.addEventListener('click', function(e){
    const btn = e.target.closest('button');
    if(!btn) return;
    const act = btn.getAttribute('data-action');
    if(act==='copy'){
      const short = result.querySelector('.short').href;
      navigator.clipboard.writeText(short).then(()=> btn.textContent='Copied');
    }
  });

  historyEl.addEventListener('click', function(e){
    const b = e.target.closest('button.h-copy');
    if(!b) return;
    const s = b.getAttribute('data-short');
    navigator.clipboard.writeText(s).then(()=> b.textContent='Copied');
  });

  clearBtn.addEventListener('click', function(){
    longUrl.value=''; alias.value=''; expire.value=''; hideResult();
  });

  function escapeHtml(s){ return String(s).replace(/[&<>"']/g, c=>({
    '&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":"&#39;"
  }[c])); }

  // initialize
  renderHistory();

})();

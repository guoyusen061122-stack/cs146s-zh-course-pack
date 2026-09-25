
(function(){
  var body=document.body;
  var saved=localStorage.getItem('cs146s-mode')||'zh';
  if(saved==='bi') body.classList.add('mode-bi');
  var btn=document.getElementById('mode-btn');
  function label(){btn.textContent = body.classList.contains('mode-bi')?'切换：仅中文':'切换：中英对照';}
  label();
  if(btn) btn.addEventListener('click',function(){
    body.classList.toggle('mode-bi');
    localStorage.setItem('cs146s-mode', body.classList.contains('mode-bi')?'bi':'zh');
    label();
  });
  var box=document.getElementById('q');
  var out=document.getElementById('results');
  var idx=(window.SEARCH_INDEX||[]);
  function esc(s){return s.replace(/[&<>]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;'}[c];});}
  function run(){
    var q=box.value.trim().toLowerCase();
    if(!q){out.innerHTML='';return;}
    var hits=[];
    for(var i=0;i<idx.length;i++){
      var it=idx[i];
      var pos=it.text.toLowerCase().indexOf(q);
      if(pos<0) continue;
      hits.push({it:it,pos:pos});
      if(hits.length>=60) break;
    }
    if(!hits.length){out.innerHTML='<p class="meta">没有匹配结果。</p>';return;}
    var html='<p class="meta">命中 '+hits.length+' 处</p>';
    for(var j=0;j<hits.length;j++){
      var h=hits[j], t=h.it.text, p=h.pos;
      var s=Math.max(0,p-60), e=Math.min(t.length,p+q.length+90);
      html+='<a href="'+h.it.url+'"><span class="badge">'+esc(h.it.group)+'</span>'
        +esc(h.it.title)+'<br><span class="meta">…'+esc(t.slice(s,e))+'…</span></a>';
    }
    out.innerHTML=html;
  }
  if(box){box.addEventListener('input',run);}
})();

(function(){
  var links=document.querySelectorAll('nav.side a');
  for(var i=0;i<links.length;i++){
    if(links[i].pathname===location.pathname) links[i].classList.add('active');
  }
})();

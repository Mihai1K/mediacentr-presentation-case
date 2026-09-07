/* Mediacentr interactions */
var pb=document.getElementById('progress');
addEventListener('scroll',function(){var h=document.documentElement,b=document.body;var st=h.scrollTop||b.scrollTop,sh=(h.scrollHeight||b.scrollHeight)-h.clientHeight;pb.style.width=(sh>0?(st/sh*100):0)+'%';},{passive:true});
var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}});},{threshold:.16,rootMargin:'0px 0px -8% 0px'});
document.querySelectorAll('.reveal').forEach(function(el){io.observe(el)});
var slides=[].slice.call(document.querySelectorAll('.slide'));
addEventListener('keydown',function(e){var i=slides.findIndex(function(s){return s.getBoundingClientRect().top>=-2;});if(e.key==='ArrowDown'||e.key==='PageDown'){e.preventDefault();(slides[i+1]||slides[i]||slides[0]).scrollIntoView({behavior:'smooth'});}if(e.key==='ArrowUp'||e.key==='PageUp'){e.preventDefault();(slides[Math.max(0,i-1)]||slides[0]).scrollIntoView({behavior:'smooth'});}});

document.addEventListener("DOMContentLoaded", function(event) { 

function myJquery (selector, context = document){
  this.elements = Array.from(context.querySelectorAll(selector));
  return this
}

myJquery.prototype.each = function (fn){
  this.elements.forEach((element, index) => fn.call(element, element, index));
  return this;
}

myJquery.prototype.click = function(fn){
  this.each(element => element.addEventListener('click', fn))
  return this
}

myJquery.prototype.hide = function(){
  this.each(element => element.style.display = 'none')
  return this;
}

myJquery.prototype.show = function(){
  this.each(element => element.style.display = 'block')
  return this;
}

myJquery.prototype.remove = function(){
  this.each(element => element.remove())
  return this;
}

myJquery.prototype.class = function(name){
  this.each(element => element.className = name)
  return this;
}
myJquery.prototype.html = function(html){
    if (html) {
this.each(element=> element.innerHTML = html)
return this
}
else {
this.each(element=>element.innerHTML)
  return this;
}
}

myJquery.prototype.text = function (text) {
if (text) {
this.each(element=> element.innerText = text)
return this
}
else {
this.each(element=>element.innerText)
return this
}
}

const $ = (e) => new myJquery(e);

const timer = document.querySelector('.countdown');
const minutes = document.querySelector('.minutes');
const seconds = document.querySelector('.seconds');
const message = document.querySelector('.message');
const plus = document.querySelector('.plus');
const minus = document.querySelector('.minus');
const start = document.querySelector('.start');
const pause = document.querySelector('.pause');
const body = document.querySelector('body');
const keys = document.querySelector('.keys');
const title = document.querySelector('.countdown-title');
const clock_set = document.querySelector('.set');
const clock_submit = document.querySelector('.submit');
const min = document.querySelector('.min');
const sec = document.querySelector('.sec');

let countSec = 0;
let countMin = 0;

const updateText = () =>{	
  minutes.innerHTML = (0 + String(countMin)).slice(-2);
  seconds.innerHTML = (0 + String(countSec)).slice(-2);
}
updateText();

const countDown = () => {	
	let total = countSec + countMin * 60;

  if (total < 1) {
    clearInterval(timerID);
    $('.countdown-title').hide();
    $('.countdown').hide();
    body.style.backgroundColor = '#262626';
    body.style.backgroundImage = 'none';
    $('.pause').hide();
    message.innerHTML = '<p>BOOM</p>'
  }
  if (countSec > 0) countSec--;
  else {
  	countSec = 59;
    countMin--;
  }

  updateText();
  }

  const timeinterval = function() {
  timerID = setInterval(countDown, 1000);
  }

plus.onclick = () =>{
  if(countSec < 59) ++countSec;
  else{
  	countSec = 0;
  	++countMin;
  }
  updateText()
  }

minus.onclick = () =>{
	if(countMin <= 0 && countSec===0){
  	countSec = 0;
    countMin = 0;
    return;
  }
  if(countSec > 0) --countSec;
  else{
  	countSec = 59;
  	--countMin;
  }
  updateText();
  } 

start.onclick = () => {
	// countDown();
  body.style.backgroundImage = "url('bomb.jpg')";
  body.style.backgroundColor = '#ffffff';
  $('.keys').hide();
  $('.pause').show();
  timeinterval();  
}

pause.onclick = () => {
  clearInterval(timerID);
}

clock_set.onclick = () => {
  $('.settimer').show();
  $('.keys').hide();
}

min.onchange = () => {
  countMin = min.value;
  updateText();
}

sec.onchange = () => {
  countSec = sec.value;
  updateText();
}

clock_submit.onclick = () => {
  $('.settimer').hide();
  $('.keys').show();
}

});

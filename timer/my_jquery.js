document.addEventListener("DOMContentLoaded", function(event) { 

function my_jQuery (selector, context = document){
	this.elements = Array.from(context.querySelectorAll(selector));
	return this
}

my_jQuery.prototype.each = function (fn){
	this.elements.forEach((element, index) => fn.call(element, element, index));
	return this;
}

my_jQuery.prototype.click = function(fn){
	this.each(element => element.addEventListener('click', fn))
	return this
}

my_jQuery.prototype.hide = function(){
	this.each(element => element.style.display = 'none')
  return this;
}

my_jQuery.prototype.show = function(){
	this.each(element => element.style.display = '')
  return this;
}

my_jQuery.prototype.remove = function(){
	this.each(element => element.remove())
  return this;
}

my_jQuery.prototype.class = function(name){
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
});

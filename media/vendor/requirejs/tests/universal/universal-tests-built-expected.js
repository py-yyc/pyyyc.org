!function(name,definition){if(typeof module!='undefined')module.exports=definition()
else if(typeof define=='function'&&typeof define.amd=='object')define('tail',[],function(){return definition()})
else this[name]=definition()}('tail',function(){return{name:'tail'}});!function(name,definition){if(typeof module!='undefined')module.exports=definition()
else if(typeof define=='function'&&typeof define.amd=='object')define(name,definition)
else this[name]=definition()}('eye',function(){return{name:'eye'}});define("eye",function(){});(function(define){

define('newt',['require','tail','eye'],function(require){ var tail=require('tail'),eye=require('eye');return{name:'newt',eyeName:eye.name,tailName:tail.name};});}(typeof define==='function'&&define.amd?define:function(id,factory){if(typeof module!=='undefined'&&module.exports){ module.exports=factory(require);}else{

window.myGlobal=factory(function(value){return window[value];});}}));(function(define){

define('spell',['require','newt'],function(require){ var newt=require('newt');return{name:'spell',newtName:newt.name,tailName:newt.tailName,eyeName:newt.eyeName};});}(typeof define==='function'&&define.amd?define:function(id,factory){if(typeof module!=='undefined'&&module.exports){ module.exports=factory(require);}else{

window.myGlobal=factory(function(value){return window[value];});}}));require({baseUrl:requirejs.isBrowser?"./":"./universal/"},["spell"],function(spell){doh.register("universal",[function universal(t){t.is('spell',spell.name);t.is('newt',spell.newtName);t.is('tail',spell.tailName);t.is('eye',spell.eyeName);}]);doh.run();});define("universal-tests",function(){});
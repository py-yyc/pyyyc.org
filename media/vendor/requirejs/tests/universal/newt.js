(function(define){

define(function(require){ var tail=require('tail'),eye=require('eye');return{name:'newt',eyeName:eye.name,tailName:tail.name};});}(typeof define==='function'&&define.amd?define:function(id,factory){if(typeof module!=='undefined'&&module.exports){ module.exports=factory(require);}else{

window.myGlobal=factory(function(value){return window[value];});}}));
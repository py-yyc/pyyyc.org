(function(define){

define('spell',function(require){ var newt=require('newt');return{name:'spell',newtName:newt.name,tailName:newt.tailName,eyeName:newt.eyeName};});}(typeof define==='function'&&define.amd?define:function(id,factory){if(typeof module!=='undefined'&&module.exports){ module.exports=factory(require);}else{

window.myGlobal=factory(function(value){return window[value];});}}));
define({load:function(name,require,load,config){if(!name){name='main';}else if(name.charAt(0)==='/'){name='main'+name;}

name=name.split('/').shift();name='plug/'+name;require([name],load);}});
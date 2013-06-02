(function(){var buildMap={},fetchText,fs,progIds=['Msxml2.XMLHTTP','Microsoft.XMLHTTP','Msxml2.XMLHTTP.4.0'];function createXhr(){var xhr,i,progId;if(typeof XMLHttpRequest!=="undefined"){return new XMLHttpRequest();}else{for(i=0;i<3;i++){progId=progIds[i];try{xhr=new ActiveXObject(progId);}catch(e){}
if(xhr){progIds=[progId]; break;}}}
if(!xhr){throw new Error("require.getXhr(): XMLHttpRequest not available");}
return xhr;}
if(typeof window!=="undefined"&&window.navigator&&window.document){fetchText=function(url,callback){var xhr=createXhr();xhr.open('GET',url,true);xhr.onreadystatechange=function(evt){
if(xhr.readyState===4){callback(xhr.responseText);}};xhr.send(null);};}else if(typeof process!=="undefined"&&process.versions&&!!process.versions.node){fs=require.nodeRequire('fs');fetchText=function(url,callback){callback(fs.readFileSync(url,'utf8'));};}else if(typeof Packages!=='undefined'){fetchText=function(url,callback){var encoding="utf-8",file=new java.io.File(url),lineSeparator=java.lang.System.getProperty("line.separator"),input=new java.io.BufferedReader(new java.io.InputStreamReader(new java.io.FileInputStream(file),encoding)),stringBuffer,line,content='';try{stringBuffer=new java.lang.StringBuffer();line=input.readLine();

 if(line&&line.length()&&line.charAt(0)===0xfeff){
line=line.substring(1);}
stringBuffer.append(line);while((line=input.readLine())!==null){stringBuffer.append(lineSeparator);stringBuffer.append(line);}
content=String(stringBuffer.toString());}finally{input.close();}
callback(content);};}
define(function(){return{load:function(name,parentRequire,load,config){var url=parentRequire.toUrl(name+'.refine');fetchText(url,function(text){text=text.replace(/refine/g,'define');if(config.isBuild){buildMap[name]=text;} 
text+="\r\n//@ sourceURL="+url;load.fromText(name,text);parentRequire([name],function(value){load(value);});});},write:function(pluginName,name,write){if(name in buildMap){var text=buildMap[name];write.asModule(pluginName+"!"+name,text);}}};});}());
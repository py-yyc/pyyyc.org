
if(!this["doh"]){doh={};}

doh.selfTest=false;doh.global=this;doh.hitch=function(thisObject,method){var args=[];for(var x=2;x<arguments.length;x++){args.push(arguments[x]);}
var fcn=((typeof method=="string")?thisObject[method]:method)||function(){};return function(){var ta=args.concat([]); for(var x=0;x<arguments.length;x++){ta.push(arguments[x]);}
return fcn.apply(thisObject,ta);};}
doh._mixin=function(obj,props){

var tobj={};for(var x in props){

 if(tobj[x]===undefined||tobj[x]!=props[x]){obj[x]=props[x];}} 
if(this["document"]&&document.all&&(typeof props["toString"]=="function")&&(props["toString"]!=obj["toString"])&&(props["toString"]!=tobj["toString"])){obj.toString=props.toString;}
return obj;}
doh.mixin=function(obj,props){for(var i=1,l=arguments.length;i<l;i++){doh._mixin(obj,arguments[i]);}
return obj;}
doh.extend=function(constructor,props){

for(var i=1,l=arguments.length;i<l;i++){doh._mixin(constructor.prototype,arguments[i]);}
return constructor;}
doh._line="------------------------------------------------------------";doh.debug=function(){

}
doh._AssertFailure=function(msg,hint){if(!(this instanceof doh._AssertFailure)){return new doh._AssertFailure(msg,hint);}
if(hint){msg=(new String(msg||""))+" with hint: \n\t\t"+(new String(hint)+"\n");}
this.message=new String(msg||"");return this;}
doh._AssertFailure.prototype=new Error();doh._AssertFailure.prototype.constructor=doh._AssertFailure;doh._AssertFailure.prototype.name="doh._AssertFailure";doh.Deferred=function(canceller){this.chain=[];this.id=this._nextId();this.fired=-1;this.paused=0;this.results=[null,null];this.canceller=canceller;this.silentlyCancelled=false;};doh.extend(doh.Deferred,{getTestErrback:function(cb,scope){ var _this=this;return function(){try{cb.apply(scope||doh.global||_this,arguments);}catch(e){_this.errback(e);}};},getTestCallback:function(cb,scope){var _this=this;return function(){try{cb.apply(scope||doh.global||_this,arguments);}catch(e){_this.errback(e);return;}
_this.callback(true);};},getFunctionFromArgs:function(){var a=arguments;if((a[0])&&(!a[1])){if(typeof a[0]=="function"){return a[0];}else if(typeof a[0]=="string"){return doh.global[a[0]];}}else if((a[0])&&(a[1])){return doh.hitch(a[0],a[1]);}
return null;},makeCalled:function(){var deferred=new doh.Deferred();deferred.callback();return deferred;},_nextId:(function(){var n=1;return function(){return n++;};})(),cancel:function(){if(this.fired==-1){if(this.canceller){this.canceller(this);}else{this.silentlyCancelled=true;}
if(this.fired==-1){this.errback(new Error("Deferred(unfired)"));}}else if(this.fired==0&&(this.results[0]instanceof doh.Deferred)){this.results[0].cancel();}},_pause:function(){this.paused++;},_unpause:function(){this.paused--;if((this.paused==0)&&(this.fired>=0)){this._fire();}},_continue:function(res){this._resback(res);this._unpause();},_resback:function(res){this.fired=((res instanceof Error)?1:0);this.results[this.fired]=res;this._fire();},_check:function(){if(this.fired!=-1){if(!this.silentlyCancelled){throw new Error("already called!");}
this.silentlyCancelled=false;return;}},callback:function(res){this._check();this._resback(res);},errback:function(res){this._check();if(!(res instanceof Error)){res=new Error(res);}
this._resback(res);},addBoth:function(cb,cbfn){var enclosed=this.getFunctionFromArgs(cb,cbfn);if(arguments.length>2){enclosed=doh.hitch(null,enclosed,arguments,2);}
return this.addCallbacks(enclosed,enclosed);},addCallback:function(cb,cbfn){var enclosed=this.getFunctionFromArgs(cb,cbfn);if(arguments.length>2){enclosed=doh.hitch(null,enclosed,arguments,2);}
return this.addCallbacks(enclosed,null);},addErrback:function(cb,cbfn){var enclosed=this.getFunctionFromArgs(cb,cbfn);if(arguments.length>2){enclosed=doh.hitch(null,enclosed,arguments,2);}
return this.addCallbacks(null,enclosed);},addCallbacks:function(cb,eb){this.chain.push([cb,eb]);if(this.fired>=0){this._fire();}
return this;},_fire:function(){var chain=this.chain;var fired=this.fired;var res=this.results[fired];var self=this;var cb=null;while(chain.length>0&&this.paused==0){ var pair=chain.shift();var f=pair[fired];if(f==null){continue;}
try{res=f(res);fired=((res instanceof Error)?1:0);if(res instanceof doh.Deferred){cb=function(res){self._continue(res);};this._pause();}}catch(err){fired=1;res=err;}}
this.fired=fired;this.results[fired]=res;if((cb)&&(this.paused)){res.addBoth(cb);}}});
doh._testCount=0;doh._groupCount=0;doh._errorCount=0;doh._failureCount=0;doh._currentGroup=null;doh._currentTest=null;doh._paused=true;doh._init=function(){this._currentGroup=null;this._currentTest=null;this._errorCount=0;this._failureCount=0;this.debug(this._testCount,"tests to run in",this._groupCount,"groups");}
doh._groups={};
doh.registerTestNs=function(group,ns){



for(var x in ns){if((x.charAt(0)!="_")&&(typeof ns[x]=="function")){this.registerTest(group,ns[x]);}}}
doh._testRegistered=function(group,fixture){}
doh._groupStarted=function(group){}
doh._groupFinished=function(group,success){}
doh._testStarted=function(group,fixture){}
doh._testFinished=function(group,fixture,success){}
doh.registerGroup=function(group,tests,setUp,tearDown,type){













if(tests){this.register(group,tests,type);}
if(setUp){this._groups[group].setUp=setUp;}
if(tearDown){this._groups[group].tearDown=tearDown;}}
doh._getTestObj=function(group,test,type){var tObj=test;if(typeof test=="string"){if(test.substr(0,4)=="url:"){return this.registerUrl(group,test);}else{tObj={name:test.replace("/\s/g","_")
};tObj.runTest=new Function("t",test);}}else if(typeof test=="function"){ tObj={"runTest":test};if(test["name"]){tObj.name=test.name;}else{try{var fStr="function ";var ts=tObj.runTest+"";if(0<=ts.indexOf(fStr)){tObj.name=ts.split(fStr)[1].split("(",1)[0];}
}catch(e){}}
}

if(type==="perf"||tObj.testType==="perf"){tObj.testType="perf";if(!doh.perfTestResults){doh.perfTestResults={};doh.perfTestResults[group]={};}
if(!doh.perfTestResults[group]){doh.perfTestResults[group]={};}
if(!doh.perfTestResults[group][tObj.name]){doh.perfTestResults[group][tObj.name]={};}
tObj.results=doh.perfTestResults[group][tObj.name];
if(!("trialDuration"in tObj)){tObj.trialDuration=100;}

if(!("trialDelay"in tObj)){tObj.trialDelay=100;}
if(!("trialIterations"in tObj)){tObj.trialIterations=10;}}
return tObj;}
doh.registerTest=function(group,test,type){





if(!this._groups[group]){this._groupCount++;this._groups[group]=[];this._groups[group].inFlight=0;}
var tObj=this._getTestObj(group,test,type);if(!tObj){return null;}
this._groups[group].push(tObj);this._testCount++;this._testRegistered(group,tObj);return tObj;}
doh.registerTests=function(group,testArr,type){


 for(var x=0;x<testArr.length;x++){this.registerTest(group,testArr[x],type);}}
doh.registerUrl=function(group,url,timeout,type){this.debug("ERROR:");this.debug("\tNO registerUrl() METHOD AVAILABLE.");}
doh.registerString=function(group,str,type){}
doh.register=doh.add=function(groupOrNs,testOrNull,type){

if((arguments.length==1)&&(typeof groupOrNs=="string")){if(groupOrNs.substr(0,4)=="url:"){this.registerUrl(groupOrNs,null,null,type);}else{this.registerTest("ungrouped",groupOrNs,type);}}
if(arguments.length==1){this.debug("invalid args passed to doh.register():",groupOrNs,",",testOrNull);return;}
if(typeof testOrNull=="string"){if(testOrNull.substr(0,4)=="url:"){this.registerUrl(testOrNull,null,null,type);}else{this.registerTest(groupOrNs,testOrNull,type);}
return;}
if(doh._isArray(testOrNull)){this.registerTests(groupOrNs,testOrNull,type);return;}
this.registerTest(groupOrNs,testOrNull,type);};doh.registerDocTests=function(module){ this.debug("registerDocTests() requires dojo to be loaded into the environment. Skipping doctest set for module:",module);};(function(){if(typeof dojo!="undefined"){try{dojo.require("dojox.testing.DocTest");}catch(e){
 console.debug(e);doh.registerDocTests=function(){}
return;}
doh.registerDocTests=function(module){
var docTest=new dojox.testing.DocTest();var docTests=docTest.getTests(module);var len=docTests.length;var tests=[];for(var i=0;i<len;i++){var test=docTests[i];var comment="";if(test.commands.length&&test.commands[0].indexOf("//")!=-1){var parts=test.commands[0].split("//");comment=", "+parts[parts.length-1];}
tests.push({runTest:(function(test){return function(t){var r=docTest.runTest(test.commands,test.expectedResult);t.assertTrue(r.success);}})(test),name:"Line "+test.line+comment});}
this.register("DocTests: "+module,tests);}}})();
doh.t=doh.assertTrue=function(condition,hint){if(arguments.length<1){throw new doh._AssertFailure("assertTrue failed because it was not passed at least 1 argument");}
if(!eval(condition)){throw new doh._AssertFailure("assertTrue('"+condition+"') failed",hint);}}
doh.f=doh.assertFalse=function(condition,hint){if(arguments.length<1){throw new doh._AssertFailure("assertFalse failed because it was not passed at least 1 argument");}
if(eval(condition)){throw new doh._AssertFailure("assertFalse('"+condition+"') failed",hint);}}
doh.e=doh.assertError=function(expectedError,scope,functionName,args,hint){try{scope[functionName].apply(scope,args);}catch(e){if(e instanceof expectedError){return true;}else{throw new doh._AssertFailure("assertError() failed:\n\texpected error\n\t\t"+expectedError+"\n\tbut got\n\t\t"+e+"\n\n",hint);}}
throw new doh._AssertFailure("assertError() failed:\n\texpected error\n\t\t"+expectedError+"\n\tbut no error caught\n\n",hint);}
doh.is=doh.assertEqual=function(expected,actual,hint){

if((expected===undefined)&&(actual===undefined)){return true;}
if(arguments.length<2){throw doh._AssertFailure("assertEqual failed because it was not passed 2 arguments");}
if((expected===actual)||(expected==actual)||(typeof expected=="number"&&typeof actual=="number"&&isNaN(expected)&&isNaN(actual))){return true;}
if((this._isArray(expected)&&this._isArray(actual))&&(this._arrayEq(expected,actual))){return true;}
if(((typeof expected=="object")&&((typeof actual=="object")))&&(this._objPropEq(expected,actual))){return true;}
throw new doh._AssertFailure("assertEqual() failed:\n\texpected\n\t\t"+expected+"\n\tbut got\n\t\t"+actual+"\n\n",hint);}
doh.isNot=doh.assertNotEqual=function(notExpected,actual,hint){

if((notExpected===undefined)&&(actual===undefined)){throw new doh._AssertFailure("assertNotEqual() failed: not expected |"+notExpected+"| but got |"+actual+"|",hint);}
if(arguments.length<2){throw doh._AssertFailure("assertEqual failed because it was not passed 2 arguments");}
if((notExpected===actual)||(notExpected==actual)){throw new doh._AssertFailure("assertNotEqual() failed: not expected |"+notExpected+"| but got |"+actual+"|",hint);}
if((this._isArray(notExpected)&&this._isArray(actual))&&(this._arrayEq(notExpected,actual))){throw new doh._AssertFailure("assertNotEqual() failed: not expected |"+notExpected+"| but got |"+actual+"|",hint);}
if(((typeof notExpected=="object")&&((typeof actual=="object")))&&(this._objPropEq(notExpected,actual))){throw new doh._AssertFailure("assertNotEqual() failed: not expected |"+notExpected+"| but got |"+actual+"|",hint);}
return true;}
doh._arrayEq=function(expected,actual){if(expected.length!=actual.length){return false;}
for(var x=0;x<expected.length;x++){if(!doh.assertEqual(expected[x],actual[x])){return false;}}
return true;}
doh._objPropEq=function(expected,actual){if(expected===null&&actual===null){return true;}
if(expected===null||actual===null){return false;}
if(expected instanceof Date){return actual instanceof Date&&expected.getTime()==actual.getTime();}
var x;for(x in actual){if(expected[x]===undefined){return false;}};for(x in expected){if(!doh.assertEqual(expected[x],actual[x])){return false;}}
return true;}
doh._isArray=function(it){return(it&&it instanceof Array||typeof it=="array"||(!!doh.global["dojo"]&&doh.global["dojo"]["NodeList"]!==undefined&&it instanceof doh.global["dojo"]["NodeList"]));}

doh._setupGroupForRun=function(groupName,idx){var tg=this._groups[groupName];this.debug(this._line);this.debug("GROUP","\""+groupName+"\"","has",tg.length,"test"+((tg.length>1)?"s":"")+" to run");}
doh._handleFailure=function(groupName,fixture,e){ this._groups[groupName].failures++;var out="";if(e instanceof this._AssertFailure){this._failureCount++;if(e["fileName"]){out+=e.fileName+':';}
if(e["lineNumber"]){out+=e.lineNumber+' ';}
out+=e+": "+e.message;this.debug("\t_AssertFailure:",out);}else{this._errorCount++;}
this.debug(e);if(fixture.runTest["toSource"]){var ss=fixture.runTest.toSource();this.debug("\tERROR IN:\n\t\t",ss);}else{this.debug("\tERROR IN:\n\t\t",fixture.runTest);}
if(e.rhinoException){e.rhinoException.printStackTrace();}else if(e.javaException){e.javaException.printStackTrace();}}



doh.setTimeout=function(func){return func();};doh._runPerfFixture=function(groupName,fixture){




var tg=this._groups[groupName];fixture.startTime=new Date();
var def=new doh.Deferred();tg.inFlight++;def.groupName=groupName;def.fixture=fixture;def.addErrback(function(err){doh._handleFailure(groupName,fixture,err);});var retEnd=function(){if(fixture["tearDown"]){fixture.tearDown(doh);}
tg.inFlight--;if((!tg.inFlight)&&(tg.iterated)){doh._groupFinished(groupName,!tg.failures);}
doh._testFinished(groupName,fixture,def.results[0]);if(doh._paused){doh.run();}};
 var timer;var to=fixture.timeout;if(to>0){timer=doh.setTimeout(function(){def.errback(new Error("test timeout in "+fixture.name.toString()));},to);}
def.addBoth(function(arg){if(timer){clearTimeout(timer);}
retEnd();});

var res=fixture.results;res.trials=[];var itrDef=doh._calcTrialIterations(groupName,fixture);itrDef.addErrback(function(err){fixture.endTime=new Date();def.errback(err);});
itrDef.addCallback(function(iterations){if(iterations){var countdown=fixture.trialIterations;doh.debug("TIMING TEST: ["+fixture.name+"]\n\t\tITERATIONS PER TRIAL: "+
iterations+"\n\tTRIALS: "+
countdown);var trialRunner=function(){ var start=new Date();var tTimer=new doh.Deferred();var tCountdown=iterations;var tState={countdown:iterations};var testRunner=function(state){while(state){try{state.countdown--;if(state.countdown){var ret=fixture.runTest(doh);if(ret instanceof doh.Deferred){var atState={countdown:state.countdown};ret.addCallback(function(){testRunner(atState);});ret.addErrback(function(err){doh._handleFailure(groupName,fixture,err);fixture.endTime=new Date();def.errback(err);});state=null;}}else{tTimer.callback(new Date());state=null;}}catch(err){fixture.endTime=new Date();tTimer.errback(err);}}};tTimer.addCallback(function(end){var tResults={trial:(fixture.trialIterations-countdown),testIterations:iterations,executionTime:(end.getTime()-start.getTime()),average:(end.getTime()-start.getTime())/iterations};res.trials.push(tResults);doh.debug("\n\t\tTRIAL #: "+
tResults.trial+"\n\tTIME: "+
tResults.executionTime+"ms.\n\tAVG TEST TIME: "+
(tResults.executionTime/tResults.testIterations)+"ms.");countdown--;if(countdown){doh.setTimeout(trialRunner,fixture.trialDelay);}else{var t=res.trials;fixture.endTime=new Date();def.callback(true);}});tTimer.addErrback(function(err){fixture.endTime=new Date();def.errback(err);});testRunner(tState);};trialRunner();}});if(def.fired<0){doh.pause();}
return def;};doh._calcTrialIterations=function(groupName,fixture){



var def=new doh.Deferred();var calibrate=function(){var testFunc=fixture.runTest;

var iState={start:new Date(),curIter:0,iterations:5};var handleIteration=function(state){while(state){if(state.curIter<state.iterations){try{var ret=testFunc(doh);if(ret instanceof doh.Deferred){var aState={start:state.start,curIter:state.curIter+1,iterations:state.iterations};ret.addCallback(function(){handleIteration(aState);});ret.addErrback(function(err){fixture.endTime=new Date();def.errback(err);});state=null;}else{state.curIter++;}}catch(err){fixture.endTime=new Date();def.errback(err);return;}}else{var end=new Date();var totalTime=(end.getTime()-state.start.getTime());if(totalTime<fixture.trialDuration){var nState={iterations:state.iterations*2,curIter:0}
state=null;doh.setTimeout(function(){nState.start=new Date();handleIteration(nState);},50);}else{var itrs=state.iterations;doh.setTimeout(function(){def.callback(itrs)},50);state=null;}}}};handleIteration(iState);};doh.setTimeout(calibrate,10);return def;};doh._runRegFixture=function(groupName,fixture){
var tg=this._groups[groupName];fixture.startTime=new Date();var ret=fixture.runTest(this);fixture.endTime=new Date();

if(ret instanceof doh.Deferred){tg.inFlight++;ret.groupName=groupName;ret.fixture=fixture;ret.addErrback(function(err){doh._handleFailure(groupName,fixture,err);});var retEnd=function(){if(fixture["tearDown"]){fixture.tearDown(doh);}
tg.inFlight--;if((!tg.inFlight)&&(tg.iterated)){doh._groupFinished(groupName,!tg.failures);}
doh._testFinished(groupName,fixture,ret.results[0]);if(doh._paused){doh.run();}}
var timer=doh.setTimeout(function(){ret.errback(new Error("test timeout in "+fixture.name.toString()));},fixture["timeout"]||1000);ret.addBoth(function(arg){clearTimeout(timer);retEnd();});if(ret.fired<0){doh.pause();}
return ret;}};doh._runFixture=function(groupName,fixture){var tg=this._groups[groupName];this._testStarted(groupName,fixture);var threw=false;var err=null; try{
 fixture.group=tg; if(fixture["setUp"]){fixture.setUp(this);}
if(fixture["runTest"]){if(fixture.testType==="perf"){return doh._runPerfFixture(groupName,fixture);}else{var ret=doh._runRegFixture(groupName,fixture);if(ret){return ret;}}}
if(fixture["tearDown"]){fixture.tearDown(this);}}catch(e){threw=true;err=e;if(!fixture.endTime){fixture.endTime=new Date();}}
var d=new doh.Deferred();doh.setTimeout(this.hitch(this,function(){if(threw){this._handleFailure(groupName,fixture,err);}
this._testFinished(groupName,fixture,!threw);if((!tg.inFlight)&&(tg.iterated)){doh._groupFinished(groupName,!tg.failures);}else if(tg.inFlight>0){doh.setTimeout(this.hitch(this,function(){doh.runGroup(groupName);}),100);this._paused=true;}
if(doh._paused){doh.run();}}),30);doh.pause();return d;}
doh._testId=0;doh.runGroup=function(groupName,idx){





var tg=this._groups[groupName];if(tg.skip===true){return;}
if(this._isArray(tg)){if(idx<=tg.length){if((!tg.inFlight)&&(tg.iterated==true)){if(tg["tearDown"]){tg.tearDown(this);}
doh._groupFinished(groupName,!tg.failures);return;}}
if(!idx){tg.inFlight=0;tg.iterated=false;tg.failures=0;}
doh._groupStarted(groupName);if(!idx){this._setupGroupForRun(groupName,idx);if(tg["setUp"]){tg.setUp(this);}}
for(var y=(idx||0);y<tg.length;y++){if(this._paused){this._currentTest=y;return;}
doh._runFixture(groupName,tg[y]);if(this._paused){this._currentTest=y+1;if(this._currentTest==tg.length){tg.iterated=true;}
return;}}
tg.iterated=true;if(!tg.inFlight){if(tg["tearDown"]){tg.tearDown(this);}
doh._groupFinished(groupName,!tg.failures);}}}
doh._onEnd=function(){}
doh._report=function(){

this.debug(this._line);this.debug("| TEST SUMMARY:");this.debug(this._line);this.debug("\t",this._testCount,"tests in",this._groupCount,"groups");this.debug("\t",this._errorCount,"errors");this.debug("\t",this._failureCount,"failures");}
doh.togglePaused=function(){this[(this._paused)?"run":"pause"]();}
doh.pause=function(){this._paused=true;}
doh.run=function(){this._paused=false;var cg=this._currentGroup;var ct=this._currentTest;var found=false;if(!cg){this._init(); found=true;}
this._currentGroup=null;this._currentTest=null;for(var x in this._groups){if(((!found)&&(x==cg))||(found)){if(this._paused){return;}
this._currentGroup=x;if(!found){found=true;this.runGroup(x,ct);}else{this.runGroup(x);}
if(this._paused){return;}}}
this._currentGroup=null;this._currentTest=null;this._paused=false;this._onEnd();this._report();}

doh.standardDeviation=function(a){return Math.sqrt(this.variance(a));};doh.variance=function(a){var mean=0,squares=0;dojo.forEach(a,function(item){mean+=item;squares+=Math.pow(item,2);});return(squares/a.length)-Math.pow(mean/a.length,2);};doh.mean=function(a){var t=0;dojo.forEach(a,function(v){t+=v;});return t/Math.max(a.length,1);};doh.min=function(a){return Math.min.apply(null,a);};doh.max=function(a){return Math.max.apply(null,a);},doh.median=function(a){return a.slice(0).sort()[Math.ceil(a.length/2)-1];},doh.mode=function(a){
var o={},r=0,m=Number.MIN_VALUE;dojo.forEach(a,function(v){(o[v]!==undefined)?o[v]++:o[v]=1;});for(var p in o){if(m<o[p]){m=o[p],r=p;}}
return r;};doh.average=function(a){var i;var s=0;for(i=0;i<a.length;i++){s+=a[i];}
return s/a.length;}
tests=doh;if(typeof skipDohSetup==="undefined"){(function(){ var x;try{if(typeof dojo!="undefined"){dojo.platformRequire({browser:["doh._browserRunner"],rhino:["doh._rhinoRunner"],spidermonkey:["doh._rhinoRunner"]});try{var _shouldRequire=dojo.isBrowser?(dojo.global==dojo.global["parent"]||!Boolean(dojo.global.parent.doh)):true;}catch(e){ _shouldRequire=true;}
if(_shouldRequire){if(dojo.isBrowser){dojo.addOnLoad(function(){if(dojo.global.registerModulePath){dojo.forEach(dojo.global.registerModulePath,function(m){dojo.registerModulePath(m[0],m[1]);});}
if(dojo.byId("testList")){var _tm=((dojo.global.testModule&&dojo.global.testModule.length)?dojo.global.testModule:"dojo.tests.module");dojo.forEach(_tm.split(","),dojo.require,dojo);doh.setTimeout(function(){doh.run();},500);}});}else{}}}else{if(typeof load=="function"&&(typeof Packages=="function"||typeof Packages=="object")){throw new Error();}else if(typeof load=="function"){throw new Error();}
if(this["document"]){}}}catch(e){print("\n"+doh._line);print("The Dojo Unit Test Harness, $Rev: 20389 $");print("Copyright (c) 2009, The Dojo Foundation, All Rights Reserved");print(doh._line,"\n");try{var dojoUrl="../../dojo/dojo.js";var testUrl="";var testModule="dojo.tests.module";var dohBase="";for(x=0;x<arguments.length;x++){if(arguments[x].indexOf("=")>0){var tp=arguments[x].split("=");if(tp[0]=="dohBase"){dohBase=tp[1];
dohBase=dohBase.replace(/\\/g, "/");
                                                    if(dohBase.charAt(dohBase.length - 1) != "/"){
                                                            dohBase += "/";
                                                    }
                                            }
                                            if(tp[0] == "dojoUrl"){
                                                    dojoUrl = tp[1];
                                            }
                                            if(tp[0] == "testUrl"){
                                                    testUrl = tp[1];
                                            }
                                            if(tp[0] == "testModule"){
                                                    testModule = tp[1];
                                            }
                                    }
                            }

                            load(dohBase + "_rhinoRunner.js");

                            if(dojoUrl.length){
                                    if(!this["djConfig"]){
                                            djConfig = {};
                                    }
                                    djConfig.baseUrl = dojoUrl.split("dojo.js")[0];
                                    load(dojoUrl);
                            }
                            if(testUrl.length){
                                    load(testUrl);
                            }
                            if(testModule.length){
                                    dojo.forEach(testModule.split(","), dojo.require, dojo);
                            }
                    }catch(e){
                            print("An exception occurred:" + e);
                    }

                    doh.run();
            }
    }).apply(this, typeof arguments != "undefined"
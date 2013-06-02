require({baseUrl:'./'},['a'],function(a){

a.doSomething();doh.register('nestedRequire',[function nestedRequire(t){t.is(1,a.counter);t.is('base',a.base.name);}]);doh.run();});
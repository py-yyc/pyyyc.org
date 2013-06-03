define([
	'jquery', 
	'./models', 
	'module', 
	'mustache',
	'text!../../tpl/event.tpl',
	'text!../../tpl/events.tpl'
	], 

	function($, eventModels, module, Mustache, eventTpl, eventsTpl) {
	var sig_id = module.config().sig_id;
	var sig = module.config().sig;
	var eventsUrl = 'http://api.meetup.com/2/events?status=upcoming%2Cpast' +
	'&order=time&limited_events=False&group_urlname=py-yyc&desc=true&offset=0' + 
	'&format=json&page=20&fields=&sig_id=' + sig_id + '&sig=' + sig + '&callback=?';

	$.getJSON(eventsUrl, {}, function(data, textStatus, jqXHR) {
		//ingest the event objects returned
		var events = $.map(data.results, function(obj) {
			return new eventModels.Event(obj);
		});

		//separate the events into upcoming and past events
		var upcomingEvents = [], pastEvents = [];
		$.each(events, function(index, evt) {
			if (evt.status == 'upcoming')
				upcomingEvents.push(evt);
			else if (evt.status == 'past')
				pastEvents.push(evt);
		});
		
		//render the template with the events
		var eventsContainer = $('#events-container');
		eventsContainer.html(Mustache.render(eventsTpl, {
			"upcomingEvents": upcomingEvents,
			"pastEvents": pastEvents
		}, {
			"eventTpl": eventTpl
		}));
	});
});